import session_csrf
from django.conf.urls import patterns, include, url
from django.contrib import admin

session_csrf.monkeypatch()

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^_ah/', include('djangae.urls')),

                       # Note that by default this is also locked down with login:admin in app.yaml
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^csp/', include('cspreports.urls')),

                       url(r'', include('djangae.contrib.gauth.urls')),
                       url(r'', include('tracker.site.urls')),
                       )
