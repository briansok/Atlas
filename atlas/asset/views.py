from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Asset, Hardware, Software

@login_required
def index(request):
    assets = Asset.objects.all()

    context = {
        'assets': assets,
        'filter': 'all',
    }

    return render(request, 'asset/assets.html', context)

@login_required
def detail(request, id):
    asset = Asset.objects.get(id=id)

    context = {
        'asset': asset,
        'filter': 'all',
    }

    return render(request, 'asset/detail.html', context)

@login_required
def hardware(request):
    assets = Hardware.objects.all()

    context = {
        'assets': assets,
        'filter': 'hardware',
    }

    return render(request, 'asset/assets.html', context)

@login_required
def software(request):
    assets = Software.objects.all()

    context = {
        'assets': assets,
        'filter': 'software',
    }

    return render(request, 'asset/assets.html', context)
