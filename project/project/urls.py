from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^home/$', 'irb.views.home', name='home'),
	url(r'^home/options_pd/$', 'irb.views.options_pd', name='options_pd'),
	url(r'^home/options_ed/$', 'irb.views.options_ed', name='options_ed'),
	url(r'^home/options_qf/$', 'irb.views.options_qf', name='options_qf'),
	url(r'^home/options_in/$', 'irb.views.options_in', name='options_in'),
	url(r'^home/options_pr/$', 'irb.views.options_pr', name='options_pr'),
	url(r'^home/options_coxco/$', 'irb.views.options_coxco', name='options_coxco'),
	url(r'^home/options_inp/$', 'irb.views.options_inp', name='options_inp'),
	url(r'^home/options_ref/$', 'irb.views.options_ref', name='options_ref'),


    url(r'^admin/', include(admin.site.urls)),
) 

