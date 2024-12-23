import pandas as pd

# 读取 Excel 文件
file_path = r"C:\Users\mryjk\Desktop\top公司信息汇总(4).xls"
df = pd.read_excel(file_path)

# 提取 '用户' 列的数据
user_list = df['@'].tolist()

# 输出结果
print(user_list)
