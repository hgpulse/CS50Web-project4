from django.contrib import admin
from network.models import Post
from network.models import User
from network.models import Profile
# Register your models here.
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Profile)