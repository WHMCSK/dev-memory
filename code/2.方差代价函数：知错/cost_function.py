import dataset
import matplotlib.pyplot as plt
import numpy as np

xs, ys = dataset.get_beans(100)

plt.title("Cost Function", fontsize = 12)
plt.xlabel("Bean Size")
plt.ylabel("Toxicity")

plt.scatter(xs, ys, c='b', label='Real Data')

w = 0.5
y_pre = w*xs

plt.plot(xs, y_pre)
plt.show()

es = (ys - y_pre)**2

sum_e = np.sum(es)

sum_e = (1/100)*sum_e

print(sum_e)

ws = np.arange(0, 3, 0.01)

es = []
for w in ws:
    y_pre = w*xs
    e = (1/100)*np.sum((ys - y_pre)**2)
    es.append(e)
    print("w:" + str(w) + " es:" + str(es))

plt.title("Cost Function", fontsize = 12)
plt.xlabel("w")
plt.ylabel("e")

plt.plot(ws, es)
plt.show()

# 顶点坐标公式b/-2a
w_min = np.sum(xs*ys)/np.sum(xs*xs)
print("最小点的w值为：" + str(w_min))

y_pre = w_min*xs


plt.title("Cost Function", fontsize = 12)
plt.xlabel("Bean Size")
plt.ylabel("Toxicity")

plt.scatter(xs, ys, c='b', label='Real Data')

plt.title("Cost Function", fontsize = 12)
plt.xlabel("w")
plt.ylabel("e")

plt.plot(xs, y_pre)
plt.show()