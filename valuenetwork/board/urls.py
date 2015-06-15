from django.conf.urls import patterns, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns("",
    url(r'^dhen-board/(?P<context_agent_id>\d+)/$', 'valuenetwork.board.views.dhen_board', name="dhen_board"),
    url(r'^add-available/(?P<context_agent_id>\d+)/(?P<assoc_type_identifier>\w+)/$', 'valuenetwork.board.views.add_available', 
        name="add_available"),
    url(r'^transfer-resource/(?P<context_agent_id>\d+)/(?P<resource_id>\d+)/(?P<assoc_type_identifier>\w+)/$', 
        'valuenetwork.board.views.transfer_resource', name="transfer_resource"),
)