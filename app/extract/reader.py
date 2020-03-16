import tabula
import os
import pandas as pd

folder = '../../data/'


def extract():

    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            process_file(folder + filename)


def process_file(filename):
    print(f'process_file: {filename}')

    df = tabula.read_pdf(filename, multiple_tables=True, pages='all')

    i = 0
    filename_only = filename_without_extension(filename)

    print(f'len {len(df)}')

    for d in df:



        if len(d.columns) > 3:
            # d.columns = ["Country", "Total confirmed cases", "Total confirmed new cases", "Total deaths",
            #              "Total new deaths", "Transmission classification", "Days since last reported case"]

            d.columns = pd.MultiIndex.from_tuples(zip(range(0, len(d.columns)), d.columns))

            #d.columns = range(0, len(d.columns))
            print('****')
            print(d.columns)
            print(d)

            pdf_filename = f'{filename_only}-{i}.csv'

            #d = d.dropna()

            if not d.empty:
                d.insert(0, 'Date', filename_only)
                d.to_csv(folder + 'csv/' + pdf_filename, index=False, header=True)

                print(f"Saving {pdf_filename}")

                i = i + 1


def filename_without_extension(path):
    filename = os.path.basename(path)
    return os.path.splitext(filename)[0]
