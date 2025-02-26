#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import re


def f(i):
    if pd.isna(i) or i in(["Missing", '', np.nan, None]):
        return "Missing"
    elif i == "OTH":
        return "OTH"
    elif i in ["Other", "OTHER"]:
        return "Other"
    elif i == "UNK":
        return "UNK"
    elif i =="NI":
        return "NI"
    elif i in (["Unknown", "UNKNOWN"]):
        return "Unknown"
#     elif i in (["No known active allergies"]): 
#         return "No known active allergies"

    elif i=="Tags":
        return "Tags"
#     elif i=="Narrative does not match structure":
#         return "Narrative does not match structure"
    elif i.find("Narrative does not match") !=-1:
        return "Narrative does not match"
    elif i=="See Comment":
        return "See Comment"
    elif i=="Jibber-Jabber":
        return "Jibber-Jabber"
    elif i=="punctuations":
        return "Punctuations"
    
#     elif i == "No Allergy Information Available":
#         return "No Allergy Information Available"
    
        
#     elif i in (["NKMA", "NKA"]):
#         return "NKMA/NKA"


    elif i in (["Other (see comments)", "Other (See Comments)"]):
        return "Other (see Comments)"
    elif i in (["Other (Review Comments!)"]):
        return "Other (Review Comments!)"
    elif i in (["xxxx", "XXXX"]):
        return "xxxx"
    elif i =="ASSERTION":
        return "ASSERTION"
    elif i =="Missing SIG":
        return "Missing SIG"
    elif i=="Unable to find NON-MED":
        return "Unable to find NON-MED"
#     elif i in ["No Known Medications", "No known medications"]:
#         return "No Known Medications"
#     elif i in ["Unknown Medication/Substance"]:
#         return "Unknown Medication/Substance"
    elif i in ["No data available for this section"]:
        return "No data available for this section"
    elif i in ["No Vaccine Administered"]:
        return "No Vaccine Administered"
    elif i.lower().find('information available')!=-1:
        return "No information available."
    
    
    

    elif i=="No Current Medications":
        return "No Current Medications"
    elif i=="UNKNOWN MEDICATION":
        return "UNKNOWN MEDICATION"

#     elif i==96 or i=="96":
#         return "TST-PPD intradermal"
    elif i == "The details of the medication are not available":
        return "The details of the medication are not available"
    elif i in (["immunization history", "IMMUNIZATION HISTORY", "IMMUNIZATION HX"]):
        return "IMMUNIZATION HISTORY"
    elif i in (["HX", "hx"]):
        return "HX/hx"

    
#     elif i.lower().find("diabetic foot examination")!=-1 or i.lower().find("dental consultation")!=-1 or i.lower().find("encounter")!=-1:
#         return "Encounter text"
    
    
    
    else:
        return "Present"    
    
    

    
 
    
    
    
    

def r(i):
    if i=="Missing":
        return "Missing"
    elif i == "OTH":
        return "OTH"
    elif i in ["Other", "OTHER"]:
        return "Other"
    elif i == "UNK":
        return "UNK"
    elif i =="NI":
        return "NI"
    elif i =="UNK":
        return "UNK"
    elif i in (["Unknown", "UNKNOWN"]):
        return "Unknown"
    elif i in (["No known active allergies"]): 
        return "No known active allergies"
    elif i == "No Known Drug Allergies":
        return "No Known Drug Allergies"
    elif i=="Tags":
        return "Tags"
    elif i=="Narrative does not match structure":
        return "Narrative does not match structure"
    elif i=="See Comment":
        return "See Comment"
    elif i=="Jibber-Jabber":
        return "Jibber-Jabber"
    elif i=="Punctuations":
        return "Punctuations"
    

#     elif i in (["RASH", "Rash"]):
#         return "Rash"
#     elif i in (["ITCHING", "Itching"]):
#         return "Itching"
    elif i =="No Known Allergies":
        return "No Known Allergies"
    elif i == "No Allergy Information Available":
        return "No Allergy Information Available"
    elif i in (["Other (see comments)", "Other (See Comments)"]):
        return "Other (see Comments)"
    elif i in (["xxxx", "XXXX"]):
        return "xxxx"
    elif i =="ASSERTION":
        return "ASSERTION"
    elif i =="Missing SIG":
        return "Missing SIG"
    elif i=="Unable to find NON-MED":
        return "Unable to find NON-MED"
    elif i in ["No Known Medications", "No known medications"]:
        return "No Known Medications"
    elif i=="No Current Medications":
        return "No Current Medications"
    elif i=="UNKNOWN MEDICATION":
        return "UNKNOWN MEDICATION"

