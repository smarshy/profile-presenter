from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^smarshy/', include ('my_profile.urls', namespace='my_profile')),
    url(r'^analyse/', include ('general_analysis.urls', namespace='general_analysis')),
    url(r'^$',views.home,name='home'),
]
