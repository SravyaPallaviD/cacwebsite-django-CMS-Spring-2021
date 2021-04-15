from django.db import models

# Create your models here.

class Statistics(models.Model):
	peopleserved = models.IntegerField()
	Childabusecases = models.IntegerField()
	d2l = models.IntegerField()

	
#class Slideshow(models.Model):
#	image1 = models.ImageField(upload_to='pics')
#	image2 = models.ImageField(upload_to='pics')
#	image3 = models.ImageField(upload_to='pics')
#	btn_title1 = models.CharField(max_length= 120)
#	btn_link1 = models.CharField(max_length = 120)
#	btn_title2 = models.CharField(max_length = 120)
#	btn_link2 = models.CharField(max_length = 120)
#	btn_title3 = models.CharField(max_length = 120)
#	btn_link3 = models.CharField(max_length = 120)

# Models for Statistics and slideshow images on home page
class Image1(models.Model):
	title = models.CharField(max_length = 120, default = True)
	img1 = models.ImageField(upload_to = 'pics')
	btn_text1 = models.CharField(max_length = 120)
	btn_link1 = models.CharField(max_length = 120)

class Image2(models.Model):
	title2 = models.CharField(max_length = 120, default = True)
	img2 = models.ImageField(upload_to = 'pics')
	btn_text2 = models.CharField(max_length = 120)
	btn_link2 = models.CharField(max_length = 120)

class Image3(models.Model):
	title3 = models.CharField(max_length = 120, default = True)
	img3 = models.ImageField(upload_to = 'pics')
	btn_text3 = models.CharField(max_length = 120)
	btn_link3 = models.CharField(max_length = 120)

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

# Model for editing the members of Executive Committee on Our Team page
class ExecutiveCommittee(models.Model):
	name = models.CharField(max_length = 120)
	title = models.CharField(max_length = 120, default = None)

#Model for editing the Board members on Our Team page
class BoardMember(models.Model):
	name = models.CharField(max_length = 120)
	title = models.CharField(max_length = 120, default = True)

# Models for editing the content on Events page
class Event(models.Model):
	event_image = models.ImageField(upload_to = 'pics')
	date = models.DateField(auto_now = False, auto_now_add = False)
	event_title = models.CharField(max_length = 120, default = None)
	event_description = models.TextField()
	position_to_right = models.BooleanField()

# Model for editiong the picture on the top of the events page
class EventTopImage(models.Model):
	image = models.ImageField(upload_to = 'pics')

# Model for uploading press releases
class PressRelease(models.Model):
	title = models.CharField(max_length = 120)
	date = models.DateField(auto_now = False, auto_now_add = False)
	description = models.TextField()
	document = models.FileField(upload_to = 'pressrealeases')

# Model for News releases
class NewsLetter(models.Model):
	title = models.CharField(max_length = 120)
	date = models.DateField(auto_now = False, auto_now_add = False)
	description = models.TextField() 

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
