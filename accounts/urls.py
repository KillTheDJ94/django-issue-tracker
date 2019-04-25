from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_bug_profile, user_feature_profile
from accounts import urls_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^password-reset/', include(urls_reset)),
    url(r'^user_bug_profile/', user_bug_profile, name="user_bug_profile"),
    url(r'^user_feature_profile/', user_feature_profile, name="user_feature_profile"),
    ]