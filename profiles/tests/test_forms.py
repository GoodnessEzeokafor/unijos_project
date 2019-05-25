from django.test import TestCase
from profiles.forms import ProfileForm


class ProfileFormTestCase(TestCase):
    

    def test_first_name_field(self):
        form = ProfileForm()
        self.assertTrue(form.fields['first_name'].label == None or 'first name')
        self.assertTrue(form.fields['first_name'].max_length == 255)
    

    def test_last_name_field(self):
        form 
    

    def test_level_field(self):
        pass
    
    def test_interest_field(self):
        pass
    
    def test_bio_field(self):
        pass
    
    def test_photo_field(self):
        pass

