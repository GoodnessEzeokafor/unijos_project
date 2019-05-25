from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from profiles.views import (
    CreateProfileView,
    UpdateProfileView,
    DeleteProfileView,
    dashboard,
    delete_success
)
from profiles.models import Profile


class ProfileTestView(TestCase):
    
    def setUp(self):
        self.test_user = User.objects.create_user(username="testuser", email="test@email.com", password="testpassword")
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
        for profile in Profile.objects.all():
            profile.delete()
    
    def test_redirect_if_dont_have_profile(self):
        response = self.client.get(reverse('profiles:profile_dashboard'))
        self.assertRedirects(response, '/profile/create/')
        self.assertEquals(response.status_code, 302)

    def test_redirect_if_have_profile(self):
        login = self.client.login(username='test@email.com', password="testpassword")
        response = self.client.get(reverse('profiles:profile_dashboard'))
        self.assertEquals(login, True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(str(response.context['user']), 'testuser')
        self.assertEquals(str(response.context['profile']), 'John Doe')
        self.assertTemplateUsed(response, 'profile/dashboard.html')
    
    def test_redirect_if_not_logged_in(self):
        response = self.client.get('')
        self.assertEquals(response.url, '/accounts/login')
        self.assertEquals(response.status_code, 302)
    
    def test_get_create_profile_view(self):
        login = self.client.login(username='test@email.com', password="testpassword")
        response = self.client.get('/profile/create/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/create.html')
    
    def test_get_delete_profile_view(self):
        profile = Profile.objects.get(profile_id=1)
        login = self.client.login(username='test@email.com', password="testpassword")
        response = self.client.get('/profile/delete/{}/'.format(profile.profile_id))
        self.assertTemplateUsed(response , 'profile/delete.html')
        self.assertEquals(response.status_code, 200)
        




