import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')

fix, ax = plt.subplots()

ax.plot(x_values, y_values, linewidth=3)

ax.set_title("cube numbers", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("cube of value", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()