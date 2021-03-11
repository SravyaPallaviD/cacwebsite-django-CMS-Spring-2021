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
from pages.views import home_view
from pages.views import header_footer_view
from pages.views import cannon_services_view, rutherford_services_view,d2l_view
from pages.views import d2l_schedule_training_view, d2l_attend_training_view, rutherford_cpit_view, cannon_d2l_view, cannon_cpit_view

urlpatterns = [
	path('', home_view),
	path('cannon_services/',cannon_services_view),
	path('rutherford_services/',rutherford_services_view),
	path('rutherford_services/d2l/',d2l_view),
	path('rutherford_services/d2l/d2l_schedule_training/', d2l_schedule_training_view),
	path('rutherford_services/d2l/d2l_attend_training/', d2l_schedule_training_view),
	path('rutherford_services/cpit',rutherford_cpit_view),
	path('cannon_services/d2l/',cannon_d2l_view),
	path('cannon_services/cpit',cannon_cpit_view),
    path('admin/', admin.site.urls),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)