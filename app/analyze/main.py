import pandas as pd
import os

folder = '/Users/pedwards/Beppe/github/gcatanese/Corona-Virus-WHO-Data/data/csv/'

file = folder + '13-03-2020-0.csv'


def process():
    df = pd.read_csv(file)

    df = df[df['Country'] == 'Italy']
    print(df.values)


def process_multiple_files():
    li = []

    for filename in os.listdir(folder):
        if filename.endswith(".csv"):
            df = pd.read_csv(folder + filename, index_col=None, header=0)
            li.append(df)

    df = pd.concat(li, axis=0, ignore_index=True)
    print(df.count)

    print(df['Total confirmed cases'])

    df = df[df['Country'] == 'Italy']
    print(df.values)





    it_data = df
    it_data_by_day = it_data.pivot_table(index=['Date'], values=['Total confirmed cases'])
    it_data_by_day.head()


process_multiple_files()
