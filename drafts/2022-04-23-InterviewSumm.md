---
title: "InterviewSumm"
excerpt: ""
mathjax: false
tags: 
---

> 参考自公众号《所向披靡的张大刀》<a href="https://mp.weixin.qq.com/s/5DXI0fYAWmUDubPAJ97afA">武功秘籍 | 美团大面筋</a>。此公众号盛产干货，强烈推荐。

## CNN卷积神经网络相关

### 相关原理

**图卷积的基本原理** Todo

**CNN1*1卷积核的作用？**

1、1乘1卷积核能改变通道数。对于三通道的图像，我们只用一个1乘1的卷积核，就可以将三通道的图像减小为1通道的图像。同样的，通过增加卷积核的个数，就能够增加通道的个数

2、建立更深的网络结构。实际上这对应着不改变通道数的情况。使用1乘1的卷积核实际上在不增加感受野的情况下加深了网络结构，增加了更多的非线性，从而增强了网络的表达能力。

● 卷积神经网络的权重是怎么更新的?

● dropout的随机因子会对结果的损失有影响吗

● dropout怎么反向传播？

● 卷积是空间不变性还是时间不变性？

● CNN网络有哪些层？

● 感受野在cv中的作用，大小分别有什么影响 全局感受野和局部感受野的优缺点，哪些论文的方法是从这方面考虑并进行改进的，介绍一下他们的方法？

● 平均池化和最大持化的反向传播是怎么运作的？

● 池化层如何反向传播？

● InceptionV3和ResNet50网络模型用过吗？

● 简单讲一下Inception家族(各种优缺点以及改进)

● 讲一下ResNet的原理以及它解决了什么问题？怎么解决的？

● Resnet为什么有效果？为什么能够保证很深的网络具备不错的效果？

● 对感受野的理解？例如VGG网络，最后一层卷积网络输出图片对于输入图片的感受野的大小？

● SEnet的结构？SEnet如何放到Resnet的backbone里？

● RoIPooling和ROI Align区别？

● 神经网络中的偏置项（b）尺寸应该是什么样的？

● BN知道嘛？讲一下BN的原理，作用？它有四个公式，每一个公式分别是什么，有什么各自的作用？

● BN为啥可以缓解过拟合，详细讲一下？BN有哪些需要学习的参数啊，BN训练和测试是怎么做的？

● 除了BN，你还知道那些其他的加速收敛的方法(楼主说到了归一化)，面试官说，和BN差不多的那些你了解吗？(GN, IN, FN)

● BN一般用在网络的哪个部分啊？

● BN底层如何计算，手撕BN，BN在训练、测试阶段的计算有什么区别

● 用公式推导小的batchsize会对模型训练有什么影响，我回答了BN方面的一些影响，面试官说不行，从BP角度考虑。

● 如何解决梯度消失问题？

● 梯度消失，梯度爆炸讲一下？怎么解决？

● 分类问题的loss为什么选交叉熵，MSE可以吗？基尼系数的公式为什么这么写？

### 公式推导

● 手推BP算法公式（就只有一层隐含层的那种）

● Softmax的计算公式是什么？为什么使用指数函数？

● 用公式详解BP原理

● 通过公式解释链式法则以及resnet？

## RNN循环神经网络

**RNN的梯度消失梯度爆炸问题**



● LSTM跟RNN的区别，他和RNN相比有什么优势。

● LSTM的信息传递机制是什么？

● LSTM原理，与GRU区别？使用场景的不同点？

● BiLSTM相比LSTM有哪些case上的提升。Attention是如何加的取得了哪些效果的提升？

● LSTM结构以及从数学层面谈为啥优于RNN？

## CNN & RNN通用的问题

### 基础知识点

● 注意力机制的运行过程是什么样的？

● Localattention和global attention的区别?

● attention机制的作用以及选用的原因？

● 为什么设计神经网络解决问题，目前网络存在的问题是什么，后续可以怎么优化？

● 介绍 self-attention 计算，为什么用多头注意力？

● Dropout的解释

●  介绍一下transformer。有什么可以调整的参数

●  具体讲一下self attention。

●  self attention， attention， 双向lstm的区别。

●  CNN和RNN的优缺点

### 模型评价

● Precision和Recall

● AUC的作用，AUC 计算方法，AUC的时间复杂度？

## Reference

1. <a href="https://blog.csdn.net/briblue/article/details/83151475">【深度学习】CNN 中 1x1 卷积核的作用</a>
2. Deep Learning.ai <a href="https://www.bilibili.com/video/BV1BZ4y1M7hF?p=124">C4W2L05 Network In Network</a>
3. 

