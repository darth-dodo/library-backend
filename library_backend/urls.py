from django.contrib import admin
from django.urls import path

from library_backend.settings.base import get_env_variable
from django.conf.urls import include, url
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('djadmin/', admin.site.urls),
    url(r'^auth/login/$', obtain_jwt_token),
    url(r'^accounts/', include('accounts.urls')),

]

if get_env_variable('DEBUG_MODE'):
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


admin.site.site_header = "The Library"
admin.site.site_title = "The Library"
admin.site.index_title = "Knowledge compounds by sharing!"
