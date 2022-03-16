---
layout: post
title: JavaAdMulThread
author: Guanguan
keywords: JavaAdMulThread
date: 2020-02-28 18:38:09
mathjax: false
tags: Java多线程
excerpt: 本篇博客主要是关于Java多线程的学习总结，并附有示例程序。比较广泛的记录了Java多线程的内容，并没有过多地涉及细节。
---

## 多线程和并发编程

>参考书：<a href="https://book.douban.com/subject/10484692/">Java并发编程实战</a>
>
>项目：

主要内容：

- 进程和线程的区别
- 创建线程的方式
- 线程间信息共享导致的问题。导致这种问题的原因主要有哪两个，它们对应的解决方法是什么
- 线程的状态有哪些，它们之间是如何变换的
- 线程状态变换的模型
- 线程死锁的原因
- 两个主要的并发框架
- 并发数据结构的特点
- 线程协作的几种方式
- 定时任务的实现
- 经典的多线程模型

### 1、多进程和多线程？

我们目前的操作系统都是多任务操作系统。那么这么说来，每个独立执行的任务就是一个进程。每个进程独立占有资源。操作系统将时间划分为多个时间片。在每个时间片内，操作系统将CPU分配给某一个任务，时间片结束后，CPU将自动回收，然后再分配给另外的任务。由于时间片非常小，所以我们感觉不出来它的变换，在我们看了计算机上的程序都是并行进行的。就行看电影，实际上它是一帧一帧的图片，而在我们看来它却是连续的。在单核CPU上只有串行，不可能实现并行。而多核CPU上多个任务可以实现并行，然而这也不是真正的并行。

由于CPU的频率提高会带来一系列的问题。所以通过提高频率来提高性能的方法已经不可行。通过提高CPU的核数来提高性能是最佳的选择。当CPU有多核时，我们可以将不同的进程分到不同的内核上，实现进程间的并行。比如4核CPU来运行4个进程，只需要一次就可以执行完，而单核CPU运行4个进程需要进行4次。

多进程使得计算机可以同时运行多个任务，每个任务占有时间片结束后，就会进行进程的切换。进程是比较庞大的，在这种庞大的物体间进行切换时非常费力费时的。因此就有一种更小的切换--在线程间进行切换，线程是比进程更小的单位，每个进程可以被划分为多个线程。线程与线程之间共享资源。

### 2、创建线程的两种方式

- 继承`Thread`类，实现`run`方法。

- 实现`Runnable`接口。

Java有四大接口`Clonable`，`comparable`，`serializable`，`Runnable`。

多线程的启动：

- 只能同`start()`方法进行启动，若直接调用`run()`方法程序就会变成串行执行。

- 同一个线程只能进行一次`start`。

- 实现`Runnable`接口时，在进行线程启动的时候需要用`Thread`类进行包装。

- 多个线程启动时，其先后顺序是随机的。
- 线程不需要关闭，在`run()`方法执行结束后，自动关闭线程。
- `main()`函数可能早于子线程结束。但整个程序并不终止。

**实现方式的比较：**

- 继承`Thread`会占有父类的名额，也就是该类就无法继承别的类了。所以不如`Runnable`方便。
- `Runnable`启动时需要被包装成`Thread`。但是在实现`Runnable`的对象中通过普通变量尽可以实现变量共享，而在继承`Thread`的对象中，需要使用关键字`Static`。所以`Runnable`容易实现多线程的资源共享。
- 建议通过实现`Runnable`接口来完成多线程。

### 3、线程间的信息共享

**信息共享的方式。信息共享导致了数据不一致。针对不同的共享方式有不同的解决方案。**

通过继承`Thread`类来实现的线程类需要通过static关键字进行共享。而通过实现`Runnable`接口实现的线程类通过普通的变量就可以实现共享，而这种机制主要是因为实现`Runnable`接口的类只被实例化了一次，然后该对象会被包装四次形成4个线程对象。

如果只是简单的这么进行变量共享的话，直接导致的问题就是数据不一致。这主要是由于以下两个原因造成的：

- 每个线程在对内存区的变量进行操作的时候，并不是直接进行操作，而是会拷贝一个工作缓存副本，对这个副本进行操作。那么显然这个副本在进程之间是不可见的。
- 关键步骤缺乏加锁限制。也就是说可能会存在这样的情景，多个线程同时对同一个变量进行操作。举个例子：i++。这样的操作是由4步来实现的。首先线程会将变量`i`从内存区拷贝到自己的工作缓存，然后CPU对工作缓存中的变量`i`执行加一操作，而后CPU将计算结果保存在工作缓存中，然后线程将工作缓存中的值存储到原来的内存区中。

#### volatile关键字解决工作副本的可见性

由前面的分析可以知道。导致不一致的一个原因就是工作副本不可见。那么可以使用`volatile`关键字将工作副本变成可见的。	

