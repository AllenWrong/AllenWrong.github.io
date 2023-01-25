## kernel.hh

#### 进程状态常量

- `P_FREE`：标识进程已经释放
- `P_RUNNABLE`：标识正在运行的进程
- `P_BLOCKED`：标识阻塞的进程
- `P_BROKEN`：标识出错的进程

#### 进程相关常量

- `NPROC`：16，表示允许的最大的进程的个数

#### 内存常量

- `KERNEL_START_ADDR`: 0x40000。内核内存起始地址。
- `KERNEL_STACK_TOP`: 0x80000。内核栈顶地址。内核的栈不能超过这个地址。
- `PROC_START_ADDR`: 0x100000。应用程序起始地址。
- `MEMSIZE_PHYSICAL`: 0x200000。物理内存大小
- `NPAGES`: `(MEMSIZE_PHYSICAL / PAGESIZE)`。物理内存页数。
- `MEMSIZE_VIRTUAL`: 0x300000。虚拟内存大小

#### struct proc

进程描述符类型。具有以下四个成员：

- `x86_64_pagetable* pagetable`: 进程运行所需要的页表。
- `pid_t pid`: 进程号。
- `int state`: 进程的状态。值为四个进程状态常量。
- `regstate regs`: 当前进程的寄存器值。

#### struct pageinfo

内存页信息内容。有一个成员：

- `uint8_t refcount`: 表示使用当前页的进程个数。

有一个函数：

- `bool used() const`: 返回true表示当前页正被使用，否则表示未被使用。

## kernel.cc

#### 常量

- `PROC_SIZE`：0x40000。表示运行一个进程所分配的内存空间的大小。
- `HZ`：100. 计时器中断频率。
- 