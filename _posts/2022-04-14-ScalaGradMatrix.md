---
title: "标量对矩阵求导的直观理解"
excerpt: "本文企图以一种直观简单而不失严谨性的方式来理解标量对矩阵的求导。尽管理解的方式在数学上并不严谨，但是由于它的简单和直观性，丧失一些严谨性也是值得的"
mathjax: true
---

* 目录
{:toc}

## 标量对矩阵的求导

直观的理解一下标量对矩阵求导的意义，虽然这不是严谨的数学推导，但在我看来，这是理解标量对矩阵求导的一种比较容易的方法。**如果你不能很容易的理解它，那你就很难很容易的去应用它。在我看来，寻找简单直观而不失严谨性的理解方式是非常重要的。这里在损失一点严谨性的条件下提供了很简单的理解，我觉得也是值得的。**

### 标量对矩阵的求导之矩阵乘法求导的直观理解

以2维方阵为例$$AB=C$$：

$$
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}

\begin{bmatrix}
b_{11} & b_{12} \\
b_{21} & b_{22}
\end{bmatrix}

=
\begin{bmatrix}
a_{11}b_{11} + a_{12}b_{21} & a_{11}b_{12} + a_{12}b_{22} \\
a_{21}b_{11} + a_{22}b_{21} & a_{21}b_{12} + a_{22}b_{22}
\end{bmatrix}
$$

```python
C = np.dot(A, B)
```

并且，标量对$$C$$的梯度如下：

$$
dC=\begin{bmatrix}dc_{11} & dc_{12} \\dc_{21} & dc_{22}\end{bmatrix}
$$

其中$$c_{12}=a_{11}b_{12} + a_{12}b_{22}$$。$$dc_{ij}$$可以理解为标量对$$c_{ij}$$的梯度。那么有如下结论：

$$
dA = dCB^{T}
\\
dB = A^{T}dC
$$

```python
dA = np.dot(dC, B.T)
dB = np.dot(A.T, dC)
```

上述公式有严谨的数学推导，但是这里我打算用一种直观的方式理解上面的结论。

**公式1**

如果$$a_{11}$$增加了$$\Delta a$$变成了$$a_{11}+\Delta a$$。那么矩阵$$C$$中会有两个元素发生变化，变成如下的形式：

$$
\begin{bmatrix}
a_{11}b_{11} + \Delta ab_{11} + a_{12}b_{21} & a_{11}b_{12} + \Delta ab_{12} + a_{12}b_{22} \\
a_{21}b_{11} + a_{22}b_{21} & a_{21}b_{12} + a_{22}b_{22}
\end{bmatrix}
$$

即，$$a_{11}$$发生了$$\Delta a$$的变化，那么$$C$$的变化为$$\begin{bmatrix}b_{11} & b_{12}\end{bmatrix}$$。那么这里我们不严格的认为$$c_{11}$$对$$a_{11}$$的梯度为$$b_{11}$$，$$c_{12}$$对$$a_{11}$$的梯度为$$b_{12}$$，$$c_{21}$$对$$a_{11}$$的梯度为0，$$c_{22}$$对$$a_{11}$$的梯度为0，那么$$C$$对$$a_{11}$$的梯度为$$b_{11} + b_{12}$$。如果再考虑上标量对$$C$$的梯度，根据链式法则可以得到$$C$$对$$a_{11}$$的梯度为$$dc_{11}b_{11} + dc_{12}b_{12}$$。写成矩阵的形式如下：

$$
da_{11} = \begin{bmatrix}
dc_{11} & dc_{12}
\end{bmatrix}

\begin{bmatrix}
b_{11} \\ b_{12}
\end{bmatrix}
$$

类似的，如果$$a_{12}$$发生了$$\Delta a$$的变化，那么$$C$$的变化为$$\begin{bmatrix}b_{21} & b_{22}\end{bmatrix}$$。如果再考虑上标量对$$C$$的梯度，根据链式法则可以得到$$C$$对$$a_{12}$$的梯度为$$dc_{11}b_{21} + dc_{12}b_{22}$$。写成矩阵的形式如下：

$$
da_{12} = \begin{bmatrix}
dc_{11} & dc_{12}
\end{bmatrix}

\begin{bmatrix}
b_{21} \\ b_{22}
\end{bmatrix}
$$

到这里，我们可以得到$$A$$的第一行的梯度：

