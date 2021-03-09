from django.db import models

# Create your models here.

class Statistics(models.Model):
	peopleserved = models.IntegerField()
	Childabusecases = models.IntegerField()
	d2l = models.IntegerField()

	
class Slideshow(models.Model):
	image1 = models.ImageField(upload_to='pics')
	image2 = models.ImageField(upload_to='pics')
	image3 = models.ImageField(upload_to='pics')

		