from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings
from io import BytesIO
from xhtml2pdf import pisa

from .models import Product
from .forms import ProductForm

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            product = form.save()
            return redirect('product_detail', pk=product.id)

    else:
        form = ProductForm()

    return render(request, 'details/create.html', {'form': form})



def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'details/product_detail.html', {
        'product': product
    })
    
    
    
def generate_pdf(request, pk):

    product = get_object_or_404(Product, pk=pk)

    template = get_template('details/product_pdf.html')
    html = template.render({'product': product})

    buffer = BytesIO()

    pisa_status = pisa.CreatePDF(html, dest=buffer)

    if pisa_status.err:
        return HttpResponse('PDF creation error!')

    else:
        response = HttpResponse(
            buffer.getvalue(),
            content_type='application/pdf'
        )

        response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(product.name)

        return response
    
    
    
def send_product_email(request, pk):

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':

        subject = f"Product Information: {product.name}"

        from_email = settings.DEFAULT_FROM_EMAIL

        recipient_list = [settings.SHOP_OWNER_EMAIL]

        html_message = render_to_string(
            'details/product_email.html',
            {'product': product}
        )

        plain_message = strip_tags(html_message)

        send_mail(
            subject,
            plain_message,
            from_email,
            recipient_list,
            html_message=html_message
        )

        return HttpResponse('Email sent successfully')

    return HttpResponse('Invalid request')