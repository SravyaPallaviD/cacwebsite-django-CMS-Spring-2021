from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
from django.core import mail
from .models import Statistics
from .models import Image1
from .models import Image2
from .models import Image3
from .models import Statisticscannon
from .models import Team, ExecutiveCommittee, BoardMember, Event, EventTopImage, PressRelease, NewsLetter


# Create your views here.
#view for header and footer that is common for all the pages
def header_footer_view(request, *args, **kwargs):
	return render(request, 'header_and_footer.html', {})
# view for cannon services page
def cannon_services_view(request, *args, **kwargs):

	obj4 = Statisticscannon.objects.get(id=1)

	cannoncontext = {
					'peopleservedcannon': obj4.peopleservedcannon,
					'Childabusecasescannon': obj4.Childabusecasescannon,
	}

	return render(request, 'cannon-services.html', cannoncontext)

# view for rutherford services page
def rutherford_services_view(request, *args, **kwargs):
	return render(request, 'rutherford-services.html',{})

# view for darkness to light for Rutherford.
def d2l_view(request, *args, **kwargs):
	return render(request, 'd2l.html', {})

# view for schedule training page which is displayed when we click on schedule training on darkness to light page.
# This is common for Rutherford and cannon counties as the url for both the pages are same.
def d2l_schedule_training_view(request, *args, **kwargs):
	return render(request,'d2l_schedule_training.html',{})

# view for attend training page which is displayed when we click on attend training on darkness to light page.
# This is common for Rutherford and cannon counties as the url for both the pages are same.
def d2l_attend_training_view(request, *args, **kwargs):
	return render(request, 'd2l_attend_training.html', {})

# view for Rutherford county cpit page
def rutherford_cpit_view(request, *args, **kwargs):
	return render(request, 'rutherford_cpit.html', {})

# view for darkness to light for cannon county.
def cannon_d2l_view(request, *args, **kwargs):
	return render(request, 'd2l.html', {})

# view for cannon cpit team.
def cannon_cpit_view(request, *args, **kwargs):
	return render(request, 'cannon_cpit.html', {})

# view for our team page
def teams_view(request, *args, **kwargs):
	objs5 = Team.objects.all()
	objs6 = ExecutiveCommittee.objects.all()
	objs7 = BoardMember.objects.all()

	team_context = {
					'objs5': objs5 ,
					'objs6': objs6,
					'objs7': objs7,
	}
	return render(request, 'our_team.html', team_context)

# view for ourteam community partners page
def ourteam_communitypartners_view(request, *args, **kwargs):
	return render(request, 'ourteam_communitypartners.html', {})

# view for Family services page
def family_services_view(request, *args, **kwargs):
	return render(request, 'family_services.html', {})

# view for events page
def events_view(request, *args, **kwargs):
	objs8 = Event.objects.all()
	obj9 = EventTopImage.objects.get(id=1)
	events_context = {
						'objs8' : objs8,
						'obj9' : obj9,
	}
	return render(request, 'events.html', events_context)

# views for getinvolved page
def getinvolved_view(request, *args, **kwargs):
	return render(request, 'get_involved.html', {})

# view for getinvolved volunteer page.
def getinvolved_volunteer_view(request, *args, **kwargs):
	return render(request, 'getinvolved_volunteer.html', {})
# view for darkness to light page redirected from getinvolved page
def getinvolved_d2l_view(request, *args, **kwargs):
	return render(request, 'd2l.html', {})
# view for host an event page
def getinvolved_hostanevent_view(request, *args, **kwargs):
	return render(request, 'getinvolved_host_event.html', {})

# views for volunteer page under get involved nav bar.
def gi_volunteer_view(request, *args, **kwargs):
	return render(request, 'gi_volunteer.html', {})
# view for press releases page
def press_release_view(request, *args, **kwargs):
	objs10 = PressRelease.objects.all()
	pressreleases_context = {
							'objs10': objs10
	}
	return render(request, 'press_releases.html', pressreleases_context)