$$
\begin{bmatrix}
da_{11} & da_{12}
\end{bmatrix}
= \begin{bmatrix}
dc_{11} & dc_{12}
\end{bmatrix}

\begin{bmatrix}
b_{11} & b_{21} \\ b_{12} & b_{22}
\end{bmatrix}
$$

使用类似的方法我们可以很轻松的得到$$A$$的梯度为：

$$
dA
= \begin{bmatrix}
dc_{11} & dc_{12} \\
dc_{21} & dc_{22}
\end{bmatrix}

\begin{bmatrix}
b_{11} & b_{21} \\ b_{12} & b_{22}
\end{bmatrix}
= dCB^{T}
$$

**公式2**

利用同样的方法，假设$$b_{11}$$增加了$$\Delta b$$变成了$$b_{11}+\Delta b$$。那么矩阵$$C$$中会有两个元素发生变化，变成如下的形式：

$$
\begin{bmatrix}
a_{11}b_{11} + a_{11}\Delta b + a_{12}b_{21} & a_{11}b_{12}  + a_{12}b_{22} \\
a_{21}b_{11} + a_{21}\Delta b + a_{22}b_{21} & a_{21}b_{12} + a_{22}b_{22}
\end{bmatrix}
$$

同样的，我们不严格的认为如果$$b_{11}$$发生了$$\Delta b$$的变化，那么$$C$$的变化为$$\begin{bmatrix}a_{11} \\ a_{21}\end{bmatrix}$$。如果再考虑上标量对$$C$$的梯度，根据链式法则可以得到$$C$$对$$b_{11}$$的梯度为$$dc_{11}a_{11} + dc_{21}a_{21}$$。写成矩阵的形式如下：

$$
db_{11} = 
\begin{bmatrix}
a_{11} & a_{21}
\end{bmatrix}

\begin{bmatrix}
dc_{11} \\ dc_{21}
\end{bmatrix}
$$

假设$$b_{12}$$增加了$$\Delta b$$变成了$$b_{12}+\Delta b$$。那么矩阵$$C$$中会有两个元素发生变化，变成如下的形式：

$$
\begin{bmatrix}
a_{11}b_{11} + a_{12}b_{21} & a_{11}b_{12} + a_{11} \Delta b + a_{12}b_{22} \\
a_{21}b_{11} + a_{22}b_{21} & a_{21}b_{12} + a_{21} \Delta b + a_{2}b_{22}
\end{bmatrix}
$$

同样的，我们不严格的认为如果$$b_{12}$$发生了$$\Delta b$$的变化，那么$$C$$的变化为$$\begin{bmatrix}a_{11} \\ a_{21}\end{bmatrix}$$。如果再考虑上标量对$$C$$的梯度，根据链式法则可以得到$$C$$对$$b_{11}$$的梯度为$$dc_{12}a_{11} + dc_{22}a_{21}$$。写成矩阵的形式如下：

$$
db_{12} = 
\begin{bmatrix}
a_{11} & a_{21}
\end{bmatrix}

\begin{bmatrix}
dc_{12} \\ dc_{22}
\end{bmatrix}
$$

到这里，我们可以得到$$B$$的第一行的梯度：

$$
\begin{bmatrix}
db_{11} & db_{12}
\end{bmatrix}
= \begin{bmatrix}
a_{11} & a_{21}
\end{bmatrix}

\begin{bmatrix}
dc_{11} & dc_{12} \\ dc_{21} & dc_{22}
\end{bmatrix}
$$

使用类似的方法我们可以很轻松的得到$$B$$的梯度为：

$$
dB
= \begin{bmatrix}
a_{11} & a_{21} \\
a_{12} & a_{22}
\end{bmatrix}

\begin{bmatrix}
dc_{11} & dc_{12} \\ dc_{21} & dc_{22}
\end{bmatrix}

=A^{T}dC
$$

### 标量对矩阵求导之矩阵元素乘法的直观理解

这里以$$A*B=C$$为例：

$$
\begin{bmatrix}a_{11} & a_{12} \\a_{21} & a_{22}\end{bmatrix}\begin{bmatrix}b_{11} & b_{12} \\b_{21} & b_{22}\end{bmatrix}=\begin{bmatrix}a_{11}*b_{11} & a_{12}*b_{12} \\a_{21}*b_{21} & a_{22}*b_{22}\end{bmatrix}
$$

