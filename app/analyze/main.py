import pandas as pd
import os


def process():
    df = pd.read_csv('../../data/csv/13-03-2020-0.csv')

    df = df[df['Country'] == 'Italy']
    print(df.values)


def process_global_file():
    df = pd.read_csv('../../data/csv/total_cases.csv')

    df = df[['date', 'Italy']]

    it_data = df
    it_data_by_day = it_data.pivot_table(index=['date'], values=['Italy'])
    print(it_data_by_day)


def process_multiple_files():
    li = []

    folder = '../../data/csv/'

    for filename in os.listdir(folder):
        if filename.endswith(".csv"):
            df = pd.read_csv(folder + filename, index_col=None, header=0)
            li.append(df)

    df = pd.concat(li, axis=0, ignore_index=True)
    print(df.count)

    print(df['Total confirmed cases'])

    df = df[df['Country'] == 'Italy']
    print(df.values)


process_global_file()
