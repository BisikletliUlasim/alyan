from alyan.forms import RegistrationForm, ProfileForm, BicycleForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory, modelform_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .models import Bicycle, BicyclePhoto


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
    bicycle = Bicycle.objects.get(id=bicycle_id, owner=request.user)
    if not Bicycle:
        return HttpResponse(403)

    bicycle_form = modelform_factory(Bicycle, exclude=['owner'])

    if request.method == 'GET':
        bicycle_form = bicycle_form()

    elif request.method == 'POST':
        bicycle_form = bicycle_form()

        if bicycle_form.is_valid():
            bicycle_form.save()

    return render(request, 'alyan/edit_bicycle.html', context=locals())


@login_required()
def edit_photos(request, bicycle_id):
    bicycle = Bicycle.objects.get(id=bicycle_id, owner=request.user)
    if not Bicycle:
        return HttpResponse(403)

    photos_form = inlineformset_factory(Bicycle, BicyclePhoto, exclude=[])

    if request.method == 'GET':
        photos_form = photos_form(instance=bicycle)
        return render(request, 'alyan/edit_photos.html', context=locals())

    elif request.method == 'POST':
        photos_form = photos_form(request.POST, request.FILES, instance=bicycle)
        if photos_form.is_valid():
            photos_form.save()

        return HttpResponseRedirect(bicycle.get_absolute_url())

def view_bicycle(request, bicycle_id):
    bicycle = Bicycle.objects.get(id=bicycle_id)
    if not Bicycle:
        return HttpResponse(404)

    return render(request, 'alyan/view_bicycle.html', context=locals())