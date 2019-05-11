from django.shortcuts import render, get_object_or_404
from django.views.generic import(
    CreateView, 
    UpdateView,
    DetailView, 
    UpdateView, 
    DeleteView
)
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import (
    reverse, 
    reverse_lazy
)
from allauth.account.forms import SignupForm
from .forms import ProfileForm
from .models import Profile

# Create your views here.


class DetailProfileView(DetailView):
    pass

class CreateProfileView(CreateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('profiles:profile_dashboard')
    template_name = "profile/create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        context = super().form_valid(form)
        return context


class UpdateProfileView(UpdateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('profiles:profile_dashboard')
    context_object_name = "profile_update"
    template_name = "profile/create.html"




class DeleteProfileVIew(DeleteView):
    pass


def dashboard(request):
    try:
        profile = get_object_or_404(Profile, user=request.user)
    except:
        return HttpResponseRedirect(reverse_lazy('profiles:profile_create'))

    template_name = 'profile/dashboard.html'
    context ={
        'profile':profile
    }
    return render(request, template_name, context)
