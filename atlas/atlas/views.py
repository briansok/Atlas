from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404
from asset.models import Asset, Software, Hardware, Request
from person.models import Person


@login_required
def index(request):
    if request.user.role == "user":
        return panel(request)

    assets = Asset.objects.all()
    template = 'core/admin/index.html'

    context = {
        'assets': assets,
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
