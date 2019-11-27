import pandas as pd
import json
import numpy as np

datafile = "Data//updated_sharepoint.xlsm"

FIELDS_SPECL_CHR = [('Collection Type', r'\d+;#'), ('Data Steward Email', r';#\d+'),
                    ('DRF', r'\d+;#')]


# Audience

def remove_special_character(df, field, regex):
    """
    remove special characters from a column
    :param df: data frame
    :param field: field name. i.e. 'Collection Type'
    :param regex: regex expression of the pattern that need to removed. i.e. r';#\d+'
    :return: fixed data frame
    """
    dcolumn = df[field]
    df[field] = dcolumn.str.replace(regex, '')
    return df


def main():
    df = pd.read_excel(datafile)

    df.fillna("")
    for fr in FIELDS_SPECL_CHR:
        f = fr[0]
        r = fr[1]
        df = remove_special_character(df, f, r)

    # df.to_excel("Data//new_updated_sp.xlsx")
    schema = load_schema("Data//schema.json")
    generated_dic = gen_json(schema, df)

    with open("Data//dumped_data.json", "w") as ofp:
        json.dump(generated_dic, ofp)

    with open("Data//dumped_data_asc.json", "w",encoding="cp1252") as ofp:
        json.dump(generated_dic, ofp, ensure_ascii=False)

    pass


def load_schema(file):
    sch = ""
    with open(file) as json_fp:
        sch = json.load(json_fp)
    return sch


def gen_json(schema, data_frame):
    res = []

    for i in range(10):
        row = data_frame.iloc[i]
        row = row.fillna("")
        item = {}
        for k, v in schema.items():
            value = row[v['col']]
            # if k == "publication_year":
            #     print(f'{value}')
            #     pass
            if 'multi' in v:
                value = value.split(",")
            if value is np.nan:
                value = ""
            if value is pd.NaT:
                value = ""
            if isinstance(value, np.bool_):
                value = bool(value)
            if isinstance(value, pd.Timestamp):
                value = value.strftime('%Y-%m-%d %H:%M:%S')
            # if isinstance(value, np.nan):
            #     value = "N/A"
            item[k] = value
        # print(f'{k}, {v["col"]}')
        res.append(item)

    return res


if __name__ == '__main__':
    main()
    pass
