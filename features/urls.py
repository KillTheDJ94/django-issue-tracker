from django.conf.urls import url
from features.views import features, create_or_edit_feature, feature_detail, feature_like, feature_dislike

urlpatterns = [
    url(r'^$', features, name='features'),
    url(r'^new_feature_request/$', create_or_edit_feature, name="new_feature"),
    url(r'^(?P<pk>\d+)/$', feature_detail, name="feature_detail"),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_feature, name= "edit_feature"),
    url(r'^(?P<pk>\d+)/likes/$', feature_like, name='feature_like'),
    url(r'^(?P<pk>\d+)/dislikes/$', feature_dislike, name='feature_dislike'),
    ]