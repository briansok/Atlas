from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Notification, Update
from .forms import AddUpdateForm

@login_required
def index(request):
    notifications = Notification.objects.all()
    updates = Update.objects.all()

    context = {
        'notifications': notifications,
        'updates': updates,
    }

    return render(request, 'info/info.html', context)

@login_required
def add(request):
    if request.method == 'POST':
        form = AddUpdateForm(request.POST)
        if form.is_valid():
            update = form.save(commit=False)
            update.created_by = request.user
            update.date = form.cleaned_data['date']
            update.save()

            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = AddUpdateForm()

        context = {
            'form': form,
        }

        return render(request, 'info/add.html', context)
