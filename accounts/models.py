from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    city=models.ForeignKey("City",related_name='user_city', on_delete=models.CASCADE,blank=True,null=True)
    phone_number=models.CharField(max_length=15)
    date_de_naissance=models.CharField(max_length=10)
    sexe=models.CharField(max_length=10)
    languages=models.CharField(max_length=50)
    competences=models.CharField(max_length=70)
    image=models.ImageField(upload_to='profile/')

    def __str__(self):
        return str(self.user)


#SIGNAL IS HAPPEN AFTER WE POST_SAVE THAT'S MEAN AFTER SAVING ANEW USER WE WILL HAVE A NEW PROFILE

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)




class City(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)
