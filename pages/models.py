from django.db import models

# Create your models here.

class Statistics(models.Model):
	peopleserved = models.IntegerField()
	Childabusecases = models.IntegerField()
	d2l = models.IntegerField()

	
# Models for Statistics and slideshow images on home page
class SlideshowImages(models.Model):
	title = models.CharField(max_length = 120, default = True)
	carousel_picture = models.ImageField(upload_to = 'pics', null= True, blank=True)
	btn_text = models.CharField(max_length = 120)
	btn_link = models.CharField(max_length = 120)

	def __str__(self):
		return f"{self.title}"


# Models for statics on cannon county page
class Statisticscannon(models.Model):
	peopleservedcannon = models.IntegerField()
	Childabusecasescannon = models.IntegerField()

# Models for editing team members on Our Team page
#CAC staff model
class Team(models.Model):
	job_title = models.CharField(max_length = 120, default = True)
	name = models.CharField(max_length =120, default = True)
	child_image = models.ImageField(upload_to = 'pics')
	older_image = models.ImageField(upload_to = 'pics')
	email = models.EmailField(max_length=250, default = False)
    

	def __str__(self):
		return f"{self.name}"

# Model for editing the members of Executive Committee on Our Team page
class ExecutiveCommittee(models.Model):
	name = models.CharField(max_length = 120)
	title = models.CharField(max_length = 120, default = None)

	def __str__(self):
		return f"{self.name}"
	class Meta:
        	verbose_name_plural = "Directors"


#Model for editing the Board members on Our Team page
class BoardMember(models.Model):
	name = models.CharField(max_length = 120)
	title = models.CharField(max_length = 120, default = True)

	def __str__(self):
		return f"{self.name}"

# Models for editing the content on Events page
class Event(models.Model):
	event_image = models.ImageField(upload_to = 'pics')
	date = models.DateField(auto_now = False, auto_now_add = False)
	event_title = models.CharField(max_length = 120, default = None)
	event_description = models.TextField()
	event_register = models.URLField(max_length=200, default= False)
	def __str__(self):
		return f"{self.event_title}"

# Model for editiong the picture on the top of the events page
class EventTopImage(models.Model):
	image = models.ImageField(upload_to = 'pics')

# Model for uploading press releases
class PressRelease(models.Model):
	title = models.CharField(max_length = 120)
	date = models.DateField(auto_now = False, auto_now_add = False)
	description = models.TextField()
	document = models.FileField(upload_to = 'pressrealeases')
	def __str__(self):
		return f"{self.title}"

# Model for News releases
class NewsLetter(models.Model):
	title = models.CharField(max_length = 120)
	date = models.DateField(auto_now = False, auto_now_add = False)
	description = models.URLField(max_length=200, default='None')
	def __str__(self):
		return f"{self.title}"

# Model for editing Rutherford county services page
class RutherfordService(models.Model):
	title = models.CharField(max_length = 120)
	description = models.TextField()
	image = models.ImageField(upload_to = 'pics', default = 'default.jpg')

	def __str__(self):
		return f"{self.title}"

#Model for editing Cannon county services page
class CannonService(models.Model):
	title = models.CharField(max_length = 120)
	description = models.TextField()
	image = models.ImageField(upload_to = 'pics', default = 'default.jpg')
	def __str__(self):
		return f"{self.title}"

#Model for uploading testimonies in Media information page

class MediaInformation(models.Model):
	title = models.CharField(max_length=500)
	videofile = models.FileField(upload_to = 'videos', null = True, verbose_name = "")

	def __str__(self):
		return f"{self.title}"

# Model for d2l images
class Imagesond2l(models.Model):

	image = models.ImageField(upload_to = 'pics', default = 'default.jpg')

	
class DarknesstoLight(models.Model):
	
	image = models.ForeignKey(Imagesond2l, null=True, on_delete = models.PROTECT)
	title = models.CharField(max_length=120, default = 'Add Title')
	description = models.TextField(default = 'Add description')

# Model for GratitudeSponsors
class GratitudeCards(models.Model):

	card_image = models.ImageField(upload_to = 'pics', default = 'default.jpg')
	title = models.CharField(max_length = 120, default = 'Add title')
	description = models.TextField(default = 'Add description')
	sponsorsText = models.TextField(default = 'Add Sponsors')							
	buttonID = models.CharField(max_length = 60, default = 'Add an ID')

	def __str__(self):
		return self.title
	
#Model to attach dynamic amount of images to each gratitudeobject
class PostImage(models.Model):
	post = models.ForeignKey(GratitudeCards, default=None, on_delete=models.CASCADE)
	image = models.FileField(upload_to = 'pics', default='default.jpg')
	

	def __str__(self):
		return self.post.title 
