import pandas as pd

weights = pd.Series({
    "Hoa": 37,
    "Nam": 48,
    "Hải": 42,
    "Linh": 39,
    "Nhân": 41,
    "Phương": 38,
    "Thu": 40,
    "Vũ": 40,
    "Bảo": 43
})

mean_weight = weights.mean()    
median_weight = weights.median()
mode_weight = weights.mode()    

print(f"Mean (Trung bình): {mean_weight:.2f} kg")
print(f"Median (Trung vị): {median_weight} kg")
print("Mode (Mode - Giá trị xuất hiện nhiều nhất):")

students_with_mode_weight = weights[weights.isin(mode_weight)].index.tolist()
print("Học sinh có cân nặng thuộc giá trị mode:")
print(", ".join(students_with_mode_weight))
