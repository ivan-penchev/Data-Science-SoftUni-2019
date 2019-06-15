import datetime
from time import sleep

from http_connection import HttpConnection


import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
from pandas.io.json import json_normalize

from model.car_brand_enum import CarBrand
from model.month_enum import Month
import re
#with open('page_parse_output.txt', 'r', encoding='utf-8') as fp:
    #jasonstring = fp.readlines()

'''

df = pd.read_json('json_data.txt', 'r', encoding='utf-8-sig')
df = df.drop("py/object", axis=1)
df.rename(
    columns={
        "_car_data": "car_data",
        "_car_extra_data": "car_extra_data",
        "_name": "name",
        "_price": "price",
        "_id": "id"
    },
    inplace=True
)
print (df.dtypes)
nycphil = json_normalize(df['car_data'].values)
print(nycphil.head(3))
test2 = json_normalize(df['car_extra_data'].values)

def my_fn(c):
    if type(c) is str:
        return c.split('/')[0]
def my_fn2(c):
    if type(c) is str:
        return int(c.split(' ')[0].replace(",", ""))

def my_fn3(c):
    if type(c) is str:
        month = Month[c.split(' ')[0]]
        year = int(c.split(' ')[1])
        return datetime.datetime(year, month.value, 1)

nycphil['Брой врати'] = nycphil.apply(lambda row: my_fn(row['Брой врати']), axis=1)
nycphil['Пробег'] = nycphil.apply(lambda row: my_fn2(row['Пробег']), axis=1)
nycphil['Пробег'] = nycphil['Пробег'].fillna(0)
nycphil['Пробег'] = nycphil['Пробег'].astype(int)

nycphil['Кубатура'] = nycphil.apply(lambda row: my_fn2(row['Кубатура']), axis=1)
nycphil['Кубатура'] = nycphil['Кубатура'].fillna(0)
nycphil['Кубатура'] = nycphil['Кубатура'].astype(int)

nycphil['Мощност'] = nycphil.apply(lambda row: my_fn2(row['Мощност']), axis=1)
nycphil['Мощност'] = nycphil['Мощност'].fillna(0)
nycphil['Мощност'] = nycphil['Мощност'].astype(int)

nycphil['Година'] = nycphil.apply(lambda row: my_fn3(row['Година']), axis=1)

print (nycphil.dtypes)

print(nycphil.head(3))
result = pd.concat([df, nycphil], axis=1, sort=False)
result = result.drop(['car_data'], axis=1)
print(result.head(2))
print(result.dtypes)

with open('test.json', 'w', encoding='utf-8') as file:
     result.to_json(file, force_ascii=False, date_format="iso")
'''
def my_carbrand(c):
    if type(c) is str:
        first = c.split(' ')
        try:
            brand = CarBrand[first[0].replace('-','').replace(' ','')]
        except KeyError:
            try:
                brand = CarBrand[first[0].strip()+first[1].strip()]
            except KeyError:
                return pd.np.NaN
        return brand.name
# filtering data
# df32 = pd.read_json('test.json', 'r', encoding='utf-8-sig')
# df32['Година'] = pd.to_datetime(df32['Година'])
# df32['car_brand'] = df32.apply(lambda row: my_carbrand(row['name']), axis=1)
# with open('car_data_with_brand.json', 'w', encoding='utf-8') as file:
#     df32.to_json(file, force_ascii=False, date_format="iso")

def isSold(r):
    #sleep(0.01)
    httpCon = HttpConnection()

    url = 'https://www.cars.bg/offer/'+r
    r = httpCon.requestSession.get(url)
    if r.headers.get('Set-Cookie') is None:
        print("id " + url + ' is SOLD')
        return True
    else:
        print("id " + url + ' NOT SOLD')
        return False

# df = pd.read_json('car_data_with_brand.json', 'r', encoding='utf-8-sig')
# df['Година'] = pd.to_datetime(df['Година'])
# print('starting to check if sold')
# df["sold"] = df['id'].apply(lambda row: isSold(row))
#
# with open('car_data_with_brand_and_sold_status.json', 'w', encoding='utf-8') as file:
#      df.to_json(file, force_ascii=False, date_format="iso")


df = pd.read_json('car_data_with_brand_and_sold_status.json', 'r', encoding='utf-8-sig')
df['Година'] = pd.to_datetime(df['Година'])
nycphil['Мощност'] = nycphil['Мощност'].fillna(0)
df['Брой врати'] = df['Брой врати'].astype(int)
print(df.dtypes)
print(df.head(1))