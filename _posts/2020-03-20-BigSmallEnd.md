---
title: 大端法和小端法
keywords: BigSmallEnd
date: 2020-03-20 23:05:54
tags: 计算机系统
excerpt: 本篇文章简单地介绍了大端法和小端法，并给出了演示程序。大端小端法依赖于具体的系统，不同的系统上会有不同的表现。
---

区别大端法和小端法的方式就是关注最高有效字节（也可以关注最低有效字节）。最高有效字节在低地址的存储方式称为大端法，最高有效字节在高地址的方式称为小端法。比如十六进制数字：0x01234567。那么我们首先要确定01是最高有效字节（十六进制数一个数字占4位，因此一个字节可以转换成两个十六进制数），67是最低有效字节。根据之前的介绍，如果系统是按大端法存储的话，那么大端法的输出应该是：01 23 45 67。小端法的输出应该是：67 45 23 01。下面是一段演示代码：
```c
#include<stdio.h>
typedef unsigned char *byte_pointer;

void show_bytes(byte_pointer start, size_t len)
{
	size_t i;
	for(i = 0;i<len;i++)
	{
		printf(" %.2x",start[i]);
	}
	printf("\n");
}

void test_show_bytes(int val)
{
	int ival = val;
	float fval = (float)ival;
	int *pval = &ival;
	show_int(ival);
	show_float(fval);
	show_pionter(pval);
}

int main()
{
	int val = 0x87654321;
	byte_pointer valp=(byte_pointer) &val;
	show_bytes(valp,1);
	show_bytes(valp,2);
	show_bytes(valp,3);
	return 0;
}

```
