#!/usr/bin/env python
# coding: utf-8


dme_set = {'aerochamber',  'bag', 'bags', 'bandage', 'brace', 'cane', 'canes', 'cartridges', 'catheter', 'condom', 'condoms',
            'container', 'containers', 'covidien', 'covidiens', 'cpap', 'cpaps', 'cutter', 'device', 'devices', 'dexcom', 'drainage',
            'drainages', 'equipment', 'equipments', 'freestyle', 'gauge', 'gauze', 'gauzes', 'humidifier', 'humidifiers', 'kit', 'kits',
            'lancet', 'lancets', 'liner', 'machine', 'mask', 'masks', 'meter',  'monitor', 'needle', 'needles', 'ostomy', 
           'oxygen-air', 'pad', 'padm', 'pads', 'patchs', 'pressure', 'pump', 'pumps', 'reader', 'readers', 'recon', 'socks', 'solns',
            'strip', 'strips', 'swabs', 'syringe', 'syringe-needle', 'syringes', 'tape', 'tapes', 'tests', 'transmitter', 'tube',
            'tubes', 'v-go', 'walker', 'walkers', 'wheelchair', 'wheelchairs', 'wipesscooter', 'wipesscooters'}







flue_list={"iiv", "afluria", "fluad", "flublok", "flucelvax", "flu", "flu ", "flulaval", "fluarix", "fluvirin", "fluzone", "iiv3", 
            "iiv4",  "riv3", "riv4", "cciiv4", "laiv", "flumist", "influenza", "h1n1", "flu--adult"}

anthrax_list={"anthrax", "biothrax"}

cholera_list={"cholera", "vaxchora"}

tatnus_list={"diphtheria", "dtap", "daptacel", "infanrix", "tenivac", "tdap", "adacel", "boostrix", "dtap-ipv", "kinrix", "quadracel",
             "dtap-hepb-ipv", "dpt", "dtp" ,"pediarix", "dtap-ipv", "pentacell", "tetanus", "dtap", "daptacel", "infanrix", "tenivac", 
             "adacel", "boostrix", "kinrix", "pediarix", "pentacel", "pertussis"}

other_list = {"lyme", "plague"}

hepab_list={"hepatitis", "havrix","vaqta", "hepa", "hepb", "twinrix", "hepb", "hep","hep", "engerix", "recombivax", 
                     "heplisav", "ipv", "pediarix", "hepatitis", "hepatitis", "hepatitis", "hepatitis"}

haemophilus_list={"acthib", "pedvaxhib", "hiberix", "acthib"}

hpv_list={"hpv9", "hpv", "gardasil", "9vhpv", "papillomavirus", "papilloma", "papilloma"}

japanese_encephalitis_list = {"ixiaro", "japanese", "encephalitis"}

mmr_list={"measles", "mmr", "mmrv", "proquadoi", "proquad", "mumps", "rubella"  }

meningococcal_list={"menacwy", "menactra", "menveo", "menb", "bexsero", "trumenba", "meningococcal"}


pneumococcal_list={"pneumococcal", 'pneumococcal', "pneumococcal", "pcv13", "prevnar13", "ppsv23" , "pneumonia","prevnar"}

polio_list = {"polio", "ipol"}

rabies_list={"rabies", "rabies", "imovax rabies", "rabavert"}

rotavirus_list={"rotavirus",  "rv1 ",  "rotarix",  "rv5",  "rotateq"}

shingles_varicella_list={"shingles", "rzv", "shingrix", "zoster", "varicella", "varivax", "proquad"}

smallpox_list={"smallpox", "acam2000", "small pox vaccinia"}

tuberculosis_list={"tuberculosis", "calmette-guerin", "bcg"}

typhoid_list={"typhoid", "vivotif", "typhim"}

yellow_fever_list={"yellow", "yf"}

Lyme_disease_list = {'lymerix'}

covid_brand_list={"sars",'cov' 'pfizer','moderna','novavax','johnson', 'janssen'}

no_known_medications_list={"no known medications", "no known medications", "unknown medication", "no current medications", 
                           "unable to find non-med", 'unable to find', "no data available for this section", 
                           "no data provided for this section", "known", "unknown", "unable", 'unlisted', 
                           'no data provided for this section', 'no known medications', 'unknown to patient'}

rhogam_list={"rhogam", "bayrho", "hyperrho", "micrhogam", "rhophylac", "albumin"}   





dose_list ={'%', 'amount', 'application', 'applicator', 'can', 'cap', 'caps', 'capsule', 'capsules', 'cm', 'container', 'days', 'directed', 'dose', 'drop', 'drops', 'film', 'g', 'gm', 'gram', 'grams', 'gtt', 'hr', 'inch', 'inches', 'liberal', 'liter', 'liters', 'mcg', 'meq', 'mg', 'ml', 'mls', 'moderate', 'needed', 'now', 'packet', 'packets', 'patch', 'patchssuppository', 'pill', 'pills', 'puff', 'puffs', 'ribbon', 'scoop', 'shot', 'spray', 'sprays', 'sufficient', 'supp', 't', 'tab', 'tablespoonful', 'tablet', 'tablets', 'tabs', 'tbsp', 'teaspoon', 'teaspoonful', 'teaspoons', 'topical', 'topically', 'tsp', 'unit', 'units'}         



rout_list = {'aaa', 'affected', 'applic', 'apply', 'area', 'butt', 'buttock', 'buttocks', 'cheek', 'chew', 'chewable', 'drink', 'ear', 'ears', 'eye', 'eyes', 'im', 'inhalant', 'inhalation', 'inhalations', 'inhale', 'inhaled', 'inhaler', 'inject', 'intramuscular', 'intranasal', 'intrauterine', 'intravenous', 'iv', 'lungs', 'meals', 'miscellaneous', 'mouth', 'muscle', 'nare', 'nasal', 'nose', 'noses',  'nostril', 'od', 'oph', 'ophthalmic', 'opthalmic', 'oral', 'orally', 'os', 'ou', 'oxygen', 'po', 'rectum', 'rout', 'sinus', 'skin', 'sq', 'subcutaneous', 'take', 'tbec', 'teeth', 'tongue', 'topical', 'topically', 'tracheal', 'vagina', 'vaginal', 'vaginallyrectal', 'venous', 'vial'}




freq_list = {'after', 'am', 'at', 'bed', 'bedtime', 'before', 'bid', 'breakfast', 'continuously', 'daily', 'day', 'directed', 'dose', 'doses', 'evening', 'every', 'fri', 'friday', 'hour', 'hr', 'hs', 'instructed', 'minute', 'mon', 'monday', 'month', 'monthly', 'morning', 'needed', 'nightly', 'noon', 'on', 'once', 'pm', 'po', 'prior', 'prn', 'q12h', 'q24h', 'q4h', 'q4wk', 'q6h', 'qam', 'qd', 'qdaily', 'qhs', 'qid', 'qmon', 'qmonday', 'qod', 'release', 'repeat', 'sliding scale', 'spray', 'sprays', 'subq', 'taper', 'tid', 'time', 'times', 'total', 'twice', 'wed', 'wednesday', 'week', 'weekly', 'year'}








        
