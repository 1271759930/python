import numpy as np
import random
import matplotlib.pyplot as plt

def pocket(d, n, rate):
    #生成样本
    random.seed(100)
    x = []
    for i in range(n):
        t = []
        for j in range(d):
            t.append(random.random()-0.5)
        x.append(t)

    Wf = np.array([(random.random()-0.5) for i in range(d)])
    x = np.array(x)
    y = np.sign(x @ Wf)
    #构造噪声,1%
    for i in range(n//10):
         y[i] *= -1

    wt = np.array([random.random()-0.5 for i in range(d)])
    yt0 = []
    while True:
        #将判断错误的点加入集合
        n_x = []
        #y加入的是点的序号
        n_y = []
        n0, n1 = 0, 0

        for i in range(len(x)):
            yt0 = np.sign(x[i] @ wt)
            if yt0 != y[i]:
                n_x.append( x[i] )
                n_y.append( i )
                if yt0 == 1:
                    n1 += 1
                else:
                    n0 += 1

        if  len(n_x) < (1 - rate) * n:
            break
        #选取错误少的一边：0或者1
        if n1 > n0:
            for i in range(len(n_y)):
                if y[n_y[i]] == -1:
                    wt = wt + n_x[i] * y[n_y[i]]
        else:
            for i in range(len(n_y)):
                if y[n_y[i]] == 1:
                    wt = wt + n_x[i] * y[n_y[i]]


        print(len(n_x)/n)

    return x, y, wt


def ply(d, n):
    #生成样本
    random.seed(100)
    x = []
    for i in range(n):
        t = []
        for j in range(d):
            t.append(random.random()-0.5)
        x.append(t)

    Wf = np.array([(random.random()-0.5) for i in range(d)])
    x = np.array(x)
    y = np.sign(x @ Wf)
    #print(x, y)

    wt = np.array([random.random()-0.5 for i in range(d)])
    yt0 = 0
    while True:
        n_x = []
        for i in range(len(x)):
            yt0 = np.sign(x[i] @ wt)
            if yt0 != y[i]:
                n_x = x[i]
                yt0 = y[i]
                break
        if  len(n_x) == 0:
            break
        wt = wt + n_x * yt0

    #print(wt, Wf)
    return x, y, wt


if __name__ == '__main__':
    x, y, w = pocket(2, 10000, 0.85)
    print(w)


    node_x = x.transpose()[0]
    node_y = x.transpose()[1]
    x1, y1 = [], []
    x2, y2 = [], []
    for i in range(len(y)):
        if y[i] == 1:
            x1.append(node_x[i])
            y1.append(node_y[i])
        else:
            x2.append(node_x[i])
            y2.append(node_y[i])

    color1 = "#00CED1"
    color2 = "#DC143C"


    plt.scatter(x1, y1,c=color1,  s = 5)
    plt.scatter(x2, y2,c=color2,  s = 5)
    #绘制直线
    plt.plot([w[1]*3, w[1]*-3], [-3*w[0], 3*w[0]], linewidth="2")

    plt.show()