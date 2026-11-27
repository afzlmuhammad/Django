from django.shortcuts import render
from django.http import HttpResponse
from .forms import Student_Form

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def create_student(request):

    form = Student_Form()

    if request.method == 'POST':

        form = Student_Form(request.POST, request.FILES)

        if form.is_valid():

            student = form.save(commit=False)

            student.id_card = request.FILES['id_card']

            file_type = student.id_card.url.split('.')[-1]

            file_type = file_type.lower()

            if file_type not in IMAGE_FILE_TYPES:

                return HttpResponse('Only JPG, JPEG and PNG files are supported')

            student.save()

            return HttpResponse('Student registered successfully!')

    context = {
        'form': form,
    }

    return render(request, 'registration.html', context)