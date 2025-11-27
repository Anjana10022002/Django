from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from .models import Product

from django.shortcuts import render, redirect
from .forms import ProductForm
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create.html')
    else:
        form =ProductForm()
    return render(request, 'create.html', {'form': form})

def generate_pdf(request,pk):
    # Get the product object
    product = get_object_or_404(Product,pk=pk)

    # Render the HTML template with the product data
    template = get_template('product_pdf.html')
    html = template.render({'product': product})

    # Create a file-like buffer to receive PDF data.
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file."
    pisa_status = pisa.CreatePDF(html, dest=buffer)

    # Return PDF document through a Django HTTP response.
    if pisa_status.err:
        return HttpResponse('PDF creation error!')
    else:
        response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(product.name)
        return response