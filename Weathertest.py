import urllib.request
import sys
import api
import json

try:
    ResultBytes = urllib.request.urlopen(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Kolkata?unitGroup=us&include=today&key={api.weatherapikey}&contentType=json")

    # Parse the results as JSON
    jsonData = json.load(ResultBytes)
    #print(jsonData['days'][0])
except urllib.error.HTTPError as e:
    ErrorInfo = e.read().decode()
    print('Error code: ', e.code, ErrorInfo)
    sys.exit()
except  urllib.error.URLError as e:
    ErrorInfo = e.read().decode()
    print('Error code: ', e.code, ErrorInfo)
    sys.exit()