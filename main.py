import pandas as pd

excel_file = '../pdfreader/report.csv'

data = pd.read_csv(excel_file)

print(data)