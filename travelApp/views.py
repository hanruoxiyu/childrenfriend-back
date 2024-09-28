from django.shortcuts import render

# Create your views here.
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
import geoip2.database
class RouteAPIView(APIView):
    def get(self, request):
        # 获取远程调用ip
        ip_address = request.META.get('REMOTE_ADDR')
        # ip_address="112.65.1.149"
        print(ip_address)
        # 进行ip定位获取当前的经纬度
        reader = geoip2.database.Reader('./static/GeoLite2-City.mmdb')

        # ip_address = '123.45.67.89'
    # Lookup the IP address
        response = reader.city(ip_address)
        # Get the longitude from the response
        longitude = response.location.longitude
        latitude = response.location.latitude
        # Print the longitude
        # Close the database reader
        reader.close()
        return Response({"longitude":longitude,"latitude":latitude})