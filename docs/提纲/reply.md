华为的回复：
1、RT VM上面需要跑哪些RT  OS ？
Re: 我们希望原理上RT-VM能支持通用的RTOS，包括QNX、vxworks、Preempt_RT Linux（含完全抢占补丁的Linux）等，本次技术合作可以先基于Preempt_RT Linux作为guestOS验证；

2、RT-Linux的补丁总是滞后于GP-linxu的发展，对RT-Linux的版本有什么要求?
Re： X86我们希望基于CentOS 8/RHEL 8/SLES RT 15 （Linux 4.18内核版本）, ARM64我们采用Linux 4.19的内核版本；

3、用于部署测试的guestOS的有什么具体要求(类型，版本号)？用于测试的benchmark程序有哪些？可否提供？
Re：同上，GuestOS可以选用CentOS 8/RHEL 8/SLES RT 15等的RT版本验证。
对于NRT guestOS，可以以社区openEuler(1.0-LTS)/CentOS 8、商业的RHEL 8、SLES 15等标准版作为验证的guestOS。
bencharmk对于NRT VM的吞吐测试，以常用的磁盘、网络io benchmark工具来进行验证。（磁盘IO：sysbench和fio，网络IO：netperf）
对于RT VM的实时确定性以开源的rt-tests工程下的cyclictest作为主要的测试工具。
以上这些工具都是开源可获得的。