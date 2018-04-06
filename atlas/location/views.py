from django.contrib.auth.decorators import login_required
from atlas.decorators import user, administrator
from django.shortcuts import render
from .models import Section, Location

@administrator
@login_required
def index(request):
    sections = Section.objects.all()

    context = {
        'sections': sections,
    }

    return render(request, 'location/sections.html', context)

