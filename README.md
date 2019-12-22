# GeoDjango Setup
Follow [this page](https://docs.djangoproject.com/en/3.0/ref/contrib/gis/install/geolibs/) and [this page](https://realpython.com/location-based-app-with-geodjango-tutorial/) for more info.  
Run the following command to install the required libraries for GeoDjango
```bash
sudo apt-get install binutils libproj-dev gdal-bin
```
Let's use PostgreSQL + PostGIS for our GIS database. We can simply run it as a Docker container:
```bash
docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=testpassword -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:9.6-2.4
```
But I didn't succeed with this method, maybe because I already have PostgreSQL installed. So I went ahead and [installed PostGIS extension](http://www.bostongis.com/PrinterFriendly.aspx?content_name=postgis_tut01).