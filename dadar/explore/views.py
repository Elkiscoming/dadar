from django.http.response import HttpResponse
from django.shortcuts import render
from client import client
from models import *
import json
# Create your views here.


def init(request, location):
    result = client.venues.explore(params={'ll': location})
    user = User()
    user.save()
    for item in result['groups'][0]['items']:
        venue = Venue()
        if len(Venue.objects.filter(foursquare_id=item['venue']['id'])) == 0:
            venue.foursquare_id = item['venue']['id']
            venue.name = item['venue']['name']
            venue.lat = item['venue']['location']['lat']
            venue.lng = item['venue']['location']['lng']
            venue_details = client.venues(venue.foursquare_id)
            venue.image = venue_details['venue']['bestPhoto']['prefix'] \
                          + 'original' + venue_details['venue']['bestPhoto']['suffix']
            venue.save()
            for category in venue_details['venue']['categories']:
                if Category.objects.get(name=category['name']) is not None:
                    venue.categories.add(Category.objects.get(name=category['name']))
            venue.save()
        else:
            venue = Venue.objects.filter(foursquare_id=item['venue']['id'])[0]
        user.venue_set.add(venue)
    user.save()
    return HttpResponse(user.id)  # [0]['venue']['id'])


def index(request):
    return render(request, 'explore/index.html')


def get_venue(request, user_id, place_number):
    user = User.objects.filter(pk=user_id)[0]
    venue = user.venue_set.all()[int(place_number)]

    venue_data = dict()
    venue_data['name'] = venue.name
    venue_data['image'] = venue.image
    venue_data['category'] = venue.categories.first().image
    # venue_data['icon'] = venue.category.image
    return HttpResponse(json.dumps(venue_data))


def update_categories(categories=None):
    if categories is None:
        categories = client.venues.categories()['categories']
    for item in categories:
        category = Category()
        category.name = item['name']
        category.image = item['icon']['prefix'] + "88" + item['icon']['suffix']
        category.save()
        update_categories(item['categories'])
