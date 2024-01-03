import geocoder

def get_current_location():
    try:
        g = geocoder.ip('me')  # Get location based on your IP address
        if g:
            return g
        else:
            return "Location not found"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    location = get_current_location()
    if isinstance(location, str):
        print(location)
    else:
        print(location)
        print("Current Location:")
        print("Latitude:", location.latlng[0])
        print("Longitude:", location.latlng[1])
        print("City:", location.city)
        print("State:", location.state)
        print("Country:", location.country + "DIA")