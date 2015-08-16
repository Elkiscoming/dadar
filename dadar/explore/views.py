from django.http.response import HttpResponse
from django.shortcuts import render
from client import client
from models import *
# Create your views here.


def init(request, location):
    result = client.venues.explore(params={'ll': location})
    user = User()
    user.save()
    for item in result['groups'][0]['items']:
        venue = Venue()
        venue.foursquare_id = item['venue']['id']
        venue.name = item['venue']['name']
        venue.lat = item['venue']['location']['lat']
        venue.lng = item['venue']['location']['lng']
        user.venue_set.add(venue)
    user.save()
    return HttpResponse(user.id)  # [0]['venue']['id'])


def index(request):
    return render(request, 'explore/index.html')


def get_image(request, user_id, place_number):
    user = User.objects.filter(pk=user_id)[0]
    venue = user.venue_set.all()[int(place_number)]
    venueResult = client.venues(venue.foursquare_id)
    venue.image = venueResult['venue']['bestPhoto']['prefix'] + 'original' + venueResult['venue']['bestPhoto']['suffix']
    venue.save()
    return HttpResponse(venue.image)