import pandas as pd

# Đọc file UNSW-NB15_full.csv
df = pd.read_csv("Demo/Dataset/UNSW-NB15_full.csv", low_memory=False)

# Xóa các cột không cần thiết
columns_to_drop = ['srcip',	'sport', 'dstip', 'dsport', 'res_bdy_len', 'Stime', 'Ltime']
df.drop(columns=columns_to_drop, inplace=True)
print("Shape sau khi xóa cột:", df.shape)

print(df.columns)
print(df['Label'].value_counts())

# Lưu DataFrame đã chỉnh sửa trở lại file CSV
df.to_csv("Demo/Dataset/Modified_UNSW-NB15_full.csv", index=False)
print("File đã được lưu với tên 'Modified_UNSW-NB15_full.csv'")