from django.contrib import admin
from .models import custModel,comment,tweet,like,friends,msngr,messages
from django.contrib.auth.admin import UserAdmin

admin.site.register(custModel,UserAdmin)

admin.site.register(like)

admin.site.register(comment)

admin.site.register(tweet)

admin.site.register(friends)

admin.site.register(msngr)

admin.site.register(messages)




