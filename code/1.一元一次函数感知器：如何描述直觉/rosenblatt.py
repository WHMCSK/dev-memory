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

for m in range (100):
    for i in range(100):
        x = xs[i]
        y = ys[i]
        y_pre = w * x
        e = y - y_pre
        print("误差：", e)
        alpha = 0.05
        w = w + alpha * e * x

y_pre = w * xs

print("Final Weights: ", w)

plt.plot(xs, y_pre, color='b', linewidth=2)


plt.show()