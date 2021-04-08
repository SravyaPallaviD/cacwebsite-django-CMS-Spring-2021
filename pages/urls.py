from django.urls import path

from .import views

urlpatterns = [
			path('',views.home_view),
			path('attendtraining/' , views.attendTraining),
    			path('scheduletraining/' , views.scheduleTraining),
    			path('host-event/' , views.hostEvent),
    			path('volunteer-event/' , views.volunteerEvent),
			
			]
