from django.shortcuts import render
from .models import SubscriptionUser
from .forms import SubscriptionUserSignUpForm


def subscription_signup(request):
    form = SubscriptionUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if SubscriptionUser.objects.filter(email=instance.email).exists():
            print("Sorry! This email already exist")
        else:
            instance.save()

    context = {

        'form': form,
    }
    template = "Personnel/sign_up.html"
    return render(request, template, context)


def subscription_unsubscribe(request):
    form = SubscriptionUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if SubscriptionUser.objects.filter(email=instance.email).exists(): SubscriptionUser.objects.filter(email=instance.email).delete()

        else:
            print('Sorry but we did not find your email address')

    context = {
        'form': form,
    }
    template = "Personnel/unsubscribe.html"
    return render(request, template, context)


