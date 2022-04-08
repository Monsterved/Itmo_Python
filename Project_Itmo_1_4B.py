import pandas as pd

file1 = r"/Users/alexandrefimenko/Downloads/orderdata_sample.csv"
ca = pd.read_csv(file1)
ca['Quantity'] = ca['Quantity'].astype(float)
ca['Price'] = ca['Price'].astype(float)
ca['Freight'] = ca['Freight'].astype(float)
ca = ca.eval("Total = Quantity * Price + Freight")
print(ca)
ca.to_csv(r"/Users/alexandrefimenko/Downloads/done.csv", index=False)
