from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User
from profiles.models import Profile
# print(help(TestCase))


class BaseModelTest(TestCase):
    @classmethod

    def setUpClass(cls):
        super(BaseModelTest, cls).setUpClass()
        cls.user = User.objects.create(
                    username="Goody",
                    email="goody@gmail.com",
                    password="pythonadmin"
        )
        cls.profile = Profile(
            user = cls.user,
            first_name = 'Goodness',
            last_name = 'Ezeokafor',
            level = "100lvl",
            interests = "Computer",
            department = "Computer Science"
        )
        # cls.user.save()
        cls.profile.save()
class ProfileModelTestCase(BaseModelTest):

    def test_created_properly(self):
        # self.assertEqual(self.profile.user, <User: Goody>)
        self.assertEqual(self.profile.first_name, 'Goodness')
        self.assertEqual(self.profile.last_name, 'Ezeokafor')
        self.assertEqual(self.profile.level, '100lvl')
        self.assertEqual(self.profile.interests, 'Computer')
        self.assertEqual(self.profile.department, 'Computer Science')
    

    def test_model_fields(self):
        pass
        # print(help(Profile))        
        # self.assertEqual(self.profile.field_name['first_name'], 'first_name')
        # print(self.profile.)
