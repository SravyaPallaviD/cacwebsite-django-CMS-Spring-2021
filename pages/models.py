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
class Statisticscannon(models.Model):
	peopleservedcannon = models.IntegerField()
	Childabusecasescannon = models.IntegerField()
	
		