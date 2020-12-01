import numpy as np
import matplotlib.pyplot as plt

gp_gp = [717,399,448,226,158,238,333,205,334,131]
gp_rt = [474,242,232,258,231,187,363,294,521,242]
rt_gp = [95,86,115,84,222,107,385,256,243,136]
rt_rt = [277,205,232,232,211,148,259,158,275,202]


xlabel = list(range(1,11))

plt.title("Four test case for cyclictest")
plt.xlabel("x-value")
plt.ylabel("y-label")


plt.scatter(xlabel, gp_gp, label="gp-gp",c="red",marker="o")
plt.scatter(xlabel, gp_rt, label="gp-rt",c="aquamarine",marker="o")
plt.scatter(xlabel, rt_gp, label="rt-gp",c="blue",marker="o")
plt.scatter(xlabel, rt_rt, label="rt-rt",c="brown",marker="o")

plt.legend()
plt.show()
