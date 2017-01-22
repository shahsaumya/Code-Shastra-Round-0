from django.conf.urls import include, url
from django.contrib import admin
from hunt_app import views
from rest_framework.urlpatterns import format_suffix_patterns
from hunt_app import views 


urlpatterns = [
    # Examples:
    # url(r'^$', 'great_game.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', views.index),
    url(r'^panel/', views.panel),
    url(r'^team-json/', views.TeamList.as_view()),
    url(r'^task-json/', views.TaskList.as_view()),
    url(r'^timer/', views.CountdownTimer),
    url(r'^table/', views.table),
    url(r'^chart/', views.map),





]

urlpatterns = format_suffix_patterns(urlpatterns)