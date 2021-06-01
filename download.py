import urllib.request

from zipfile import ZipFile
# print('Beginning file download with urllib2...')


liste_url = []
liste_nom = []
liste_nom_de_fichier = []

for x in range(1,31):
    url = 'https://download.open.fda.gov/device/udi/device-udi-0001-of-0030.json.zip'
    url_debut = 'https://download.open.fda.gov/device/udi/device-udi-00'
    url_fin = '-of-0030.json.zip'
    milieu = ("{:02d}".format(x))

    nomfichier = milieu

    liste_nom.append(milieu)

    

    url_complet = url_debut + milieu + url_fin
    
    liste_url.append(url_complet)


for y in range(30):

    

    print(liste_nom[y])
    print(liste_url[y])


    chemin_fichier = (r"C:\projet_de_bums\DATABASE\device\fichiers" + liste_nom[y] + ".zip")
    liste_nom_de_fichier.append(chemin_fichier)

    

    url = liste_url[y]
    urllib.request.urlretrieve(url, chemin_fichier)




for z in liste_nom_de_fichier:
    zip = ZipFile(liste_nom_de_fichier[z])
    zip.extractall()


# url = 'https://download.open.fda.gov/device/udi/device-udi-0001-of-0030.json.zip'
# urllib.request.urlretrieve(url, 'c:\projet_de_bums\partie1.zip')
