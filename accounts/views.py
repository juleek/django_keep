from .forms import AccountForm
import django.contrib.auth as asdf1
import django.contrib.messages as messages
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

import django.contrib.auth.forms as formbuit

import django.contrib as djc
import django.shortcuts as djsh


from . import base_template_params as base_templ


def create_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            user = form.save()
            djc.auth.login(request, user)
            return djsh.redirect('home')
    else:
        form = AccountForm()
    return djsh.render(request, 'create_account.html',
                       {'form': form} | base_templ.get_all_params(request))


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = djc.auth.authenticate(request, username=username, password=password)
        if user is not None:
            djc.auth.login(request, user)
            return djsh.redirect('home')
        else:
            djc.messages.error(request, ("There was an Error. Please, try again"))
    return djsh.render(request, 'login.html', base_templ.get_all_params(request))



def change_password(request):
    if request.method == "POST":
        form = formbuit.PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            asdf1.update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return djsh.redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = formbuit.PasswordChangeForm(request.user)
    return djsh.render(request, 'change_password.html',
                       {'form': form} | base_templ.get_all_params(request))



@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('username', "email")
    template_name = 'update_account.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context | base_templ.get_all_params(self.request)
