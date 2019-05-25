from django.test import TestCase
from profiles.models import Profile
from django.contrib.auth.models import User

class ProfileTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create(username='John', email ='john@gmail.com', password='testpassword')
        Profile.objects.create(
            user = user1,
            first_name = 'John',
            last_name = 'Doe',
            level = '100lvl',
            interests ='Computers, Musics, Physics',
            department = 'Computer Science',
            bio = 'John Doe Bio',
            # photo = "user_John Doe/"
        )

    def test_user_field(self):
        profile = Profile.objects.get(profile_id=1)
        field_label = profile._meta.get_field('user').verbose_name
        max_length = profile._meta.get_field('user').max_length
        self.assertEquals(field_label, 'user')
        self.assertEquals(max_length, None)
        self.assertEquals(profile.user,User.objects.get(id=1))

    def test_first_name_field(self):
        profile = Profile.objects.get(profile_id = 1)
        field_label = profile._meta.get_field('first_name').verbose_name
        max_length = profile._meta.get_field('first_name').max_length
        self.assertEquals(field_label, 'first name')
        self.assertEquals(max_length, 255)
        self.assertEquals(profile.first_name, 'John')

    def test_last_name_field(self):
        profile = Profile.objects.get(profile_id=1)
        field_label = profile._meta.get_field('last_name').verbose_name
        max_length = profile._meta.get_field('last_name').max_length
        self.assertEquals(field_label, 'last name')
        self.assertEquals(max_length, 255)
        self.assertEquals(profile.last_name, 'Doe')

    def test_level_field(self):
        profile = Profile.objects.get(profile_id=1)
        field_label = profile._meta.get_field('level').verbose_name
        max_length = profile._meta.get_field('level').max_length
        self.assertEquals(field_label, 'level')
        self.assertEquals(max_length, 40)
        self.assertEquals(profile.level, '100lvl')

    def test_interests_field(self):
        profile = Profile.objects.get(profile_id=1)
        field_label = profile._meta.get_field('interests').verbose_name
        max_length = profile._meta.get_field('interests').max_length
        help_text = profile._meta.get_field('interests').help_text
        self.assertEquals(field_label, 'interests')
        self.assertEquals(max_length, 255)
        self.assertEquals(profile.interests, 'Computers, Musics, Physics')
        self.assertEquals(help_text, 'Seperated by commas e.t.c Music, Maths, Computers')

    def test_dept_field_label(self):
        profile = Profile.objects.get(profile_id=1)
        field_label = profile._meta.get_field('department').verbose_name
        max_length = profile._meta.get_field('department').max_length
        self.assertEquals(field_label, 'department')
        self.assertEquals(max_length, 40)
        self.assertEquals(profile.department, 'Computer Science')

    def test_bio_field_label(self):
        profile = Profile.objects.get(profile_id=1)
        field_label = profile._meta.get_field('bio').verbose_name
        max_length = profile._meta.get_field('bio').max_length
        help_text = profile._meta.get_field('bio').help_text
        self.assertEquals(field_label, 'bio')
        self.assertEquals(max_length, None)
        self.assertEquals(profile.bio,'John Doe Bio')
        self.assertEquals(help_text, 'Short Bio Of Your Self')
        
    

    def test_model_string_repr(self):
        profile = Profile.objects.get(profile_id=1)
        string = '{} {}'.format(profile.first_name, profile.last_name)
        self.assertEquals(string, str(profile))


    def test_get_absolute_url(self):
        profile = Profile.objects.get(profile_id=1)
        # self.assertEquals(profile.get_absolute_url(), '/profile')
