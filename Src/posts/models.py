from django.db import models

# Create your models here.
 
class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(null=True,blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
    	return "/detail/%s/" %(self.id)
    def get_update_url(self):
        return "/update/%s/" %(self.id)
    def get_home(self):
    	return "/"
