from django.conf.urls import url
from django.conf import settings
import maps.views

urlpatterns = [

    url(r'^usefaircoin/$', maps.views.map, name="usefaircoin"),

]
