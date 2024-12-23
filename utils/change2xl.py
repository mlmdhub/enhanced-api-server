import json
import sys
import pandas as pd


with open(r'D:\Project\x_v8.0\News3.json', 'r',encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)

df.to_excel(r"D:\Project\x_v8.0\News4.xlsx", index=False)
