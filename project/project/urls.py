from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^home/$', 'irb.views.home', name='home'),
	url(r'^home/options_pd/$', 'irb.views.resume_options_pd', name='options_pd'),

    url(r'^admin/', include(admin.site.urls)),
) 

