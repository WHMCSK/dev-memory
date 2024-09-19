import dataset
from matplotlib import pyplot as plt

xs, ys = dataset.get_beans(100)
print(xs)
print(ys)

plt.title("Size-Toxicity Function",fontsize=12)
plt.xlabel("Bean Size")
plt.ylabel("Toxicity")
plt.scatter(xs, ys, marker='o', s=50, c='r')


w = 0.5

y_pre = w * xs

plt.plot(xs, y_pre, color='b', linewidth=2)


plt.show()