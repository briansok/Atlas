from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from asset.models import Asset

@login_required
def index(request):
    assets = Asset.objects.all()

    context = {
        'assets': assets,
    }

    return render(request, 'core/index.html', context)
