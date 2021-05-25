from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.AllUrls.as_view(), name='allurls'),
    path('series/', views.ListSeries.as_view(), name='listseries'),
    path('series/<int:pk>', views.GetSeries.as_view(), name='getseries'),
    path('match/<int:pk>', views.GetMatch.as_view(), name='getmatch'),
    path('players/<int:pk>', views.GetPlayers.as_view(), name='getplayers'),

]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
