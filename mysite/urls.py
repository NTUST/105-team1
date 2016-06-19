from django.conf.urls import patterns, include, url
from django.contrib import admin
from plants.views import plantlist,plant1,plant2,plant3,plant4,plant5,plant6,plant7,plant8,plant9,plant10,plant11,plant12,plant13,plant14,plant15
from homepage.views import home,link,photo,introduce,newbie
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^plantlist/$', plantlist),
    url(r'^homepage/$', home),
    url(r'^link/$', link),    
    url(r'^introduce/$', introduce),
    url(r'^newbie/$', newbie),
    url(r'^photo/$', photo),
    url(r'^七福神圖鑑詳細資料/$', plant1),
    url(r'^月兔耳圖鑑詳細資料/$', plant2),
    url(r'^玉露圖鑑詳細資料/$', plant3),
    url(r'^生石花圖鑑詳細資料/$', plant4),
    url(r'^白鳳菊圖鑑詳細資料/$', plant5),
    url(r'^星兜圖鑑詳細資料/$', plant6),
    url(r'^虹之玉圖鑑詳細資料/$', plant7),
    url(r'^姬星美人圖鑑詳細資料/$', plant8),
    url(r'^球松圖鑑詳細資料/$', plant9),
    url(r'^雪蓮圖鑑詳細資料/$', plant10),
    url(r'^熊童子圖鑑詳細資料/$', plant11),
    url(r'^碧光環圖鑑詳細資料/$', plant12),
    url(r'^錦上珠圖鑑詳細資料/$', plant13),
    url(r'^露娜蓮圖鑑詳細資料/$', plant14),
    url(r'^鷹爪圖鑑詳細資料/$', plant15),
    
)


urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)






    