```java
public class ThreadDemo2 {
	public static void main(String args[]) throws Exception {
		TestThread2 t = new TestThread2();
		t.start();
		Thread.sleep(2000);
		t.flag = false;
		System.out.println("main thread is exiting");
	}
}

class TestThread2 extends Thread {
	 boolean flag = true; //子线程不会停止
//	 volatile boolean flag = true; // 用volatile修饰的变量可以及时在各线程里面通知

	public void run() {
		int i = 0;
		while (flag) {
			i++;
		}
		System.out.println("test thread3 is exiting");
	}
}
```

在上面的代码中，如果`flag`不加`volatile`，那么在`main`线程结束的时候，子线程并不会结束。这是因为`flag`是不可见的。在内存中的`flag`发生了变化，但是线程只会使用工作副本中的`flag`。如果使用了`volatile`关键字，那么线程工作副本中的`flag`就会随着内存中的变化而变化。但是下面有一个特殊的情况，我也未搞清楚原因：

```java
package com.socket.demo;

public class Demo{
	public static void main(String[] args) throws InterruptedException {
		InnerClass innerClass = new InnerClass();
		innerClass.start();
		Thread.sleep(2000);
		innerClass.flag = false;
		System.out.println("main thread exit...");
	}
}
class InnerClass extends Thread{
	boolean flag = true;
//	volatile boolean flag = true;
	public void run() {
		int i = 0;
		while(flag) {
			i++;
			System.out.println(i);
		}
	}
}
```

#### 关键步骤加锁限制

给关键步骤加锁来保持同步。

```java
public class Test {
	public static void main(String[] args) {
		ThreadDemo threadDemo = new ThreadDemo();
		new Thread(threadDemo).start();;
		new Thread(threadDemo).start();;
		new Thread(threadDemo).start();;
		new Thread(threadDemo).start();;
	}
}

class ThreadDemo implements Runnable{
	int ticket = 100;
	// 加锁对象
	String string = "";
	
	@Override
	public void run() {
		while(true) {
			// 给代码块加锁
			synchronized (string) {
				sale();
			}
			try {
				Thread.sleep(100);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			if(ticket<=0) {
				break;
			}
		}
	}
	
	// 直接给函数加锁。两种方式使用一个即可
	private synchronized void sale() {
		System.out.println(Thread.currentThread()+" saled ticket "+ticket--);
	}
}
```

### 4、Java多线程状态管理

进状态管理的目的是为了实现线程之间的同步协作，进而完成一些复杂的任务。

#### 线程的状态

- 刚创建：
- 就绪：
- 运行：
- 阻塞：
- 结束：线程运行完毕，进入结束状态。这意味着线程声明周期的结束。

这几种状态之间的转化是我们所关心的。进程之间的协作，主要就是进程状态的变化。创建状态可以通过`start`进入就绪状态，也可能立刻就获得了CPU进入运行态。就绪态获得CPU后就进入到了运行态。运行态失去CPU后就进入到了就绪态。就绪态和运行态之间的变化主要就是CPU的有无，而不涉及其他资源的变化。如果有其他资源的变化那么就会进入到阻塞态。线程也可以在就绪态、运行态或阻塞态直接进入结束。

#### API

Thead部分已经被废弃的API：

- 暂停：`suspend`
- 恢复：`resume`
- 销毁：`stop`/`destroy`

常用API：

- sleep：休眠特定时间
- wait：进入等待
- notify：唤醒指定线程
- notifyAll：唤醒所有线程
- join：等待另外一个线程结束
- interrupt：向另外一个线程发送中断信号。线程收到中断信号后最对应的处理

**生者消费者模型：**

先描述下这个模型，然后对这个模型进行抽象，从而设计出类。

有一个指定大小的产品仓库，用来存储产品。生产者负责生产产品，消费者会消费仓库中的产品。设计程序模拟这个过程。

【抽象】：

初步可以抽象出产品仓库，产品，生产者，消费者。四个对象。产品仓库可以用一个数组来实现，而大小我们可以可以设置为10。产品比较容易设计，比如它可以有产品ID和产品名。生产者是一个线程，它需要做的工作是生产产品，然后判断仓库是否已满，如果已满就会等待。如果还不满，那么就会进行生产。消费者也是一个线程，它需要消费产品，然后判断仓库是否为空。不为空的话，则进行消费。

