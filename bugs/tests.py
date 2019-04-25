from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bugs.views import bugs, bug_status_to_do, bug_detail, bug_status_investigated, bug_status_in_development, bug_status_in_testing

class TestUrls(SimpleTestCase):
    def test_get_bugs_url_is_resolved(self):
        url = reverse('bugs')
        print(resolve(url))
        self.assertEquals(resolve(url).func, bugs)
        
    def test_bug_status_to_do_is_resolved(self):
        url = reverse('bug_status_to_do')
        print(resolve(url))
        self.assertEquals(resolve(url).func, bug_status_to_do)
        
    def test_bug_status_investigated_is_resolved(self):
        url = reverse('bug_status_investigated')
        print(resolve(url))
        self.assertEquals(resolve(url).func, bug_status_investigated)
        
    def test_bug_status_in_development_is_resolved(self):
        url = reverse('bug_status_in_development')
        print(resolve(url))
        self.assertEquals(resolve(url).func, bug_status_in_development)
        
    def test_bug_status_in_testing_is_resolved(self):
        url = reverse('bug_status_in_testing')
        print(resolve(url))
        self.assertEquals(resolve(url).func, bug_status_in_testing)
