from django.contrib.auth.decorators import login_required
from .models import Section, Location
from django.shortcuts import render

@login_required
def index(request):
    sections = Section.objects.all()

    context = {
        'sections': sections,
    }

    return render(request, 'location/sections.html', context)

