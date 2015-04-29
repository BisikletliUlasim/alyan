from alyan.forms import RegistrationForm, ProfileForm, BicycleForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .models import Bicycle


def index(request):
    latest_bicycles = Bicycle.objects.order_by('registration_date')[:10]
    registration_form = RegistrationForm()

    return render(request, 'alyan/index.html', context=locals())


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return HttpResponseRedirect("/account")


@login_required
def edit_profile(request):
    if request.method == 'GET':
        form = ProfileForm()
        user = request.user
    elif request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()

    return render(request, 'alyan/edit_profile.html', context=locals())


@login_required
def my_bicycles(request):
    bicycles = Bicycle.objects.filter(owner=request.user)
    return render(request, 'alyan/my_bicycles.html', context=locals())


@login_required
def edit_bicycle(request, bicycle_id):
    if request.method == 'GET':
        bicycle = Bicycle.objects.get(id=bicycle_id, owner=request.user)
        if bicycle:
            form = BicycleForm(instance=bicycle)
        else:
            return HttpResponse(403)
    elif request.method == 'POST':
        form = BicycleForm(request.POST)
        if form.is_valid():
            bicycle = form.save()

    return render(request, 'alyan/edit_bicycle.html', context=locals())
