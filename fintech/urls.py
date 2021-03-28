from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from myapp.views import sayhello,hello3,hello4,fv,fv2

# 2021.0320 add import from ref :
#https://docs.djangoproject.com/en/2.0/howto/static-files/
from django.conf import settings
from django.conf.urls.static import static

# 2021.0326 add views from linebotLUIS\luisapi\views 
from myapp import views

urlpatterns = [
    url('^callback', views.callback),
    path('admin/', admin.site.urls),
    url(r'^$', sayhello), 
    url(r'^hello3/(\w+)/$', hello3), 
    url(r'^hello4/(\w+)/$', hello4),
    url(r'^fv/$', fv),		
    url(r'^fv2/$', fv2),	
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
