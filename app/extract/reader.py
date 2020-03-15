import tabula
import os

folder = '/Users/pedwards/Beppe/github/gcatanese/pdfreader/'
file = folder + '12-03-2020.pdf'


def main():
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):

            process_file(filename)

            continue
        else:
            continue


def process_file(filename):
    print(f'process_file: {filename}')
    df = tabula.read_pdf(file, pages='all')

    # df = df['Country']=='Italy'

    i = 0
    filename_only = filename_without_extension(filename)

    for d in df:
        if len(d.columns) == 7:
            print(d.columns)
            pdf_filename = f'{filename_only}-{i}.csv'
            print(f"Saving {pdf_filename}")

            d.to_csv(folder + 'csv/' + pdf_filename, index=False, header=True)
            i = i + 1


# df = df[2]#.drop([0]).drop(2).drop(3)

# print(df)

# df.to_csv (folder + 'report.csv', index = False, header=True)

def filename_without_extension(filename):
    return os.path.splitext(filename)[0]
