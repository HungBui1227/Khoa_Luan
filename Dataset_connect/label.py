import pandas as pd

# Đọc file mô tả cột
desc = pd.read_csv('Demo/Dataset/NUSW-NB15_features.csv', encoding='latin1')
column_names = desc['Name'].tolist()

# Danh sách các file dữ liệu gốc
file_list = [
    'Demo/Dataset/UNSW-NB15_1.csv',
    'Demo/Dataset/UNSW-NB15_2.csv',
    'Demo/Dataset/UNSW-NB15_3.csv',
    'Demo/Dataset/UNSW-NB15_4.csv'
]

# Gắn header cho từng file
for file_path in file_list:
    # Đọc file không có header
    df = pd.read_csv(file_path, header=None)
    
    # Kiểm tra số lượng cột
    if df.shape[1] != len(column_names):
        print(f"⚠️ File {file_path} có {df.shape[1]} cột, không khớp {len(column_names)} cột mô tả!")
        continue

    # Gắn header
    df.columns = column_names

    # Điền giá trị thiếu trong cột 'attack_cat' bằng 'Normal'
    if 'attack_cat' in df.columns:
        df['attack_cat'] = df['attack_cat'].fillna('Normal')
    else:
        print(f"⚠️ File {file_path} không có cột 'attack_cat'!")
        continue


    # Tạo tên file mới
    output_path = file_path.replace('.csv', '_header.csv')
    df.to_csv(output_path, index=False)
    

    # Lưu lại
    df.to_csv(output_path, index=False)
    print(f"✅ Đã gắn header cho {file_path} → {output_path}")

