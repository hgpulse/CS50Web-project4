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

from django.core.paginator import Paginator

def index(request):
    allPosts = Post.objects.all()

    # add pagination page_obj
    paginator = Paginator(allPosts, 10) # Show 10 posts per page.
    page_number = request.GET.get('page') # 10 
    page_obj = paginator.get_page(page_number)

    
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
    
    return render(request, "network/index.html", {'form': form, 'allPosts': allPosts, 'page_obj': page_obj})



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

    post_list = None

   

    # get the username from id
    name = User.objects.get(pk=username)
    # get the current user
    currentUser = request.user
    # print(currentUser)
    
    # get profile with the specific username
    profile = Profile.objects.get(user=name)

    is_following = None
    if currentUser in User.objects.all():
        # create list of post for the current user
        post_list = Post.objects.filter(author= Profile.objects.get(user = username))

        # add pagination page_obj 
        paginator = Paginator(post_list, 10) # Show 10 posts per page.
        page_number = request.GET.get('page') # 10 
        page_obj = paginator.get_page(page_number)

        print(post_list)

       
       
        
        
        # User to follow: the visited user Profile
        user = User.objects.get(pk=username)
        #profile to check
        a_user = User.objects.get(pk=request.user.pk)
        # check if the profile is followed
        is_following = False
        
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
            

        
        
    return render(request, "network/profile.html", {'post_list': post_list, 'page_obj': page_obj, 'name':name, 'currentUser':currentUser, 'profile':profile, 'is_following':is_following })




@csrf_exempt
@login_required

def postapi(request, postid):
     # get the username from id
    
    print(f"api post ID : {postid}")
    # create user instace
    cuser = request.user
    print(f'live user: {cuser.pk}')
    # Query for requested email
    try:
        post = Post.objects.get(pk=postid)
        
    except Profile.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    # Return post contents
    if request.method == "GET":
        return JsonResponse(post.serialize())

    # Update whether email is read or should be archived
    elif request.method == "PUT":
        data = json.loads(request.body)
        
        
        if data.get("content") is not None:
            post.content = data["content"]
        
        if data.get("user") is not None:
            print(post.likes.all())
            if cuser in post.likes.all():
                # remove user ID
                # print(f'remove action: {cuser} id {cuser.pk}')
                post.likes.remove(cuser.pk)
            
            else:
                #print(f'Add action: {cuser} id {cuser.pk}')
                post.likes.add(cuser.pk)
        post.save()
        return HttpResponse(status=204)

    # Email must be via GET or PUT
    else:
        return JsonResponse({
            "error": "GET or PUT request required."
        }, status=400)
@login_required
def following(request):
    # request.user
    # 1 user = User.objects.get(pk=1)
    
    user = User.objects.get(pk=request.user.pk)

    # get a list of profiles
    # 2 list of profile : Profile.objects.filter(followers__in=[user])
    profiles = Profile.objects.filter(followers__in=[user.pk])
  
    # 3 for profile in profiles
    # Post.objects.filter(author__in=[profile])
    posts_dict = {}
    
    post_list = []
    
      # if profiles contain data = True
    if profiles:
        # store result
        
        
            
        # create a dict to store all the result
        
        for profile in profiles:
            
            # result = Post.objects.filter(author__in=[profile])
            
            # print(result)
            
            # post_list.append(result)
            posts_dict[profile] = Post.objects.filter(author__in=[profile])

            for item in posts_dict[profile]:
                 
                 post_list.append(item)
        
        
       

        paginator = Paginator(post_list, 10) # Show 10 posts per page.
        page_number = request.GET.get('page') # 10 
        page_obj = paginator.get_page(page_number)

        # total of posts
        postNbr = len(post_list)

    
    return render(request, "network/following.html", {'postNbr': postNbr, 'page_obj': page_obj })