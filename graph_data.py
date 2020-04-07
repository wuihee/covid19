import xlrd
import matplotlib.pyplot as plt
import numpy as np

file = 'covid19_data.xlsx'
wb = xlrd.open_workbook(file)
sheet = wb.sheet_by_index(0)

data = {}
for i in range(sheet.nrows):
    ranking = sheet.cell_value(i, 0)
    country = sheet.cell_value(i, 1)
    if type(ranking) == float:
        data[country] = ranking

# Plot Bar Graph
fig, ax = plt.subplots()
y_pos = np.arange(len(data))
ax.barh(y_pos, data.values(), align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(data.keys())
ax.set_xlabel('% tested positive / % of population tested')
ax.set_title('Rankings')

plt.show()
