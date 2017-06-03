from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from registration.backends.simple.views import RegistrationView
from django.contrib.auth import views as auth_views

class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/rango/'


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),  # ADD THIS NEW TUPLE!
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),

    url(r'^accounts/', include('registration.backends.simple.urls')),

url(r'^accounts/password/reset$', 'django.contrib.auth.views.password_reset_done',
   name='password_reset_done'),

url(r'^$', 'rango.views.index', name="index"),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )