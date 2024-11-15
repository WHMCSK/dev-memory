# 深度学习算法常识

1. 梯度下降算法

* 梯度下降算法（Gradient Descent Algorithm）是机器学习中常用的优化算法，它是一种迭代算法，通过不断更新模型参数来最小化代价函数，使模型逼近最优解。
* 算法的基本思想是：在每一步迭代中，算法都会计算模型在当前参数下的损失函数的梯度，并根据梯度下降方向更新模型参数，使得损失函数减小。
* 算法的具体步骤如下：
  1. 初始化模型参数；
  2. 重复以下步骤直到收敛：
     * 计算损失函数关于模型参数的梯度；
     * 更新模型参数，使得损失函数减小；
  3. 输出训练好的模型参数。

2. 随机梯度下降算法

* 随机梯度下降算法（Stochastic Gradient Descent Algorithm）是梯度下降算法的变体，它是一种在线学习算法，它每次只处理一个样本，并根据样本的梯度更新模型参数。

3. 动量法

* 动量法（Momentum）是一种用于梯度下降的优化算法，它通过引入动量变量来加速模型的收敛速度。
* 算法的基本思想是：在每一步迭代中，算法都会计算模型在当前参数下的梯度，并根据梯度下降方向更新模型参数，同时引入动量变量来记录之前的梯度方向，并根据动量变量更新模型参数。
* 算法的具体步骤如下：
  1. 初始化模型参数；
  2. 初始化动量变量；
  3. 重复以下步骤直到收敛：
     * 计算损失函数关于模型参数的梯度；
     * 更新模型参数，根据动量变量更新模型参数；
  4. 输出训练好的模型参数。
  5. 注意：动量法可以加速模型的收敛速度，但并不是保证一定能收敛到全局最优。
  6. 另外，动量法可以与随机梯度下降算法结合使用，来提高模型的鲁棒性。
  7. 动量法的公式如下：
     * v = β * v - lr * grad
     * param += v
     * 其中，β为动量超参数，lr为学习率，grad为梯度，v为动量变量，param为模型参数。
     * 动量法的超参数β可以设置为0.9或0.99。
     * 动量法的学习率可以设置为0.01或0.001。
     * 动量法的优点是能够加速模型的收敛速度，但并不是保证一定能收敛到全局最优。
     * 动量法的缺点是需要额外的内存来存储动量变量，同时动量法的收敛速度依赖于学习率。
     * 动量法的适用场景是具有高维度、非凸、非线性的模型。
     * 动量法的实现方法有两种：
       * 动量法的实现方法1：在每一步迭代中，计算梯度并更新模型参数，同时更新动量变量；
       * 动量法的实现方法2：在每一步迭代中，计算梯度并更新模型参数，同时更新动量变量，并在下一步迭代中使用动量变量来更新模型参数。
       * 两种方法的区别在于，方法1需要额外的内存来存储动量变量，方法2不需要额外的内存。
       * 两种方法的收敛速度相同，但方法2的计算量更小。

4. 自适应学习AdaGrad和RMSProp算法

* AdaGrad算法（Adaptive Gradient Algorithm）是一种自适应学习算法，它通过对每个参数的学习率进行调整，来使得模型在训练过程中更加稳定。
* RMSProp算法（Root Mean Square Propagation Algorithm）是AdaGrad算法的变体，它通过对每个参数的学习率进行调整，来使得模型在训练过程中更加稳定。
* 算法的基本思想是：在每一步迭代中，算法都会计算模型在当前参数下的梯度，并根据梯度下降方向更新模型参数，同时根据梯度的大小来调整模型参数的学习率。
* 算法的具体步骤如下：
  1. 初始化模型参数；
  2. 初始化学习率；
  3. 重复以下步骤直到收敛：
     * 计算损失函数关于模型参数的梯度；
     * 更新模型参数，根据梯度大小调整学习率；
  4. 输出训练好的模型参数。
  5. AdaGrad算法的公式如下：
     * g += grad^2
     * param -= lr * grad / (sqrt(g) + ε)
     * 其中，g为梯度的二阶矩，lr为学习率，ε为一个很小的常数，param为模型参数。
     * AdaGrad算法的优点是能够对每个参数的学习率进行调整，使得模型在训练过程中更加稳定。
     * AdaGrad算法的缺点是需要额外的内存来存储梯度的二阶矩。
     * AdaGrad算法的适用场景是具有高维度、非凸、非线性的模型。
  6. RMSProp算法的公式如下：
     * g = β * g + (1 - β) * grad^2
     * param -= lr * grad / (sqrt(g) + ε)
     * 其中，β为衰减率，g为梯度的二阶矩，lr为学习率，ε为一个很小的常数，param为模型参数。
     * RMSProp算法的优点是能够对每个参数的学习率进行调整，使得模型在训练过程中更加稳定。
     * RMSProp算法的缺点是需要额外的内存来存储梯度的二阶矩。
     * RMSProp算法的适用场景是具有高维度、非凸、非线性的模型。
     * RMSProp算法的衰减率β可以设置为0.9或0.99。
     * RMSProp算法的学习率可以设置为0.01或0.001。
     * RMSProp算法的优点是能够对每个参数的学习率进行调整，使得模型在训练过程中更加稳定。

5. 动量 & 自适应学习 Adam算法

* Adam算法（Adaptive Moment Estimation Algorithm）是一种结合了动量法和AdaGrad算法的优化算法，它通过对每个参数的学习率进行调整，来使得模型在训练过程中更加稳定。
* 算法的基本思想是：在每一步迭代中，算法都会计算模型在当前参数下的梯度，并根据梯度下降方向更新模型参数，同时引入动量变量来记录之前的梯度方向，并根据动量变量更新模型参数，同时根据梯度的大小来调整模型参数的学习率。
* 算法的具体步骤如下：
  1. 初始化模型参数；
  2. 初始化动量变量；
  3. 初始化学习率；
  4. 重复以下步骤直到收敛：
     * 计算损失函数关于模型参数的梯度；
     * 更新模型参数，根据动量变量更新模型参数，根据梯度大小调整学习率；
  5. 输出训练好的模型参数。
  6. Adam算法的公式如下：
     * m = β1 * m + (1 - β1) * grad
     * v = β2 * v + (1 - β2) * grad^2
     * m_hat = m / (1 - β1^t)
     * v_hat = v / (1 - β2^t)
     * param -= lr * m_hat / (sqrt(v_hat) + ε)
     * 其中，β1、β2为动量超参数，lr为学习率，ε为一个很小的常数，m、v为动量变量，param为模型参数。
     * Adam算法的优点是能够结合动量法和AdaGrad算法的优点，能够对每个参数的学习率进行调整，使得模型在训练过程中更加稳定。
     * Adam算法的缺点是需要额外的内存来存储动量变量和梯度的二阶矩。
     * Adam算法的适用场景是具有高维度、非凸、非线性的模型。
     * Adam算法的超参数β1、β2、lr可以设置为0.9、0.99、0.001。

6. 反向传播算法

* 反向传播算法（Backpropagation Algorithm, BP）是深度学习中常用的训练算法，它是一种计算神经网络误差梯度的算法。
* 算法的基本思想是：通过反向传播算法，可以计算神经网络中各个参数的梯度，并根据梯度下降方向更新参数，使得神经网络误差最小。
* 算法的具体步骤如下：
  1. 计算损失函数关于各个参数的梯度；
  2. 按照梯度下降方向更新各个参数；
  3. 重复以上步骤，直到模型训练误差最小。

* 加速计算参数梯度值得方法
* 计算图（Computation Graphs）

1. 卷积神经网络

2. 循环神经网络

3. 注意力机制

4. 强化学习

5. 蒙特卡洛树搜索

6. 变分自编码器

7. 变分自动编码器

8.  生成对抗网络