```java
public class Main {
	public static void main(String[] args) {
		Base base = new Base();
		Consumer consumer = new Consumer(base);
		Producer producer = new Producer(base);
		
		// 通过修改消费者和生产者的数量来观察结果变化
		new Thread(consumer).start();
		new Thread(consumer).start();
		new Thread(producer).start();
		new Thread(producer).start();
		new Thread(producer).start();
		new Thread(producer).start();
		new Thread(producer).start();
		new Thread(producer).start();
	}
}
/*****************************************************************************************/
public class Base {
	private Product[] base;
	private int top;
	
	public Base() {
		this.base = new Product[10];
		this.top = 0;
	}

	public Product[] getBase() {
		return base;
	}

	public int getTop() {
		return top;
	}
	
	public synchronized void add(Product product) {
		if(this.top == 10) {
			try {
				wait();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			System.out.println("Producer waiting...");
		}else {
			base[top++] = product;
			System.out.println(Thread.currentThread().getName()+" producted "+product.toString());
			notifyAll();
		}
	}
	
	public synchronized void minus() {
		if(this.top == 0) {
			try {
				wait();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			System.out.println("Consumer waiting...");
		}else {
			this.top--;
			Product product = base[top];
			System.out.println(Thread.currentThread().getName()+" consumered "+product.toString());
			notifyAll();
		}
	}
}
/*****************************************************************************************/
public class Product {
	private String ID;
	private String name;
	
	public Product(String ID, String name) {
		this.ID = ID;
		this.name = name;
	}

	public String getID() {
		return ID;
	}

	public String getName() {
		return name;
	}

	@Override
	public String toString() {
		return "Product [ID=" + ID + ", name=" + name + "]";
	}
}
/*****************************************************************************************/
import java.util.Random;

public class Producer implements Runnable{
	private Base base;
	
	public Producer(Base base) {
		this.base = base;
	}
	
	@Override
	public void run() {
		while(true) {
			Random random = new Random();
			int id = random.nextInt(300);
			String name = "pro"+id;
			this.base.add(new Product(id+"", name));
			try {
				Thread.sleep(500);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}

	public Base getBase() {
		return base;
	}
}
/*****************************************************************************************/
public class Consumer implements Runnable {
	private Base base;
	
	public Consumer(Base base) {
		this.base = base;
	}

	@Override
	public void run() {
		while(true) {
			this.base.minus();
			try {
				Thread.sleep(500);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
	
	public Base getBase() {
		return base;
	}
}
```

#### 线程的主动暂停和终止

在前面的`wait`，`notify`,`notifyAll`的方法都是依赖于别的线程，也就是一个线程的暂停和终止时被动的。然而，我们还希望一个线程能够主动的暂停和终止。这主要是通过定期检测共享变量来实现的。当需要暂停或终止的时候，他会首先释放资源，然后再做其他动作。因为资源是最重要的。

共享变量的机制在之间线程间的信息共享的时候已经介绍过了。这里的机制与之前的是一样的，就是利用`volatile`关键字。下面是演示程序：

```java
public class Demo{
	public static void main(String[] args) throws InterruptedException {
		InnerClass innerClass = new InnerClass();
		innerClass.start();
		Thread.sleep(2000);
		// 由于flag是通过volatile修饰的，所以在这里的修改可以被线程感知
		innerClass.flag = false;
		System.out.println("main thread exit...");
	}
}
class InnerClass extends Thread{
	volatile boolean flag = true;
	public void run() {
		int i = 0;
		while(flag) {
			i++;
		}
		System.out.println("exit....");
	}
}
```

### 5、线程死锁

每个线程相互持有别的线程所需要的锁。而所有的线程也都不放弃所持有的锁，这时候就进入了一种死锁的状态，典型的问题是哲学家就餐问题。解决方案是对资源进行等级排序。下面是程序演示：

```java

```

守护线程：是一种与main函数密切相关的线程。当run方法结束时，守护线程就会结束，或者在main函数结束的时候，守护线程也会结束。定义守护线程的方法是：`setDaemon(true)`。演示代码：

```java
public class Daemon {
	public static void main(String[] args) {
		DaemonDemo demo = new DaemonDemo();
		Thread thread = new Thread(demo);
		thread.setDaemon(true);
		thread.start();
		try {
			Thread.sleep(3000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}

class DaemonDemo implements Runnable{
	@Override
	public void run() {
		// 死循环，一般线程不会结束该死循环。而守护线程会结束
		while(true) {
			System.out.println("Deamon thread running...");
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
}
```

### 6、并发框架

**并行模式**

- 主从模式：只有一个主线程，其他的都是从线程。主线程指挥从线程去工作。类似于C/S结构
- Worker模式：点对点的模式。各个线程都平等。类似于P2P

**Java并发编程主要包括三个部分**

Thread/Runable/ThreadGroup，Executor，Fork-Join。

#### 线程组

线程组实际上是线程的一种集合。将线程添加到集合中进行管理。它是树形结构的。大线程组内还可以包含小线程。可以通过enumerate方法对它进行遍历。有效性得到了保证，但是管理效率非常低，因此就决定了它使用的非常少。但是它无法解决并发编程的痛点：**任务分配和执行过程高度耦合**。也无法重用线程。

#### Executor

Executor主要解决了线程的重用问题。也就是说，当我们new过一些线程后，虽然这些线程执行结束了，但是我们还可以再次使用它们。在之前的方法中，如果线程结束了，那么我们还需要继续new线程。另外Executor将任务的创建者和执行者分开了，在一定 程度上缓解了耦合问题。

