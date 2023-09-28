from django.db import models

from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin


# Create your models here.



class CustomUserManager(BaseUserManager):
    def create_user(self,username=None,password=None,**extra_fields):
        if not username:
            raise ValueError("User must have a Username ")
        if not password:
            raise ValueError('User must have a password')
        user=self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,username,password=None,**extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 1)
        return self.create_user(username, password,**extra_fields)



ROLL_CHOICE=[
    (1,'Admin'),
    (2,'Red_C'),
    (3,'Blue_C'),
    (4,'Green_C'),
    (5,'Red_Mem'),
    (6,'Blue_Mem'),
    (7,'Green_Mem')
]


class CustomUser(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(blank=True,null=True)
    is_active=models.BooleanField(default=True,verbose_name='active')
    is_staff=models.BooleanField(default=True)
    role=models.IntegerField(choices=ROLL_CHOICE,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=[]
    objects=CustomUserManager()


    def __str__(self):
        return self.username
    


class Red(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    standard=models.CharField(max_length=10)
    is_activae=models.BooleanField(default=False)
    sports_item=models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
    

class Green(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    standard=models.CharField(max_length=10)
    is_activae=models.BooleanField(default=False)
    sports_item=models.BooleanField(default=False)
    


    def __str__(self):
        return self.first_name
    
class Blue(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    standard=models.CharField(max_length=10)
    is_activae=models.BooleanField(default=False)
    sports_item=models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
    


    




class Sports(models.Model):
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images',blank=True)


    def __str__(self):
        return self.name


class SportsMembers(models.Model):
    sports=models.ForeignKey(Sports,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    role=models.IntegerField()

    def __str__(self):
        return self.user.username
    

    

