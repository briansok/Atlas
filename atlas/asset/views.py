import math
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.translation import gettext as _
from info.models import Update
from atlas.decorators import user, administrator
from atlas.helpers import CreateNotification
from .models import Asset, Hardware, Software, Qrcode, License, Request
from .forms import AddHardwareForm, AddSoftwareForm, AddToQrcodeForm, RequestForm, AddLicenseForm


@administrator
@login_required
def index(request):
    assets = Asset.objects.all().select_subclasses().order_by('title')

    context = {
        'assets': assets,
    }

    return render(request, 'asset/list.html', context)


@administrator
@login_required
def add(request, asset):
    if request.method == 'POST':
        if asset == 'hardware':
            form = AddHardwareForm(request.POST)
        elif asset == 'software':
            form = AddSoftwareForm(request.POST)
        else:
            form = None

        if form.is_valid():
            asset_obj = form.save(commit=False)
            if asset == 'hardware' and asset_obj.guarantee_years is not None \
                and asset_obj.bought_at is not None:
                asset_obj.valid_until = asset_obj.bought_at + \
                    relativedelta(years=asset_obj.guarantee_years)
            asset_obj.save()

            notification = CreateNotification(
                _('Asset added'),
                'info',
                request,
                asset=asset_obj.id)

            notification.create()

            if request.POST.get('qr_code'):
                qr_code = get_object_or_404(Qrcode, uid=request.POST.get('qr_code'))
                qr_code.asset = asset_obj
                qr_code.save()
                return redirect('hardware-detail', asset_obj.id)

            next = request.POST.get('next', '/')
            if next:
                return HttpResponseRedirect(next)
            else:
                return redirect('asset-list')
    else:
        if asset == 'hardware':
            if request.GET.get('section'):
                form = AddHardwareForm(initial={'section': request.GET.get('section')})
            else:
                form = AddHardwareForm()
        elif asset == 'software':
            if request.GET.get('section'):
                form = AddSoftwareForm(initial={'section': request.GET.get('section')})
            else:
                form = AddSoftwareForm()
        else:
            form = None

    context = {
        'form': form,
        'form_half': math.ceil((len(form.fields)/2)),
        'asset_name': asset,
    }

    return render(request, 'asset/add.html', context)


@administrator
@login_required
def edit(request, id):
    try:
        asset = Asset.objects.get_subclass(id=id)
        asset.has_permission(request.user)
    except ObjectDoesNotExist:
        raise Http404('Object does not exist')

    if request.method == 'POST':
        form = asset.get_post_form(request.POST, asset)

        if form.is_valid():
            obj = form.save(commit=False)

            try:
                if obj.bought_at is not None and obj.guarantee_years is not None:
                    obj.valid_until = obj.bought_at + \
                    relativedelta(years=obj.guarantee_years)
            except AttributeError:
                pass
            obj.save()

            notification = CreateNotification(
                _('Asset edited'),
                'info',
                request,
                asset=id)

            notification.create()

            next = request.POST.get('next', '/')
            if next:
                return HttpResponseRedirect(next)
            else:
                return redirect('asset-detail')
    else:
        form = asset.get_edit_form()

    context = {
        'form': form,
        'form_half': math.ceil((len(form.fields)/2)),
        'asset_name': asset.__class__.__name__.lower(),
    }

    return render(request, 'asset/edit.html', context)


@administrator
@login_required
def delete(request, id):
    asset = get_object_or_404(Asset, id=id)
    if request.method == 'POST':
        asset.delete()
    return redirect('asset-list')


@login_required
def hardware_detail(request, id):
    asset = get_object_or_404(Hardware, id=id)
    asset.has_permission(request.user)
    updates = Update.objects.filter(asset=id).order_by('date')

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

    return render(request, 'asset/hardware/detail.html', context)


@login_required
def software_detail(request, id):
    asset = get_object_or_404(Software, id=id)
    licenses = License.objects.filter(software=id).order_by('created_at')

    context = {
        'asset': asset,
        'licenses': licenses,
    }

    return render(request, 'asset/software/detail.html', context)


@administrator
@login_required
def search(request):
    if request.method == 'GET':
        if request.is_ajax():
            try:
                result = Asset.objects.all()
                json = serializers.serialize('json', result)
            except ObjectDoesNotExist:
                json = None

            return JsonResponse(json, safe=False)


