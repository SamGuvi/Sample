import streamlit as st
import pickle

st.title('Flight Price Prediction')
st.write('This app predicts the flight price')

Airline=st.sidebar.selectbox('Select the Airline',("",'SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo','Air_India'))
Airline_dict={'AirAsia':0,'Indigo':1,'GO_FIRST':3, 'SpiceJet':4, "Air_India":5 ,'Vistara':6}


Source_City=st.sidebar.selectbox('Select the Source City',('Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai'))
Source_City_dict={'Chennai':0,'Kolkata':1,'Mumbai':2,'Bangalore':3,'Hyderabad':4,'Delhi':5}

Departure_Time= st.sidebar.selectbox('Select the Departure Time',('Early_Morning', 'Morning', 'Afternoon', 'Evening', 'Night','Mid_Night'))
Departure_Time_dict={'Early_Morning':0,'Morning':1,'Afternoon':2,'Evening':3,'Night':4,'Mid_Night':5}

Stops=st.sidebar.selectbox('Select the Number of Stops',('zero', 'one', 'two','two_or_more'))
Stops_dict={'one':1,'zero':0,'two':2,'two_or_more':3}

Arrival_Time=st.sidebar.selectbox('Select the Arrival Time',('Early_Morning', 'Morning', 'Afternoon', 'Evening', 'Night','Mid_Night'))
Arrival_Time_dict={'Early_Morning':0,'Morning':1,'Afternoon':2,'Evening':3,'Night':4,'Mid_Night':5}

Destination_City=st.sidebar.selectbox('Select the Destination City',('Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai'))
Destination_City_dict={'Kolkata':0,'Chennai':1,'Bangalore':2,'Mumbai':3,'Hyderabad':4,'Delhi':5}

Class=st.sidebar.selectbox('Select the Class',('ECONOMY', 'BUSINESS'))
Class_dict={'ECONOMY':0,'BUSINESS':1}

Days_Left=st.sidebar.number_input('Select the Days Left',min_value=1,max_value=300,value=1)

Data=[Airline_dict[Airline],Source_City_dict[Source_City],Departure_Time_dict[Departure_Time],Stops_dict[Stops],Arrival_Time_dict[Arrival_Time],Destination_City_dict[Destination_City],Class_dict[Class],Days_Left]
if st.button('Predict Flight Price'):
    
    model=pickle.load(open('flight.pkl','rb'))
    result=model.predict([Data])
    st.write(result)

