from django.shortcuts import render
from .forms import CustomerForm
from .models import Customer

# Add customer
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'form-data.html', {
                'message': 'Customer details saved successfully'
            })
    else:
        form = CustomerForm()

    return render(request, 'index.html', {'form': form})


# Display all customers
def all_customers(request):
    customers = Customer.objects.all().order_by('name')
    return render(request, 'all-customers.html', {'customers': customers})


# Display filtered customers
def filtered_customers(request):
    customers = Customer.objects.filter(email__endswith='@example.com')
    return render(request, 'filtered-customers.html', {'customers': customers})