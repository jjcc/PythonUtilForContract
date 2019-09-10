#!/usr/bin/python
# -*- coding: latin-1 -*-

import yaml
import pprint
import io
import xlsxwriter


f = None
yaml_file = None
row_count = 2

mylist = ["label","help_text"]

workbook = xlsxwriter.Workbook('translateV3.xlsx')
worksheet = workbook.add_worksheet()


worksheet.write_row(0,0,['Référence', 'croisée'])

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
            worksheet.write_row(row_count,0, data)
            row_count += 1




def read_yaml(file):
    # Read YAML file
    with open(file, encoding='utf-8', mode='r') as stream:
        data_loaded = yaml.safe_load(stream)
    return data_loaded

if __name__ == '__main__':
    f = open("translate.cvs","w")

    #with open('people.csv', 'w') as writeFile:
    #    writer = csv.writer(writeFile)
    #    writer.writerows(lines)
    for y in ["aafc_presets.yaml","aafc_wg.yaml","tbs_presets.yaml"]:
        yaml_file = y
        readin = read_yaml(y)

        iterdict(readin, func1)

    #pprint.pprint(readin)
    f.close()
    workbook.close()