如果$$a_{11}$$增加了$$\Delta a$$变为$$a_{11}+\Delta a$$，那么这只影响到$$c_{11}$$，使得$$c_{11}$$变为$$a_{11}*b_{11}+\Delta a*b_{11}$$。即$$C$$发生的变化量为$$b_{11}$$。类似的，可以得到如果$$a_{ij}$$发生了$$\Delta a$$的变化量，那么$$C$$只有$$c_{ij}$$发生$$b_{ij}$$的变化量，如果再考虑上标量对$$c_{ij}$$的梯度$$dc_{ij}$$，根据链式法则，可以得到标量对$$A$$的梯度为$$b_{ij}dc_{ij}$$。同样的，如果$$b_{ij}$$发生了$$\Delta b$$的变化量，那么$$C$$只有$$c_{ij}$$发生$$a_{ij}$$的变化量,如果再考虑上标量对$$c_{ij}$$的梯度$$dc_{ij}$$，根据链式法则，可以得到标量对$$A$$的梯度为$$a_{ij}dc_{ij}$$。因此有如下结论：

$$
dA = B * dC \\ dB = A * dC
$$

```python
dA = B * dC
dB = A * dC
```

### 梯度在激活函数的传播

以sigmoid为例，$$A=sigmoid(Z)$$，标量对$$A$$的梯度为$$dA$$：

$$
\begin{bmatrix}sigmoid(z_{11}) & sigmoid(z_{12}) \\sigmoid(z_{21}) & sigmoid(z_{22})\end{bmatrix}=\begin{bmatrix}a_{11} & a_{12} \\a_{21} & a_{22}\end{bmatrix}
$$

$$
dA = \begin{bmatrix}da_{11} & da_{12} \\da_{21} & da_{22}\end{bmatrix}
$$

加入$$z_{11}$$增加了$$\Delta z$$那么$$A$$中只有$$a_{11}$$受到影响，发生的变化为$$sigmoid(z_{11}+\Delta z)-sigmoid(z_{11})$$这里我们称这种关系为一对一的关系。那么，不严谨的说，当$$Z$$发生变化时，$$A$$对它的梯度为：

$$
\begin{bmatrix}sigmoid(z_{11})' & sigmoid(z_{12})' \\sigmoid(z_{21})' & sigmoid(z_{22})'\end{bmatrix}
$$

考虑上标量对$$A$$的梯度，以及链式法则，那么就可以得到标量对未激活值的梯度：

$$
dZ = \begin{bmatrix}sigmoid(z_{11})'da_{11} & sigmoid(z_{12})'da_{12} \\sigmoid(z_{21})'da_{21} & sigmoid(z_{22})'da_{22}\end{bmatrix}
$$

```python
dZ = sigmoid(Z) * (1-sigmoid(Z)) * dA
```

### 对db的求导

看如下简单的例子$$WA+b=C$$:

$$
\begin{bmatrix}w_{11} & w_{12} \\w_{21} & w_{22} \\ w_{31} & w_{32}\end{bmatrix}\begin{bmatrix}a_{11} & a_{12} \\a_{21} & a_{22}\end{bmatrix}+\begin{bmatrix}b_{1} \\b_{2} \\b_{3}\end{bmatrix}=\begin{bmatrix}w_{11}a_{11}+w_{12}a_{21}+b_1 & w_{11}a_{12}+w_{12}a_{22}+b_1 \\w_{21}a_{11}+w_{22}a_{21}+b_2 & w_{21}a_{12}+w_{22}a_{22}+b_2 \\w_{31}a_{11}+w_{32}a_{21}+b_3 & w_{31}a_{12}+w_{32}a_{22}+b_3\end{bmatrix}
$$

并且假设标量对矩阵$$C$$的梯度为：

$$
dC=\begin{bmatrix}dc_{11} & dc_{12} \\dc_{21} & dc_{22} \\dc_{31} & dc_{32}\end{bmatrix}
$$

当$$b_1$$增加$$\Delta b$$时，那么$$C$$的变化量为$$\begin{bmatrix}\Delta b & \Delta b \end{bmatrix}$$，考虑上标量对$$C$$的梯度以及链式法则，就可以得到变量对$$b_1$$梯度为$$dc_{11}+dc_{12}$$。因为在这里，第0维度表示的是特征，第1维度表示的是样本的个数或者是batch size。因此他会出现对$$dC$$的每行求和的形式，如果第0维度表示的是样本的个数，那么就会出现对$$dC$$每列求和的形式。类似的，我们可以得到：

