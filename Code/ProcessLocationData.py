import pandas as pd

#################################################################################################################
### Other Functions

def ProcessLocationDF():
    locations_DF = pd.read_csv('Data\locations.csv')
    return locations_DF

#################################################################################################################
### Variables

#################################################################################################################
### Main Code

if __name__ == "__main__":
    locations_DF = ProcessLocationDF()
    print(locations_DF.head())