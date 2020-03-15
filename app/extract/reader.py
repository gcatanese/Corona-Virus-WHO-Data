import tabula
import os

folder = '/Users/pedwards/Beppe/github/gcatanese/Corona-Virus-WHO-Data/data/'


def extract():

    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            process_file(folder + filename)


def process_file(filename):
    print(f'process_file: {filename}')

    df = tabula.read_pdf(filename, pages='all')

    i = 0
    filename_only = filename_without_extension(filename)

    for d in df:

        if len(d.columns) == 7:
            d.columns = ["Country", "Total confirmed cases", "Total confirmed new cases", "Total deaths",
                         "Total new deaths", "Transmission classification", "Days since last reported case"]

            pdf_filename = f'{filename_only}-{i}.csv'

            d = d.dropna()

            if not d.empty:
                d.insert(0, 'Date', filename_only)
                d.to_csv(folder + 'csv/' + pdf_filename, index=False, header=True)

                i = i + 1
                print(f"Saving {pdf_filename}")


def filename_without_extension(path):
    filename = os.path.basename(path)
    return os.path.splitext(filename)[0]
