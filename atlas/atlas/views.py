from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from asset.models import Asset, Software, Hardware, Request, License
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
    requests = Request.objects.all().order_by('created_at')
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
    distinct_software_title = []
    distinct_software = []
    requests = None

    try:
        users = Person.objects.filter(category=request.user.category)
        user_ids = [user.id for user in users]
        recommended_software = License.objects.filter(user__id__in=user_ids)

        for item in recommended_software:
            if item.software.title not in distinct_software_title:
                distinct_software_title.append(item.software.title)
                distinct_software.append(item.software)

        requests = Request.objects.filter(user=request.user.id)
    except ObjectDoesNotExist:
        pass

    context = {
        'recommended_software': distinct_software,
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

        software_q = {}
        software_q['title__icontains'] = q
        software_results = Software.objects.filter(**software_q).values('id', 'title')
        if software_results:
            results['software'] = list(software_results)

        hardware_q = {}
        hardware_q['title__icontains'] = q
        hardware_results = Hardware.objects.filter(**hardware_q).values('id', 'title')
        if hardware_results:
            results['hardware'] = list(hardware_results)

        section_q = {}
        section_q['title__icontains'] = q
        section_results = Section.objects.filter(**section_q).values('id', 'title')
        if section_results:
            results['sections'] = list(section_results)

        parsed_results = json.dumps(results)
        return JsonResponse(parsed_results, safe=False)

