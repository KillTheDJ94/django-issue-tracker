from django.test import SimpleTestCase
from django.urls import reverse, resolve
from features.views import feature_request_to_do, feature_request_investigated, feature_request_in_development, feature_request_in_testing, features 

class TestUrls(SimpleTestCase):
    def test_feature_request_all_features_is_resolved(self):
        url = reverse('features')
        print(resolve(url))
        self.assertEquals(resolve(url).func, features)
        
    def test_feature_request_to_do_is_resolved(self):
        url = reverse('feature_request_to_do')
        print(resolve(url))
        self.assertEquals(resolve(url).func, feature_request_to_do)
        
    def test_feature_request_investigated_is_resolved(self):
        url = reverse('feature_request_investigated')
        print(resolve(url))
        self.assertEquals(resolve(url).func, feature_request_investigated)
        
    def test_feature_request_in_development_is_resolved(self):
        url = reverse('feature_request_in_development')
        print(resolve(url))
        self.assertEquals(resolve(url).func, feature_request_in_development)
        
    def test_feature_request_in_testing_is_resolved(self):
        url = reverse('feature_request_in_testing')
        print(resolve(url))
        self.assertEquals(resolve(url).func, feature_request_in_testing)