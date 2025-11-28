from itertools import product
from django.shortcuts import render, redirect
from .forms import ProductForm
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from .models import Product
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('product_details', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'create.html', {'form': form})

def generate_pdf(request, pk):
    product = get_object_or_404(Product, pk=pk)
    template = get_template('product_pdf.html')
    html = template.render({'product': product})
    buffer = BytesIO()

    pisa_status = pisa.CreatePDF(html, dest=buffer)

    if pisa_status.err:
        return HttpResponse(html)   # Show error inside browser
    response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{product.name}.pdf"'
    return response
    
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def send_product_email(request, pk):
    product = Product.objects.get(pk=pk)
    subject = 'Product Details: {}'.format(product.name)
    from_email = 'pranjana333@gmail.com'
    recipient_list = ['recipient@example.com']  # Replace with the recipient's email address    
    html_message = render_to_string('product_email.html', {'product': product})
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
    return HttpResponse('Email sent successfully')