$$
db =\begin{bmatrix}dc_{11} + dc_{12} \\dc_{21} + dc_{22} \\dc_{31} + dc_{32}\end{bmatrix}
$$

```
db = np.sum(dC, axis=1, keepdims=True)
```

也可以这么理解，偏置是对每个特征维度上的偏置。在这个例子中，我们将$$A$$看成是样本矩阵，也就是说这个batch有两个样本，每个样本的维度是2，这里，经过权重矩阵$$W$$把它的样本的特征维度由两维变换成三维，然后对每个特征维度加上一个偏置。也就是每个样本的每个特征上都被加上了一个偏置，而由于每个样本都会有一个损失，该损失就会对该样本有个梯度，从而损失通过该样本对偏置的每个维度上都有了一个梯度。显然，当我们有了batch size个样本的时候，损失对偏置就会有batch size个梯度，然后把这batch size个梯度加和作为损失对偏置的梯度。所以他会出现加和的形式。

### 卷积运算的求导

为了避免混淆，下面的部分使用$$conv(*)$$表示卷积，使用$$*$$表示元素乘法。

先贴上结论，然后再看简单的分析：

对于$$Aconv(*)W=C$$已知标量对$$C$$的梯度为$$dC$$，那么

- 标量对$$W$$的梯度为：$$dW=Aconv(*)dC$$
- 标量对A的梯度为：$$dA=np.pad(dC, pad\_width=((1,1), (1,1)), mode="contant", contant\_value=0) conv(*)W^{rotation180^o}$$

```python
dW = np.convolve(A, dC)
padded_dC = np.pad(dC, pad_width=((1,1), (1,1)), mode="contant", contant_value=0)
dA = np.convolve(padded_dC, np.flip(np.flip(W,axis=0), axis=1))
```

看如下的例子$$Aconv(*)W=C$$：

$$
\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{bmatrix}

conv(*)

\begin{bmatrix}
w_{11} & w_{12} \\
w_{21} & w_{22}
\end{bmatrix}

=
 
\left[
    \begin{array}{c|c}
a_{11}w_{11} + a_{12}w_{12} & a_{12}w_{11} + a_{13}w_{12} \\
+ a_{21}w_{21} + a_{22}w_{22} &  + a_{22}w_{21} + a_{23}w_{22} \\
\hline 
a_{21}w_{11} + a_{22}w_{12} & a_{22}w_{11} + a_{23}w_{12} \\
+ a_{31}w_{21} + a_{32}w_{22} &  + a_{32}w_{21} + a_{33}w_{22} 
    \end{array}
\right]
$$

变量对矩阵$$C$$的梯度为如下：

$$
dC=
\begin{bmatrix}
dc_{11} & dc_{12} \\
dc_{21} & dc_{22}
\end{bmatrix}
$$

**首先看对矩阵$$W$$的求导**。下面用$$w_{ij}+\delta w$$表示$$w_{ij}$$发生了$$\delta w$$的变化。考虑上标量对矩阵$$C$$的梯度和链式法则，用$$dw_{ij}$$表示标量对$$w_{ij}$$的梯度。

当$$w_{11}+\delta w$$时，$$C$$发生的变化为：

$$
\begin{bmatrix}
a_{11}\delta w & a_{12}\delta w \\
a_{21}\delta w & a_{22}\delta w
\end{bmatrix}
$$

$$
dw_{11}=
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}
conv(*)
\begin{bmatrix}
dc_{11} & dc_{12} \\
dc_{21} & dc_{22}
\end{bmatrix}
$$

当$$w_{12}+\delta w$$时，$$C$$发生的变化为：

$$
\begin{bmatrix}
a_{12}\delta w & a_{13}\delta w \\
a_{22}\delta w & a_{23}\delta w
\end{bmatrix}
$$

$$
dw_{12}=
\begin{bmatrix}
a_{12} & a_{13} \\
a_{22} & a_{23}
\end{bmatrix}
conv(*)
\begin{bmatrix}
dc_{11} & dc_{12} \\
dc_{21} & dc_{22}
\end{bmatrix}
$$

当$$w_{21}+\delta w$$时，$$C$$发生的变化为：

