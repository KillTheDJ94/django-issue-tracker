from django.conf.urls import url
from features.views import features, create_or_edit_feature, feature_detail, feature_like, feature_dislike, feature_request_to_do, feature_request_investigated, feature_request_in_development, feature_request_in_testing, delete_feature

urlpatterns = [
    url(r'^$', features, name='features'),
    url(r'^new_feature_request/$', create_or_edit_feature, name="new_feature"),
    url(r'^(?P<pk>\d+)/$', feature_detail, name="feature_detail"),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_feature, name= "edit_feature"),
    url(r'^(?P<pk>\d+)/likes/$', feature_like, name='feature_like'),
    url(r'^(?P<pk>\d+)/dislikes/$', feature_dislike, name='feature_dislike'),
    url(r'^features_to_do/$', feature_request_to_do, name='feature_request_to_do'),
    url(r'^features_investigated/$', feature_request_investigated, name='feature_request_investigated'),
    url(r'^features_in_development/$', feature_request_in_development, name='feature_request_in_development'),
    url(r'^features_in_testing/$', feature_request_in_testing, name='feature_request_in_testing'),
    url(r'^new_feature_request/$', create_or_edit_feature, name="new_feature"),
    url(r'^(?P<pk>\d+)/delete/$', delete_feature, name="delete_feature"),
    ]