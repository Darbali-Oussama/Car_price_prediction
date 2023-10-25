import pandas as pd

df=pd.read_csv('avitoCarprices.csv',encoding='utf-8')
print(df.head())
df.drop(['Première main', 'Marque', 'État', 'Nombre de portes','Origine'], axis=1, inplace=True)

def clean(x):
    x=x.encode().decode("utf-8")
    x.replace("\u202f","")
    y=list(x)[:-7]+list(x)[-6:-3]
    s = ''.join(map(str, y))
    try:
        s = ''.join(map(str, y))
        n=len(y)
        if n< 5 or n> 6:
            return('prixnonspec')
        else:
            return(int(str(s)))
    except ValueError:
        y=list(x)[2:-7]+list(x)[-6:-3]
        n=len(y)
        s = ''.join(map(str, y))
        if n< 5 or n> 6:
            return('prixnonspec')
        else:
            return(int(str(s)))
def anneetonbr(x):
    return 2023-int(x)
df.rename(columns = {'Chev':'Cheval','Boite a vitesse':'Boite_a_vitesse','Modèle':'Modele','Kilométrage':'Kilometrage','Nombre de portes':'Nombre_de_portes','Année-Modèle':'Age'}, inplace=True)
df['prix'] = df['prix'].apply(clean)
df.drop(df[df['prix'] == 'prixnonspec'].index, inplace=True)
df.drop(df[df['Age'] == '1980 ou plus ancien'].index, inplace=True)
df['Age'] = df['Age'].apply(anneetonbr)
df.drop(df[df['Cheval'] == 'LPG'].index, inplace=True)
df.drop(df[df['Boite_a_vitesse'] == 'Plus de 41 CV'].index, inplace=True)
df.drop(df[df['Boite_a_vitesse'] == 'Electrique'].index, inplace=True)
def cleanchev(x):
    return int(x[:-3])
df['Cheval'] = df['Cheval'].apply(cleanchev)
print(df.head())
df.drop(columns=df.columns[0:2], axis=1,  inplace=True)
print(df.head())
df.to_csv('avito_prix_des_voitures.csv')
