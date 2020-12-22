import numpy as np 
import matplotlib.pyplot as plt

fname1 = "results/gp-rt/log4.txt"
fname2 = "results/gp-rt/log5.txt"

fname3 = "results/gp-rt/log8.txt"
fname4 = "results/gp-rt/log9.txt"
fname5 = "results/gp-rt/log10.txt"

#origins = [474,242,232,258,231,187,363,294,521,242]

def get_max_list(fname):
    res = []
    with open(fname,"r") as f:
        for line in f.readlines():
            lst = list(line.strip().split())
            if(len(lst) == 0):
                continue

            res.append(int(lst[len(lst)-1]))
    
    return res

def plot_all():
    rr_normal   = get_max_list(fname1)
    rr_mlockall = get_max_list(fname2)
    fifo_normal = get_max_list(fname3)
    fifo_mlockall = get_max_list(fname4)
    origins = get_max_list(fname5)
    #start plot
    xvalues = list(range(1,len(rr_normal) + 1))
    '''
    plt.scatter(xvalues, rr_normal, label="sched-rr-normal",c="red")
    plt.scatter(xvalues, rr_mlockall, label="sched-rr-mlockall",c="aquamarine")
    plt.scatter(xvalues, fifo_normal, label="sched-fifo-normal",c="blue")
    plt.scatter(xvalues, fifo_mlockall, label="sched-fifo-mlockall",c="brown")
    '''
    plt.plot(xvalues, rr_normal, label="sched-rr-normal",c="red",marker="o")
    plt.plot(xvalues, rr_mlockall, label="sched-rr-mlockall",c="green", marker="+")
    plt.plot(xvalues, fifo_normal, label="sched-fifo-normal",c="blue", marker="*")
    plt.plot(xvalues, fifo_mlockall, label="sched-fifo-mlockall",c="brown", marker="p")
    plt.plot(xvalues, origins, label="origin-result",c="black", marker=".")

    plt.legend()
    plt.show()
    



if __name__ == "__main__":
    plot_all()