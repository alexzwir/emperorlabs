from django.conf.urls import include, url
from django.contrib import admin
from website.core import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$/', core.views),
    url(r'^admin/', include(admin.site.urls)),
]
