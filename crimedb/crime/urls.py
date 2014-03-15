from django.conf.urls import patterns, url

from crime import views

urlpatterns = patterns('',
    url(r'^$', views.homepage, name='homepage'),
#Report
    url(r'^report/$', views.report_crime, name='report_crime'),
#
    url(r'^crimes/$', views.crimes, name='crimes'),
    url(r'^crimes/(?P<report_id>\d+)/$', views.crimes_detail, name='crimes_detail'),
    url(r'^crimes/(?P<report_id>\d+)/delete/$', views.crimes_delete, name='crimes_delete'),
    url(r'^crimes/(?P<report_id>\d+)/edit/$', views.crimes_edit, name='crimes_edit'),
#
#Suspect
    url(r'^suspects/$', views.suspects, name='suspects'),
    url(r'^suspects/(?P<suspect_id>\d+)/$', views.suspects_detail, name='suspects_detail'),
    url(r'^suspects/add/$', views.suspects_add, name='suspects_add'),
    url(r'^suspects/(?P<suspect_id>\d+)/delete/$', views.suspects_delete, name='suspects_delete'),
    url(r'^suspects/(?P<suspect_id>\d+)/edit/$', views.suspects_edit, name='suspects_edit'),	
#Agent
    url(r'^agents/$', views.agents, name='agents'),
    url(r'^agents/(?P<agent_id>\d+)/$', views.agents_detail, name='agents_detail'),	
    url(r'^agents/add/$', views.agents_add, name='agents_add'),
    url(r'^agents/(?P<agent_id>\d+)/delete/$', views.agents_delete, name='agents_delete'),
    url(r'^agents/(?P<agent_id>\d+)/edit/$', views.agents_edit, name='agents_edit'),
#Category
    url(r'^addcategory/$', views.add_category, name='add_category'),
#
#Location
	url(r'^locations/$', views.locations, name='locations'),
    url(r'^locations/(?P<loc_id>\d+)/$', views.locations_detail, name='locations_detail'),   
#
#Search
	url(r'^search/$', views.search, name='search'),

    url(r'^thanks/$', views.thanks, name='thanks'),
    
)