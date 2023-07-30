#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat July 29 07:05:05 2023


"""

import pandas as pd
import numpy as np
#from sklearn.preprocessing import MinMaxScaler

def preprocess(df, option):
    """
    This function is to cover all the preprocessing steps on the churn dataframe. It involves selecting important features, encoding categorical data, handling missing values,feature scaling and splitting the data
    """
    #Defining the map function
    def binary_map(feature):
        return feature.map({'Yes':1, 'No':0})
    
    #Drop values based on operational options
    if (option == "Online"):
        # Encode binary categorical features
        binary_list = ['room_type_Entire home/apt',

 'room_type_Private room',
 'LA',
 'property_type_Hostel',

 'tv',
 'SF',

 'elevator',
 'DC',
 'property_type_Apartment',
 'NYC',
 
 'property_type_House',
 'gym',

 'property_type_Dorm',
 'cleaning_fee',
 'Chicago',
 'white_goods',
 'internet',
 'thumbnail_url',
 'event_suitable',
 'property_type_Loft',
 'bed_type_Real Bed',
 'room_type_Shared room',
 'child_friendly',
 'property_type_Condominium',
 'property_type_Other',
 'super_host',
 'breakfast',
 'bed_type_Pull-out Sofa',
 'property_type_Bed & Breakfast',
 'long_term_stays',
 'host_greeting',
 'parking',
 'hot_tub_sauna_or_pool',
 'Boston',
 'accessible',
 'host_has_profile_pic',
 'air_conditioning',
 ]
        df[binary_list] = df[binary_list].apply(binary_map)
        columns =  ['room_type_Entire home/apt',
                    'bathrooms',
                    'room_type_Private room',
                    'LA',
                    'property_type_Hostel',
                    'accommodates',
                    'tv',
                    'SF',
                    'median_home_value',
                    'distance_to_center',
                    'elevator',
                    'DC',
                    'property_type_Apartment',
                    'NYC',
                    'time_since_last_review',
                    'property_type_House',
                    'gym',
                    'number_of_reviews',
                    'property_type_Dorm',
                    'cleaning_fee',
                    'Chicago',
                    'white_goods',
                    'internet',
                    'thumbnail_url',
                    'event_suitable',
                    'property_type_Loft',
                    'bed_type_Real Bed',
                    'room_type_Shared room',
                    'child_friendly',
                    'property_type_Condominium',
                    'property_type_Other',
                    'super_host',
                    'breakfast',
                    'bed_type_Pull-out Sofa',
                    'property_type_Bed & Breakfast',
                    'long_term_stays',
                    'host_greeting',
                    'parking',
                    'hot_tub_sauna_or_pool',
                    'Boston',
                    'accessible',
                    'host_has_profile_pic',
                    'air_conditioning',
                    'host_since_day']
        #Encoding the other categorical categoric features with more than two categories
        df = pd.get_dummies(df).reindex(columns=columns, fill_value=0)
        #print(df.head())
    elif (option == "Batch"):
        pass
        #Drop Id
        #df.drop(labels = ["id"], axis = 1, inplace = True)
        # Property_type operation
        #property_type_counts = df['property_type'].value_counts()
        #property_type_counts_less_than_25 = property_type_counts[property_type_counts < 25]
        #df.loc[df['property_type'].isin(property_type_counts_less_than_25.index), 'property_type'] = 'Other'
        #df = pd.get_dummies(df,columns=["property_type"])
        #accommodates operation
        #df = pd.get_dummies(df,columns=["accommodates"])
        #cancellation_policy operation
        #df = pd.get_dummies(df,columns=["cancellation_policy"])
        #cleaning_fee operation
        #df['cleaning_fee'] = df['cleaning_fee'].astype(int)
        #bed_type operation
        #df = pd.get_dummies(df,columns=["bed_type"])
        #room_type operation
        #df = pd.get_dummies(df, columns=["room_type"])
        #bathrooms operation
        #df = pd.get_dummies(df, columns=["bathrooms"])
        #amenities operations
        '''import re
        amenities_set = set()
        for amenitie in df['amenities']:
              amenitie_set = set(re.sub(r'(\"|\{|\})', '', amenitie).split(','))
              for piece in amenitie_set:
                  if "translation missing" not in piece and piece:
                      amenities_set.add(piece.strip())
        amenities_list = list(df.amenities)
        amenities_list_string = " ".join(amenities_list)
        amenities_list_string = amenities_list_string.replace('{', '')
        amenities_list_string = amenities_list_string.replace('}', ',')
        amenities_list_string = amenities_list_string.replace('"', '')
        amenities_set = [x.strip() for x in amenities_list_string.split(',')]
        amenities_set = set(amenities_set)    
        
        df.loc[df['amenities'].str.contains('24-hour check-in'), 'check_in_24h'] = 1
        df.loc[df['amenities'].str.contains('Air conditioning|Central air conditioning'), 'air_conditioning'] = 1
        df.loc[df['amenities'].str.contains('Amazon Echo|Apple TV|Game console|Netflix|Projector and screen|Smart TV'), 'high_end_electronics'] = 1
        df.loc[df['amenities'].str.contains('BBQ grill|Fire pit|Propane barbeque'), 'bbq'] = 1
        df.loc[df['amenities'].str.contains('Balcony|Patio'), 'balcony'] = 1
        df.loc[df['amenities'].str.contains('Beach view|Beachfront|Lake access|Mountain view|Ski-in/Ski-out|Waterfront'), 'nature_and_views'] = 1
        df.loc[df['amenities'].str.contains('Bed linens|'), 'bed_linen'] = 1
        df.loc[df['amenities'].str.contains('Breakfast'), 'breakfast'] = 1
        df.loc[df['amenities'].str.contains('TV'), 'tv'] = 1
        df.loc[df['amenities'].str.contains('Coffee maker|Espresso machine'), 'coffee_machine'] = 1
        df.loc[df['amenities'].str.contains('Cooking basics'), 'cooking_basics'] = 1
        df.loc[df['amenities'].str.contains('Dishwasher|Dryer|Washer'), 'white_goods'] = 1
        df.loc[df['amenities'].str.contains('Elevator'), 'elevator'] = 1
        df.loc[df['amenities'].str.contains('Exercise equipment|Gym|gym'), 'gym'] = 1
        df.loc[df['amenities'].str.contains('Family/kid friendly|Children|children'), 'child_friendly'] = 1
        df.loc[df['amenities'].str.contains('parking'), 'parking'] = 1
        df.loc[df['amenities'].str.contains('Garden|Outdoor|Sun loungers|Terrace'), 'outdoor_space'] = 1
        df.loc[df['amenities'].str.contains('Host greets you'), 'host_greeting'] = 1
        df.loc[df['amenities'].str.contains('Hot tub|Jetted tub|hot tub|Sauna|Pool|pool'), 'hot_tub_sauna_or_pool'] = 1
        df.loc[df['amenities'].str.contains('Internet|Pocket wifi|Wifi'), 'internet'] = 1
        df.loc[df['amenities'].str.contains('Long term stays allowed'), 'long_term_stays'] = 1
        df.loc[df['amenities'].str.contains('Pets|pet|Cat(s)|Dog(s)|Pets live on this property'), 'pets_allowed'] = 1
        df.loc[df['amenities'].str.contains('Private entrance'), 'private_entrance'] = 1
        df.loc[df['amenities'].str.contains('Safe|Security system'), 'secure'] = 1
        df.loc[df['amenities'].str.contains('Self check-in'), 'self_check_in'] = 1
        df.loc[df['amenities'].str.contains('Smoking allowed'), 'smoking_allowed'] = 1
        df.loc[df['amenities'].str.contains('Step-free access|Wheelchair|Accessible'), 'accessible'] = 1
        df.loc[df['amenities'].str.contains('Suitable for events'), 'event_suitable'] = 1   

        # Replacing nulls with zeros for new columns
        cols_to_replace_nulls = df.iloc[:,29:].columns
        df[cols_to_replace_nulls] = df[cols_to_replace_nulls].fillna(0)

        # Produces a list of amenity features where one category (true or false) contains fewer than 10% of listings
        infrequent_amenities = []
        for col in df.iloc[:,75:].columns:
            if (df[col].sum() < len(df)/50) | (df[col].sum() > len(df)/1.02):
               infrequent_amenities.append(col)  

        for i in df.iloc[:,29:].columns : 
          print(df[i].value_counts())     
        
        #????????????????????????????
        # del df['amenities']
        # del df['self_check_in']
        # del df['bed_linen']
        # del df['nature_and_views'] 

        # city operations 
        df = pd.concat([df, pd.get_dummies(df['city'])], axis=1)

        #last_review operations
        df.first_review = pd.to_datetime(df.first_review) 

        import datetime # we create a new column named 'time_since_last_review'
        df['time_since_last_review'] = (datetime.datetime.today() - pd.to_datetime(df['last_review'])).dt.days
        df['time_since_last_review']

        #host_since operations
        df.host_since = pd.to_datetime(df.host_since) # Converting to datetime

        import datetime # we create a new column named 'host_since_day'
        df['host_since_day'] = (datetime.datetime.today() - pd.to_datetime(df['host_since'])).dt.days
        df['host_since_day']

        #host_response_rate operations
        # Bin into four categories
        df.host_response_rate = pd.cut(df.host_response_rate, bins=[0, 50, 90, 99, 100], labels=['0-49%', '50-89%', '90-99%', '100%'], include_lowest=True)

        df.host_response_rate = df.host_response_rate.astype('str') # Converting to string

        df.host_response_rate.replace('nan', 'unknown', inplace=True) # Replace nulls with 'unknown'

        #review_scores_raating operations
        # Bin into four categories
        df.review_scores_rating = pd.cut(df.review_scores_rating, bins=[0, 50, 90, 99, 100], labels=['0-49%', '50-89%', '90-99%', '100%'], include_lowest=True)

        df.review_scores_rating = df.review_scores_rating.astype('str') # Converting to string

        df.review_scores_rating.replace('nan', 'unknown', inplace=True) # Replace nulls with 'unknown'

        #host_profile_pic operations
           #We changed the true ones 1 the false ones 0 and filled the nan values with 0
        df.loc[df.host_has_profile_pic == 't', 'host_has_profile_pic'] = 1
        df.loc[df.host_has_profile_pic == 'f', 'host_has_profile_pic'] = 0

        #host_identity_verified operations
           #We changed the true ones 1 the false ones 0 and filled the nan values with 0
        df.loc[df.host_identity_verified == 't', 'host_identity_verified'] = 1
        df.loc[df.host_identity_verified == 'f', 'host_identity_verified'] = 0

        #instant_bookable
           #We changed the true ones 1 the false ones 0 
        df.loc[df.instant_bookable == 't', 'instant_bookable'] = 1
        df.loc[df.instant_bookable == 'f', 'instant_bookable'] = 0

        #super_host operations
        df['super_host'] = ((df['host_since_day'] > df['host_since_day'].mean()) &
                    (df['host_identity_verified'] == 1) &
                    (df['host_has_profile_pic'] == 1) &
                    ((df['host_response_rate'] == '90-99%') | (df['host_response_rate'] == '100%')) &
                    ((df['review_scores_rating'] == '90-99%') | (df['review_scores_rating'] == '100%')))
        df['super_host'].astype('int')

        #median_home_value operations ????????????????

        #distance_to_center operations

        for index, row in df.iterrows(): # Defining center coordinates of each city
            if df.loc[index, 'city'] == 'NYC':
                df.loc[index, 'lat_center'] = 40.72
                df.loc[index, 'long_center'] = -74.0060
            elif df.loc[index, 'city'] == 'LA':
                df.loc[index, 'lat_center'] = 34.0522
                df.loc[index, 'long_center'] = -118.2437
            elif df.loc[index, 'city'] == 'SF':
                df.loc[index, 'lat_center'] = 37.7749
                df.loc[index, 'long_center'] = -122.4194
            elif df.loc[index, 'city'] == 'DC':
                df.loc[index, 'lat_center'] = 38.9072
                df.loc[index, 'long_center'] = -77.0369
            elif df.loc[index, 'city'] == 'Chicago':
                df.loc[index, 'lat_center'] = 41.8781
                df.loc[index, 'long_center'] = -87.6298
            elif df.loc[index, 'city'] == 'Boston':
                df.loc[index, 'lat_center'] = 42.3601
                df.loc[index, 'long_center'] = -71.0589

        df['distance_to_center']=np.sqrt((df['lat_center']-df['latitude'])**2+(df['long_center']-df['longitude'])**2)# Creates the new column'''

        '''del df['description'] # String values
        del df['first_review'] #  Used to create 'super_host'
        del df['host_since'] # # Used to create 'super_host'
        del df['last_review'] #  Used to create 'super_host'
        del df['name'] # String values
        del df['neighbourhood'] # String values
        del df['city'] # get dummies is implemented
        del df['latitude'] # Coordinates
        del df['longitude'] # Coordinates
        del df['host_response_rate'] # Used to create 'super_host'
        del df['review_scores_rating'] # Used to create 'super_host'
        del df['bedrooms'] # High correlation with accomadation
        del df['beds'] # High correlation with accomadation
'''
        df['time_since_last_review'] = df['time_since_last_review'].fillna(0)

        boolean_columns = df.select_dtypes(include='bool').columns
        df[boolean_columns] = df[boolean_columns].astype(int)

                    
    else:
        print("Incorrect operational options")


    #feature scaling
    #sc = MinMaxScaler()
    #df['tenure'] = sc.fit_transform(df[['tenure']])
    #df['MonthlyCharges'] = sc.fit_transform(df[['MonthlyCharges']])
    #df['TotalCharges'] = sc.fit_transform(df[['TotalCharges']])
    return df
        

    