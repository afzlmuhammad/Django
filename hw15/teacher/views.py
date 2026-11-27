from django.shortcuts import render
from django.http import HttpResponse
from .forms import Teacher_Form

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def create_teacher(request):

    form = Teacher_Form()

    if request.method == 'POST':

        form = Teacher_Form(request.POST, request.FILES)

        if form.is_valid():

            teacher = form.save(commit=False)

            teacher.profile_photo = request.FILES['profile_photo']

            file_type = teacher.profile_photo.url.split('.')[-1]

            file_type = file_type.lower()

            if file_type not in IMAGE_FILE_TYPES:

                return HttpResponse('Only JPG, JPEG and PNG files are supported')

            teacher.save()

            return HttpResponse('Teacher details saved successfully!')

    context = {
        'form': form,
    }

    return render(request, 'create_teacher.html', context)