from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, PostForm, Post, Profile

# convert to JSON for javascript
from django.http import JsonResponse

def index(request):
    allPosts = Post.objects.all()
    # Return posts in reverse chronologial order
    allPosts = allPosts.order_by("-date").all()
    if request.method == 'POST':
        print(request.user.id)
        form = PostForm(request.POST, request.user)
     
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            author = request.user
            print(author)
           
            
            if not request.user == instance.user:
                raise Http404
            
            content = request.POST["content"]
            
           
            # # create the Post
            new_post = Post(author = Profile.objects.get(user = author), content = content,like = 0 )
            new_post.save()
         
            
            # p0 = Post(author=profile, content=content, like=0)
            # # save the post
            # p0.save()

            
            
            


            return HttpResponseRedirect(reverse("index"))
            
    else:
        
        form = PostForm()
    
    return render(request, "network/index.html", {'form': form, 'allPosts': allPosts})



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)

        # create profile
        user = request.user
        profile = Profile(user=user)
        profile.save()
        
       

        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")



def profile(request, username):
    post_list = Post.objects.filter(author= Profile.objects.get(user = username))
    # Return posts in reverse chronologial order
    post_list = post_list.order_by("-date").all()
    print(username)
    print(post_list)
    return render(request, "network/profile.html", {'post_list': post_list})