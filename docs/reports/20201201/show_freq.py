import numpy as np
import matplotlib.pyplot as plt
import sys

# run 的方法
#  python show_freq.py [fname] label
#  fname 是要画图的数据文件名， label是保存的标签(如果gp-gp)
# example:
#  python show_freq.py ans.txt gp-gp

fname = "./kvm/ans2.txt"


def show(fname, prefix):
    #提取文件
    frequency=[]
    with open(fname, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            #跳过注释
            if line[0].startswith("#"):
                continue
            line = list(line.strip().split())
            if len(line)==0:
                continue
            #print("line[0]={}. line[1]={}".format(line[0], line[1]))        
            frequency.append(int(line[1]))
            #break
    
    #print(frequency)



    #开始画图 x是不同的latency y是对应的频数
    print(max(frequency))
    xlen = len(frequency)
    xvalues = list(range(0,xlen))
    xvalues = list(filter(lambda x: frequency[x]>0, xvalues))
    yvalues = list(filter(lambda x: x>0, frequency))


    title = "({}){}".format(prefix, "The The frequency of latency")
    plt.title(title)
    plt.xlabel("latency")
    plt.ylabel("count")
    plt.plot(xvalues, yvalues ,c="red")
    #plt.scatter(xvalues, yvalues ,c="red", s=10)

    #标出最大的late和最小的latency
    xmin = xvalues[0]
    xmax = xvalues[len(xvalues)-1]

    xlen = len(xvalues)
    ylen = len(yvalues)
    plt.annotate("Min", (xvalues[0], yvalues[0]), xycoords='data',
        arrowprops=dict(arrowstyle='->'))
    plt.annotate("Max", (xvalues[xlen-1], yvalues[ylen-1]), xycoords='data',
        arrowprops=dict(arrowstyle='->'))

    max_latenct_index = yvalues.index(max(yvalues))

    plt.scatter(xvalues[max_latenct_index],0, c="blue",marker="o")
    plt.annotate("{}us".format(xvalues[max_latenct_index]), (xvalues[max_latenct_index], 0), xycoords='data',
        arrowprops=dict(arrowstyle='->'))
    
    plt.savefig("{}.png".format(prefix),dpi=600,format="png")
    plt.show()

    print("The most frequency lactency is {}. It appeared {} times".format(xvalues[max_latenct_index], yvalues[max_latenct_index]))


if __name__ == "__main__":
    fname = sys.argv[1]
    prefix = sys.argv[2]
    show(fname, prefix)