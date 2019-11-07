from django.conf.urls import url
from . import views

app_name = "shaver_mgt_ns"

urlpatterns = [
    url(r'^$', views.add_shaver, name="addshaver"),
    url(r'^editshaver/$', views.edit_shaver, name="editshaver"),
    url(r'^deleteshaver/$', views.delete_shaver, name='deleteshaver'),
]