线程池的理解：

- 线程池，顾名思义就像一个池子，里面装有一定数量的线程，而且线程的数量并不是固定的，是可以弹性增长的。
- 线程池中的线程可以多次执行很多很小的任务。就像停车区的共享单车可以被多个人骑行。
- 任务的创建和执行是解耦的。
- 我们无需关心线程池执行任务的过程。

理解线程池，有一个比较好的例子就是，共享单车的停车区，而里面的线程就像共享单车。

主要的类：

- `ExecutorService`：线程池服务类。对线程池的抽象。可以通过`Executors.newFixedThreadPool(num)`来创建包含固定线程数量的线程池。也可以通过`ExecutorService.newCachedThreadPool()`来创建线程数量可变的线程池。
- `Callable`：是一个接口。与`Runnable`的区别在于run方法没有返回值，而实现`Callable`需要重写的call方法有返回值
- `Future`：存储线程返回结果的类

#### Fork-join

Fork-join采用的是分治的编程模式，适用于计算量无法准确评估但任务却可以逐层分解的计算任务。下面是一个计算数组和的列子：

```java
import java.util.concurrent.RecursiveTask;

/**
 * 需要继承RecursiveTask类
 */
public class SumTask extends RecursiveTask<Long>{
	private static final long serialVersionUID = 1L;
	/** 子任务的开始索引*/
	private int start;
	/** 子任务的结束索引*/
	private int end;
	/** 最小不可分的任务所能包含的计算数量*/
	private static final int THREAD_HOLD = 5;
	
	public SumTask(int start, int end) {
		this.start = start;
		this.end = end;
	}
	
	@Override
	protected Long compute() {
		// 保存计算结果
		Long sum = 0L;
		
		// 当分割的批量任务数小于指定的阈值时，就进行计算，不再分割
		// 这相当于递归的结束条件
		boolean canCompute = (this.end-this.start) <= THREAD_HOLD;
		
		if(canCompute) {
			// 注意这里是需要小于和等于的。可以通过手算来理解
			for(int i = this.start;i<=this.end;i++) {
				sum=sum+i;
			}
		// 不满足条件，那么我们继续分割
		}else {
			// 分割
			int middle = (this.end+this.start)/2;
			SumTask task1 = new SumTask(start, middle);
			SumTask task2 = new SumTask(middle+1, end);
			
			// 执行上面分割的任务
			invokeAll(task1, task2);
			
			// 合并结果
			// Join方法：Returns the result of the computation when it is done.
			sum = task1.join()+task2.join();
		}		

		// 返回结果
		return sum;
	}
}
/*******************************************************************************************/
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.ForkJoinTask;

public class SumTest {
	public static void main(String[] args) throws InterruptedException, ExecutionException {
		// 创建线程池
		ForkJoinPool pool = new ForkJoinPool();
		
		// 创建任务。具体的任务执行细节在Compute方法中
		SumTask task = new SumTask(1, 10000000);
		
		// 提交任务
		ForkJoinTask<Long> result = pool.submit(task);
		
		do {
			// 查看线程数量和并行度，并不是必须的
			System.out.println("Main: Thread count is " + pool.getActiveThreadCount());
			System.out.println("Main: Paralelism is "+pool.getParallelism());
			try {
				Thread.sleep(50);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}while(!task.isDone());
		
		// 输出结果
		System.out.println("result: "+ result.get());
	}
}
```

### 7、并发数据结构

传统的数据结构List，Set，Map并不是线程安全的，也就是不能保证同步，再进行多线程编程时显然是不可能使用这样的数据结构的。因此就需要一些线程安全的数据结构。下面列出了常用的数据结构及其性能分析：

1. List
   - Vector：线程安全的，适用于写多读少的情况性能较差
   - ArrayList：
   - Collections.synchronizedList()：
   - CopyOnWriteArrayList：基于复制实现的。适用于读多写少的情况，非阻塞容器
2. Set
   - HashSet：
   - Collections.synchronizedSet()：基于synchronized关键字实现的同步，性能较差
   - CopyOnWriteArraySet：基于CopyOnWriteArrayList实现的数据结构。适用于读多写少的情况，非阻塞容器。
3. Map
   - Hashtable：
   - HashMap：
   - Collections.synchronizedMap()：基于synchronized关键字实现的同步，性能较差
   - ConcurrentHashMap()：适用于读多写少的情况，非阻塞容器。
4. Queue/Deque
   - ConcurrentLinkedQueue：
   - ArrayBlockingQueue/LinkedBlockingQueue：阻塞队列

可以看出上面三种数据结构的类型基本是一样的，有适用于写多读少的情况，有适用于读多写少的情况，而且后者都是非租塞容器。另外他们都基于synchronized关键字实现了同步。

关于上面的这些数据结构只有在练习中才能理解的更加深刻。只看Demo的效果并不是很好。

### 8、线程协作

