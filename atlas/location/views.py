from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from atlas.decorators import user, administrator
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core import serializers
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import gettext as _
from asset.models import Asset
from atlas.helpers import CreateNotification
from .models import Section, Location
from .forms import AddSectionForm, EditLocationForm, SectionPlanForm, AddLocationForm
import math
import json

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

            try:
                section = serializers.serialize('json', Section.objects.filter(plan_x=plan_x, plan_y=plan_y), fields=('id', 'title'))
            except ObjectDoesNotExist:
                section = None

            return JsonResponse(section, safe=False)


@administrator
@login_required
def set_plan_section(request):
    if request.method == 'POST':
        if request.is_ajax():
            section = get_object_or_404(Section, id=request.POST['section'])
            form = SectionPlanForm(request.POST, instance=section)
            if form.is_valid():
                section = form.save(commit=False)
                section.plan_x = request.POST['plan_x']
                section.plan_y = request.POST['plan_y']
                section.save()

                notification = CreateNotification(
                    _('Section linked to plan'),
                    'info',
                    request,
                    section=section.id)
                notification.create()

    return redirect('home')


@administrator
@login_required
def get_plan_section(request):
    x = request.GET['x']
    y = request.GET['y']
    if request.is_ajax():
        if x and y:
            try:
                section = Section.objects.get(plan_x=x, plan_y=y)
                json = serializers.serialize('json', [section])
                return JsonResponse(json, safe=False)
            except ObjectDoesNotExist:
                return JsonResponse({'x': 'none'}, safe=False)


@administrator
@login_required
def delete_plan_section(request):
    if request.method == "POST":
        x = request.POST['plan_x']
        y = request.POST['plan_y']
        if x and y:
            try:
                section = Section.objects.get(plan_x=x, plan_y=y)
                section.plan_x = 0
                section.plan_y = 0
                section.save()
                return JsonResponse({'saved': True}, safe=False)
            except ObjectDoesNotExist:
                return JsonResponse({'saved': False}, safe=False)
    return redirect('home')

@administrator
@login_required
def edit_location(request, id):
    location = get_object_or_404(Location, id=id)

    if request.method == 'POST':
        form = EditLocationForm(request.POST, request.FILES, instance=location)

        if form.is_valid():
            form.save()

            notification = CreateNotification(
                _('Location edited'),
                'info',
                request)
            notification.create()

            next = request.POST.get('next', '/')
            if next:
                return HttpResponseRedirect(next)
            else:
                return redirect('location-detail')

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
def section_detail(request, id):
    section = get_object_or_404(Section, id=id)
    assets = Asset.objects.filter(section=section.id).select_subclasses()

    context = {
        'section': section,
        'assets': assets,
    }

    return render(request, 'location/section/detail.html', context)


@administrator
@login_required
def add_section(request):
    if request.method == 'POST':
        form = AddSectionForm(request.POST)
        if form.is_valid():
            section = form.save(commit=False)
            section.save()

            notification = CreateNotification(
                _('Section added'),
                'info',
                request,
                section=section.id)

            notification.create()

            next = request.POST.get('next', '/')
            if next:
                return HttpResponseRedirect(next)
            else:
                return redirect('location-detail')
    else:
        form = AddSectionForm()

    context = {
        'form': form,
        'form_half': math.ceil((len(form.fields)/2)),
    }

    return render(request, 'location/section/add.html', context)


@administrator
@login_required
def add_location(request):
    if request.method == 'POST':
        form = AddLocationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            notification = CreateNotification(
                _('Location added'),
                'info',
                request)

            notification.create()

            next = request.POST.get('next', '/')
            if next:
                return HttpResponseRedirect(next)
            else:
                return redirect('location-detail')
    else:
        form = AddLocationForm()

    context = {
        'form': form,
        'form_half': math.ceil((len(form.fields)/2)),
    }

    return render(request, 'location/location/add.html', context)
