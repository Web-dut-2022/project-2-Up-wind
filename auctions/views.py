from django.contrib.auth import authenticate, get_user, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Biding, Listing, User, Watch


def index(request):
    context = {
        "listings": Listing.objects.all(),
    }
    return render(request, "auctions/index.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            
            if "next" in request.POST:
                next_url = request.POST["next"]
                return HttpResponseRedirect(next_url)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        if "next" in request.GET:
            next_url = request.GET["next"]
            context = {
                "next": next_url
            }
            return render(request, "auctions/login.html", context)
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        Watch(user).save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def img(request, imgurl):
    return HttpResponseRedirect(reverse("static", args=(imgurl,)))


def static():
    pass

@login_required(login_url='/login')
def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        des = request.POST["description"]
        startBid = request.POST["startingBid"]
        current = startBid
        img = request.FILES.get("img")
        cate = request.POST["category"]
        user = get_user(request)

        try:
            item = Listing(title=title, description=des, startingBid=startBid,
                    currentPrice=current, image=img, category=cate,
                    listedBy=user, isActive=True)
            item.save()
        except:
            return render(request, "auctions/create.html", {
                "message": "Something wrong!"
            })
        return HttpResponseRedirect(reverse("listing", args=(item.id,)))
    else:
        context = {
            "categories": Listing.CATEGORY_CHOICES
        }
        return render(request, "auctions/create.html", context)


@login_required(login_url='/login')
def listing(request, listId):
    item = Listing.objects.get(pk=listId)
    bidConut = item.biding_set.count()
    bidList = item.biding_set.all()
    commentList = item.comments_set.all()
    user = get_user(request)
    creater=False
    watched=False
    if item.listedBy == user:
        creater=True
    if user.watch.list.contains(item):
        watched=True
    watchCount = user.watch.list.count()
    context = {
        "item": item,
        "watched": watched,
        "watchCount": watchCount,
        "creater": creater,
        "bidCount": bidConut,
        "bids": bidList,
        "comments": commentList
    }
    return render(request, "auctions/listing.html", context)

@login_required(login_url='/login')
def watch(request, listId):
    item = Listing.objects.get(pk=listId)
    user = get_user(request)
    if request.POST["watch"]=="yes":
        user.watch.list.add(item)
    else:
        user.watch.list.remove(item)
    return HttpResponseRedirect(reverse("listing", args=(item.id,)))


@login_required(login_url='/login')
def watchlist(request):
    user = get_user(request)
    context = {
        "listings": user.watch.list.all(),
        "watchCount": user.watch.list.count()
    }
    return render(request, "auctions/watchlist.html", context)
    