import glob 
import time
import json


#Critères :
# Dans les products codes 
# Avec premarket submissions

def isInside(pc):
    if pc in pcodef:
        return pcodef.get(pc)
    elif pc in pcodeh:
        return pcodeh.get(pc)
    elif pc in pcodeu:
        return pcodeu.get(pc)
    else:
        return -1


pcodeu = { "HRY":59, "JDG":57,"NAV":28, "NCA":28, "NKB":47, "NKG":47, "NVC":47,  "ODH":42,
   "OIR":42, "OQB":47, "OVZ":47, "OWI":47, "PAZ":42, "PFM":47,  "PML":47,  "QNI":59, "DSW":42,
    "DSZ":42, "DTB":42, "DTD":42, "DXY":42,"EZT":42, "KJF":42,  "NVM":42,  "PNJ":42,
      "HRY":59, "HRZ":59, "HSA":59, "HSH":59, "HSX":59, "HTG":59, "JWH":59, "KMB":59,"KRN":59,
       "KRO":59, "HRP":59, "KRQ":59, "KRR":59, "KRS":59, "KTX":59, "KYK":59,"LGE":59, "LXY":59,
        "MBD":59, "MBH":59, "MBV":59, "NJD":59, "NPJ":59,"OIY":59,"JDD":57, "JDG":57, "JDH":57,
         "JDI":57,"JDJ":57, "JDK":57, "JDL":57, "KMC":57, "KWA":57, "KWB":57, "KWL":57, "KWY":57,
             "KXA":57, "KXB":57, "KXD":57, "LPF":57, "LPH":57, "LTO":57, "LWJ":57,
             "LZO":57, "LZY":57, "MAY":57, "MBL":57, "MEH":57,   "OCG":57,
              "OQG":57, "OQH":57, "OQI":57, "OVO":57, "PBI":57,  "PKK":28, "PNB":28,
                 "JDN":47, "KWP":47, "KWQ":47, "LYP":47,
                  "MCV":47, "MNH":47, "MNI":47,  "NQP":47, "NQW":47, "NVR":47, "OPD":47,
                   "OJB":47, "OJM":47, "OVD":47, "OVE":47, "PEK":47, "PHM":47, "PHQ":47, "PLR":47,
                    "PWG":47, "HSD":56, "KWR":56, "KWS":56, "KWT":56, "KYM":56, "MBF":56, "MJT":56,
                     "PAO":56, "PHX":56, "PKC":56, "QHQ":56, "MPC":23, "MRM":23,  }

pcodeh = {"PEW":0, "OTM":0, "FTQ":0, "JCW":0, "FAE":0, "FHW":0, "NOY":0, "FAF":0, "FTO":0, "EZZ":0, "NJC":0}
pcodef = {"OTN":100, "OTO":100, "OTP":100, "PAG":100, "PAH":100, "PAI":100, "PAJ":100, "PBQ":100, "HDO":100, "HDT":100, "HFJ":100, "HFY":100, "HGB":100, "HHS":100, "KNH":100, "NAJ":100, "FTR":100, "FWM":100, "PQN":100, "OXM":100, "OXN":100}

debug = 1
liste_strings =[]

fichier_ref = "C:\projet_de_bums\DATABASE\Device\calls\call_device_all.json"

for f in glob.iglob("*.json"): # generator, search immediate subdirectories 
    print(f)#debug

    with open(f) as json_file:
            data = json.load(json_file)
            for element in data['results']:
                



                #PREMARKET NUMBER FILTERING
                if 'premarket_submissions' not in element :
                    premarket_found = False
                    
                else:
                    premarket_found = True
                    


                if len(element["product_codes"]) > 0 and premarket_found:
                    x = element["product_codes"][0]["code"].replace(",","")
                    

                    type = isInside(x)

                    

                    if type >= 0:


                        #BRAND NAME FILTERING
                        tempBrand = element["brand_name"].encode("ascii","ignore")
                        filterBrand = tempBrand.decode().replace(",","").rstrip("\n")
                        filterBrand = filterBrand.replace(";","").replace("+","").replace("#","")
                        brand_name = filterBrand



                        # Modèle

                        if 'version_or_model_number' not in element :
                            model_number.append("N/A")
                        else:
                            tempModl = element["version_or_model_number"].encode("ascii","ignore")
                            filterModl = tempModl.decode().replace(",","").rstrip("\n")
                            modl = filterModl.replace("+","").replace("#","")
                        


                       


                        company_name = element['company_name']
                        brand_name = filterBrand
                        product_code = x
                        model_number = modl
                        med_speciality = element["product_codes"][0]["openfda"]["medical_specialty_description"]
                        device_gender = type
                        premarket_submission = element["premarket_submissions"][0]["submission_number"].replace(",","")
                        device_class = element["product_codes"][0]["openfda"]["device_class"]




                        if debug == 1:

                            # print(company_name) # A
                            # print(brand_name) # B
                            # print(product_code) # C
                            # print(model_number) # D 
                            # print(med_speciality) # E 
                            # print(str(device_gender)) # F 
                            # print(premarket_submission) # G 
                            # print(device_class) # H 


                            stringfinal = (company_name + "@" + brand_name + "@" + product_code + "@" + model_number + "@" + med_speciality + "@" + str(device_gender) + "@" + premarket_submission + "@" + device_class)
                            liste_strings.append(stringfinal)
                            # company_name@brand_name@product_code@model_number@med_speciality@device_gender@premarket_submission@device_class

                            
                        ###
                        # Company_name
                        # brand_name
                        # product_code
                        # model_number
                        # med_specialty 
                        # device_gender
                        # premarket_submission
                        # device_class



print(len(liste_strings))

textfile = open("c_file.csv", "w")
for element in liste_strings:
    textfile.write(element + "\n")

                        








   




