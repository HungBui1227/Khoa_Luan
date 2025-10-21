import pandas as pd

# Danh sách file đã gắn header và đã giảm kích thước
files = [
    'Demo/Dataset/UNSW-NB15_1_header_reduced.csv',
    'Demo/Dataset/UNSW-NB15_2_header_reduced.csv',
    'Demo/Dataset/UNSW-NB15_3_header_reduced.csv',
    'Demo/Dataset/UNSW-NB15_4_header_reduced.csv'
]

# Đọc và gộp tất cả các file
df_list = []
for file in files:
    print(f"\nĐã đọc file: {file}")
    df = pd.read_csv(file, low_memory=False)
    df_list.append(df)
    print("Shape ban đầu: ", df.shape)

    # Số lượng nhãn trong file
    label_counts = df['Label'].value_counts()
    print("Số lượng nhãn trong file:")
    print(label_counts)

# Gộp thành 1 DataFrame duy nhất
df_full = pd.concat(df_list, ignore_index=True)

print("\nGộp thành công!\n")
print("Shape của file sau khi gộp:", df_full.shape)

# Số lượng nhãn trong file gộp:
print("Số lượng nhãn trong file gộp:")
print(df_full['Label'].value_counts())


# # Kiểm tra tổng số dòng khớp nhau
# expected_total = sum(len(df) for df in df_list)
# actual_total = len(df_full)
# print("Đủ dữ liệu:", expected_total == actual_total)

# # Kiểm tra trùng lặp hoàn toàn (nếu muốn)
# duplicates = df_full.duplicated().sum() 
# print("Số dòng trùng lặp:", duplicates)

# Lưu file gộp
df_full.to_csv('Demo/Dataset/UNSW-NB15_full.csv', index=False)
print("Đã lưu file gộp tại", 'Demo/Dataset/UNSW-NB15_full.csv')
