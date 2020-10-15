from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import User, PostForm, Post, Profile

# convert to JSON for javascript
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

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

    

    # get the username from id
    name = User.objects.get(pk=username)
    # get the current user
    currentUser = request.user
    # print(currentUser)
    # create list of post for the current user
    post_list = Post.objects.filter(author= Profile.objects.get(user = username))
    # Return posts in reverse chronologial order
    post_list = post_list.order_by("-date").all()
    
    # get profile with the specific username
    profile = Profile.objects.get(user=name)
    # User to follow: the visited user Profile
    user = User.objects.get(pk=username)
    #profile to check
    a_user = User.objects.get(pk=request.user.pk)
    # check if the profile is followed
    is_following = False
    print(a_user.is_following.all())
    print(user.user)
    if user.user in a_user.is_following.all():
        is_following = True
        print(is_following)


    if request.method == 'POST':
        
        
        # User to follow: the visited user Profile
        user = User.objects.get(pk=username)
        v_profile = Profile.objects.get(user=user)
        # Create user instance: Choose the active User
        
        
        a_Profile = Profile.objects.get(user=User.objects.get(pk=request.user.pk))
        
        #check that the user cannot follow himself
        
        if user != a_user:
            if a_user in profile.followers.all():
                v_profile.followers.remove(a_user)
                is_following = False
            
            else:
                #add the new follower to user
                v_profile.followers.add(a_user)
                is_following = True
            

        
        
    return render(request, "network/profile.html", {'post_list': post_list, 'name':name, 'currentUser':currentUser, 'profile':profile, 'is_following':is_following })



@csrf_exempt
@login_required
def profileapi(request, user):
     # get the username from id
    
    print(f"api user: {user}")
    # create user instace
    cuser = request.user
    # cuser = request.user
    # print(f"current user: {cuser}")
    # Query for requested email
    try:
        profile = Profile.objects.get(user=User.objects.get(pk=user))
    except Profile.DoesNotExist:
        return JsonResponse({"error": "Profile not found."}, status=404)

    # Return email contents
    if request.method == "GET":
        return JsonResponse(profile.serialize())

    # Update whether profile is read or should be archived
    elif request.method == "PUT":
        # profile.follow = cuser
        data = json.loads(request.body)
        if data.get("follow") is not None:
            profile.follow = cuser
        profile.save()
        return HttpResponse(status=204)

    # Email must be via GET or PUT
    else:
        return JsonResponse({
            "error": "GET or PUT request required."
        }, status=400)
