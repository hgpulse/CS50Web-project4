from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm, SelectDateWidget, Textarea


class User(AbstractUser):
    pass

class Post (models.Model):
    #user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="Post")
    author = models.IntegerField(blank=False)
    content = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    like = models.IntegerField(blank=True)
   

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
