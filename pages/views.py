<<<<<<< HEAD
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
from django.core import mail
from .models import Statistics
from .models import Image1
from .models import Image2
from .models import Image3
from .models import Statisticscannon
from .models import Team, ExecutiveCommittee, BoardMember, Event, EventTopImage, PressRelease, NewsLetter, Resource, Link
#from .models import Resource, Link
=======
from django.http import HttpResponse
from django.shortcuts import render
from .models import Statistics
from .models import SlideshowImages
from .models import Statisticscannon
from .models import Team, ExecutiveCommittee, BoardMember, Event, EventTopImage, PressRelease, NewsLetter, RutherfordService,CannonService,MediaInformation
from .models import DarknesstoLight,Imagesond2l, GratitudeCards, PostImage
from .forms import ContactusForm 
from django.core.mail import send_mail, BadHeaderError

>>>>>>> 18140e79ee359a5792e322ec4efb24b84de933b3

# Create your views here.
#view for header and footer that is common for all the pages
def header_footer_view(request, *args, **kwargs):
	return render(request, 'header_and_footer.html', {})
# view for cannon services page
def cannon_services_view(request, *args, **kwargs):

<<<<<<< HEAD
	obj4 = Statisticscannon.objects.get(id=1)
=======
	obj4 = Statisticscannon.objects.last()
	cannonservices = CannonService.objects.all()
>>>>>>> 18140e79ee359a5792e322ec4efb24b84de933b3

	cannoncontext = {
					'peopleservedcannon': obj4.peopleservedcannon,
					'Childabusecasescannon': obj4.Childabusecasescannon,
<<<<<<< HEAD
=======
					'cannonservices':cannonservices,
>>>>>>> 18140e79ee359a5792e322ec4efb24b84de933b3
	}

	return render(request, 'cannon-services.html', cannoncontext)

# view for rutherford services page
def rutherford_services_view(request, *args, **kwargs):
<<<<<<< HEAD
	return render(request, 'rutherford-services.html',{})

# view for darkness to light for Rutherford.
def d2l_view(request, *args, **kwargs):
	return render(request, 'd2l.html', {})
=======
	rutherfordservices = RutherfordService.objects.all()

	rutherford_context = {
							'rutherfordservices' : rutherfordservices,
	}
	return render(request, 'rutherford-services.html',rutherford_context)

# view for darkness to light for Rutherford.
def d2l_view(request, *args, **kwargs):
	d2l = DarknesstoLight.objects.last()
	imgd2l = Imagesond2l.objects.all()
	
	d2l_context = {
					'title': d2l.title,
					'description': d2l.description,
					'imgd2l':imgd2l,
					
				}
	return render(request, 'd2l.html', d2l_context)
>>>>>>> 18140e79ee359a5792e322ec4efb24b84de933b3

# view for schedule training page which is displayed when we click on schedule training on darkness to light page.
# This is common for Rutherford and cannon counties as the url for both the pages are same.
def d2l_schedule_training_view(request, *args, **kwargs):
<<<<<<< HEAD
	return render(request,'d2l_schedule_training.html',{})
=======
	teams = Team.objects.all()
	member = Team.objects.get(job_title='Drug Endangered Children Coordinator')
	if request.method == "POST":
		toEmail =[Team.objects.get(job_title = 'Drug Endangered Children Coordinator').email]
		message_subject = "Darkness to light schedule a training"
		user_name = request.POST["name"]
		org_name = request.POST["organizationname"]
		user_address = request.POST["address"]
		user_city = request.POST["city"]
		user_state = request.POST["state"]
		user_zip = request.POST["zip"]
		user_number = request.POST["phonenumber"]
		mail = request.POST["userEmail"]
		event_details = request.POST["aboutevent"]

		message = "Name:" + user_name + '\n'
		message += "Organization Name:" + org_name + '\n'
		message += "Address:" + user_address +'\n'
		message += "City:" + user_city + '\n'
		message += "State:" + user_state + '\n'
		message += "Zip:" + user_zip + '\n'
		message += "Phone Number:" + user_number + '\n'
		message += "Email:" + mail + '\n'
		message += "Event Details:" + event_details + '\n'

		send_mail(
				message_subject, #subject
				message, #message
				mail, #from email
				toEmail #to email
				) 
		return render(request,'d2l_schedule_training.html',{'member':member})
	else:
		return render(request, 'd2l_schedule_training.html', {'member': member, 'teams': teams })
