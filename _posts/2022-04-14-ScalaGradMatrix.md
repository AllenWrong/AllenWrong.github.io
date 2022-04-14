---
layout: post
title: "标量对矩阵求导的直观理解"
excerpt: "本文企图以一种直观简单而不失严谨性的方式来理解标量对矩阵的求导。尽管理解的方式在数学上并不严谨，但是由于它的简单和直观性，丧失一些严谨性也是值得的"
date: 2022-04-14 21:30:22
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

### 为什么对db的求导要有加和？

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