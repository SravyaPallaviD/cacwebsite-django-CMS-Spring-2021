from django.http import HttpResponse
from django.shortcuts import render
from .models import Statistics
from .models import Image1
from .models import Image2
from .models import Image3
from .models import Statisticscannon


# Create your views here.
def header_footer_view(request, *args, **kwargs):
	return render(request, 'header_and_footer.html', {})

def cannon_services_view(request, *args, **kwargs):

	obj4 = Statisticscannon.objects.get(id=1)

	cannoncontext = {
					'peopleservedcannon': obj4.peopleservedcannon,
					'Childabusecasescannon': obj4.Childabusecasescannon,
	}

	return render(request, 'cannon-services.html', cannoncontext)

def rutherford_services_view(request, *args, **kwargs):
	return render(request, 'rutherford-services.html',{})
def d2l_view(request, *args, **kwargs):
	return render(request, 'd2l.html', {})
def d2l_schedule_training_view(request, *args, **kwargs):
	return render(request,'d2l_schedule_training.html',{})
def d2l_attend_training_view(request, *args, **kwargs):
	return render(request, 'd2l_attend_training.html', {})
def rutherford_cpit_view(request, *args, **kwargs):
	return render(request, 'rutherford_cpit.html', {})
def cannon_d2l_view(request, *args, **kwargs):
	return render(request, 'd2l.html', {})
def cannon_cpit_view(request, *args, **kwargs):
	return render(request, 'cannon_cpit.html', {})


def home_view(request, *args, **kwargs):

	obj = Statistics.objects.get(id=3)
	obj1 = Image1.objects.get(id = 1)
	obj2 = Image2.objects.get(id = 1)
	obj3 = Image3.objects.get(id = 1)

	context = {
			'peopleserved': obj.peopleserved,
			'Childabusecases': obj.Childabusecases,
			'd2l': obj.d2l,
			'img1': obj1.img1,
			'btn_text1': obj1.btn_text1,
			'btn_link1': obj1.btn_link1,
			'img2': obj2.img2,
			'btn_text2': obj2.btn_text2,
			'btn_link2': obj2.btn_link2,
			'img3': obj3.img3,
			'btn_text3': obj3.btn_text3,
			'btn_link3': obj3.btn_link3,
			

	}
	return render(request, 'home.html', context)