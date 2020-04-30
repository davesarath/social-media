from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models.signals import post_delete,pre_save,pre_delete,post_save
from django.dispatch import receiver
import os
from uuid import uuid4
import threading 



def path_and_rename(instance,filename):
    upload_to='dp'
    ext=filename.split(".")[-1]
    if instance.pk:
        filename="{}.{}".format(instance.pk,ext)
    else:
        filename= "{}.{}".format(uuid4().hex,ext)
    return os.path.join(upload_to,filename)


class custModel(AbstractUser):
    email   =   models.EmailField(max_length=254, null=False, unique=True)
    pro_pic      =   models.ImageField( upload_to=path_and_rename,null=True)

    def save(self, *args, **kwargs):
        if self.email:
            self.username=self.email
        return super().save(*args, **kwargs)

    
    def delete(self,*args, **kwargs):
        self.pro_pic.delete(False) 
        return super().delete(*args, **kwargs)


@receiver(pre_save, sender=custModel)
def submission_save(sender, instance, **kwargs):
    if not instance.pk:# new instance
        return False
    try:    #old instance
        old_obj=sender.objects.get(pk=instance.pk)
        old_file = old_obj.pro_pic
        new_file = instance.pro_pic
        if not old_file == new_file: #image is changed
            old_obj.pro_pic.delete(False) 
    except sender.DoesNotExist:
        return False



class tweet(models.Model):
    img=models.ImageField( upload_to='post',blank=True)
    author=models.ForeignKey("myapp.custModel", on_delete=models.CASCADE)
    created_date=models.DateTimeField( auto_now=True,editable=False)
    content=models.CharField(max_length=360,blank=True)
    likes=models.IntegerField(default=0)
    comments=models.IntegerField(default=0)

    class Meta:
        ordering =  ['-created_date','likes','comments']
    def __str__(self):
        return self.content[:50]
    
    def clean(self):
        img=self.img
        content=self.content
        if(not img and not content):
            raise ValidationError("cant post empty post")
        return super().clean()


@receiver(pre_delete, sender=tweet)
def submission_delete(sender, instance, **kwargs):
    if instance.img:
        filename    =   instance.img.name.split('/')[-1]
        print(filename)
        instance.img.delete(False) 


class like(models.Model):
    user=models.ForeignKey(custModel,models.CASCADE)
    post=models.ForeignKey(tweet, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.post.likes+=1
            self.post.save()
        super().save(*args, **kwargs)  # Call the "real" save() method.
    
    def clean(self):
        user=self.user
        post=self.post
        if like.objects.filter(user=user,post=post):
            raise ValidationError("This user already liked this post")
        return super().clean()    
    

    def delete(self, using=None, keep_parents=False):
        self.post.likes-=1
        self.post.save()
        return super().delete(using=using, keep_parents=keep_parents)


class comment(models.Model):
    user=models.ForeignKey(custModel,models.CASCADE)
    post=models.ForeignKey(tweet, on_delete=models.CASCADE)
    comments=models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.post.comments+=1
            self.post.save()
        super().save(*args, **kwargs) 

    def delete(self, using=None, keep_parents=False):
        self.post.comments-=1
        self.post.save()
        return super().delete(using=using, keep_parents=keep_parents)

    def __str__(self):
        return self.comments[:10]


class friends(models.Model):
    follower =models.ForeignKey(custModel, on_delete=models.CASCADE,related_name="follower")
    friend=models.ForeignKey(custModel, on_delete=models.CASCADE)

    def clean(self):
        follower=self.follower
        friend=self.friend

        if follower==friend:
            raise ValidationError("Can't follow yourself ")

        if friends.objects.filter(follower=follower,friend=friend):
            raise ValidationError("you are already following this person")
        return super().clean()

class msngr(models.Model):
    user1=models.ForeignKey(custModel, on_delete=models.CASCADE,related_name="user1")
    user2=models.ForeignKey(custModel, on_delete=models.CASCADE,related_name="user2")
    user1_status    =   models.BooleanField(default=False)
    user2_status    =   models.BooleanField(default=False)
    last_used       =   models.DateTimeField(auto_now=True, auto_now_add=False)

class messages(models.Model):
    sender=models.ForeignKey(custModel, on_delete=models.CASCADE)
    msg=models.CharField(max_length=50)
    user=models.ForeignKey(msngr, on_delete=models.CASCADE)

