import csv

import cloudscraper
from bs4 import BeautifulSoup

#requests
#cloudfire protection
scraper = cloudscraper.create_scraper(delay=10, browser='chrome')
l=[]
for i in range(2,345):
    print(i)
    htmlpg=scraper.get('https://www.avito.ma/fr/maroc/voitures-%C3%A0_vendre?o='+str(i)+'&brand=13&model=dokker%2Cduster%2Clogan').text
    soup0= BeautifulSoup(htmlpg,'lxml')
    carac0=soup0.find_all('a',class_= 'jejop8-1 cvhTQL')
    for p in carac0:
        g=p.get('href')
        if g!=None:
            htmltest=scraper.get(g).text
            soup= BeautifulSoup(htmltest,'lxml')
            carac=soup.find('div',class_= 'sc-1g3sn3w-3 jhwFxA')
            obj0=soup.find('p',class_='sc-1x0vz2r-0 dYtyob sc-1g3sn3w-13 kliyMh')
            l1=[]
            l2=[]
            l3=[]
            try:
                #erreur d'encoding
                u=obj0.text
                j=u.encode().decode("utf-8").replace(u"\u202f", " ").encode("utf-8")
                l2+=[j]
            except AttributeError:
                l2+=['prixnonspec']
            try:
                obj1=carac.find_all('span',class_= 'sc-1x0vz2r-0 kuCwGF')
                for x in obj1:
                    f=x.text
                    if len(f)<6:
                        c=f
                    elif len(f)<8:
                        h=f
                    else:
                        k=f
                l2+=[c]
                l2+=[h]
                l2+=[k]
                obj2=carac.find_all('li',class_= 'sc-qmn92k-1 ldnQxr')
                for y in obj2:
                    c1=y.find('span',class_= 'sc-1x0vz2r-0 brylYP')
                    c2=y.find('span',class_= 'sc-1x0vz2r-0 jsrimE')
                    l1+=[c1.text]
                    l3+=[c2.text]
                try:
                    l2+=[l3[l1.index('Modèle')]]
                except ValueError:
                    l2+=[None]
                try:
                    l2+=[l3[l1.index('Kilométrage')]]
                except ValueError:
                    l2+=[None]
                try:
                    l2+=[l3[l1.index('Première main')]]
                except ValueError:
                    l2+=[None]
                try:
                    l2+=[l3[l1.index('Marque')]]
                except ValueError:
                    l2+=[None]
                try:
                    l2+=[l3[l1.index('État')]]
                except ValueError:
                    l2+=[None]
                try:
                    l2+=[l3[l1.index('Nombre de portes')]]
                except ValueError:
                    l2+=[None]
                try:
                    l2+=[l3[l1.index('Année-Modèle')]]
                except ValueError:
                    l2+=[None]
                try:
                    l2+=[l3[l1.index('Origine')]]
                except ValueError:
                    l2+=[None]
                l+=[l2]
                print(l2)
            except AttributeError:
                pass
fields = ['prix','Chev','Carburant','Boite a vitesse', 'Modèle','Kilométrage','Première main','Marque','État','Nombre de portes','Année-Modèle','Origine']
with open('avitoCarprices.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(fields)
    write.writerows(l)
        
    


