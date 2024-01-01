---
title: 链表的一些常用操作
keywords: 链表
date: 2021-02-20 11:44:59
tags: 算法
excerpt: 本文记录了刷LeetCode过程中遇到的一些常用的链表操作技巧，这些技巧由程序片段表示的，熟练掌握这些技巧可以提高对链表的操作水平。
---

* 目录
{:toc}

## 链表结构定义
以下的操作都是基于这种结构的。
```java
// Definition for singly-linked list.
public class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) {
        this.val = val; this.next = next;
    }
}
```

## 求链表长度
```java
// ListNode root表示链表的第一个结点
ListNode p = root;
int length = 0;
while (p != null) {
    p = p.next;
    length++;
}
```

## 逆置链表
逆置操作是使用非常多的操作，下面是头插法逆置链表的操作。必须熟练掌握
```java
public ListNode reverseList(ListNode head) {
    ListNode newHead = new ListNode();
    while (head != null) {
        ListNode next = head.next;
        head.next = newHead.next;
        newHead.next = head;
        head = next;
    }
    return newHead.next;
}
```

## 判断两个链表是否相等
**1. 要求值相等并且长度相等。这是最常见的方法**
```java
public boolean isEqual(ListNode l1, ListNode l2) {
    while (l1 != null && l2 != null) {
        if (l1.val != l2.val) {
            return false;
        }
    }

    return l1 == l2;
}
```

**2. 要求值相等，但是两个链表的长度相差为1。这个判断方法在判断链表是否是回文链表时会用到**
```java
public boolean isEqual(ListNode l1, ListNode l2) {
    while (l1 != null && l2 != null) {
        if (l1.val != l2.val) {
            return false;
        }
    }

    return true;
}
```
可以看出，两者只有最后返回语句的差别。

## 找链表的中间节点
**当链表的个数为偶数个时，将中间两个元素中索引较大的那一个认为是中间元素，比如1-2-3-4，将3所在节点认为是中间节点。**
```java
public ListNode findMidNode(ListNode head) {
    if (head == null || head.next == null) {
        return head;
    }

    ListNode slow = head;
    ListNode fast = head.next;

    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }
}
```