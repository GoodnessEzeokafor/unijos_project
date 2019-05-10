from django.contrib.auth import logout
from django.contrib.messages.views import SuccessMessageMixin
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

class CreateProfileView(SuccessMessageMixin,CreateView):
    '''
    Inherites the CreateView from django.views.generic
    Responsible for the creation of user profile
    '''
    model = Profile  # model
    form_class = ProfileForm  # form
    success_url = reverse_lazy('profiles:profile_dashboard') # link to redirect to
    template_name = "profile/create.html"  # template name
    success_message = "Profile was created successfully"
    def form_valid(self, form):
        '''
        This method basically assigns the currently logged in users to the
        user field in the Profile method
        '''
        form.instance.user = self.request.user
        context = super().form_valid(form)
        return context


class UpdateProfileView(SuccessMessageMixin,UpdateView):
    '''
    The view that enable users to edit their profile
    '''
    model = Profile # model
    form_class = ProfileForm # form
    success_url = reverse_lazy('profiles:profile_dashboard')  # url to redirect to
    context_object_name = "profile_update" # context variable
    template_name = "profile/create.html"  # template name
    success_message = "Profile was edited successfully"



class DeleteProfileView(DeleteView):
    model = Profile
    template_name = "profile/delete.html"
    success_url = reverse_lazy("profiles:delete_success")
    # success_message = "Your Profile was deleted successfully"





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


def delete_success(request):
    from django.contrib import messages
    template_name = "profile/delete/thanks.html"
    messages.success(request, "Profile Deleted Successfully!!")
    return render(request, template_name, {})