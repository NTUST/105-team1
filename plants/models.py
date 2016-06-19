from django.db import models

# Create your models here.
class  Plantkind(models.Model):
	name = models.CharField(max_length=20)	
	introduce = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.name

class  Plant(models.Model):
	name = models.CharField(max_length=20)			
	plantkind = models.ForeignKey(Plantkind)
	
	def __str__(self):
		return self.name


