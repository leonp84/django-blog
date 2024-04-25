from django.shortcuts import render
from .models import About
from .forms import CollaborateRequestForm
from django.contrib import messages


# Create your views here.
def about_page(request):
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateRequestForm()

    if request.method == 'POST':
        print(request.POST)
        interested_party = CollaborateRequestForm(data=request.POST)

        if interested_party.is_valid():
            interested_party.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Thanks for getting in touch. I'll have a look and get back to\
                 you (possibly, let's see)"
            )

    return render(
        request,
        'about/about.html',
        {'content': about,
         'collaborate_form': collaborate_form}
    )
