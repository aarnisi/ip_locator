import os
from geopy.geocoders import Nominatim
from geopy.geocoders import MapQuest
import ipinfo
import sys


class track():  
    def __init__(self, ip_address: str):
        # Initialize instance variables
        self.ipinfo_access_token = os.environ.get('ipinfo_access_token')
        self.mapquest_access_token = os.environ.get('mapquest_access_token')
        self.ip_address = ip_address
        
        self.IPTracking()

        if self.mapquest_access_token != None:
            self.get_location_info()
        else:
            print("-------------------")
            print("Mapquest access token is currently missing, so it can't be used")
            print("-------------------")
        
    def IPTracking(self):
         # create a client object with the access token
        self.handler = ipinfo.getHandler(self.ipinfo_access_token)
        # get the ip info
        self.details = self.handler.getDetails(self.ip_address)

        for key, value in self.details.all.items():
            if key == 'latitude':
                self.latitude = value
            elif key == 'longitude':
                self.longitude = value
            print(f"{key}: {value}")

    def get_location_info(self):
        # Initialize a MapQuest geocoder with your API key
        self.geolocator = MapQuest(api_key = self.mapquest_access_token)
        # Combine latitude and longitude into a single string
        self.location = f"{self.latitude}, {self.longitude}"
        try:
            # Get location information
            self.location_info = self.geolocator.reverse(self.location, exactly_one=True)
            print("-------------------")
            print(f"Location is: {self.location_info}")
            print("-------------------")
            
        except Exception as e:
            print(f'error', str(e))
            return {'error': str(e)}
