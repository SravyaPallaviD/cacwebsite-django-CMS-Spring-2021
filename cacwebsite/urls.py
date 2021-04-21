"""cacwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# imports for downloading the documents on press releases page
from django.conf.urls import url
from django.views.static import serve
from pages.views import home_view
from pages.views import header_footer_view
from pages.views import cannon_services_view, rutherford_services_view,d2l_view
from pages.views import d2l_schedule_training_view, d2l_attend_training_view, rutherford_cpit_view, cannon_d2l_view, cannon_cpit_view
from pages.views import teams_view, family_services_view, events_view, getinvolved_view, getinvolved_volunteer_view
from pages.views import getinvolved_d2l_view, getinvolved_hostanevent_view, press_release_view,newsletter_view, mediainfo_view, gratitude_view, contactus_view,board_of_directors_view
urlpatterns = [
	path('', home_view),
	path('home/',home_view),
	path('cannon_services/',cannon_services_view),
	path('rutherford_services/',rutherford_services_view),
	path('rutherford_services/d2l/',d2l_view),
	path('rutherford_services/d2l/d2l_schedule_training/', d2l_schedule_training_view, name = "d2l_schedule_training"),
	path('rutherford_services/d2l/d2l_attend_training/', d2l_attend_training_view, name = "d2l_attend_training"),
	path('rutherford_services/cpit/',rutherford_cpit_view),
	path('cannon_services/d2l/',cannon_d2l_view),
	path('cannon_services/cpit/',cannon_cpit_view),
	path('our_team/', teams_view, name = "our_team" ),
	path('our_team/contactus/', contactus_view, name = "contactus"),
	path('our_team/board_of_directors/', board_of_directors_view),
	path('family_services/', family_services_view),
	path('events/', events_view),
	path('get_involved/', getinvolved_view),
	path('get_involved/getinvolved_volunteer/', getinvolved_volunteer_view, name = "get_involved_volunteer"),
	path('get_involved/d2l/', getinvolved_d2l_view),
	path('get_involved/getinvolved_host_event/', getinvolved_hostanevent_view, name = "host_an_event"),
	#path('get_involved/getinvolved_volunteer/', gi_volunteer_view, name = "get_involved_volunteer"),
	path('press_releases/', press_release_view),
	# path for downloading the files on press releases page
	url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
	path('press_releases/news_letters/', newsletter_view),
	path('press_releases/media_info/', mediainfo_view),
	path('gratitude/', gratitude_view),
    path('admin/', admin.site.urls),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)