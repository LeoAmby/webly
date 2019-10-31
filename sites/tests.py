from django.test import TestCase
from .models import Project, Profile

# Create your tests here.
class ProjectTest(Testcase):
    def test_instance(self):
        self.assertTrue(isinstance(self.photo, Project))
    
    
    def test_save(self):
        self.photo.save_image()
        self.assertTrue(Project.photo)


    def setUp(self):
        self.akan = Profile(name = 'akan')


    def delete_photo(self):
        Project.photo_name.remove(self)

  
class ProfileTest(TestCase):
    def setUp(self):
        self.image = Profile(id = 'image')
        self.bio = Profile(bio = 'bio')
    

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Profile))
        self.assertTrue(isinstance(self.bio,Profile))


    def test_save(self):
        self.image.save_image()
        self.assertTrue(Profile.user.username)

    def delete_profile(self):
        Profile.profile_image.remove(self)
        Profile.profile_bio.remove(self)

