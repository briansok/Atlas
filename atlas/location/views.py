from django.contrib.auth.decorators import login_required
from atlas.decorators import user, administrator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Section, Location
from .forms import AddSectionForm
import math


@administrator
@login_required
def index(request):
    sections = Section.objects.all()

    context = {
        'sections': sections,
    }

    return render(request, 'location/sections.html', context)


@administrator
@login_required
def add(request):
    if request.method == 'POST':
        form = AddSectionForm(request.POST)
        if form.is_valid():
            form.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = AddSectionForm()

    context = {
        'form': form,
        'form_half': math.ceil((len(form.fields)/2)),
    }

    return render(request, 'location/section/add.html', context)
