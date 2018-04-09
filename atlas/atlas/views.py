from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404
from asset.models import Asset
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
    asset_list = []

    try:
        users = Person.objects.filter(category=request.users.category)

        if users:
            for user in users:
                user_assets = Asset.objects.filter(user=user.id)
                asset_list.append(user_assets)

    context = {
        'assets': asset_list,
    }

    return render(request, template, context)
