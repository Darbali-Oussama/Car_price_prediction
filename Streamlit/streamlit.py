import pickle as pk

import sklearn
import streamlit as st

filename = 'LR_model_prix_voitures_avito.sav'
lr = pk.load(open(filename, 'rb'))

st.title("Avito : Prediction de prix des voitures")
chev = st.selectbox('Cheval',[i for i in range(4,43)])
annee = st.selectbox('Annee',[i for i in range(2023,1980,-1)])
carb = st.selectbox('Carburant',['Diesel', 'Essence','Hybride'])
boite = st.selectbox('boite a vitesse',['Automatique','Manuelle'])
model = st.selectbox('Modele',['Dokker', 'Duster','Logan'])

lstt=['0 - 4 999','5 000 - 9 999', '10 000 - 14 999',
      '15 000 - 19 999','20 000 - 24 999','25 000 - 29 999',
      '30 000 - 34 999','35 000 - 39 999','40 000 - 44 999',
      '45 000 - 49 999','50 000 - 54 999', '55 000 - 59 999',
       '60 000 - 64 999', '65 000 - 69 999','70 000 - 74 999',
       '75 000 - 79 999', '80 000 - 84 999', '85 000 - 89 999',
       '90 000 - 94 999', '95 000 - 99 999','100 000 - 109 999',
       '110 000 - 119 999','120 000 - 129 999', '130 000 - 139 999', 
       '140 000 - 149 999','150 000 - 159 999', '160 000 - 169 999',
       '170 000 - 179 999', '180 000 - 189 999','190 000 - 199 999',
       '200 000 - 249 999',  '250 000 - 299 999','300 000 - 349 999', 
       '350 000 - 399 999', '400 000 - 449 999', '450 000 - 499 999',
       'Plus de 500 000']
kilom=st.selectbox('kilometrage',lstt)
ls3=['Cheval', 'Age', 'Diesel', 'Essence',
       'Hybride', 'Automatique',
       'Manuelle', 'Dokker', 'Duster',
       'Logan', '0 - 4 999', '10 000 - 14 999',
       '100 000 - 109 999', '110 000 - 119 999',
       '120 000 - 129 999', '130 000 - 139 999',
       '140 000 - 149 999', '15 000 - 19 999',
       '150 000 - 159 999', '160 000 - 169 999',
       '170 000 - 179 999', '180 000 - 189 999',
       '190 000 - 199 999', '20 000 - 24 999',
       '200 000 - 249 999', '25 000 - 29 999',
       '250 000 - 299 999', '30 000 - 34 999',
       '300 000 - 349 999', '35 000 - 39 999',
       '350 000 - 399 999', '40 000 - 44 999',
       '400 000 - 449 999', '45 000 - 49 999',
       '450 000 - 499 999', '5 000 - 9 999',
       '50 000 - 54 999', '55 000 - 59 999',
       '60 000 - 64 999', '65 000 - 69 999',
       '70 000 - 74 999', '75 000 - 79 999',
       '80 000 - 84 999', '85 000 - 89 999',
       '90 000 - 94 999', '95 000 - 99 999',
       'Plus de 500 000']
def tomlvect():
    ls=47*[0]
    age=2023-int(annee)
    ls[0]=int(chev)
    ls[1]=age
    ls[ls3.index(carb)]=1
    ls[ls3.index(boite)]=1
    ls[ls3.index(model)]=1
    ls[ls3.index(kilom)]=1
    return ls

pr=str(lr.predict([tomlvect()])[0])+" DH"
if st.button('Predire le prix'):
    st.title(pr)