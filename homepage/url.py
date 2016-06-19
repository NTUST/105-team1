from django.conf.urls import patterns, include, url
from django.contrib import admin
from plants.views import plantlist
from homepage.views import home,link,photo

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('homepage.views',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^plantlist/$', plantlist),
    url(r'^homepage/$', home),
    url(r'^link/$', link),
    url(r'^photo/$', photo),


   
    
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)






    
