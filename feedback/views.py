from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .forms import FeedbackForm
from .models import Feedback
from django.views.generic import CreateView
from profiles.models import Profile
# Create your views here.




class FeedBackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = "feedback/form.html"
    success_url = "/feedback/thanks/"

    def form_valid(self, form):
        profile = get_object_or_404(Profile, user=self.request.user)
        form.instance.profile = profile
        # print(self.request.user)
        send_mail(
                form.instance.subject,  #subject
                form.instance.detail,  # message
                form.instance.email,  # from email
                ['goody@gmail.com']  # to email
                )
        context = super().form_valid(form)
        return context



def success_feedback_view(request):
    context = {
        'message':"Success",
    }
    template_name = "feedback/thanks.html"
    return render(request, template_name, context)

# def feedback_view(request):
#     if request.method == 'POST':
#         form = FeedbackForm(data = request.POST)
#         if form.is_valid():
#             pass
#     else:
#         form = FeedbackForm()
#     template_name = 'feedback/form.html'
#     context = {}
#     return render(request, template_name,context)

