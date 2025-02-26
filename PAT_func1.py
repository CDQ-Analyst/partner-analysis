#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def remove_punc(text):
    for punc in ('!"#$&\'()*+,./:;<=>?@[\\]^_`{|}~'):
        text = text.replace(punc, ' ')
    return text
    
def dme_finder (x):
    m_words = set(x.split(' '))
    extract_words = dme_set.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "DME"

def flu_finder (x):      
    m_words = set(x.split(' '))
    extract_words = flue_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Seasonal Influenza (Flu)"


def anthrax_finder (x):      
    m_words = set(x.split(' '))
    extract_words = anthrax_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Anthrax"

def cholera_finder (x):      
    m_words = set(x.split(' '))
    extract_words = cholera_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Cholera"        
        
def tatnus_finder (x):      
    m_words = set(x.split(' '))
    extract_words = tatnus_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Tatnus, Diphtheria, Pertussis" 
        

def other_finder (x):      
    m_words = set(x.split(' '))
    extract_words = other_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Other_Immunization"        
        
def hepab_finder (x):      
    m_words = set(x.split(' '))
    extract_words = hepab_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Hepatitis A, B" 
                     
def haemophilus_finder (x):      
    m_words = set(x.split(' '))
    extract_words = haemophilus_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Haemophilus influenzae type b (Hib)"         
        
        
def hpv_finder (x):      
    m_words = set(x.split(' '))
    extract_words = hpv_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Human Papillomavirus (HPV)"         
                
        
def encephalitis_finder (x):      
    m_words = set(x.split(' '))
    extract_words = japanese_encephalitis_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Japanese Encephalitis"            
        
        
def mmr_finder (x):      
    m_words = set(x.split(' '))
    extract_words = mmr_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Measles, Mumps, Rubella"           
        
def mng_finder (x):      
    m_words = set(x.split(' '))
    extract_words = meningococcal_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Meningococcal"
        
def pneumococcal_finder (x):      
    m_words = set(x.split(' '))
    extract_words = pneumococcal_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Pneumococcal"     

def polio_finder (x):      
    m_words = set(x.split(' '))
    extract_words = polio_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Polio" 

def rabies_finder (x):      
    m_words = set(x.split(' '))
    extract_words = rabies_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Rabies" 

def rotavirus_finder (x):      
    m_words = set(x.split(' '))
    extract_words = rotavirus_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Rotavirus" 


def shingles_varicella_finder (x):      
    m_words = set(x.split(' '))
    extract_words = shingles_varicella_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Smallpox_Varicella" 

def smallpox_finder (x):      
    m_words = set(x.split(' '))
    extract_words = smallpox_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Smallpox" 

def tuberculosis_finder (x):      
    m_words = set(x.split(' '))
    extract_words = tuberculosis_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Tuberculosis"         
        
def typhoid_finder (x):      
    m_words = set(x.split(' '))
    extract_words = typhoid_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Typhoid"          
        
     
        
def yellow_fever_finder (x):      
    m_words = set(x.split(' '))
    extract_words = yellow_fever_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Yellow Fever"           
        
        
def covid_brand_finder (x):      
    m_words = set(x.split(' '))
    extract_words = covid_brand_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Covid_Brand"
        
        
        
def rhogam_finder (x):      
    m_words = set(x.split(' '))
    extract_words = rhogam_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Rhogam" 
        
def no_known_medications_finder (x):      
    m_words = set(x.split(' '))
    extract_words = no_known_medications_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return 'No_known_medications'
    for i in extract_words:
        if i not in extract_words:
            return sig['Med_Text']
        
        
        
        
        
        
def dose_finder(x):      
    m_words = set(x.split(' '))
    extract_words = dose_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Dose"         
        
 
  
def rout_finder(x):      
    m_words = set(x.split(' '))
    extract_words = rout_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Rout"          
        
        
def freq_finder(x):      
    m_words = set(x.split(' '))
    extract_words = freq_list.intersection(m_words)
    for i in extract_words:
        if i in extract_words:
            return "Freq"          
        
        
        
        
        
        
        
        
        
        
        