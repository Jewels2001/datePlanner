import pandas as pd
import time

#################################################################################################################
### Other Functions

def ProcessLocationDF(price=None):
    locations_DF = pd.read_csv('Data\locations.csv')
    if price is not None:
        excluded_subcategories = list(set(locations_DF['Subcategory'].tolist()))
        excluded_subcategories = list(filter(lambda x: x not in ['malls','dancing','parks','recreation','yoga studios','museums','theaters','cinemas'], excluded_subcategories))
        filtered_locations_DF = locations_DF[~((locations_DF['Subcategory'].isin(excluded_subcategories)) & (locations_DF['price'].isna()))]
        filtered_locations_DF = filtered_locations_DF.copy()
        filtered_locations_DF['price'].fillna('Free/Unknown', inplace=True)
        locations_processed_DF = filtered_locations_DF.copy()   
        if price == 'Cheap':
            price = '$'
        elif price == 'Moderate':
            price = '$$'
        elif price == 'Pricey':
            price = '$$$'
        else:
            price = '$$$$' 
        locations_processed_DF = locations_processed_DF[locations_processed_DF['price'].isin([price, 'Free/Unknown'])].copy()

       
    locations_processed_DF.to_csv('Data\locations_processed.csv')    
    return locations_processed_DF

#################################################################################################################
### Variables

price = 'Cheap'

#################################################################################################################
### Main Code

if __name__ == "__main__":
    start_time = time.time()
    locations_processed_DF = ProcessLocationDF(price)
    print(locations_processed_DF.head())
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")