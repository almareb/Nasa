from django.db import models

class CountryPollution(models.Model):
	title = models.CharField(max_length=100)
	CHOICES = (
		('1','good'),
		('2','worse'),
		('3','moderate'),)
	condition = models.CharField(max_length=100, choices = CHOICES,default='1')
	PM25_DOMINANT    = models.DecimalField(max_digits=10,decimal_places=2)
	O3    = models.DecimalField(max_digits=10,decimal_places=2)
	PM10  = models.DecimalField(max_digits=10,decimal_places=2)
	NO2   = models.DecimalField(max_digits=10,decimal_places=2)
	SO2    = models.DecimalField(max_digits=10,decimal_places=2)
	NO    = models.DecimalField(max_digits=10,decimal_places=2)
	NOX    = models.DecimalField(max_digits=10,decimal_places=2)
	CO    = models.DecimalField(max_digits=10,decimal_places=2)
	

	def __str__(self):
		return self.title