>>>>>>> 18140e79ee359a5792e322ec4efb24b84de933b3

# view for attend training page which is displayed when we click on attend training on darkness to light page.
# This is common for Rutherford and cannon counties as the url for both the pages are same.
def d2l_attend_training_view(request, *args, **kwargs):
<<<<<<< HEAD
	return render(request, 'd2l_attend_training.html', {})
=======
	#if request.method == "GET":
	teams = Team.objects.all()
	member = Team.objects.get(job_title='Drug Endangered Children Coordinator')
	if request.method == "POST":
		toEmail =[Team.objects.get(job_title = 'Drug Endangered Children Coordinator').email]
		message_subject = "Darkness to light attend a training"
		user_name = request.POST['username']
		user_address = request.POST['address']
		user_city = request.POST['city']
		user_state = request.POST['state']
		user_zip = request.POST['zip']
		user_number = request.POST['phonenumber']
		mail = request.POST['userEmail']
		
		message = "Name:" +  user_name +'\n'
		message += "Address:" + user_address + '\n'
		message += "City:" + user_city + '\n'
		message += "State:" + user_state +'\n'
		message += "Zip:" + user_zip +'\n'
		message += "Phone Number:" + user_number +'\n'
		message += "Email:" + mail + '\n' 
	
		#message = [user_name,user_address,user_city,user_state,user_zip,user_number,mail]	
		# send an email 
		send_mail(
				message_subject,#subject
				message,#message
				mail,#from email
				toEmail,#to email

				)
					
		
		return render(request, 'd2l_attend_training.html', {'member': member, 'teams': teams})
		
	else:
		return render(request, 'd2l_attend_training.html', {'member': member, 'teams': teams })

#	return render(request, 'd2l_attend_training.html', {'member':member})
>>>>>>> 18140e79ee359a5792e322ec4efb24b84de933b3

# view for Rutherford county cpit page
def rutherford_cpit_view(request, *args, **kwargs):
	return render(request, 'rutherford_cpit.html', {})

# view for darkness to light for cannon county.
def cannon_d2l_view(request, *args, **kwargs):
<<<<<<< HEAD
	return render(request, 'd2l.html', {})
=======
	d2l = DarknesstoLight.objects.get(id=1)
	imgd2l = Imagesond2l.objects.all()
	
	d2l_context = {
					'title': d2l.title,
					'description': d2l.description,
					'imgd2l':imgd2l,
					
				}
	return render(request, 'd2l.html', d2l_context)
	
>>>>>>> 18140e79ee359a5792e322ec4efb24b84de933b3

# view for cannon cpit team.
def cannon_cpit_view(request, *args, **kwargs):
	return render(request, 'cannon_cpit.html', {})

# view for our team page
def teams_view(request, *args, **kwargs):
<<<<<<< HEAD
	objs5 = Team.objects.all()
	
	team_context = {
					'objs5': objs5 ,				
	}
	return render(request, 'our_team.html', team_context)

# view for board of directors
def board_of_directors_view(request, *args, **kwargs):
	directors = ExecutiveCommittee.objects.all()
	members = BoardMember.objects.all()

	board_context = {
					'directors': directors,
					'members': members,
	}

	return render(request, 'board_of_directors.html', board_context)


# view for Family services page
def resourses_view(request, *args, **kwargs):
	return render(request, 'resourses.html', {})

