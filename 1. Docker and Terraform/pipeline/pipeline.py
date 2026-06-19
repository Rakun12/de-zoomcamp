import sys
import pandas

print('arguments', sys.argv)

month = int(sys.argv[1])

df = pandas.DataFrame({"day": [1, 2], "num_passengers": [3, 4]})
df['month'] = month
print(df.head())

df.to_parquet(f"output_{month}.parquet")

print(f'hello pipeline, month={month}')