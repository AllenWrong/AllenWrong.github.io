---
title: "CS70-CheatSeet"
excerpt: ""
mathjax: true
tags: 
---

Note0

- 集合(set)：collections of objects. 包含一系列元素。元素不重复，无序
- 基数(Cardinality)：集合中元素的个数
- 子集(subsets)和真子集(proper subsets)：若A中的元素全在B中，则A是B的子集。若A中的元素全在B中，且B中的元素至少有一个不在A中，则A是B的真子集。
- 交集(intersection)：共同存在于A和B中的元素
- 不交(disjoint)：A和B中无共同元素
- 并集(unions)：A，B中所有元素的集合
- 补集(complements)：A在B中的相对补集（又可以说B和A的差集）。记作B-A或者B\A
- 重要的集合：$$\N, \Z, \Q, \R, \C$$
- 笛卡尔积（Cartesian product or Cross product）：一对一组合
- 幂集（power set）：所有子集构成的集合
- 全称量词（universal quantifiers）：$$\forall$$
- 存在量词（exist quantifiers）：$$\exist$$

Note1

- 命题（proposition）：非对即错的语句
- 断言（predicates）：带有猜测或者预测性的肯定，英文形式和predict很像
- 合取（conjunction）：且
- 析取（disjunction）：或
- 非（negation）：非
- 重言式（tautology）：永远是true的命题
- 悖论（contradiction）：永远是false的命题
- 真值表（truth table）：会画真值表
- 蕴含式（implication）：$$P\rightarrow Q$$。如果P，则Q。
  - 只有当P为true，Q为false的时候蕴含式才是错误的。
  - $$P\rightarrow Q = \neg P \or Q$$
  - 蕴含式是存在最广泛的形式
- 德摩根律（De Morgan's Laws）：分发，翻转
- 除（divide）：divide又可以翻译为划分。例如：2 divide 6，即2除6，这里是主动语态，也可以翻译成使用2来划分6。那么除以实际上表示的是一个被动语态，4除之以2，可以理解成以2除4。这就可以理解在我们小数数学中，为什么在之前的叫被除数，而后面的叫除数。