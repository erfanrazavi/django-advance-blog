from django.db import models
from django.contrib.auth.models import (BaseUserManager , AbstractBaseUser , PermissionsMixin)
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserManager(BaseUserManager):
    '''
    custom user model manager where email is the uniqe identifiers
      for authentication insted of usernames.

    '''
    def create_user(self, email, password, **extra_fields):
        '''
            create and save a user with the given email and password and extra data

        '''
        if not email:
            raise ValueError(_('the Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email = email , **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
        
    def create_superuser(self,email,password,**extra_fields):
        '''
                create and save a user with the given email and password and extra data

        '''
        extra_fields.setdefault('is_staff' , True)
        extra_fields.setdefault('is_superuser' , True)
        extra_fields.setdefault('is_active' , True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('SuperUser must have is_staffTrue.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('SuperUser must have is_superUserTrue.'))
        return self.create_user(email,password , **extra_fields)

        




class User(AbstractBaseUser , PermissionsMixin):
    '''
    custom user model for our app

    '''
    email = models.EmailField(max_length=255,unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #When I want a field to be required, I write the name of that variable here

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    

    objects = UserManager()

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    image = models.ImageField(blank=True , null=True)
    descibtion = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
    

'''Post Save Signal Trigger after Inserting in User Model'''
@receiver(post_save , sender = User)
def save_profile(sender , instance , created , **kwargs):
    if created:
        Profile.objects.create(user = instance)