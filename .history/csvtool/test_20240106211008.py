import os
excel_file = '/workspace/DATA/xpj/dataset/best_poi_result/bangkok/bangkok_desc_poi_1.xlsx'
base_name = os.path.splitext(os.path.basename(excel_file))[0]
print(base_name)