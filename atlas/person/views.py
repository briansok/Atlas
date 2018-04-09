from django.contrib.auth.decorators import login_required
from atlas.decorators import user, administrator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from asset.models import Asset
from .models import Person


@administrator
@login_required
def index(request):
    users = Person.objects.all()

    context = {
        'users': users,
    }

    return render(request, 'person/users.html', context)


@administrator
@login_required
def detail(request, id):
    user = get_object_or_404(Person, id=id)
    assets = get_list_or_404(Asset, user=user.id)

    context = {
        'user': user,
        'assets': assets,
    }

    return render(request, 'person/detail.html', context)