在前面的内容线程与线程之间都是独立的，没有什么交互，而仅仅保持了数据的一致性。

#### a、Lock

Lock是synchronized的升级版。它也可以实现同步的效果。实现更复杂的临界区结构。性能更好，并且允许分离读写的操作。主要有两个类：

- `ReentrantLock`类，可重入的互斥锁
- `ReentrantReadWriteLock`，可重入的读写锁

主要的方法有

- `tryLock()`：尝试这加锁，如果能加锁则进行加锁，然后进行相应的处理。如果不能加锁，也就是临界资源被别人在使用，那么继续进行下面的内容。而在之前的方法中会被阻塞。
- `lock()、unlock()`：加锁和释放的方法

【案例】：有家奶茶店，点单有时需要排队。假设想买奶茶的人如果看到需要排队，就决定等待一会，然后再去查看是否可以购买奶茶。又假设奶茶店有老板和多名员工，记单方式比较原始，只有一个订单本。老板负责写新订单，员工不断地查看订单本得到信息来制作奶茶，在老板写新订单时员工不能看订单本，多个员工可同时看订单本，在员工看时老板不能写新订单。

分析：在这个案例中，顾客的到来是随机的，这与线程的随机性是相符的。这里的需要排队，并不是严格意义上的排队。如果真的需要排队的话，那么我们就得指定优先级。所以这里的场景实际上就是在一个时间段只有一个顾客购买奶茶，而其他人都是在等待，不能购买奶茶，至于下一个是谁购买奶茶也是随机的。因此，使用一个线程代表一个顾客，它的到来顺序是随机的。它具有的行为是买奶茶。在买奶茶的时候由于只能一个人购买，所以要加锁。用线程来抽象表示老板和员工，员工线程是多个的，老板只有一个。老板具有的行为是写订单，但是写订单的时候需要加上写锁，写完之后注意释放。员工具有的行为是读订单和制作奶茶，读订单的时候需要加上读锁，读完之后释放。下面是模拟程序：

```java
public class Consumer implements Runnable {
	private ReentrantLock lock;
	
	public Consumer(ReentrantLock lock) {
		this.lock = lock;
	}
	
	public void buyMilkTea() {
		System.out.println(Thread.currentThread().getName()+" is milking tea.");
		try {
			// 等待工作人员制作奶茶
			Thread.sleep(2000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		System.out.println(Thread.currentThread().getName()+" get his milk tea.");
	}
	
	@Override
	public void run() {
		boolean buyMyTea = false;
		
		// 没有买到奶茶就继续尝试和等待
		while(!buyMyTea) {
			if(this.lock.tryLock()) {
				buyMilkTea();
				buyMyTea = true;
				this.lock.unlock();
			}else {
				System.out.println(Thread.currentThread().getName()+" Waiting...");
				try {
					Thread.sleep(1000);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
		}
		
	}
}
/*******************************************************************************************/
public class Worker implements Runnable {
	private ReentrantReadWriteLock readWriteLock;
	
	public Worker(ReentrantReadWriteLock readWriteLock) {
		this.readWriteLock = readWriteLock;
	}
	
	public void viewOrder() {
		// 加锁
		readWriteLock.writeLock().lock();
		System.out.println(Thread.currentThread().getName()+" viewing order.");
		try {
			// 模拟看订单
			Thread.sleep(2000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		// 看完订订单释放锁
		readWriteLock.writeLock().unlock();
	}
	
	@Override
	public void run() {
		while(true) {
			viewOrder();
			// 模拟制作奶茶，并交付的过程。完成后继续看下一个订单
			try {
				Thread.sleep(2000);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		
	}
}
/*******************************************************************************************/
public class Boss implements Runnable{
	private ReentrantReadWriteLock readWriteLock;
	
	public Boss(ReentrantReadWriteLock readWriteLock) {
		this.readWriteLock = readWriteLock;
	}
	
	public void addOrder() {
		// 加锁
		readWriteLock.readLock().lock();
		System.out.println(Thread.currentThread().getName()+" writing order.");
		try {
			// 模拟写订单的过程
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		// 写完订单释放锁
		readWriteLock.readLock().unlock();
	}

	@Override
	public void run() {
		while(true) {
			// 老板所需要的做的只是不断的写订单。这里假设客源源不断
			addOrder();
			System.out.println(Thread.currentThread().getName()+" end writing.");
		}
	}
}
/*******************************************************************************************/
public class Demo {
	public static void main(String[] args) {
		// 10个顾客
		Thread[] consumers = new Thread[10];
		// 4个工作人员
		Thread[] workers = new Thread[4];
		
		ReentrantLock lock = new ReentrantLock();
		ReentrantReadWriteLock readWriteLock = new ReentrantReadWriteLock();
		
		for(int i = 0;i<consumers.length;i++) {
			consumers[i] = new Thread(new Consumer(lock));
			consumers[i].start();
		}
		
		Thread boss = new Thread(new Boss(readWriteLock));
		boss.start();
		
		for(int i = 0;i<workers.length;i++) {
			workers[i] = new Thread(new Worker(readWriteLock));
			workers[i].start();
		}
	}
}
```

