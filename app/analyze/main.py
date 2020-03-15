import pandas as pd

folder = '/Users/pedwards/Beppe/github/gcatanese/Corona-Virus-WHO-Data/data/csv/'

file = folder + '11-03-2020-0.csv'


def process():
    df = pd.read_csv(file)

    print(df)
    print(df.columns)

    df = df['Country'] == 'Italy'
    print(df)

process()