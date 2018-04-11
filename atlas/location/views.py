from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from atlas.decorators import user, administrator
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from .models import Section, Location
from asset.models import Asset
from .forms import AddSectionForm, EditLocationForm, SectionPlanForm
import math


@administrator
@login_required
def index(request):
    location = Location.objects.all().first()

    context = {
        'location': location,
    }

    return render(request, 'location/location.html', context)


@administrator
@login_required
def plan(request):
    if request.method == 'GET':
        if request.is_ajax():
            plan_x = request.GET.get('plan_x', '')
            plan_y = request.GET.get('plan_y', '')

            try:
                plan_x = float(plan_x)
                plan_y = float(plan_y)
            except ValueError:
                plan_x = 0
                plan_y = 0

            print(plan_x)
            print(plan_y)

            try:
                section = serializers.serialize('json', Section.objects.filter(plan_x=plan_x, plan_y=plan_y), fields=('id', 'title'))
            except ObjectDoesNotExist:
                section = None

            return JsonResponse(section, safe=False)


@administrator
@login_required
def setPlanSection(request):
    if request.method == 'POST':
        if request.is_ajax():
            section = get_object_or_404(Section, id=request.POST['section'])
            form = SectionPlanForm(request.POST, instance=section)
            if form.is_valid():
                section = form.save(commit=False)
                section.plan_x = request.POST['plan_x']
                section.plan_y = request.POST['plan_y']
                section.save()
                return HttpResponse('shit is goed')
    return render(request)


@administrator
@login_required
def editLocation(request, id):
    location = get_object_or_404(Location, id=id)

    if request.method == 'POST':
        form = EditLocationForm(request.POST, request.FILES, instance=location)

        if form.is_valid():
            form.save()

            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = location.get_edit_form()

    context = {
        'form': form,
        'form_half': math.ceil((len(form.fields)/2)),
    }

    return render(request, 'location/location/edit.html', context)

@administrator
@login_required
def sections(request):
    sections = Section.objects.all()

    context = {
        'sections': sections,
    }

    return render(request, 'location/sections.html', context)


@administrator
@login_required
def sectionDetail(request, id):
    section = get_object_or_404(Section, id=id)
    assets = Asset.objects.filter(section=section.id)

    context = {
        'section': section,
        'assets': assets,
    }

    return render(request, 'location/section/detail.html', context)


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