#     elif i==96 or i=="96":
#         return "TST-PPD intradermal"
    elif i == "The details of the medication are not available":
        return "The details of the medication are not available"
    else:
        return "Present"
    
    
def p(k):
    return ('|'.join(k))

def L(x ):
    return set(x['File_Name'])

def pampi_finder(x):
    if x == i_set & m_set & a_set & pb_set & pc_set:
        return (len(d_set.intersection(x)))/len(d_set)
    elif x == m_set & a_set & pb_set & pc_set:
        return (len(d_set.intersection(x)))/len(d_set)
    elif x == a_set & pb_set & pc_set:
        return (len(d_set.intersection(x)))/len(d_set)
    elif x ==  pb_set & pc_set:
        return (len(d_set.intersection(x)))/len(d_set)
    elif x == pb_set:
        return (len(d_set.intersection(x)))/len(d_set)

    

# Miscellaneous entries
Vit_C_M=["Notes", "Portal_Access", "HEADER1", "Sticky_Note", "Skicky_Note", "PrimaryCSN", "Registration",
        "Financial_Class",  "OrderRec",  "Registration_1","Emp_Status", "Emergency_contact_cell_phone",
        "Visually_Impaired", "Precautions", "Registration_8", "ActivityCode_Visit_Comment", "Code_Status"]
vit_m = [i.lower() for i in Vit_C_M]

# Problem Domain content
Vit_C_P=["IS LACTATING", "Pregnancy status [Interpretation] - Reported", "VISUALLY IMPAIRED?", "HEARING IMPAIRED?"  ]
vit_p = [i.lower() for i in Vit_C_P]

# Social History Domain content 
Vit_C_S=["Living Situation", "Lives With (SW)",  "EMPLOYMENT STATUS", "EMERGENCY NOTIFICATION CELL PHONE", "Current Living Environment"]
vit_s = [i.lower() for i in Vit_C_S]


def vit(v):
    if pd.isna(v) or v in ['', None, 'missing']:
        return 'Missing'
    if v in ['oth']:
        return 'OTH'
    elif v in ['unk']:
        return 'UNK'
    elif v in ['unknown']:
        return 'Unknown'
    elif v in ['other']:
        return 'Other'
    elif v in vit_m:
        return "Miscellaneous content"
    elif v in vit_p:
        return "Problem Domain content"
    elif v in vit_s:
        return "Social History Domain content"
    elif v.find('no data available')!=-1:
        return "No data available for this section"
    else:
        return "Present"

def scs_val(s):
    if s in ['oth']:
        return 'OTH'
    elif s in ['unk']:
        return 'UNK'
    elif s in ['unknown']:
        return 'Unknown'
    elif s.lower().find("unkn")!=-1:
        return 'Unknown'
    elif s in ['other']:
        return 'Other'
    elif s in ['ni']:
        return 'NI'
    elif pd.isnull(s) or s in ['', ' ', None, 'missing', 'None', 'na']:
        "Missing"
    elif (all(char.isalpha() or char ==":" or char =="-" for char in str(s))) and (s != "Missing"):
        return "Miss Placed" 
    else:
        return 'Present' if s != None else "Missing"
    
    
    
    
def extract_year(date_str):
    try:
        return pd.to_datetime(date_str, format = '%m/%d/%Y').year
    except(ValueError, TypeError):
        return None
    
    
def categorize_year(value):

    if value < 2010:
        return "Before 2010"
    elif 2010 <= value < 2020:
        return "2010 - 2019"
    else:
        return value
        

def ensure_columns(df):
    if 'Present' not in df.columns:
        df['Present'] = np.nan
    if ''  in df.columns:
        df["Missing"] = df['']
    return df  
    
    
    
    