from django.shortcuts import render, redirect
from .forms import ProductForm
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from .models import Product

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')
    else:
        form = ProductForm()

    return render(request, 'create.html', {'form': form})

def generate_pdf(request, pk):
    product = get_object_or_404(Product, pk=pk)
    template = get_template.render('product_pdf.html')
    html = template.render({'product':product})
    buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=buffer)
    if pisa_status.error:
        return HttpResponse('PDF creation error!!')
    else:
        response = HttpResponse(buffer.getvalue(), content_type = 'application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(product.name)
        return response