#!/usr/bin/env python
# coding: utf-8

# In[ ]:

wb=load_workbook(path)
shts=wb.sheetnames


def find_sht():
    Doc_s, Vit_s, Imm_s, Med_s, Alr_s, Prob_s, Proc_s,   Res_s =None, None, None, None, None, None, None, None

    for i in shts:
        if 'DOC' in i.upper():
            Doc_s = i
            
        elif 'VIT' in i.upper():
            Vit_s =i
        elif 'IMM' in i.upper():
            Imm_s =i
        elif 'MED' in i.upper():
            Med_s =i
        elif 'AL' in i.upper():
            Alr_s =i
        elif 'PROB' in i.upper():
            Prob_s =i
        elif 'PROC' in i.upper():
            Proc_s =i
#         elif 'SOC' in i.upper():
#             Soc_s =i
#         elif 'VitalSigns' in i.upper():
#             Vit_s =i

        elif 'RES' in i.upper():
            Res_s =i
#         break
          
    return Doc_s, Imm_s, Med_s, Alr_s, Prob_s, Proc_s,  Vit_s, Res_s


Doc_s, Imm_s, Med_s, Alr_s, Prob_s, Proc_s,  Vit_s, Res_s= find_sht()
Doc_s, Imm_s, Med_s, Alr_s, Prob_s, Proc_s,  Vit_s, Res_s

print('Vit_s: ', Vit_s, '\n')


# def d_f(x):
#     data=[]
#     for row in x.iter_rows(values_only = True):
#         data.append(row)

#     df= pd.DataFrame(data) 
#     df.columns = df.iloc[0]
#     df=df[1:]
#     return df

def read_file(sheet_name):
    
    try:
        if sheet_name is None:
            return pd.DataFrame()
        sheet = wb[sheet_name]
        data=[]
        for row in sheet.iter_rows(values_only = True):
            data.append(row)
       
        df= pd.DataFrame(data) 
        df.columns = df.iloc[0]
        df=df[1:]   
    except KeyError:
        df=pd.DataFrame()
    return df
# sheet_name = Doc_s
Doc=read_file(Doc_s)
Doc.shape
Imm=read_file(Imm_s)
Imm.shape
Med=read_file(Med_s)
Med.shape
Alr=read_file(Alr_s)
Alr.shape
Prob=read_file(Prob_s)
Prob.shape
Proc=read_file(Proc_s)
Proc.shape
# Soc=read_file(Soc_s)
# Soc.shape
Vit=read_file(Vit_s)
Vit.shape
sheet_name = Res_s
Res=read_file(Res_s)
Res.shape



def uniq_by_P_ID(x):
    return x.drop_duplicates(subset=['Patient_ID'], keep='first')

# start=datetime.now()

doc=uniq_by_P_ID(Doc)
print("Doc:",len(Doc), ";  ", "doc:",len(doc))

imm=uniq_by_P_ID(Imm)
print("Imm:",len(Imm), ";  ", "imm:",len(imm))

med=uniq_by_P_ID(Med)
print("Med:",len(Med), ";  ", "med:",len(med))

alr=uniq_by_P_ID(Alr)
print("Alr:",len(Alr), ";  ", "alr:",len(alr))

prob=uniq_by_P_ID(Prob)
print("Prob:",len(Prob), ";  ", "prob:",len(prob))

proc=uniq_by_P_ID(Proc)
print("Proc:",len(Proc), ";  ", "proc:",len(proc))

# soc=uniq_by_P_ID(Soc)
# print("Soc:",len(Soc), ";  ", "soc:",len(soc))

vit=uniq_by_P_ID(Vit)
print("Vit:",len(Vit), ";  ", "vit:",len(vit))

res=uniq_by_P_ID(Res)
print("Res:",len(Res), ";  ", "res:",len(res))

# print(datetime.now()-start)




data = {
    "Domain":["Document", "Immunization", "Medication", "Allergy","Problem", "Procedure",  "Vital Signs", "Result"],
        "Unique Patient":[len(doc), len(imm), len(med), len(alr), len(prob),len(proc),
                          len(vit), len(res) ],
       "Total Records":[len(Doc), len(Imm), len(Med), len(Alr), len(Prob), len(Proc),
                        len(Vit), len(Res)]
       }
df_Unique_Total = pd.DataFrame(data)
df_Unique_Total
