import matplotlib.pyplot as plt
import seaborn as sns


def reporting(table_analysis):
    top_20_percent = table_analysis.sort_values(by='percent_GDP', ascending=False)[0:20]
    top_20_expense = table_analysis.sort_values(by='percent_GDP', ascending=False)[0:20]
    top_20_expense_zoom = table_analysis.sort_values(by='rd_expense_billions', ascending=False)[2:20]

    f = plt.figure(figsize=(6, 9))
    g = sns.scatterplot(
        x=top_20_percent['percent_GDP'],
        y=top_20_percent['billionaires'],
        hue=top_20_percent['country'],
        size=top_20_percent['rd_expense_billions'])

    f.savefig('data/results/%GDP_and_billionaires.png')

    f = plt.figure(figsize=(5, 10))
    g = sns.scatterplot(
        x=top_20_expense['rd_expense_billions'],
        y=top_20_expense['total_billionaire_worth'],
        hue=top_20_expense['country'],
        size=top_20_expense['percent_GDP'])

    f.savefig('data/results/R&D_Expense_and_billionaire_worth.png')

    f = plt.figure(figsize=(8, 10))
    g = sns.scatterplot(
        x=top_20_expense_zoom['rd_expense_billions'],
        y=top_20_expense_zoom['total_billionaire_worth'],
        hue=top_20_expense_zoom['country'],
        size=top_20_expense_zoom['percent_GDP'])

    f.savefig('data/results/R&D_Expense_and_billionaire_worth_zoom.png')
    print('check the generated reports!')
