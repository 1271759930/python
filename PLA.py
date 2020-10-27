import numpy as np
import random
import matplotlib.pyplot as plt

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
            yt0 = np.sign(x[i] @ wt.T)
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
    x, y, w = ply(2, 10000)
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
    tiaojiao = 0.1
    plt.plot([w[1]*tiaojiao, w[1]*(-1)*tiaojiao], [-1*tiaojiao*w[0], tiaojiao*w[0]], linewidth="2")

    plt.show()