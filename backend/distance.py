from geopy.distance import vincenty
import geocoder
import geohash

def hash_to_geo(locname):
	for location in r.zrange(locname, 0, -1):
	     geohash = r.geohash(locname, location)[0]
         nodes = Geohash.decode(geohash.rstrip('0'))
    return nodes

def closest_node(latlng, city):
	closest_locname = None
	distance = None
	for locname in r.zrange(city, 0, -1):
		geotag = hash_to_geo(locname)
		if distance is None:
			distance = vincenty(latlng, geotag).km

		if vincenty(latlng, geotag) <= distance:
			distance = vincenty(node, n).km
			closest_locname = locname
			
	return closest_locname

def getCity(latlng):
	g = geocoder.baidu(latlng, method='reverse')
	return g.city

def getClosestStation(latlng):
	import redis
	r = redis.StrictRedis(host='localhost', port=6379, db=0)
	# FIXME(dan): using setcity name for. dev
	#city = getCity(latlng)
	city = "Shanghai"
	return(closest_node(latlng, city))