from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Asset, Hardware, Software, Qrcode
from info.models import Update
from .forms import AddHardwareForm, AddToQrcodeForm

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
    form = AddHardwareForm()

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
        'extend': "asset/detail.html",
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

@login_required
def scan(request, uid):
    qr_code = get_object_or_404(Qrcode, uid=uid)
    if request.method == 'POST':
        form = AddToQrcodeForm(request.POST)
        if form.is_valid():
            qr_code.asset = form.cleaned_data['asset']
            qr_code.save()
            return redirect(request.path)
        else:
            asset = None
            template = 'asset/scan.html'
    else:
        if qr_code.asset:
            try:
                asset = Asset.objects.get_subclass(id=qr_code.asset.id)
                template = asset.get_class_name().lower().replace('.', '/') + '/info.html'
            except ObjectDoesNotExist:
                pass
        else:
            asset = None
            template = 'asset/scan.html'

        form = AddToQrcodeForm()

    context = {
        'extend': "asset/scan.html",
        'qr_code': qr_code,
        'asset': asset,
        'form': form,
    }

    return render(request, template, context)

