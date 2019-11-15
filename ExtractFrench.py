#!/usr/bin/python
# -*- coding: latin-1 -*-

import yaml
import pprint
import io
#import xlsxwriter
import pandas as pd
import codecs
import sys


print(sys.getdefaultencoding())

#reload(sys)  # Reload does the trick!
#sys.setdefaultencoding('UTF8')


f = None
yaml_file = None
row_count = 2
current_yaml = ""

mylist = ["label","help_text"]

# workbook = xlsxwriter.Workbook('translateV3.xlsx')
# worksheet = workbook.add_worksheet()

file_translated = "Data\\Translated.xlsx"

#worksheet.write_row(0,0,['Référence', 'croisée'])

def iterdict(d, callback):
  if not isinstance(d, dict):
      callback( None,d)
      return
  for k,v in d.items():
     #print ("%s=>"%k)
     if (k == "choices"):
         pass
     if( k in mylist ):
         callback(k,v, True)
         #return
     elif isinstance(v, dict):
         iterdict(v, callback)
     elif isinstance(v,list):
         for  l in v :
             iterdict(l, callback)
     else:
         callback (k, v)



def func1 (k, v, take = False):
    global row_count
    sample1 = 'Référence'
    if take:
        #print("%s => %s"%(k,v))
        #print("%s" % v )
        if isinstance(v, dict):
            ven = ""
            vfr = ""
            if "en" in v:
                ven = v["en"]
            if "fr" in v:
                vfr = v["fr"]
            if row_count in [124]:
                print("break!")
            print ("%s,%s"%(ven,vfr))
            f.write("%s\t%s\t%s\t%s\n"%(ven,vfr,k,yaml_file))
            data = (ven,vfr,k,yaml_file)
            #worksheet.write_row(row_count,0, data)
            row_count += 1




def read_yaml(file):
    # Read YAML file
    with open(file, encoding='utf-8', mode='r') as stream:
        data_loaded = yaml.safe_load(stream)
    return data_loaded


def get_translated(file):
    '''Read the traslated file, return a dictionary of parsed result'''
    #file = "Data\\Translated.xlsx"
    data = pd.ExcelFile(file)
    df = data.parse("Sheet1")
    dict = {}
    for index, row in df.iterrows():
        # if index > 20:
        #    break
        loc = row['Location']
        if not loc in dict.keys():
            dict[loc] = {}
        dict[loc][row['English']]=row['Français']
    return dict

def func2(k, v, take = False):
    global row_count
    ef_pairs = translation[current_yaml]

    if take:
        if isinstance(v, dict):
            ven = ""
            vfr = ""
            translated_f = ""
            if "en" in v:
                ven = v["en"]
                #vf = ef_pairs[ven]
            if "fr" in v:
                vfr = v["fr"]
                if ven in ef_pairs.keys():
                    v["fr"] = ef_pairs[ven]
                    print(f">> now {ven} of French {vfr} becomes {v['fr']}")
                else:
                    print(f"<< {ven} not in translation")
            #if row_count in [124]:
            #    print("break!")


            print ("%s,%s"%(ven,vfr))
            row_count += 1


def extract_traslation(output_file):
    '''Main fuction for extracting English and French from yaml files
    '''
    global f
    f =  open(output_file , "w",encoding='utf-8')
    for y in ["aafc_presets.yaml", "aafc_wg.yaml", "tbs_presets.yaml"]:
        readin = read_yaml(y)
        iterdict(readin, func1)
    f.close()

if __name__ == '__main__':

    extract_traslation("translate2.csv") # Now for extract all the infor into a cvs file only




    #translation = get_translated(file_translated) # prepare the translated

    for y in ["aafc_presets.yaml","aafc_wg.yaml","tbs_presets.yaml"]:
    #for y in [ "aafc_wg.yaml"]:
        yaml_file = y
        current_yaml = y
        readin = read_yaml(y)


    #     #Flowing is for extract
    #     iterdict(readin, func1)
    #
    # f.close()
    #workbook.close()

        # iterdict(readin, func2)
        # new_file = "new_" + yaml_file
        # #with open(new_file, 'w') as outfile:
        # #    yaml.dump(readin, stream=outfile, default_flow_style=False, allow_unicode=True)
        # f = codecs.open(new_file, "w", encoding="utf-8")
        # yaml_string = yaml.dump(readin, allow_unicode=True,)
        # f.write(yaml_string)
        # f.close()