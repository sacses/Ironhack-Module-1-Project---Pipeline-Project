import json
import requests
import pandas as pd


def lowercase_feature(df, col):
    return df[col].str.lower()


def export_csv(path, df, deli):
    return df.to_csv(path, sep=deli, index=False)


def extract_float(df, col, regex):
    return df[col].str.extract(regex).astype('float64')


def enrich(df_cleaned):

    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_research_and_development_spending'
    rnd_spending = pd.read_html(url)[0]
    export_csv(f'data/raw/enrich_input.csv', rnd_spending, ';')
    print('Enrich input is found in raw folder')
    rnd_spending.columns = rnd_spending.iloc[1]
    rnd_spending.drop(rnd_spending.index[0:2], inplace=True)
    rnd_spending.rename(columns={'Country/Region': 'country',
                                 'Expenditures on R&D (billions of US$, PPP),': 'r&dExpense_billions',
                                 '% of GDP PPP': '%GDP',
                                 'Expenditures on R&D per capita (US$ PPP),': 'r&dExpensePerCapita'}, inplace=True)
    rnd_spending['%GDP'] = extract_float(rnd_spending, '%GDP', r"(\d+.?\d*)")
    rnd_spending[['r&dExpense_billions', 'r&dExpensePerCapita']] = rnd_spending[
        ['r&dExpense_billions', 'r&dExpensePerCapita']].astype('float64')
    rnd_spending['country'] = lowercase_feature(rnd_spending, 'country')
    merged_df = pd.merge(df_cleaned, rnd_spending[['country', 'r&dExpense_billions', '%GDP', 'r&dExpensePerCapita']],
                         on='country', how='left')
    merged_df[['r&dExpense_billions', '%GDP', 'r&dExpensePerCapita']] = merged_df[
        ['r&dExpense_billions', '%GDP', 'r&dExpensePerCapita']].fillna(0)
    table_analysis = merged_df.groupby('country').agg(billionaires=('id', 'count'),
                                                      age=('age', 'mean'),
                                                      gender=('gender', 'mean'),
                                                      mean_billionaire_pos=('position', 'mean'),
                                                      median_billionaire_pos=('position', 'median'),
                                                      total_billionaire_worth=('worth', 'sum'),
                                                      mean_billionaire_worth=('worth', 'mean'),
                                                      median_billionaire_worth=('worth', 'median'),
                                                      rd_expense_billions=('r&dExpense_billions', 'max'),
                                                      rd_expense_capita=('r&dExpensePerCapita', 'max'),
                                                      percent_GDP=('%GDP', 'max')).sort_values(by='billionaires',
                                                                                               ascending=False)[
                     1:].reset_index()
    export_csv(f'data/processed/enriched_df.csv', table_analysis, ';')
    print('Enriched DataFrame can be found in processed folder')
    return table_analysis
