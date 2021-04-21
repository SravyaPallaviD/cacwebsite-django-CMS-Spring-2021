from django.urls import path

from .import views

urlpatterns = [
			path('',views.home_view),
<<<<<<< HEAD
			path('attendtraining/' , views.attendTraining),
    			path('scheduletraining/' , views.scheduleTraining),
    			path('host-event/' , views.hostEvent),
    			path('volunteer-event/' , views.volunteerEvent),
			
			]
=======
			]
>>>>>>> 18140e79ee359a5792e322ec4efb24b84de933b3
