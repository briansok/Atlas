from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from asset.models import Asset, Software, Hardware, Request
from location.models import Location
from person.models import Person
from location.forms import SectionPlanForm
from datetime import datetime, timedelta


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
