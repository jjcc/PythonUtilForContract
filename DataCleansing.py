import pandas as pd

datafile = "Data//updated_sharepoint.xlsm"

FIELDS_SPECL_CHR = [('Collection Type',r'\d+;#'),('Data Steward Email',r';#\d+')]
#Audience

def remove_special_character(df,field,regex):
    """
    remove special characters from a column
    :param df: data frame
    :param field: field name. i.e. 'Collection Type'
    :param regex: regex expression of the pattern that need to removed. i.e. r';#\d+'
    :return: fixed data frame
    """
    dcolumn = df[field]
    df[field] = dcolumn.str.replace(regex,'')
    return df


def main():
    df = pd.read_excel(datafile)

    for fr in FIELDS_SPECL_CHR:
        f = fr[0]
        r = fr[1]
        df = remove_special_character(df,f,r)


    df.to_excel("Data//new_updated_sp.xlsx")

    pass

if __name__ == '__main__':
    main()