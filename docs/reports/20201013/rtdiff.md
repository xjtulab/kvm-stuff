## Linux实时补丁工作

### 高精度定时器

主要在硬件层面...

### 中断处理

原来的中断服务程序(interrupt service routine is processed)在中断上下文中进行，不可抢占。RT补丁强制中断线程化的配置，即每一个ISR都对应一个内核的线程，是起在线程上下文中进行，从而可以抢占。增加了local_irq_lock来保护中断资源，在非RT的情况下因为中断默认是禁止抢占的所以不需要该锁。

```c
struct local_irq_lock {
	spinlock_t		lock;
	struct task_struct	*owner;
	int			nestcnt;
	unsigned long		flags;
};
```



### rt-mutex

修改所有的mutex类型变量为rt-mutex的类型。

```c
struct mutex {
	struct rt_mutex		lock;
#ifdef CONFIG_DEBUG_LOCK_ALLOC
	struct lockdep_map	dep_map;
#endif
```

rt-mutex为新增加的一种变量类型。实现了优先级继承来避免优先级反转的问题。具体实现比较复杂。






### 更改自旋锁操作
RT补丁修改了大部分的内核中的自旋锁(spinlock)为普通的互斥量(rt_mutex)。对于自旋锁当线程锁住时，其他线程如果尝试获取锁，会一直处于忙等待状态。儿对于rt_mutex,线程如果不能获取锁则会挂起等待被释放。对于不能修改的spinlock保持原样。



### 调度策略
1. SCHED_OTEHR: 每一个任务都有一个nice值，-20~19。每个任务的平均执行时间取决于它的nice值
2. SCHED_FIFO: 每个任务都有一个优先级1~99。一个任务会执行直到完成或者被高优先级的抢占。
3. SCHED_RR: 继承自SCHED_FIFO，相当于带时间片轮转的FIFO。
...
实时补丁会修改内核任务的调度策略，使其变为可以抢占的。



### 参考资料
1. [linux-rt wiki](https://wiki.linuxfoundation.org/realtime/documentation/technical_basics/start)






