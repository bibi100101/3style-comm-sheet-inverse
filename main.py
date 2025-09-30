import csv
import sheet_manager

#The path of the sheet duh
sheet_path = 'bld stuff  - Edges.csv'
# NxN size of sheet not including headers, just comm portion
sheet_size = 22

with open(sheet_path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    sheet = list(reader)

sheet = sheet_manager.generate_inverses(sheet, sheet_size);

with open('out.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(sheet)