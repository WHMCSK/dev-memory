# CUDA 入门

## config cuda
export LD_LABRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-11.6/lib64
export PATH=$PATH:/usr/local/cuda-11.6/bin
export CUDA_HOME=$CUDA_HOME:/usr/local/cuda-11.6
export PATH=/usr/local/cuda/bin:$PATH


## 核函数（Kernel function）

外观： 

1. 核函数在GPU上进行并行执行。
2. 核函数外观要注意两点：
   - 必须用限定词__global__修饰符。
   - 核函数返回值必须是void。

特点：

1. 核函数只能访问GPU内存
2. 核函数不能使用变长参数
3. 核函数不能使用静态变量
4. 核函数不能使用函数指针
5. 核函数具有异步性


2. 核函数的输入参数是全局内存中的数据，输出参数是全局内存中的数据。
3. 核函数的执行时间由GPU硬件决定，通常是微秒级。
4. 核函数的编程语言是CUDA C。
5. 核函数的执行效率高于CPU上的函数，因为GPU的并行性可以提高计算效率。
6. 核函数的编程难度较低，只需要熟悉CUDA C语言即可。

## CUDA编程模型

1. CUDA编程模型是一种并行编程模型，它将程序分解为多个核函数，每个核函数运行在一个线程块上。
2. 线程块是一组线程，它们共享同一块全局内存。
3. 线程块的大小由硬件决定，通常是128、256、512、1024或2048个线程。
4. 线程块的数量由硬件决定，通常是由GPU的核心数决定的。
5. 线程块之间可以并行执行，因此可以提高计算效率。
6. CUDA编程模型的编程难度较高，需要熟悉CUDA C语言、CUDA运行时库、CUDA编程模型、GPU硬件架构等知识。

## CUDA编程模型的基本步骤

1. 编写核函数，在CUDA C语言中定义。
2. 编译核函数，将核函数编译成可执行文件。
3. 加载核函数，将可执行文件加载到GPU上。
4. 创建线程块，在GPU上创建线程块。
5. 启动线程块，启动线程块中的线程。
6. 等待线程块完成，等待线程块中的线程完成计算。
7. 释放资源，释放线程块、全局内存等资源。

## CUDA编程模型的基本代码示例

```
#include <stdio.h>
#include <cuda_runtime.h>

__global__ void add(int *a, int *b, int *c) {
    int i = threadIdx.x;
    c[i] = a[i] + b[i];
}

int main() {
    int a[10], b[10], c[10];
    int *dev_a, *dev_b, *dev_c;
    size_t size = sizeof(int) * 10;

    // 申请设备内存
    cudaMalloc((void**)&dev_a, size);
    cudaMalloc((void**)&dev_b, size);
    cudaMalloc((void**)&dev_c, size);

    // 向设备内存中拷贝数据
    cudaMemcpy(dev_a, a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(dev_b, b, size, cudaMemcpyHostToDevice);

    // 启动核函数
    add<<<1, 10>>>(dev_a, dev_b, dev_c);

    // 等待核函数完成
    cudaDeviceSynchronize();

    // 从设备内存中拷贝数据
    cudaMemcpy(c, dev_c, size, cudaMemcpyDeviceToHost);

    // 释放设备内存
    cudaFree(dev_a);
    cudaFree(dev_b);
    cudaFree(dev_c);

    // 输出结果
    for (int i = 0; i < 10; i++) {
        printf("%d + %d = %d\n", a[i], b[i], c[i]);
    }

    return 0;
}
```


参考：https://www.bilibili.com/video/BV1sM4y1x7of?spm_id_from=333.788.videopod.episodes&vd_source=665e35db8f931ad6292d3b95f67d4554&p=2

