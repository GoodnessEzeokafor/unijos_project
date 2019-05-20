from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import( 
        CreateView,
        UpdateView,
        DeleteView,
        DetailView
)
from .models import FileUpload
from .forms import FileUploadForm
from profiles.models import Profile
# Create your views here.


class UpoadFileCreateView(CreateView):
    model = FileUpload
    form_class = FileUploadForm
    template_name = "blog/upload/form.html"
    success_url = reverse_lazy('profiles:profile_dashboard')



    def form_valid(self, form):
        form.instance.profile = Profile.objects.get(user=self.request.user)
        context = super().form_valid(form)
        return context


class UploadFileEditView(UpdateView):
    pass


class UploadFileDetailView(DetailView):
    pass

class UploadFileDeleteView(DeleteView):
    pass
