import pandas as pd
print("Test code to check : Conversion of csv to df")
input_csv=pd.read_csv('\input.csv')
df=pd.DataFrame(input_csv)
print(df)

