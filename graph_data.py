import matplotlib.pyplot as plt
import numpy as np
import get_data

values = get_data.main()

data = {}
for v in values:
    country = v[0]
    ranking = float(v[1])
    if type(ranking) == float:
        if ranking > 0.1:
            data[country] = ranking

# Plot Bar Graph
fig, ax = plt.subplots()
y_pos = np.arange(len(data))
ax.barh(y_pos, data.values(), align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(data.keys())
ax.invert_yaxis()
ax.set_xlabel('% tested positive / % of population tested')
ax.set_title('Rankings')

plt.show()
