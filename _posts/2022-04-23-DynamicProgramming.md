---
title: "DynamicProgramming"
excerpt: "动态规划学习的简单总结。并没有太多的干货，慎重参考"
mathjax: false
tags: "动态规划"
---

两个属性：

- 最优子结构：问题的最优解可以由通解解决子问题的最优解而得到
- 子问题重叠：解决子问题的时候会包含重复的计算（求解）过程

主要解决的问题类型：

- 组合型：一般来说主要解决有多少的问题（How many?）
- 优化型：优化型问题很好识别，一般都会涉及到最大最小等典型特征

五个步骤：

1. 定义目标函数
2. 找到边界情况。找到最简单的那个情况或者说找到最trivial的情况，此外还要找到最后的情况。这是算法的边界情况
3. 写出转换函数。或者说，写出关系函数。所谓转换函数是指，在这样的问题中状态变化的函数或描述状态之间关系的函数。以我目前的学习经验来看，将转换函数的实现和数组的操作联系起来是解决问题的关键。
4. 确定解决子问题的顺序
5. 找到问题的解
6. *分析时间复杂度和空间复杂度。这一步不是必须的，但是我认为这是一个好习惯

总结：

- 数组操作尤其要注意索引的边界
- 此外，我习惯让程序的流程尽可能和数学公式保持一致，但是有些时候还是不得不做出妥协
- 当有特殊的约束时，不妨先考虑无约束的情况，然后再加上约束，进行改进
- 过早的优化是万恶之源。--高德纳
- 可以先将优化型问题看成组合型问题来看待。然后在解决组合型问题的基础上，再考虑最小化成本从而解决优化问题。比如：找到到点(x,y)的最优的路径。我们可以先寻找到(x, y)有多少种路径，解决了这样的组合型问题。然后再考虑上每条路径的代价，基于前面组合型问题的答案，就可以很容易的解决这种最优的问题。

DP的其他形式：

- Top Down Method: 自顶向下方法和人类的思考的方式类似。其实递归就是一种自顶向下的方法。自顶向下的DP其实就是利用了递归的方法，然后再结合暂存方法，将一些中间结果值暂时存储起来，从而实现对速度的优化。
- Bottom Up Forward Method：自底向上的前向方法。DP问题的一个特点是最优子结构，一个问题的解决依赖于它的子问题的解决。前向的方法就是我们计算完一些子问题后，然后去计算这些子问题构成的一个大问题。这是比较常用实现方法。一般来说，我们分析的时候都是自顶向下分析，实现的时候是自底向上的，所以这是我习惯使用的方法。
- Bottom Up Backward Method：自底向上的反向方法。与前向方法不同的是，反向方法不会等着一个大问题的子问题都解决完再去解决大问题，在解决完某一个子问题时，它就会把该子问题的答案暂存到依赖于它大问题的缓存中，然后大问题直接将缓存中的值综合起来就得到了大问题的值。徒说无益，还是要看实例比较清晰。

以斐波那契数列为例展示DP其他形式的实现：

```java
// Top Down Method
public static int topDownFib(int n) {
    int[] arr = new int[n+1];
    return topDownFibHelper(n, arr);
}

private static int topDownFibHelper(int n, int[] memo) {
    if (n == 0) {
        memo[0] = 0;
    } else if (n <= 2) {
        memo[n] = 1;
    } else {
        if (memo[n] > 0) {
            return memo[n];
        }
        memo[n] = topDownFibHelper(n-1, memo) + topDownFibHelper(n-2, memo);
    }
    return memo[n];
}

// Bottom Up Forward Method
public static int bottomUpFibForward(int n) {
    if (n == 0) {
        return 0;
    }
    if (n <= 2) {
        return 1;
    }

    int[] arr = new int[n+1];
    arr[0] = 0;
    arr[1] = 1;
    for (int i = 2; i < n+1; i++) {
        arr[i] = arr[i-1] + arr[i-2];
    }
    return arr[n];
}

// Bottom Up Backward Method
public static int bottomUpFibBackward(int n) {
    if (n == 0) {
        return 0;
    }

    if (n <= 2) {
        return 1;
    }

    int[] arr = new int[n+2];
    arr[0] = 0;
    arr[1] = 1;
    for (int i = 1; i < n; i++) {
        arr[i+1] += arr[i];
        arr[i+2] += arr[i];
    }
    return arr[n];
}
```



