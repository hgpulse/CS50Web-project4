from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm, SelectDateWidget, Textarea


class User(AbstractUser):
    pass

# create This one-to-one model is often called a profile model, as it might store non-auth related information about a site user
class Profile(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE, related_name="user") # user.user
    title = models.CharField(max_length=100, blank=True)                               
    followers = models.ManyToManyField("User",related_name="is_following", blank=True)     # user.is_following.all()
   # following = models.ManyToManyField("User",related_name="following", blank=True)    # user.following.all()

    

    def serialize(self):
        return {
            "user": self.user.username,
            "followers": self.followers,   
        }

    def __str__(self):
        return f"{self.user} Profile"

class Post (models.Model):
    author = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="author") #profile.author
    content = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField("User",related_name="likes")

    def totallikes(self):
        return self.likes.count()
    
    def serialize(self):
        return {
            "id": self.pk,
            "author": self.author.user.username,
            "content": self.content,
            "date": self.date.strftime("%b %-d %Y, %-I:%M %p"),
            "likes": self.likes.count()
        }

    def __str__(self):
        return f"  {self.author} wrote {self.content} on the {self.date}"

    def __unicode__(self):
        return self.Post.id
    
    # order in descending order for the all Post in the app
    class Meta:
        ordering = ('-date', )

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('__all__')
        exclude =('author','like')
        widgets = {
            'content': Textarea(attrs={'placeholder':'What do you dream about ?', 'class':'form-control', 'id':'inputlg', 'rows':'6'}), 
            'date': SelectDateWidget()
        }

