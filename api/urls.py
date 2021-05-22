from . import views
from django.urls import path

urlpatterns = [
    path('series', views.ListSeries.as_view(), name='listseries'),
    path('series/<int:pk>', views.GetSeries.as_view(), name='getseries'),
    path('match/<int:pk>', views.GetMatch.as_view(), name='getmatch'),

]