@administrator
@login_required
def hardware_list(request):
    assets = Hardware.objects.all().order_by('title')

    context = {
        'assets': assets,
    }

    return render(request, 'asset/hardware/list.html', context)


@administrator
@login_required
def software_list(request):
    assets = Software.objects.all().order_by('title')

    context = {
        'assets': assets,
    }

    return render(request, 'asset/software/list.html', context)


@login_required
def scan(request, uid):
    qr_code = get_object_or_404(Qrcode, uid=uid)
    if request.method == 'POST':
        form = AddToQrcodeForm(request.POST)
        if form.is_valid():
            qr_code.asset = form.cleaned_data['asset']
            qr_code.save()

            notification = CreateNotification(
                _('Qrcode linked'),
                'info',
                request,
                asset=form.cleaned_data['asset'].id)

            notification.create()

            return redirect(request.path)
        else:
            asset = None
            updates = None
            template = 'asset/scan.html'
    else:
        if qr_code.asset:
            try:
                asset = Asset.objects.get_subclass(id=qr_code.asset.id)
                updates = Update.objects.filter(asset=asset.id).order_by('-id')
                template = asset.get_class_name().lower().replace('.', '/') + '/info.html'
            except ObjectDoesNotExist:
                pass
        else:
            asset = None
            updates = None
            template = 'asset/scan.html'

        form = AddToQrcodeForm()

    context = {
        'extend': "asset/scan.html",
        'qr_code': qr_code,
        'updates': updates,
        'asset': asset,
        'form': form,
    }

    return render(request, template, context)


@login_required
def request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.user = request.user
            req.save()

            notification = CreateNotification(
                _('Request created'),
                'info',
                request)

            notification.create()

            next = request.POST.get('next', '/')
            if next:
                return HttpResponseRedirect(next)
            else:
                return redirect('home')
    else:
        try:
            form = RequestForm(initial={'title': request.GET['title']})
        except MultiValueDictKeyError:
            form = RequestForm()


    context = {
        'form': form,
    }

    return render(request, 'asset/request.html', context)


@login_required
def edit_request(request, id):
    req = get_object_or_404(Request, id=id)
    if request.method == 'POST':
        form = RequestForm(request.POST, instance=req)
        if form.is_valid():
            form.save()
            notification = CreateNotification(
                _('Request edited'),
                'info',
                request)
            notification.create()
            next = request.POST.get('next', '/')
            if next:
                return HttpResponseRedirect(next)
            else:
                return redirect('home')
    else:
        form = req.get_edit_form()

    context = {
        'form': form,
        'form_half': math.ceil((len(form.fields)/2)),
    }

    return render(request, 'asset/request/request_edit_form.html', context)


@login_required
def delete_request(request, id):
    req = get_object_or_404(Request, id=id)
    if request.method == 'POST':
        req.delete()
    return redirect('home')


@administrator
@login_required
def add_license(request, id):
    if request.method == 'POST':
        form = AddLicenseForm(request.POST)
        if form.is_valid():
            software = get_object_or_404(Software, id=id)

            license = form.save(commit=False)
            license.software = software
            license.save()

            notification = CreateNotification(
                'License added',
                'info',
                request,
                asset=software.id)
            notification.create()

            next = request.POST.get('next', '/')
            if next:
                return HttpResponseRedirect(next)
            else:
                return redirect('asset-list')
    else:
        form = AddLicenseForm()

        context = {
            'form': form,
        }

        return render(request, 'asset/license/add.html', context)


@administrator
@login_required
def edit_license(request, id):
    license = get_object_or_404(License, id=id)
    if request.method == 'POST':
        form = license.get_post_form(request.POST, license)
        if form.is_valid():
            form.save()
            notification = CreateNotification(
                _('License edited'),
                'info',
                request)
            notification.create()
            next = request.POST.get('next', '/')
            if next:
                return HttpResponseRedirect(next)
            else:
                return redirect('software-detail')
    else:
        form = license.get_edit_form()

    context = {
        'form': form,
        'form_half': math.ceil((len(form.fields)/2)),
    }

    return render(request, 'asset/software/license_edit_form.html', context)


@administrator
@login_required
def delete_license(request, id):
    license = get_object_or_404(License, id=id)
    if request.method == 'POST':
        license.delete()
    return redirect('software-detail', id=license.software.id)