#### b、Semaphore

信号量机制也是进行线程协作的一种方法，它的机制是可以指定允许几个线程同时访问指定的临界资源。信号量实际上就是一种计数器。

Semaphore类也提供了tryAcquire()方法。

【案例1】：停车模拟。有一个车库，里面只能停5辆车，现有10辆车需要进行停放。每次停放是去申请信号量。如果不能申请到，那么就等待一会，然后再去申请。

分析：这两主要就有一个类，Car。它具有的行为是停车和离开。停车的时候首先去获取信号量，如果能获取到那么就停车，如果不能获取到那么就等待一会再去申请。循环这个过程只能完成停车并开走。主类负责整个过程的驱动。

```java
public class StopCar {
	private static final Semaphore number = new Semaphore(5);
	
	public void parking() {
		boolean complete = false;
		
		while(!complete) {
			if(number.tryAcquire()) {
				System.out.println(Thread.currentThread().getName()+" stop car.");
				try {
					Thread.sleep(2000);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				complete = true;
			}else {
				System.out.println(Thread.currentThread().getName()+" waiting...");
				try {
					Thread.sleep(1000);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
		}
	}
	
	public void leave() {
		number.release();
		System.out.println(Thread.currentThread().getName()+" leaved.");
	}
	
	public static void main(String[] args) {
		Thread[] cars = new Thread[10];
		StopCar stopCar = new StopCar();
		
		for(int i = 0;i < 10;i++) {
			// 匿名对象的方式。比较常用
			cars[i] = new Thread(new Runnable() {
				@Override
				public void run() {
					stopCar.parking();
					stopCar.leave();
				}
			});
			cars[i].start();
		}
	}
}
```

【案例2】：哲学家就餐问题的信号量机制实现。哲学家就餐问题，这里设定有6个哲学家，6根筷子。每个哲学家只有获得到两根筷子时才能去就餐。当筷子被别的哲学家使用的时候，其他哲学家不能使用。

分析：在这里，哲学家是一个对象，将筷子抽象成信号量。哲学家所具有的行为是拿筷子，就餐和放下筷子。在拿筷子的时候需要申请信号量。就餐完毕后需要释放信号量。另外需要注意的就是。哲学家只能拿取与他相邻的两个筷子。下面是演示代码，该程序会有死锁的危险。实际上，我们可以简单地通过一个数组就可以实现信号量。

```java
public class Philosophier implements Runnable {
	// 筷子信号量。6个信号量分别作用在6根筷子上。
	public Semaphore[] chopSticks;
	public int index;
	
	@Override
	public void run() {
		while(true) {
			// 拿筷子
			if(pickLeft() && pickRight()) {
				eat();
			// 拿筷子失败，进入等待
			}else {
				System.out.println(Thread.currentThread().getName()+" waiting...");
				try {
					Thread.sleep(2000);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
		}
	}
	
	// 初始化信号量
	public Philosophier(Semaphore[] chopSticks, int index) {
		this.chopSticks = chopSticks;
		this.index = index;
	}
	
	public void eat() {
		System.out.println(Thread.currentThread().getName()+" eating.");
		// 表示哲学家就餐的过程
		try {
			Thread.sleep(2000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		System.out.println(Thread.currentThread().getName()+" end eating.");
	}
	
	/** 哲学家拿起左筷子*/
	public boolean pickLeft() {
		// 尝试申请信号量
		return this.chopSticks[index].tryAcquire();
	}
	
	/** 哲学家拿起右筷子*/
	public boolean pickRight() {
		// 尝试申请信号量
		if(index == 0) {
			return this.chopSticks[5].tryAcquire();
		}
		return this.chopSticks[index-1].tryAcquire();
	}
	
	public void putLeft(int index) {
		this.chopSticks[index].release();
	}
	
	public void putRight(int index) {
		if(index == 0) {
			this.chopSticks[5].release();
		}else {
			this.chopSticks[index-1].release();
		}
	}
}
/*******************************************************************************************/
public class Demo {
	public static void main(String[] args) {
		Semaphore[] chopSticks = new Semaphore[6];
		for(int i = 0;i<chopSticks.length;i++) {
			chopSticks[i] = new Semaphore(1);
		}
		
		Thread[] philosophiers = new Thread[6];
		for(int i = 0;i<philosophiers.length;i++) {
			philosophiers[i] = new Thread(new Philosophier(chopSticks, i));
			philosophiers[i].start();
		}
	}
}
```

#### c、Latch

Latch是一个等待锁，是一个同步辅助类，它的作用并不是保护临界资源的，而是用来进行等待的，在某个时刻，我们等待一下，等到所需要的线程都到达后，再继续往前进行。

