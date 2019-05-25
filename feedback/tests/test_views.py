from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from feedback.views import (
    FeedBackCreateView,
    success_feedback_view
)

from feedback.models import Feedback
from profiles.models import Profile

class FeedbackViewTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
                username="testuser", 
                email="test@email.com", 
                password="testpassword"
        )
        self.test_user.save()
        self.test_profile = Profile.objects.create(
            user = self.test_user,
            first_name = 'John',
            last_name = 'Doe',
            level = '100lvl',
            interests ='Computers, Musics, Physics',
            department = 'Computer Science',
            bio = 'John Doe Bio',
            # photo = "user_John Doe/"
        )


    
    def tearDown(self):
        for feedback in Feedback.objects.all():
            feedback.delete()
    
    def test_get_feedback_create_view(self):
        login = self.client.login(username="test@gmail.com",password="testpassword")
        response = self.client.get(reverse('feedback:feedback_form'))
        self.assertTemplateUsed(response, 'feedback/form.html')
        # self.assertEquals

    def test_get_feedback_success_view(self):
        login = self.client.login(username="test@gmail.com",password="testpassword")
        response = self.client.get(reverse('feedback:success_message'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedback/thanks.html')
        self.assertContains(response, 'Thanks For Submiting The Form')
        
    # def test_post_feedback_create_view(self):
    #     login = self.client.login(username="test@gmail.com",password="testpassword")
    #     response = self.client.post(reverse('feedback:feedback_form'), {
    #         # 'profile': self.test_profile,
    #         'subject':'Feedback Topic',
    #         'email':'feed@gmail.com',
    #         'detail':'Feedback Content',
    #         # 'complain':False,
    #         # 'happy':True
    #     })
    #     self.assertEquals(response.status_code, 200)

        # print(response)
        # self.assertContains(response, 'Feedback Topic')
        # self.assertContains(response, 'feed@gmail.com')
        # # self.assertContains(response, False)
        # # self.assertContains(response, True)
        # test@email.com
