import requests
from geopy.geocoders import Nominatim

#################################################################################################################
### Other Functions

def GetCoordinatesFromPostalCode(postal_code):
    geolocator = Nominatim(user_agent="your_app_name")
    location = geolocator.geocode(postal_code)
    return location.latitude,location.longitude

def get_nearest_restaurants(client_id, client_secret, latitude, longitude, radius=1000, category='food', price_range=None):
    base_url = 'https://api.foursquare.com/v3/venues/explore'

    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'v': '20220210',  # Use the current date in YYYYMMDD format
        'll': f'{latitude},{longitude}',
        'radius': radius,
        'section': category,
        'limit': 5  # Limit the number of results, adjust as needed
    }

    if price_range is not None:
        params['price'] = price_range

    response = requests.get(base_url, params=params)
    print(response.json())
    groups = response.json()['response'].get('groups', [])

    items = groups[0].get('items', [])
    
    restaurants_info = []

    for result in items:
        venue = result.get('venue', {})
        restaurant_name = venue.get('name', 'N/A')
        restaurant_address = venue.get('location', {}).get('address', 'N/A')
        restaurant_categories = [cat['name'] for cat in venue.get('categories', [])]
        price_tier = venue.get('price', {}).get('tier', 'N/A')

        restaurants_info.append({
            'name': restaurant_name,
            'address': restaurant_address,
            'categories': restaurant_categories,
            'price_tier': price_tier
        })

    return restaurants_info

#################################################################################################################
### Variables

postal_code = "N2L 6G8"
client_id = '04YZWOZ5RLXDGNB5BR20VCFP3EN4LSFXHBXWWUPQEOJPOLSY'
client_secret = 'T33MW5OCMWVOT5HFRSBSK2PJNVLOV1O24HYFHY42O2O211RV'
api_key = 'fsq3kN13s6mmzScl3ZZWcQvppENcv6j2MEshGfdsnOOi/BY='

#################################################################################################################
### Main Code

if __name__ == "__main__":
    latitude,longitude = GetCoordinatesFromPostalCode(postal_code)
    print(latitude,longitude)
    nearest_restaurants = get_nearest_restaurants(client_id, client_secret, latitude, longitude)

    for restaurant in nearest_restaurants:
        print(f"Name: {restaurant['name']}")
        print(f"Address: {restaurant['address']}")
        print(f"Categories: {', '.join(restaurant['categories'])}")
        print(f"Price Tier: {restaurant['price_tier']}")
        print("--------------")
        
        
