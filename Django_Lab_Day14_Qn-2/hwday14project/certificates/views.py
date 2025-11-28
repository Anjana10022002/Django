from django.shortcuts import render, redirect
from .forms import CertificateForm
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from .models import CertificateForm

def certificate_create(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cert_details.html')
    else:
        form = CertificateForm()
        return render(request, 'certificate_create.html', {'form':form})

def download_pdf(request):
    certificate = get_object_or_404(certificate)
    template = get_template('certificate_pdf.html')
    html = template.render({'certificate':certificate})
    buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest = buffer)
    if pisa_status.err:
        return HttpResponse('PDF creation error.')
    else:
        response = HttpResponse(buffer.getvalue(), content_type = 'application/pdf')
        response['Content-Disposition']= 'attachment; filname="{}.pdf"'.format(certificate.name)
        return response