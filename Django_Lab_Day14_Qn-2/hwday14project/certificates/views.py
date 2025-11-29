from itertools import product
from django.shortcuts import render, redirect
from .forms import CertificateForm
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from .models import Certificate
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.shortcuts import render

def certificate_create(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            certificate = form.save()
            return redirect('cert_details.html')
    else:
        form = CertificateForm()
    return render(request, 'certificate_create.html', {'form':form})

def download_pdf(request,pk):
    certificate = get_object_or_404(Certificate,pk=pk)
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
    
def send_mail(request):
    def send_product_email(request,pk):
        certificate =Certificate.objects.get(pk=pk)
        subject = f"New Product: {certificate.name}"
        from_email = "pranjana333@gmail.com"
        recipient_list = ["your_mailtrap_inbox@mailtrap.io"]
        html_message = render_to_string('certificate_email.html', {'certificate': certificate})
        plain_message = strip_tags(html_message)
        send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
        return HttpResponse('Email sent successfully')