$$
\begin{bmatrix}
a_{21}\delta w & a_{22}\delta w \\
a_{31}\delta w & a_{32}\delta w
\end{bmatrix}
$$

$$
dw_{21}=
\begin{bmatrix}
a_{21} & a_{22} \\
a_{31} & a_{32}
\end{bmatrix}
conv(*)
\begin{bmatrix}
dc_{11} & dc_{12} \\
dc_{21} & dc_{22}
\end{bmatrix}
$$

当$$w_{22}+\delta w$$时，$$C$$发生的变化为：

$$
\begin{bmatrix}
a_{22}\delta w & a_{23}\delta w \\
a_{32}\delta w & a_{33}\delta w
\end{bmatrix}
$$

$$
dw_{22}=
\begin{bmatrix}
a_{22} & a_{23} \\
a_{32} & a_{33}
\end{bmatrix}
conv(*)
\begin{bmatrix}
dc_{11} & dc_{12} \\
dc_{21} & dc_{22}
\end{bmatrix}
$$

观察并对比就可以发现，求梯度的过程实际上也是一个卷积的过程：

$$
dW = 
\begin{bmatrix}
dw_{11} & dw_{12} \\
dw_{21} & dw_{22}
\end{bmatrix}
=
\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{bmatrix}

conv(*)

\begin{bmatrix}
dc_{11} & dc_{12} \\
dc_{21} & dc_{22}
\end{bmatrix}
=
Aconv(*)dC
$$

**使用同样的方法，我们也来看一下对$$A$$的梯度**。下面使用$$a_{ij}+\delta a$$来表示$$a_{ij}$$发生了$$\delta a$$的变换，用$$da_{ij}$$来表示标量对$$a_{ij}$$的梯度。

当$$a_{11}+\delta a$$是，C发送的变化为：

$$
\begin{bmatrix}
w_{11}\delta a & 0 \\ 0 & 0
\end{bmatrix}
$$

当$$a_{12}+\delta a$$是，C发送的变化为：

$$
\begin{bmatrix}
w_{12}\delta a & w_{11} \delta a \\ 
0 & 0
\end{bmatrix}
$$

当$$a_{13}+\delta a$$是，C发送的变化为：

$$
\begin{bmatrix}
0 & w_{12}\delta a \\ 0 & 0
\end{bmatrix}
$$

当$$a_{21}+\delta a$$是，C发送的变化为：

$$
\begin{bmatrix}
w_{21}\delta a & 0 \\
w_{11}\delta a & 0
\end{bmatrix}
$$

当$$a_{22}+\delta a$$是，C发送的变化为：

$$
\begin{bmatrix}
w_{22}\delta a & w_{21}\delta a \\
w_{12}\delta a & w_{11}\delta a
\end{bmatrix}
$$

当$$a_{23}+\delta a$$是，C发送的变化为：

$$
\begin{bmatrix}
0 & w_{22}\delta a \\
0 & w_{12}\delta a
\end{bmatrix}
$$

当$$a_{31}+\delta a$$是，C发送的变化为：

$$
\begin{bmatrix}
0 & 0 \\
w_{21}\delta a & 0
\end{bmatrix}
$$

当$$a_{32}+\delta a$$是，C发送的变化为：

$$
\begin{bmatrix}
0 a & 0 \\
w_{22}\delta a & w_{21}\delta a
\end{bmatrix}
$$

当$$a_{33}+\delta a$$是，C发送的变化为：

$$
\begin{bmatrix}
0 & 0 \\
0 & w_{22}\delta a
\end{bmatrix}
$$

在前面的分析中，我们发现$$dW$$是由$$dC$$和$$A$$算出来的。这里我们不妨猜测，$$dA$$与$$dC$$和$$W$$有关。基于这样的猜测，我们企图把这种关系比较规整的表达出来。若能规整的表达出来，那这样的公式就是我们要找的一个优雅的求导的公式。

由于当$$a_{22}$$发生变化时，$$C$$的四个元素都受到了影响，并且$$W$$的每一个元素都出现在了$$C$$中，因此我们先拿这个特例开刀。那么可以得出如下的式子：

- $$W^{totate}$$表示翻转180度后的矩阵。

$$
da_{22} = 
\begin{bmatrix}
dc_{11} & dc_{12} \\
dc_{21} & dc_{22}
\end{bmatrix}
conv(*)
\begin{bmatrix}
w_{22} & w_{21} \\
w_{12} & w_{11}
\end{bmatrix}
=dCconv(*)W^{rotate}
$$