主要的实现类是`CountDownLatch`。主要的方法有：`countDown()`计数减一，`await()`等带变成0。下面是示例代码：

```java
public class LatchDemo {
	public static void main(String[] args) {
		int studentNum = 10;
		// 开始信号
		CountDownLatch startSignal = new CountDownLatch(1);
		// 结束信号
		CountDownLatch endSignal = new CountDownLatch(studentNum);

		for(int i = 0;i<studentNum;i++) {
			new Thread(new Student(startSignal,endSignal)).start();
		}
		
		System.out.println("各就位...");
		startSignal.countDown(); // 开始信号
		try {
			// 等到所有人到达终点
			endSignal.await();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		System.out.println("比赛结束...");
		
	}
}

class Student implements Runnable{
	private final CountDownLatch startSignal;
	private final CountDownLatch doneSignal;

	public Student(CountDownLatch startSignal, CountDownLatch doneSignal) {
		this.startSignal = startSignal;
		this.doneSignal = doneSignal;
	}
	
	@Override
	public void run() {
		try {
			// 等待开始信号
			startSignal.await();
			doWork();
			// 到达终点后对信号减一
			doneSignal.countDown();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	
	public void doWork() {
		System.out.println(Thread.currentThread().getName()+" arrive at the finish...");
	}
}
```

上面的代码中，最重要的部分就是对信号的减一以及等待所有的线程到达指定的同步点（对上面的例子而言就是同步点就是重点）。

#### d、Barrier

Barrier也是一个同步辅助类。允许多个线程在某一个点上进行同步。Barrier一种典型的应用情景就是：等到所有的子线程执行完毕后，合并它们的结果。

主要的类是`CyclicBarrier`，能够指定需要同步的线程的数量（类似于前面的endSignal），也有`await()`方法。下面是一个分行计算数组的和的例子。每个线程负责计算其中的一行。

```java
public class CyclicBarrierExample {
	/**
	 * 假定有三行数，用三个线程分别计算每一行的和，最终计算总和
	 * @param args
	 */
	public static void main(String[] args) {
		final int[][] numbers = new int[3][5];
		final int[] results = new int[3];
		int[] row1 = new int[]{1, 2, 3, 4, 5};
		int[] row2 = new int[]{6, 7, 8, 9, 10};
		int[] row3 = new int[]{11, 12, 13, 14, 15};
		numbers[0] = row1;
		numbers[1] = row2;
		numbers[2] = row3;
		
		CalculateFinalResult finalResultCalculator = new CalculateFinalResult(results);
		//当有3个线程在barrier上await，就执行finalResultCalculator
		CyclicBarrier barrier = new CyclicBarrier(3, finalResultCalculator);
		
		for(int i = 0; i < 3; i++) {
			CalculateEachRow rowCalculator = new CalculateEachRow(barrier, numbers, i, results);
			new Thread(rowCalculator).start();
		}		
	}
}

class CalculateEachRow implements Runnable {
	final int[][] numbers;
	final int rowNumber;
	final int[] res;
	final CyclicBarrier barrier;	
	CalculateEachRow(CyclicBarrier barrier, int[][] numbers, int rowNumber, int[] res) {
		this.barrier = barrier;
		this.numbers = numbers;
		this.rowNumber = rowNumber;
		this.res = res;
	}
	
	@Override
	public void run() {
		int[] row = numbers[rowNumber];
		int sum = 0;
		for (int data : row) {
			sum += data;
			res[rowNumber] = sum;
		}
		try {
			System.out.println(Thread.currentThread().getName() + ": 计算第" + (rowNumber + 1) + "行结束，结果为: " + sum);
			barrier.await(); //等待！只要超过3个(Barrier的构造参数)，就放行。
		} catch (InterruptedException | BrokenBarrierException e) {
			e.printStackTrace();
		}
	}
}

class CalculateFinalResult implements Runnable {
	final int[] eachRowRes;
	int finalRes;
	public int getFinalResult() {
		return finalRes;
	}
	CalculateFinalResult(int[] eachRowRes) {
		this.eachRowRes = eachRowRes;
	}
	
	@Override
	public void run() {
		int sum = 0;
		for(int data : eachRowRes) {
			sum += data;
		}
		finalRes = sum;
		System.out.println("最终结果为: " + finalRes);
	}
}
```

#### e、Phaser

Phaser。同步辅助类，应用场景和Barrier的场景基本类似，不同的是Phaser可以被多次应用。Barrier只能等待一次，Phaser可以等待多次。

主要的方法是：`arriveAndAwaitAdvance()、arrive()`。下面是一个例子：假设举行考试，总共三道大题，每次下发一道题目，等所有学生完成后再进行下一道。这里主要用来演示Phaser的多次等待效果。这里需要注意的地方就是`Phaser phaser = new Phaser(studentNum);`

