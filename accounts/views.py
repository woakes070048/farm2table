from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from .forms import RegistrationForm


# class UserRegistrationView(CreateView):
#     form_class = UserCreationForm
#     template_name = 'user_registration.html'
#
#     def get_success_url(self):
#         return reverse('profile')

def user_registration(request):
    form = RegistrationForm(request.POST)

    context = {
        'form': form,
    }

    return render(request, "user_registration.html", context)


class UserProfileView(CreateView):
    form_class = UserCreationForm
    template_name = 'profile.html'