同样的，我们尽可能想换出非零元素多的矩阵来做观察，接下来不妨看看$$a_{23}，a_{21}$$发生变化时的特例：

$$
da_{23} =
\begin{bmatrix}
dc_{11} & dc_{12} \\
dc_{21} & dc_{22}
\end{bmatrix}
conv(*)
\begin{bmatrix}
0 & w_{22} \\
0 & w_{12}
\end{bmatrix}
$$

$$
da_{21} =
\begin{bmatrix}
dc_{11} & dc_{12} \\
dc_{21} & dc_{22}
\end{bmatrix}
conv(*)
\begin{bmatrix}
w_{21} & 0 \\
w_{11} & 0
\end{bmatrix}
$$

然后，我们不妨尝试统一上述这个特例，如果能统一到一个优雅的式子，那么就尝试将它推广到其它的$$a_{ij}$$上，然后看是这个式子的结构，是否和我们分析的结果一致。观察可以发现，$$a_{23}$$和$$a_{21}$$其实可以通过在矩阵$$W$$的两遍补零来实现，补零之后，对这三个元素的求导又可以表达成一个卷积的过程，如下式所示：

$$
\begin{bmatrix}
da_{23} & da_{22} & da_{21}
\end{bmatrix}
=
\begin{bmatrix}
dc_{11} & dc_{12} \\
dc_{21} & dc_{22}
\end{bmatrix}
conv(*)
\begin{bmatrix}
0 & w_{22} & w_{21} & 0 \\
0 & w_{12} & w_{11} & 0
\end{bmatrix}
$$

到这里，我们确实将其统一到一个优雅的式子上了，那必然就要大胆的将这个式子进行推广，得到下面的式子：

$$
\begin{bmatrix}
da_{33} & da_{32} & da_{31} \\
da_{23} & da_{22} & da_{21} \\
da_{13} & da_{12} & da_{11}
\end{bmatrix}
=
\begin{bmatrix}
dc_{11} & dc_{12} \\
dc_{21} & dc_{22}
\end{bmatrix}
conv(*)
\begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & w_{22} & w_{21} & 0 \\
0 & w_{12} & w_{11} & 0 \\
0 & 0 & 0 & 0 
\end{bmatrix}
$$

但是这样得到的$$dA$$是一个旋转过的矩阵，和我们的期望有点差异。这里我们分析为什么它是旋转过的。其实这个问题缩小一下，也就是说为什么$$da_{21}$$出现在了$$a_{23}$$的位置上。不妨看一下$$da_{21}$$需要哪些元素：

$$
da_{21}
= dc_{11}w_{21}+dc_{21}w_{11}
$$
在上面的例子中，我们通过对$$W$$补零避免了$$dC$$的第二例对$$da_{21}$$产生贡献，由于它是向右补零，因此导致了$$da_{21}$$的位置右偏。实际上，这里我们也可以通过对$$dC$$补零来避免$$W$$的第一列对$$d_a{21}$$产生贡献，由于它是向左补零，这和$$da_{21}$$在左边是一致的。因此，它会出现我们期望的结果：

$$
\begin{bmatrix}
da_{21} & da_{22} & da_{23} \\
\end{bmatrix}
=
\begin{bmatrix}
0 & dc_{11} & dc_{12} & 0 \\
0 & dc_{21} & dc_{22} & 0 \\
\end{bmatrix}
conv(*)
\begin{bmatrix}
w_{22} & w_{21} \\
w_{12} & w_{11}
\end{bmatrix}
$$

这样位置就对齐的，然后把它进行推广，就可以得到很优雅的答案：

$$
\begin{bmatrix}
da_{11} & da_{12} & da_{13} \\
da_{21} & da_{22} & da_{23} \\
da_{31} & da_{32} & da_{33}
\end{bmatrix}
=
\begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & dc_{11} & dc_{12} & 0 \\
0 & dc_{21} & dc_{22} & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
conv(*)
\begin{bmatrix}
w_{22} & w_{21} \\
w_{12} & w_{11}
\end{bmatrix}
$$

即：$$dA=padded(dC)conv(*)W^{rotate}$$。可以验证这个式子计算出来的结果和我们一开始分析的结果是一致的

