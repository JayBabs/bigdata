import csv
import socket
import requests
import random

infile = "c_File.csv"
outfile = "d1.csv"




with open(infile, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter="@")
    line_count = 0
    liste_de_liste = []

    
    liste_strings = []
    liste_cle = ["oOoFBxZ9XfHu2g6CihCVA77WdjwjnEWw3W2msbsl", "qgs32EuMqJuePIf7g9mGTj4YEjuohFxRcq7c8J32", "MK0Lb9aQBg3rjRiTfBMEA6VBt1HbcT6M19y6Hyp0" , "YU7Y1YVA1Z0SaumBdTVahkfGqeD8OlCdUreOO703", "vsNQc9AWLskxkBStJDJkw4FEPtlQ7AP6zOIb9SqT", "eeKYhxuWzFYqaTYTbyvlk8IecCX00lqXcyfqF94d", "okJvt8q1nMUddRmdI0qeGOnVPn7zfYjH37dmWb4z", "QjV44nBlvQBJJtdbmCTxTtqg2gil7iJUFtX87oUt",  "7p2Sb0rnSz4wuVMqgITaqjrgAjDooCTEOocZIqC4", "i451zSa5WaoPoj1BRik1NKrlBuEaWuvBwZsoFFdG", "uTcCJ8BJRS8hyaIhbfm1cgpQhb0AudfOxiYzKrvA"]
    for row in csv_reader:


        company_name = (row['company_name'])
        brandname = (row['brand_name'])
        product_code = (row['product_code'])
        model_number = (row['model_number'])
        med_specialty = (row['med_speciality'])
        device_gender = (row['device_gender'])
        premarket_submission = (row['premarket_submission'])
        device_class = (row['device_class'])

        line_count += 1




        
        



        cle = random.choice(liste_cle)
        


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
        liste_strings.append(stringfinal)
        print(len(liste_strings))

        



print(len(liste_strings))

textfile = open(outfile, "w")
for element in liste_strings:
    textfile.write(element + "\n")
