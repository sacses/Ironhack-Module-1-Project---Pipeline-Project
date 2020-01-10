import pandas as pd


def extract_str(df, col, regex):
    return df[col].str.extract(regex)


def extract_float(df, col, regex):
    return df[col].str.extract(regex).astype('float64')


def lowercase_feature(df, col):
    return df[col].str.lower()


def export_csv(path, df, deli):
    return df.to_csv(path, sep=deli, index=False)


def wrangling(df_master):
    df_master['sourceDetails'] = extract_str(df_master, 'source', r"> (.*)")
    df_master['source'] = extract_str(df_master, 'source', r"(.*)  =")
    df_master['worth'] = extract_float(df_master, 'worth', r"(\d+.?\d)")
    df_master['age'] = extract_float(df_master, 'age', r'(\d+)')
    df_master['age'] = [2018 - i if i > 1000 else i for i in df_master['age']]
    df_master['worthChange'] = extract_float(df_master, 'worthChange', r"(-?\d+.?\d*) ")
    df_master['country'] = \
        ['' if i == 'None'
            else 'United States' if i == 'USA'
            else 'China' if i == "People's Republic of China"
            else 'United Kingdom' if i == 'UK' else i for i in df_master['country']]
    df_master['gender'] = [0 if i == 'F' or i == 'Female' else 1 if i == 'M' or i == 'Male' else '' for i in
                           df_master['gender']]
    df_master['gender'] = pd.to_numeric(df_master['gender'], errors='ignore')

    to_lower_cols = ['lastName', 'fullName', 'country', 'source']

    for cols in to_lower_cols:
        df_master[cols] = lowercase_feature(df_master, cols)

    for i, j in zip(df_master.dtypes, df_master.columns):
        if i == 'float64' or i == 'int64':
            df_master[j].fillna(0, inplace=True)
        else:
            df_master[j].fillna('', inplace=True)
    print(f'DataFrame has been cleaned')

    export_csv(f'data/processed/cleaned_output.csv', df_master, ';')

    print(f'Cleaned DataFrame has been exported to .csv')

    return df_master

