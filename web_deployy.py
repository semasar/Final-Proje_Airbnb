#Import libraries
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#load the model from disk
import joblib
filename = 'XGB_model.sav'
model = joblib.load(filename)

#Import python scripts
from preprocessingg import preprocess


def main():
    #Setting Application title
    st.title('Infotech Academy Airbnb Price-Predict Model App')

      #Setting Application description
    st.markdown("""
     :dart:  Predict Airbnb accommodation prices based on various features and parameters. Instant and batch data predictions supported. \n
    """)
    st.markdown("<h3></h3>", unsafe_allow_html=True)

    #Setting Application sidebar default
    #image = Image.open('airbnb.png')
    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?", ("Online", "Batch"))
    st.sidebar.info('This app is created to predict Airbnb price use case')
    #st.sidebar.image(image)



    if add_selectbox == "Online":
        st.info("Input data below")
        st.subheader("***")

        #Based on our optimal features selection
        #city
        st.subheader("City data")
        city_ny=0
        city_sf=0
        city_la=0
        city_dc=0
        city_boston=0
        city_chicago=0
        city=['NY','SF','DC','LA','Chicago','Boston']
        cityw = st.selectbox('City ', (city),key="city")
        if cityw=='NY':city_ny=1
        if cityw=='SF':city_sf=1
        if cityw=='DC':city_dc=1
        if cityw=='LA':city_la=1
        if cityw=='Chicago':city_chicago=1
        if cityw=='Boston':city_boston=1
        else:city_boston=1
        #accommodates
        st.subheader("Number of Guest")                       
        guest = st.slider('Number of Guest ', min_value=1, max_value=16, value=1)
        #property_type
        st.subheader("Property Type")  
        prop_apartment=0
        prop_house=0
        prop_condominium=0
        prop_townhouse=0
        prop_loft=0
        prop_guesthouse=0
        prop_bedandbreakfast=0
        prop_bungalow=0
        prop_villa=0
        prop_dorm=0
        prop_camper=0
        prop_timeshare=0
        prop_cabin=0
        prop_inlaw=0
        prop_hostel=0
        prop_butik_hotel=0
        prop_boat=0
        prop_other=0
        prop=['Apartment','House','Condominium','Townhouse','Loft','Guesthouse','Bed & Breakfast','Bungalow','Villa','Dorm','Camper/RV','Timeshare','Cabin','In-law','Hostel','Boutique hotel','Boat','Other']
        propw = st.selectbox('What kind of property would you like to stay in?',(prop),key='prop')
        
        if propw=='Apartment':prop_apartment=1
        if propw=='House':prop_house=1
        if propw=='Other':prop_other=1
        else:prop_other=1
        #room_type
        st.subheader("Room Type") 
        room_entire=0
        room_privat=0
        room_shared=0
        room_type=['Entire Home','Private Room','Shared Room']
        room_typew = st.selectbox('What kind of room would you like to stay in?', (room_type),key='room_type')
        if room_typew=='Entire Home':room_entire=1
        if room_typew=='Private Room':room_privat=1
        if room_typew=='Shared Room':room_shared=1
        else:room_shared=1
        #bed_type
        st.subheader("Bed Type") 
        Real_Bed=0              
        Pull_out_Sofa=0          
        Airbed=0                 
        Futon=0                   
        Couch=0   
        bed_type=['Real Bed','Pull-out Sofa','Airbed','Futon','Couch']
        bed_typew=st.selectbox('What kind of bed would you like?', (bed_type),key='bed_type')
        if bed_typew=='Pull-out Sofa':Pull_out_Sofa=1
        else: Real_Bed=1
          
        
        #Bathroom
        st.subheader("Number of Bathroom")   
        bathrooms = st.slider('Number of Bathroom', min_value=0.0, max_value=8.0, value=1.0,step=0.5)
        #amenities
        
        st.subheader("Basic Amenities")   
         
        a_c = st.selectbox('Do you want air conditioning?', ('No','Yes'))
      
        breakfast = st.selectbox('Do you want breakfast?', ('No','Yes')) 
        tv = st.selectbox('Do you want tv?', ('No','Yes')) 
      
        w_g =  st.selectbox('Do you want white goods?', ('No','Yes')) 
        elevator =  st.selectbox('Do you want elevator?', ('No','Yes')) 
        gym=  st.selectbox('Do you want gym?', ('No','Yes')) 
        c_f =  st.selectbox('Do you want child friendly?', ('No','Yes'))
        park =  st.selectbox('Do you want parking?', ('No','Yes'))
        
        h_g =  st.selectbox('Do you want host greeting?', ('No','Yes')) 
        h_t = st.selectbox('Do you want hot tub,sauna or pool?', ('No','Yes')) 
        int = st.selectbox('Do you want internet?', ('No','Yes')) 
        l_s = st.selectbox('Do you want long term stays?', ('No','Yes')) 
      
        accessible =  st.selectbox('Do you want accessible?', ('No','Yes')) 
        e_s =  st.selectbox('Do you want event suitable?', ('No','Yes'))
        c_fee=st.selectbox('Is there Cleaning Fee?',('No','Yes'))
        host_prof=st.selectbox('Is there Host Profile Picture?',('No','Yes'))
        thumb_nail=st.selectbox('Is there Home Picture?',('No','Yes'))
        
        
        #superhost
        st.subheader("Top Notch Accommodation")   
        s_host = st.selectbox('Super Host', ('No','Yes')) 
        st.subheader("Enter House value")
        house_value = st.number_input('House Value', min_value=0, value=1000,step=1000)
        st.subheader("Distance")
        distance_value = st.number_input('Distance')#???????
        st.subheader("Number of Reviews")
        number_of_reviews = st.number_input('Number of Reviews')#???????
        st.subheader("Host since day")
        host_since_day = st.number_input('Number of host since day')#???????
        

        #time_since_last
        st.subheader("Timeliness")   
        timeliness= st.number_input('Last Commented',value=1)#??????

        data = {   'room_type_Entire home/apt':room_entire,
                   'bathrooms':bathrooms,
                   'room_type_Private room':room_privat,
                    'LA':city_la,
                    'property_type_Hostel':prop_hostel,
                    'accommodates':guest,
                    'tv':tv,
                    'SF':city_sf,
                    'median_home_value':house_value,
                    'distance_to_center':distance_value,
                    'elevator':elevator,
                    'DC':city_dc,
                    'property_type_Apartment':prop_apartment,
                    'NYC':city_ny,
                    'time_since_last_review':timeliness,
                    'property_type_House':prop_house,
                    'gym':gym,
                    'number_of_reviews':number_of_reviews,
                    'property_type_Dorm':prop_dorm,
                    'cleaning_fee':c_fee,
                    'Chicago':city_chicago,
                    'white_goods':w_g,
                    'internet':int,
                    'thumbnail_url':thumb_nail,
                    'event_suitable':e_s,
                    'property_type_Loft':prop_loft,
                    'bed_type_Real Bed':Real_Bed,
                    'room_type_Shared room':room_shared,
                    'child_friendly':c_f,
                    'property_type_Condominium':prop_condominium,
                    'property_type_Other':prop_other,
                    'super_host':s_host,
                    'breakfast':breakfast,
                    'bed_type_Pull-out Sofa':Pull_out_Sofa,
                    'property_type_Bed & Breakfast':prop_bedandbreakfast,
                    'long_term_stays':l_s,
                    'host_greeting':h_g,
                    'parking':park,
                    'hot_tub_sauna_or_pool':h_t,
                    'Boston':city_boston,
                    'accessible':accessible,
                    'host_has_profile_pic':host_prof,
                    'air_conditioning':a_c,
                    'host_since_day':host_since_day
                   }
            
        features_df = pd.DataFrame.from_dict([data])
        st.markdown("<h3></h3>", unsafe_allow_html=True)
        st.write('Overview of input is shown below')
        st.markdown("<h3></h3>", unsafe_allow_html=True)
        st.dataframe(features_df)
        
        #Preprocess inputs
        preprocess_df = preprocess(features_df, 'Online')

        #prediction = model.predict(preprocess_df)

        if st.button('Predict'):
    # Burada tahmin işlemini yapacak olan modelinize göre giriş verilerini almanız gerekecektir.
    # Örnek olarak "input_features" adında bir değişken kullanarak giriş özelliklerini alalım.
          #input_features = get_input_features()  # Bu fonksiyonu kendi projenize uygun şekilde tanımlamalısınız.

    # Modeli kullanarak fiyat tahminini gerçekleştirin.
          predicted_price = model.predict(preprocess_df)

    # Tahmin sonucunu ekrana yazdırın.
          st.success(f"Predicted Price of AIRBNB House: ${np.exp(predicted_price[0]):.1f}")
    
    else:
        st.subheader("Dataset upload")
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file,encoding= 'utf-8')
            #Get overview of data
            st.write(data.head())
            st.markdown("<h3></h3>", unsafe_allow_html=True)
            #Preprocess inputs
            preprocess_df = preprocess(data, "Batch")
            if st.button('Predict'):
                #Get batch prediction
                prediction = model.predict(preprocess_df)
                prediction_df = pd.DataFrame(prediction, columns=["Predictions"])
                prediction_df = prediction_df.replace(f"Predicted Price: ${predicted_price:.1f}")

                st.markdown("<h3></h3>", unsafe_allow_html=True)
                st.subheader('Prediction')
                st.write(prediction_df)
            
if __name__ == '__main__':
        main()


                            
                             