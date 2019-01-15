#!/usr/bin/python
# -*- coding: utf-8 -*-

from models import UseFaircoin
from work.utils import *
from work.forms import *
from valuenetwork.valueaccounting.models import *
from valuenetwork.valueaccounting.views import *

def map(request):
    agent = get_agent(request)
    locations = UseFaircoin.objects.all()
    nolocs = UseFaircoin.objects.filter(latitude=0.0)
    latitude = settings.MAP_LATITUDE
    longitude = settings.MAP_LONGITUDE
    zoom = settings.MAP_ZOOM
    return render(request, "maps/map.html", {
        "agent": agent,
        "locations": locations,
        "nolocs": nolocs,
        "latitude": latitude,
        "longitude": longitude,
        "zoom": zoom,
        #"help": get_help("work_map"),
    })
