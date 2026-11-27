from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.conf import settings
from io import BytesIO
from xhtml2pdf import pisa

from .forms import StudentForm


def certificate_create(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():

            student = form.save()

            # Generate PDF
            template = get_template('students/certificate_pdf.html')

            html = template.render({'student': student})

            buffer = BytesIO()

            pisa_status = pisa.CreatePDF(html, dest=buffer)

            if pisa_status.err:
                return HttpResponse('PDF creation error!')

            # Send email
            subject = 'Course Completion Certificate'

            message = render_to_string(
                'students/certificate_email.html',
                {'student': student}
            )

            plain_message = strip_tags(message)

            send_mail(
                subject,
                plain_message,
                settings.DEFAULT_FROM_EMAIL,
                [student.email],
                html_message=message
            )

            # Download PDF
            response = HttpResponse(
                buffer.getvalue(),
                content_type='application/pdf'
            )

            response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'

            return response

    else:
        form = StudentForm()

    return render(request, 'students/create.html', {'form': form})