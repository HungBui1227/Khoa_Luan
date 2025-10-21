import pandas as pd

# Danh sách file cần xử lý
files = [
    'Demo/Dataset/UNSW-NB15_1_header.csv',
    'Demo/Dataset/UNSW-NB15_2_header.csv',
    'Demo/Dataset/UNSW-NB15_3_header.csv',
    'Demo/Dataset/UNSW-NB15_4_header.csv'
]

for file in files:
    print(f"\n- Đang xử lý: {file}")
    df = pd.read_csv(file, low_memory=False)
    print("Shape ban đầu:", df.shape)


    # Xem số lượng từng nhãn
    label_counts = df['Label'].value_counts()
    print("Số lượng nhãn trước khi giảm:")
    print(label_counts)

    # Giữ lại toàn bộ dòng Attack (label != 0)
    df_attack = df[df['Label'] != 0]
    print(f"Số dòng Attack giữ lại: {len(df_attack)}")

    # Lấy mẫu 1 phần nhỏ dòng Normal (ví dụ 10%)
    df_normal = df[df['Label'] == 0].sample(frac=0.1, random_state=42)
    print(f"Số dòng Normal giữ lại: {len(df_normal)}")

    # In ra số dòng và cột sau khi giảm
    print("Số dòng và số cột sau khi giảm:", len(df_attack) + len(df_normal), df.shape[1])

    # Ghép lại
    df_reduced = pd.concat([df_attack, df_normal], ignore_index=True)
    print("Shape sau khi ghép:", df_reduced.shape)

    # Lưu lại file mới
    out_file = file.replace('.csv', '_reduced.csv')
    df_reduced.to_csv(out_file, index=False)

    print(f"File đã giảm lưu tại: {out_file}")
