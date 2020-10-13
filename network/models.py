from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm, SelectDateWidget, Textarea


class User(AbstractUser):
    pass

# create This one-to-one model is often called a profile model, as it might store non-auth related information about a site user
class Profile(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE, related_name="user")
    title = models.CharField(max_length=100, blank=True)
    follow = models.ManyToManyField("User")
    followed_by = models.ForeignKey("User", on_delete=models.CASCADE, related_name="followed_by", blank=True, null=True)

    def __str__(self):
        return f"{self.user} Profile"

class Post (models.Model):
    author = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="author")
    content = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    like = models.IntegerField(blank=True)
    
    def serialize(self):
        return {
            "id": self.id,
            "author": self.author,
            "content": self.content,
            "date": self.date.strftime("%b %-d %Y, %-I:%M %p"),
            "like": self.like
        }

    def __str__(self):
        return f"  {self.author} wrote {self.content} on the {self.date}"

    def __unicode__(self):
        return self.Post.id


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('__all__')
        exclude =('author','like')
        widgets = {
            'content': Textarea(attrs={'placeholder':'What do you dream about ?', 'class':'form-control', 'id':'inputlg', 'rows':'6'}), 
            'date': SelectDateWidget()
        }
