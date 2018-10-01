# -*- coding: utf-8 -*-
import googlemaps,math
gmaps = googlemaps.Client(key = "AIzaSyDcKSAQlMtfWlYHi3qF1Q05ZK0nGDM6uHI")
number_of_address = int(raw_input("Enter number of addresses\n"))
address = [raw_input("Enter the address\n") for x in range(number_of_address)]
dict_latitude = {}
dict_longitude = {}
for x in range(number_of_address):
	geocode_result = gmaps.geocode(address[x])
	latitude = geocode_result[0]['geometry']['location']['lat']
	longitude = geocode_result[0]['geometry']['location']['lng']
	dict_latitude[address[x]] = latitude
	dict_longitude[address[x]] = longitude

def distance(lat1,lng1,lat2,lng2):
	radius = 6371
	psi1 = math.radians(lat1)
	psi2 = math.radians(lat2)
	delta_psi = math.radians(lat2-lat1)
	delta_lamda = math.radians(lng1-lng2)
	a = math.sin(delta_psi/2) * math.sin(delta_psi/2) + math.cos(psi1) * math.cos(psi2) * math.sin(delta_lamda/2) * math.sin(delta_lamda/2)
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))															
	d = radius * c
	return d

print distance(dict_latitude[address[0]],dict_longitude[address[0]],dict_latitude[address[1]],dict_longitude[address[1]])
distance_matrix = gmaps.distance_matrix(address[0],address[1])
if distance_matrix['rows'][0]['elements'][0]	['status'] == 'ZERO_RESULTS':
	print "No results for " + distance_matrix['origin_addresses'][0] + " and " + distance_matrix['destination_addresses'][0]
else:
	print "Distance between " + distance_matrix['origin_addresses'][0] + " and " + distance_matrix['destination_addresses'][0] + " is " + distance_matrix['rows'][0]['elements'][0]['distance']['text']
