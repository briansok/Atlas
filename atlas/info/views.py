from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from atlas.decorators import user, administrator
from atlas.helpers import CreateNotification
from .models import Notification, Update
from .forms import AddUpdateForm

@administrator
@login_required
def index(request):
    notifications = Notification.objects.all()[:10]
    updates = Update.objects.all()[:10]

    context = {
        'notifications': notifications,
        'updates': updates,
    }

    return render(request, 'info/info.html', context)

@administrator
@login_required
def add(request):
    if request.method == 'POST':
        form = AddUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            update = form.save(commit=False)
            update.created_by = request.user
            update.save()

            if form.cleaned_data['asset']:
                asset_id = form.cleaned_data['asset'].id
            else:
                asset_id = None

            notification = CreateNotification(
                'Update added',
                'info',
                request,
                asset=asset_id)
            notification.create()

            next = request.POST.get('next', '/')
            if next:
                return HttpResponseRedirect(next)
            else:
                return redirect('asset-list')
    else:
        if request.GET.get('asset'):
            form = AddUpdateForm(initial={'asset': request.GET.get('asset')})
        else:
            form = AddUpdateForm()

        context = {
            'form': form,
        }

        return render(request, 'info/add.html', context)
