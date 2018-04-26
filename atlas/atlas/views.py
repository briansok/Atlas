from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from asset.models import Asset, Software, Hardware, Request
from location.models import Location, Section
from location.forms import SectionPlanForm
from person.models import Person
from datetime import datetime, timedelta
import json


@login_required
def index(request):
    if request.user.role == "user":
        return panel(request)

    plan_form = SectionPlanForm()
    expired_assets = Asset.objects.filter(valid_until__lte=datetime.now()+timedelta(days=31)).order_by('valid_until')
    location = Location.objects.all().first()
    requests = Request.objects.filter(user=request.user.id)
    template = 'core/admin/index.html'

    context = {
        'expired_assets': expired_assets,
        'location': location,
        'requests': requests,
        'plan_form': plan_form,
    }

    return render(request, template, context)


@login_required
def panel(request):
    template = 'core/user/panel.html'
    recommended_software = None
    requests = None

    try:
        users = Person.objects.filter(category=request.user.category)
        user_ids = [user.id for user in users]
        recommended_software = Software.objects.filter(user__id__in=user_ids).distinct()
        requests = Request.objects.filter(user=request.user.id)
    except ObjectDoesNotExist:
        pass

    context = {
        'recommended_software': recommended_software,
        'requests': requests,
    }

    return render(request, template, context)


@login_required
def search(request):
    if request.method == 'GET':
        q = request.GET.get('q', '')

        results = {}

        person_q = {}
        person_q['username__icontains'] = q
        person_result = Person.objects.filter(**person_q)
        if person_result:
            for person in person_result:
                results['person_assets'] = list(Asset.objects.filter(user=person.id).values('id', 'title'))

        asset_q = {}
        asset_q['title__icontains'] = q
        asset_results = Asset.objects.filter(**asset_q).values('id', 'title')
        if asset_results:
            results['assets'] = list(asset_results)

        section_q = {}
        section_q['title__icontains'] = q
        section_results = Section.objects.filter(**section_q).values('id', 'title')
        if section_results:
            results['sections'] = list(section_results)

        parsed_results = json.dumps(results)
        return JsonResponse(parsed_results, safe=False)

