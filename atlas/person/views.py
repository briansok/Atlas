from django.contrib.auth.decorators import login_required
from atlas.decorators import user, administrator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from asset.models import Asset
from .models import Person
from .forms import EditPersonForm
import math


@administrator
@login_required
def index(request):
    users = Person.objects.all()

    context = {
        'users': users,
    }

    return render(request, 'person/users.html', context)


@login_required
def detail(request, id):
    user = get_object_or_404(Person, id=id)
    assets = get_list_or_404(Asset, user=user.id)

    context = {
        'user': user,
        'assets': assets,
    }

    return render(request, 'person/detail.html', context)


@administrator
@login_required
def edit(request, id):
    person = get_object_or_404(Person, id=id)

    if request.method == 'POST':
        form = EditPersonForm(request.POST, request.FILES, instance=person)

        if form.is_valid():
            form.save()

            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = person.get_edit_form()

    context = {
        'form': form,
        'form_half': math.ceil((len(form.fields)/2)),
    }

    return render(request, 'person/edit.html', context)

