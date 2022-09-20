import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

print(x_values[-1])
print(y_values[-1])

plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=10)
# ax.scatter(x_values,y_values,s=10,c='red')
# ax.scatter(x_values,y_values,s=10,c=[0,0.8,0])
ax.scatter(x_values,y_values,s=10,c=y_values,cmap=plt.cm.Blues)

ax.set_title("cube numbers", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("cube of value", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

# ax.axis([0, 1100, 0, 1100000])

plt.show()
# plt.savefig('/home/zhs2si/Pictures/squares_plot.png')
# plt.savefig('/home/zhs2si/Pictures/squares_plot.png', bbox_inches='tight')