from django.test import TestCase
from feedback.models import Feedback
from profiles.models import Profile
from django.contrib.auth.models import User


class FeedbackTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create(username='John', email ='john@gmail.com', password='testpassword')
        profile_data = Profile.objects.create(
            user = user1,
            first_name = 'John',
            last_name = 'Doe',
            level = '100lvl',
            interests ='Computers, Musics, Physics',
            department = 'Computer Science',
            bio = 'John Doe Bio',
            # photo = "user_John Doe/"
        )   
        
        Feedback.objects.create(
            profile = profile_data,
            subject = 'Complains',
            email = 'profile@gmail.com',
            detail = 'Feedback Complains',
            complain = True,
            happy = False
        )   


    def test_profile_field(self):
        feedback = Feedback.objects.get(id=1)
        label = feedback._meta.get_field('profile').verbose_name
        max_length = feedback._meta.get_field('profile').max_length
        self.assertEquals(label, 'profile')
        self.assertEquals(max_length, None)
        self.assertEquals(feedback.profile, Profile.objects.get(profile_id=1))

    def test_subject_field(self):
        feedback = Feedback.objects.get(id=1)
        label = feedback._meta.get_field('subject').verbose_name
        max_length = feedback._meta.get_field('subject').max_length
        help_text = feedback._meta.get_field('subject').help_text
        self.assertEquals(label, 'subject')
        self.assertEquals(max_length, 30)
        self.assertEquals(help_text, 'Feedback Topic')
        self.assertEquals(feedback.subject, 'Complains')
    
    def test_email_field(self):
        feedback = Feedback.objects.get(id=1)
        label = feedback._meta.get_field('email').verbose_name
        max_length = feedback._meta.get_field('email').max_length
        help_text = feedback._meta.get_field('email').help_text
        self.assertEquals(label, 'email')
        self.assertEquals(max_length, 254)
        self.assertEquals(help_text, 'Enter Your Email')
        self.assertEquals(feedback.email, 'profile@gmail.com')

    def test_detail_field(self):
        feedback = Feedback.objects.get(id=1)
        label = feedback._meta.get_field('detail').verbose_name
        max_length = feedback._meta.get_field('detail').max_length
        help_text = feedback._meta.get_field('detail').help_text
        self.assertEquals(label, 'Text')
        self.assertEquals(max_length, None)
        self.assertEquals(help_text, 'Enter Message')
        self.assertEquals(feedback.detail, 'Feedback Complains')        


    def test_complain_field(self):
        feedback = Feedback.objects.get(id=1)
        label = feedback._meta.get_field('complain').verbose_name
        self.assertEquals(feedback.complain, True)

    def test_happy_field(self):
        feedback = Feedback.objects.get(id=1)
        label = feedback._meta.get_field('happy').verbose_name
        self.assertEquals(feedback.happy, False)
