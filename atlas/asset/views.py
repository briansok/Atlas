from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Asset, Hardware, Software, Qrcode
from info.models import Update
from .forms import AddAssetForm

@login_required
def index(request):
    assets = Asset.objects.all()

    context = {
        'assets': assets,
    }

    return render(request, 'asset/assets.html', context)

@login_required
def add(request):
    assets = Asset.objects.all()
    form = AddAssetForm()

    context = {
        'assets': assets,
        'form': form,
    }

    return render(request, 'asset/add.html', context)

@login_required
def detail(request, id):
    try:
        asset = Asset.objects.get_subclass(id=id)
    except ObjectDoesNotExist:
        raise Http404('Object does not exist')

    updates = Update.objects.filter(asset=id).order_by('-id')

    try:
        qr_code = Qrcode.objects.get(asset=id)
    except ObjectDoesNotExist:
        qr_code = None

    if qr_code:
        qr_code = qr_code.get_qr_code_url(request.get_host())

    context = {
        'asset': asset,
        'updates': updates,
        'qr_code': qr_code,
    }
    return render(request, asset.get_class_name().lower().replace('.', '/') + '/info.html', context)

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