# view for events page
def events_view(request, *args, **kwargs):
	objs8 = Event.objects.all()
	obj9 = EventTopImage.objects.get(id=1)
	events_context = {
						'objs8' : objs8,
						'obj9' : obj9,
=======
	cacteam = Team.objects.all()
	#execcommittee = ExecutiveCommittee.objects.all()
	#boardmemb = BoardMember.objects.all()

	team_context = {
					'cacteam': cacteam ,
					#'execcommittee': execcommittee,
					#'boardmemb': boardmemb,
	}
	return render(request, 'our_team.html', team_context)

# view for ourteam community partners page


# view for Family services page
def family_services_view(request, *args, **kwargs):
	return render(request, 'family_services.html', {})

# view for events page
def events_view(request, *args, **kwargs):
	eventdetails = Event.objects.all()
	eventheaderimg = EventTopImage.objects.last()
	events_context = {
						'eventdetails' : eventdetails,
						'eventheaderimg' : eventheaderimg,
>>>>>>> 18140e79ee359a5792e322ec4efb24b84de933b3
	}
	return render(request, 'events.html', events_context)

# views for getinvolved page
def getinvolved_view(request, *args, **kwargs):
	return render(request, 'get_involved.html', {})

# view for getinvolved volunteer page.
<<<<<<< HEAD
def getinvolved_volunteer_view(request, *args, **kwargs):
	return render(request, 'getinvolved_volunteer.html', {})
=======
#def getinvolved_volunteer_view(request, *args, **kwargs):
#	return render(request, 'getinvolved_volunteer.html', {})
>>>>>>> 18140e79ee359a5792e322ec4efb24b84de933b3
# view for darkness to light page redirected from getinvolved page
def getinvolved_d2l_view(request, *args, **kwargs):
	return render(request, 'd2l.html', {})
# view for host an event page
def getinvolved_hostanevent_view(request, *args, **kwargs):
<<<<<<< HEAD
	return render(request, 'getinvolved_host_event.html', {})

# views for volunteer page under get involved nav bar.
def gi_volunteer_view(request, *args, **kwargs):
	return render(request, 'gi_volunteer.html', {})
# view for press releases page
def press_release_view(request, *args, **kwargs):
	objs10 = PressRelease.objects.all()
	pressreleases_context = {
							'objs10': objs10
=======
	teams = Team.objects.all()
	member = Team.objects.get(job_title = 'Development Coordinator')

	if request.method == "POST":
		toEmail =[Team.objects.get(job_title = 'Development Coordinator').email]
		message_subject = "Host an Event"
		user_name = request.POST['username']
		org_name = request.POST['organizationname']
		mailing_address = request.POST['mailingaddress']
		user_address = request.POST['address']
		mail = request.POST['userEmail']
		user_number = request.POST['phonenumber']
		event_details = request.POST['aboutevent']

		message = "Name:" + user_name + '\n'
		message += "Organization Name:" + org_name + '\n'
		message += "Mailing Address" + mailing_address + '\n'
		message += "City, State, Zip:" + user_address + '\n'
		message += "Email:" + mail + '\n'
		message += "Phone Numer:" + user_number + '\n'
		message += "Event Details:" + event_details + '\n'

		send_mail(
				message_subject,#subject
				message,#message
				mail,#from email
				toEmail,#to email

				)
					
		
		return render(request, 'getinvolved_host_event.html', {'member': member, 'teams': teams})
		
	else:
		return render(request, 'getinvolved_host_event.html', {'member': member, 'teams': teams })
	

# views for volunteer page under get involved nav bar.
def getinvolved_volunteer_view(request, *args, **kwargs):
	teams = Team.objects.all()
	member = Team.objects.get(job_title = 'Development Coordinator')

	if request.method == "POST":
		toEmail =[Team.objects.get(job_title = 'Development Coordinator').email]
		message_subject = "Host an Event_Volunteer"
		user_name = request.POST['username']
		user_number = request.POST['phonenumber']
		mail = request.POST['userEmail']
		volunteer_type = request.POST['volunteertype']

		message = "Name:" + user_name + '\n'
		message += "Phone Number:" + user_number + '\n'
		message += "Email:" + mail + '\n'
		message += "Volunteer Type:" + volunteer_type + '\n'

		send_mail(
				message_subject, #subject
				message,#message
				mail,#from email
				toEmail,#to email
			)
		return render(request, 'getinvolved_volunteer.html', {'member': member, 'teams': teams})
		
	else:
		return render(request, 'getinvolved_volunteer.html', {'member': member, 'teams': teams })	
	
# view for press releases page
def press_release_view(request, *args, **kwargs):
	pressrelease = PressRelease.objects.all()
	pressreleases_context = {
							'pressrelease': pressrelease
>>>>>>> 18140e79ee359a5792e322ec4efb24b84de933b3
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
<<<<<<< HEAD
	objs11 = NewsLetter.objects.all()
	newsletter_context = {
							'objs11' : objs11
=======
	newsletter = NewsLetter.objects.all()
	newsletter_context = {
							'newsletter' : newsletter
>>>>>>> 18140e79ee359a5792e322ec4efb24b84de933b3
	}
	return render(request, 'news_letters.html', newsletter_context)

# view for media information page.
def mediainfo_view(request, *args, **kwargs):
<<<<<<< HEAD
	return render(request, 'media_info.html', {})
=======
	video = MediaInformation.objects.all()
	return render(request, 'media_info.html', {'video':video})
>>>>>>> 18140e79ee359a5792e322ec4efb24b84de933b3

# view for gratitude page
def gratitude_view(request, *args, **kwargs):
	category = GratitudeCards.objects.all()
	multipleimages = PostImage.objects.all()

	
	gratitude_context = {
							'category' : category,
							'multipleimages' : multipleimages,
	}
	return render(request, 'gratitude.html', gratitude_context)

<<<<<<< HEAD

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
=======
	
# view for home page.
def home_view(request, *args, **kwargs):

	statistics = Statistics.objects.last()
	carousel = SlideshowImages.objects.all()
	
	context = {
			'peopleserved': statistics.peopleserved,
			'Childabusecases': statistics.Childabusecases,
			'd2l': statistics.d2l,
			'carousel': carousel,
			
>>>>>>> 18140e79ee359a5792e322ec4efb24b84de933b3
			

	}
	return render(request, 'home.html', context)
<<<<<<< HEAD


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

# View for resourses page
def resources_view(request, *args, **kwargs):
	objs = Resource.objects.all()
	context = {
		'objects' : objs,
	}
	return render(request, 'resourses.html', context)

# View for contact family coordinator form
def contact_family_coordinator_view(request, *args, **kwargs):
	return render(request, 'contact_family_coordinator.html', {})

#views for contact family coordinator form that is functioning to send to client
def contactCoordinator(request):
	if request.method == 'POST':
		subject = "Darkness to Light : Attend Training"
		body = {
			'name':request.POST.get('name', ''),
			'address' : request.POST.get('address', ''),
			'city' : request.POST.get('city', ''),
			'state': request.POST.get('state', ''),
			'zipcode' : request.POST.get('zip', ''),
			'number' : request.POST.get('number', ''),
			'the_message' : request.POST.get('msg', ''),
			}
		message = "\n".join(body.values())
		email = request.POST.get('email', '')			
		try:
			send_mail(subject, message, email,['my3c@mtmail.mtsu.edu'],fail_silently=False, html_message=None)
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
	return render(request, 'contact_family_coordinator.html')
=======
#view for contactus from our_teams page
def contactus_view(request, *args, **kwargs):
	if request.method == "GET":
		teams = Team.objects.all()
		member = Team.objects.get(id=request.GET.get("id"))

	if request.method == "POST":

		id = request.POST['toEmail']
		toEmail = [Team.objects.get(id=id).email]
		message_firstname = request.POST['message-firstname']
		message_lastname = request.POST['message-lastname']
		email = request.POST['email']
		message_subject = request.POST['message-subject']
		message = request.POST['message']
		
		# send an email 
		send_mail(
				message_subject,#subject
				message,#message
				email,#from email
				toEmail,#to email

				)
		return render(request, 'contactus.html', {})
		
	else:
		return render(request, 'contactus.html', {'member': member, 'teams': teams })

# view for board of directors
def board_of_directors_view(request, *args, **kwargs):
	directors = ExecutiveCommittee.objects.all()
	members = BoardMember.objects.all()

	board_context = {
					'directors': directors,
					'members': members,
	}

	return render(request, 'board_of_directors.html', board_context)

>>>>>>> 18140e79ee359a5792e322ec4efb24b84de933b3
