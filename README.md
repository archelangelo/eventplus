# Event Plus Backend
An app that lets you create and find nearby events! When you have something fun to do, invite others. If you are looking forward to meet new people and explore, look for nearby events!

This repo is a Django REST framework backend service that provides the APIs that the app uses.

### Example usage:
Find nearby events:
```
GET /apis/events/nearby/?lng=151.195697&amp; lat=-33.870481&amp; dist=0.5 HTTP/1.1
```

Get event details:
```
GET /apis/events/1/ HTTP/1.1
```

## Server Setup
As are prerequisite, you should already have Python 3 and pip installed. To start the server, you need to install:

### Django and its related packages
Create the virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate
```

Use pip to install the requirements
```bash
pip3 install -r requirements.txt
```

### PostgreSQL and PostGIS
Follow [this page](https://docs.djangoproject.com/en/3.0/ref/contrib/gis/install/geolibs/) and [this page](https://realpython.com/location-based-app-with-geodjango-tutorial/) for more info.  
Run the following command to install the required libraries for GeoDjango
```bash
sudo apt-get install binutils libproj-dev gdal-bin
```
Let's use PostgreSQL + PostGIS for our GIS database. You can simply run it as a Docker container:
```bash
docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=testpassword -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:9.6-2.4
```
Or, if PostgreSQL is already installed on the computer, you can [install PostGIS extension](http://www.bostongis.com/PrinterFriendly.aspx?content_name=postgis_tut01).

##### Query the GIS database
Refer to [this Django document](https://docs.djangoproject.com/en/3.0/ref/contrib/gis/db-api/#distance-lookups) for more detail.
```python
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D
from apis.models import Event
my_location = GEOSGeometry('POINT(151.195697 -33.870481)', srid=4326)
qs = Event.objects.filter(location__distance_lte=(my_location, D(km=1)))
qs[0].place
```
Output:
```
'ChIJkeO_AzquEmsRUpGQn1ZK7Tg'
```

## Models
### Event
Example usage (suppose you already have `PLACES_API_KEY` environment variable set up):

```python
from django.contrib.auth.models import User
from apis.models import Event
user = User.objects.get(pk=1)
Event.objects.all()
```

Output:
```
<QuerySet [<Event: Google Australia>, <Event: Harbour Bar & Kitchen>, <Event: Google Australia>]>
```

Now we can create a new event by calling `Event.objects.create_event()`:

```python
Event.objects.create_event(host=user, place_id='ChIJN1t_tDeuEmsRUsoyG83frY4')
Event.objects.all()
```

Output:
```
 <QuerySet [<Event: Google Australia>, <Event: Harbour Bar & Kitchen>, <Event: Google Australia>, <Event: Google Australia>]>
 ```
