from django.conf.urls import url
from basic_app import views

# Template tagging
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$',views.rel_url_template,name='relative'),
    url(r'^other/$',views.other,name='other'),
    url(r'^index/$',views.index,name="index"),
]