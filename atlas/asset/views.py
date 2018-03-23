from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Asset, Hardware, Software

@login_required
def index(request):
    assets = Asset.objects.all()

    context = {
        'assets': assets,
    }

    return render(request, 'asset/assets.html', context)

@login_required
def hardware(request):
    assets = Hardware.objects.all()

    context = {
        'assets': assets,
    }

    return render(request, 'asset/hardware.html', context)

@login_required
def software(request):
    assets = Software.objects.all()

    context = {
        'assets': assets,
    }

    return render(request, 'asset/software.html', context)