# view for downloading the file on press releases page
def download(request,path):
	file_path = os.path.join(settings.MEDIA_ROOT,path)
	if os.path.exists():
		with open(file_path,'rb') as fh:
			response = HttpResponse(fh.read(), content_type = "application/pages")
			response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
			return response
	raise Http404

# view for newsletters page.
def newsletter_view(request, *args, **kwargs):
	objs11 = NewsLetter.objects.all()
	newsletter_context = {
							'objs11' : objs11
	}
	return render(request, 'news_letters.html', newsletter_context)

# view for media information page.
def mediainfo_view(request, *args, **kwargs):
	return render(request, 'media_info.html', {})

# view for gratitude page
def gratitude_view(request, *args, **kwargs):
	objs12 = GratitudeCards.objects.all()
	
	gratitude_context = {
							'objs12' : objs12,
	}
	return render(request, 'gratitude.html', gratitude_context)

# view for home page.
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


#views for D2L attendTraining form that is functioning to send to client
def attendTraining(request):
	if request.method == 'POST':
		subject = "Darkness to Light : Attend Training"
		body = {
			'name':request.POST.get('name', ''),
			'address' : request.POST.get('address', ''),
			'city' : request.POST.get('city', ''),
			'state': request.POST.get('state', ''),
			'zipcode' : request.POST.get('zip', ''),
			'number' : request.POST.get('number', ''),
			
			}
		message = "\n".join(body.values())
		email = request.POST.get('email', '')			
		try:
			send_mail(subject, message, email,['imarree33@gmail.com'],fail_silently=False, html_message=None)
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
	return render(request, 'd2l_attend_training.html')

#views for D2L scheduleTraining form that is functioning to send to client
def scheduleTraining(request):
	if request.method == 'POST':
		subject = "Darkness to Light : Schedule Training"
		body = {
			'name':request.POST.get('name', ''),
			'organizationName' : request.POST.get('organizationName', ''),
			'address' : request.POST.get('address', ''),
			'city' : request.POST.get('city', ''),
			'state': request.POST.get('state', ''),
			'zipcode' : request.POST.get('zip', ''),
			'number' : request.POST.get('number', ''),
			'aboutEvent' : request.POST.get('aboutEvent', ''),
			
			}
		message = "\n".join(body.values())
		email = request.POST.get('email', '')			
		try:
			send_mail(subject, message, email,['imarree33@gmail.com'],fail_silently=False, html_message=None)
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
	return render(request, 'd2l_schedule_training.html')

#views for GI: Host Event form that is functioning to send to client
def hostEvent(request):
	if request.method == 'POST':
		subject = "Get Involved: Host Event"
		body = {
			'name':request.POST.get('name', ''),
			'organizationName' : request.POST.get('organizationName', ''),
			'address' : request.POST.get('address', ''),
			'citySTATEzip' : request.POST.get('citySTATEzip', ''),
			#'state': request.POST.get('state', ''),
			#'zipcode' : request.POST.get('zip', ''),
			'email' : request.POST.get('email', ''),
			'number' : request.POST.get('number', ''),
			'aboutEvent' : request.POST.get('aboutEvent', ''),
			
			}
		message = "\n".join(body.values())
		email = request.POST.get('email', '')			
		try:
			send_mail(subject, message, email,['imarree33@gmail.com'],fail_silently=False, html_message=None)
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
	return render(request, 'getinvolved_host_event.html')


#views for GI: Volunteer an Event form that is functioning to send to client
def volunteerEvent(request):
	if request.method == 'POST':
		subject = "Get Involved: Volunteer for an Event"
		body = {
			'name':request.POST.get('name', ''),
			'number' : request.POST.get('number', ''),
			'email' : request.POST.get('email', ''),
			'volunteerType' : request.POST.get('volunteerType', ''),
			
			}
		message = "\n".join(body.values())
		email = request.POST.get('email', '')			
		try:
			send_mail(subject, message, email,['imarree33@gmail.com'],fail_silently=False, html_message=None)
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
	return render(request, 'getinvolved_volunteer.html')
