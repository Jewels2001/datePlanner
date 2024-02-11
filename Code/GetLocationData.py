from geopy.geocoders import Nominatim
import requests
import pandas as pd
import time

#################################################################################################################
### Other Functions

def GetCoordinatesFromPostalCode(postal_code):
    geolocator = Nominatim(user_agent="your_app_name")
    location = geolocator.geocode(postal_code)
    return location.latitude,location.longitude

def GetNearestLocationsDF(latitude,longitude,n=None):
    api_key = "vuSSTtEtm-SgqmrtPvRos5PfyME0ngKs9dyNOWw9xFP2L6JIVE2224Dt2NvdvaQ40z7sbiqwMBSJlCXBVKRH1QAqT4bkFubnURqROXYEJbgW5WuTq6gPTRrpRLXIZXYx" 
    list_of_location_types_DICT = {
        "Restaurants": ["restaurants", "food", "dining", "cuisine", "eateries", "diners", "bistros"],
        "Bars": ["bars", "pubs", "lounges", "cocktail bars", "wine bars", "beer bars"],
        "Coffee & Tea": ["coffee", "tea", "cafes", "coffee shops", "tea houses", "espresso bars"],
        "Hotels": ["hotels", "motels", "lodging", "accommodation", "bed and breakfast", "inns"],
        "Shopping": ["shopping", "stores", "retail", "malls", "shopping centers", "boutiques"],
        "Nightlife": ["nightlife", "clubs", "nightclubs", "music venues", "bars and clubs", "dancing"],
        "Beauty & Spas": ["beauty", "spa", "salon", "wellness", "massage", "hair salon"],
        "Fitness & Recreation": ["fitness", "gyms", "fitness centers", "yoga studios", "parks", "recreation"],
        "Arts & Entertainment": ["arts", "entertainment", "museums", "theaters", "galleries", "cinemas"],
    }
    i = -1
    endpoint = "https://api.yelp.com/v3/businesses/search"
    
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    for category,keywords in list_of_location_types_DICT.items():    
        j = 0
        limit1 = 50
        for keyword in keywords:
            
            params = {
                "latitude": latitude,
                "longitude": longitude,
                "term": keyword,
                "limit": limit1,
                "sort_by": "distance"
            }
            
            response = requests.get(endpoint,headers=headers,params=params)
            data = response.json()
            
            businesses = data['businesses']
            if not businesses:
                continue
            if n != None:
                businesses = businesses[:n]
            if i == -1 and j == 0:
                full_column_list = ['Category','Subcategory']
                column_list = list(businesses[0].keys())
                full_column_list.extend(column_list)
                locations_DF = pd.DataFrame(columns=full_column_list)
                i = 0
            temp_locations_DF = pd.DataFrame([[None]*len(full_column_list) for _ in range(len(businesses))], columns=full_column_list)
            temp_locations_DF.loc[:len(businesses) - 1, 'Category'] = category
            temp_locations_DF.loc[:len(businesses) - 1, 'Subcategory'] = keyword
            
            if 'price' not in list(businesses[0].keys()):
                position_to_add_price = 11
                first_dict = businesses[0]
                keys = list(first_dict.keys())
                values = list(first_dict.values())
                new_businesses = {}
                for i, (key, value) in enumerate(zip(keys, values)):
                    new_businesses[key] = value
                    if i == position_to_add_price - 1:
                        new_businesses['price'] = None
                businesses[0] = new_businesses
            businesses_df = pd.DataFrame(businesses)
            businesses_df = businesses_df[column_list]
            temp_locations_DF.loc[:len(businesses) - 1, column_list] = businesses_df
            locations_DF = pd.concat([locations_DF, temp_locations_DF], axis=0, ignore_index=True)
            j = j + 1
        if i >= 0:
            i = i+1
    specified_column = 'id'
    locations_DF.drop_duplicates(subset=specified_column,keep='first',inplace=True)
    locations_DF.to_csv('Data\locations.csv')
    return locations_DF

#################################################################################################################
### Variables

postal_code = "ANA NAN"

#################################################################################################################
### Main Code

if __name__ == "__main__":
    start_time = time.time()
    latitude,longitude = GetCoordinatesFromPostalCode(postal_code)
    #print(latitude,longitude)
    latitude = 0
    longitude = 0
    locations_DF = GetNearestLocationsDF(latitude,longitude)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")
        
        