```java
public class Demo {
	public static void main(String[] args) {
		int studentNum = 5;
		// note
		Phaser phaser = new Phaser(studentNum);
		for(int i = 0; i<studentNum;i++) {
			new Thread(new Student(phaser)).start();
		}
	}
}

class Student implements Runnable{
	private Phaser phaser;
	
	public Student(Phaser phaser) {
		this.phaser = phaser;
	}
	
	@Override
	public void run() {
		doTest(1);
		// note
		phaser.arriveAndAwaitAdvance();
		doTest(2);
		phaser.arriveAndAwaitAdvance();
		doTest(3);
		phaser.arriveAndAwaitAdvance();
		System.out.println("All done.");
	}
	
	public void doTest(int i) {
		System.out.println(Thread.currentThread().getName()+" doing the "+i+" problem...");
		try {
			Thread.sleep(2000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		System.out.println(Thread.currentThread().getName()+" end the "+i+" problem.");
	}
}
```

#### f、Exchanger

Exchanger。是一个用于交换消息的类。允许并发线程中互相交换消息。它会在某个时刻等待另一个线程的到来，当另一个线程来到这一个时刻的时候（也就是达到了同步，这个时刻称为同步点），它们就相互交换信息，这个交换是双向的，而且只能在两个线程之间进行信息的交换。

主要的类是Exchanger。主要的方法是`exchange()`。下面是一个成绩查询的例子。

```java
public class GradeSelect {
	public static void main(String[] args) {
		// 定义一个exchanger
        Exchanger<String> exchanger = new Exchanger<>();
		new Thread(new Base(exchanger)).start();
		
		Scanner scanner = new Scanner(System.in);
		String input = "";
		while(!input.equals("q")) {
			System.out.print(">> ");
			input = scanner.nextLine();
			try {
				exchanger.exchange(input);
				System.out.println(input+" grade is "+exchanger.exchange(null));
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		scanner.close();
	}
}

class Base implements Runnable{
	private Exchanger<String> exchanger;
	
	public Base(Exchanger<String> exchanger) {
		this.exchanger = exchanger;
	}
	
	@Override
	public void run() {
		boolean exit = false;
		while(!exit) {
			try {
				String msg = exchanger.exchange(null);
				switch (msg) {
				case "zhangsan":
					exchanger.exchange("70");
					break;
				case "lisi":
					exchanger.exchange("80");
					break;
				case "wangwu":
					exchanger.exchange("90");
					break;
				case "q":
					exit = true;
					// 如果不返回的话会阻塞main线程
					exchanger.exchange("");
					break;
				default:
					break;
				}
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
}
```

### 9、定时任务

在实际编程中，我们有时会希望在某个时间点执行某个任务，或者以某个周期执行某个任务。比如我之前做的一个管理系统，我们希望在数据库启动之后每隔10分钟备份一次，这是模拟的一个简单的数据库的备份功能。在Java中提供了Timer类，它是一个定时器，还有TimerTask类，它是用来封装任务的。下面依然做一个模拟数据库备份的例子。

```java
public class BackUp {
	public static void main(String[] args) {
		Timer timer = new Timer();
		DataBase dataBase = new DataBase();
		// 每5秒执行一次备份。在启动之后会先等待1秒，然后再进行执行
		// 实际上只有3秒的间隔，因为数据库备份时sleep了2秒
		timer.scheduleAtFixedRate(dataBase, 1000, 5000);
	}
}

class DataBase extends TimerTask{
	@Override
	public void run() {
		System.out.println("Database start backuping...");
		try {
			Thread.sleep(2000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		System.out.println("DataBase end backup.");
	}
}
```

在之前的这种方法中，我们只能并发的执行一个任务，当我们有多个任务的时候，我们期望并发地执行多个任务。这种需求可以通过Executor+定时器机制来实现。主要的类就是`ScheduleExecutorService`。

那么我们可以将上面的场景进行一下扩展，假设我们有多个数据库，需要在固定的时间对它们进行备份。下面是模拟程序。

```java
public class GroupBackUp {
	public static void main(String[] args) {
		// 这里我们有5个数据库
		ScheduledExecutorService scheduledExecutorService = Executors.newScheduledThreadPool(5);
		for(int i = 0;i<5;i++) {
			DataBases dataBases = new DataBases();
			// 任务是dataBases,一开始推迟2秒，备份时间间隔为7秒，实际上是两秒。时间单位是Seconds
			scheduledExecutorService.scheduleWithFixedDelay(dataBases, 2, 7, TimeUnit.SECONDS);
		}
	}
}

class DataBases implements Runnable{
	@Override
	public void run() {
		doBackUp();
	}
	
	public void doBackUp() {
		System.out.println(Thread.currentThread().getName()+"-DataBase is backing up...");
		try {
			Thread.sleep(2000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		System.out.println(Thread.currentThread().getName()+"-DataBae end back up.");
	}
}
```

**第三方库Quartz**

Quartz是一个较为完善的任务调度框架。解决程度中Timer零散管理的问题。