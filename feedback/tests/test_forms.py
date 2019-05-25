from django.test import TestCase
from feedback.forms import FeedbackForm
from django.forms.fields import CharField

class FeedbackFormTestCase(TestCase):
    def test_subject_field(self):
        form = FeedbackForm(data={'subject':'Happy'})
        self.assertTrue(form.fields['subject'].label == None or 'subject')
        self.assertTrue(form.fields['subject'].max_length == 30)
        self.assertTrue(form.fields['subject'].help_text == 'Feedback Topic')
      

    def test_email_field(self):
        form = FeedbackForm(data={'email':'feed@gmail.com'})
        self.assertTrue(form.fields['email'].label == None or 'email')
        self.assertTrue(form.fields['email'].max_length == 254)
        self.assertTrue(form.fields['email'].help_text == 'Enter Your Email')
    

    def test_detail_field(self):
        form = FeedbackForm(data={'detail':'Nice Platform'})
        self.assertTrue(form.fields['detail'].label == None or 'Text')
        self.assertTrue(form.fields['detail'].max_length == None)
        self.assertTrue(form.fields['detail'].help_text == 'Enter Message')


    def test_happy_field(self):
        form = FeedbackForm(data={'detail':True})
        self.assertTrue(form.fields['happy'].label == None or 'happy')

    def test_complain_field(self):
        form = FeedbackForm(data={'complain':False})
        self.assertTrue(form.fields['complain'].label == None or 'complain')