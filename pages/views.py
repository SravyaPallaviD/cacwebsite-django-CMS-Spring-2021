from django.http import HttpResponse
from django.shortcuts import render
from .models import Statistics
from .models import Slideshow
# Create your views here.
def home_view(request, *args, **kwargs):

	#stats = Statistics()
	#stats.peopleserved = 270234
	#stats.Childabusecases = 12343
	#stats.d2l = 2762
	stats = Statistics.objects.all()

   

	slides = Slideshow()	
	slides.img1 = "secret_santa.jpg"
	slides.img2 = "walk.jpg"
	slides.img3 = "d2l.jpg"

	#slides = Slideshow.objects.all()

	home_context = {'stat': stats,
					'slides':slides

					}
	return render(request, 'home.html', home_context)