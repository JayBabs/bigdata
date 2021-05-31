import csv
import socket
import requests
import random
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time



infile = "c_File.csv"
outfile = "d.csv"
apifile = "apikey.txt"
liste_cle = []
liste_strings=[]



def request_test(liste_cle1, company_name1,brandname1,product_code1, model_number1,med_specialty1,device_gender1,premarket_submission1,device_class1):

    
    
    cle = random.choice(liste_cle1)
    
    company_name= company_name1
    brandname = brandname1
    product_code = product_code1
    model_number = model_number1
    med_specialty = med_specialty1
    device_gender = device_gender1
    premarket_submission = premarket_submission1
    device_class = device_class1

    
    # Event 

    url = "https://api.fda.gov/device/event.json?api_key="+ cle +"&search=device.brand_name:"+str(brandname)+" + AND +device.model_number:" + str(model_number) + "&count=event_type.exact"
    v1 = ""
    v2 = ""
    v3 = ""
    #url = "https://api.fda.gov/device/event.json?search=device.brand_name:"+val+" + AND +device.model_number:" + modl + "&count=event_type.exact"
    try:
        response = requests.get(url,timeout=10)
    except socket.gaierror:
        print("connection error")
        response = "err"
        v1 = "connection error"
        v2 = "connection error"
        v3 = "connection error"

    data = response.json()

    if 'results' in data:
        res = data['results']
        #print(data['results'])
        
        for x in res:
            if x["term"] == "Malfunction":
                v1 = x["count"]
                malfunction = v1
            elif x["term"] == "Injury":
                v2 = x["count"]
                injury = v2
            elif x["term"] == "Death":
                v3 = x["count"]
                death = v3
    if v1 == "":
        malfunction = 0
    if v2 == "":
        injury = 0
    if v3 == "":
        death = 0

    #Recalls
    rec = ""
    url = "https://api.fda.gov/device/event.json?"+ cle +"&search=device.brand_name:"+brandname+" +AND +device.model_number:" + model_number + "&count=remedial_action.exact"
    try:
        response = requests.get(url,timeout=10)
    except socket.gaierror:
        print("connection error")
        response = "err"
        rec = "connection error"

    data = response.json()

    if 'results' in data:
        for x in data['results']:
            if x["term"] == "Recall":
                rec = x["count"]

    if rec == "":
        rec = "0"


    stringfinal = (company_name + "@" + brandname + "@" + product_code + "@" + model_number + "@" + med_specialty + "@" + str(device_gender) + "@" + premarket_submission + "@" + device_class + "@" + str(rec) + "@" + str(malfunction) + "@" + str(injury) + "@" + str(death))
    print(stringfinal)
    liste_strings.append(stringfinal)


with open(apifile,mode='r') as ficher_ref_Cle:
    liste_cle = [x.rstrip("\n") for x in ficher_ref_Cle.readlines()]


   



with open(infile, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter="@")
    line_count = 0
    liste_de_liste = []

    

    
   
    for row in csv_reader:

        

        

        
        processes = []
        with ThreadPoolExecutor(max_workers=5000) as executor:
            for row in csv_reader:
                company_name = (row['company_name'])
                brandname = (row['brand_name'])
                product_code = (row['product_code'])
                model_number = (row['model_number'])
                med_specialty = (row['med_speciality'])
                device_gender = (row['device_gender'])
                premarket_submission = (row['premarket_submission'])
                device_class = (row['device_class'])
                
                processes.append(executor.submit(request_test,liste_cle, company_name,brandname,product_code, model_number,med_specialty,device_gender,premarket_submission,device_class))
        


      
 
print(len(liste_strings))

textfile = open(outfile, "w")
for element in liste_strings:
    textfile.write(element + "\n")
