## 实时操作系统(Linux)抢占模型

- GP-Linux: 任务在用户态可以抢占，但是在内核态不可抢占。

- RT-Linux: 任务在用户态和内核态都可以抢占。

  注：　在RT-Linux下，所有的内核代码段几乎都是可抢占的，处理少数临界区的资源。包括中断处理程序。



## RT-OS 的中断处理

在GP-Linux的情况下，中断处理流程可以看做：
```flow
st=>start: 接受到中断信号
op1=>operation: cli指令关闭中断
op2=>operation: 调用中断处理程序(handler)
op3=>operation: sti 指令开启中断()
e=>end: 中断处理结束
st->op1->op2
op2->op3
op3->e
&```
```



然后在RealTime的情况下，为了保证实时性，不能够真正的关闭中断。为了解决这个问题，RT-Linux的解决方式如下：

+ 引入一个全局变量 int soft_interrupt_enable;
+ 调用cli指令时，并不会关闭中断，而是会将soft_interrupt_enable清零。
+ 调用sti指令时，会生成一个模拟的软中断通知中断的pending队列可以处理中断了。
+ 中断返回的操作用一个return_from_interrupt的函数来代替原来的iret指令。

在RT-Linux的情况下，中断流程可以表示为下图：
```flow
st=>start: 接受到中断信号
op1=>operation: RT-handler收到中断信号
cond=>condition: soft_interrupt_enable==1?
op_handle_interrupt=>operation: 将中断发送到Linux真正的Interrept handler
real_handle_interrupt=>operation: 调用中断处理例程(如上图)
add_pending=>operation: 加入中断到pending队列
check_pending=>operation: 检查是否有pending的中断
whether_pending=>condition:  是否有pending的中断
has_not_pending=>operation: 调用iret指令返回中断
has_pending=>operation: 处理更高优先级的中断
e=>end: 中断处理结束

st->op1
op1->cond
cond(yes)->op_handle_interrupt
cond(no)->add_pending
op_handle_interrupt->real_handle_interrupt
real_handle_interrupt->whether_pending
whether_pending(yes)->has_pending->op1
whether_pending(no)->has_not_pending
has_not_pending->e
e->e
&```
```



简单来说实时操作系统采取了一些措施保证中断是可以抢占的。具体流程解释参考：

[Real-Time Linux](https://users.soe.ucsc.edu/~sbrandt/courses/Winter00/290S/rtlinux.pdf)



## 虚拟机中断相关

//todo 