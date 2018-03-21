from django.shortcuts import render, redirect
from asset.models import Asset

def index(request):
    assets = Asset.objects.all()

    context = {
        'assets': assets,
    }

    return render(request, 'core/index.html', context)
