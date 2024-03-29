# -*- coding: utf-8 -*-
"""SplitRecords.ipynb
Automatically generated by Colaboratory.
Original file is located at
    ## ¬ Omitted
"""

import pandas as pd
import re

data_url = 'Your Hosted Data URL'
df = pd.read_csv(data_url, keep_default_na=False)
new_df = df.replace(regex=r'.*\\Data to find with Regex', value='\\\\\Replace Data with Regex')




def create_xml(record_num):
    xmlTemplate = """<?xml version="1.0" encoding="UTF-8"?>
    <root>
        <row>
            <ID>%(ID)s</ID>
            <CustomerID>%(CustomerID)s</CustomerID>
            <SessionID>%(SessionID)s</SessionID>
            <Telephone>%(Telephone)s</Telephone>
            <Location>%(Location)s</Location>
            <ContactID>%(ContactID)s</ContactID>
            <OBSessionID>%(OBSessionID)s</OBSessionID>
            <File>%(File)s</File>
        </row>
    </root>"""
    xo = r'\\t'
    wav_file = new_df['Telephone'][record_num]
    removeSpaces = re.sub(r"[\t]", xo, wav_file)
    data = {'ID':new_df['ID'][record_num], 
            'CustomerID':new_df['CustomerID'][record_num],
            'SessionID':new_df['SessionID'][record_num],
            'Telephone':new_df['Telephone'][record_num],
            'Location':new_df['Location'][record_num],           
            'ContactID':new_df['ContactID'][record_num],
            'OBSessionID':new_df['OBSessionID'][record_num],
            'File':new_df['File'][record_num]
            }
    myfile = open(str(new_df['ID'][record_num])+ ".xml", "w")
    myfile.write((xmlTemplate%data))
    print(xmlTemplate%data)

create_xml(0)





for i, row in new_df.iterrows():
    if i > len(new_df):
        break
    else:
        create_xml(i)
        i += 1
