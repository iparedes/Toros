
import tools
import Mundo

def main():

    # import numpy as np
    # shape, scale = 1., 1.  # mean=4, std=2*sqrt(2)
    # s = np.random.gamma(shape, scale, 1000)
    # import matplotlib.pyplot as plt
    # import scipy.special as sps
    # count, bins, ignored = plt.hist(s, 50, density=True)
    # y = bins**(shape-1)*(np.exp(-bins/scale) / (sps.gamma(shape)*scale**shape))
    # plt.plot(bins, y, linewidth=2, color='r')
    # plt.show()

    # import numpy as np
    # mu, sigma = 50, 0.1 # mean and standard deviation
    # s = np.random.normal(mu, sigma, 1000)
    #
    # import matplotlib.pyplot as plt
    # count, bins, ignored = plt.hist(s, 30, density=True)
    # plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
    # plt.show()

    # from scipy.stats import truncnorm
    # import matplotlib.pyplot as plt
    # import numpy as np
    #
    # def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    #     return truncnorm((low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)
    #
    # mu, sigma = 50, 0.1 # mean and standard deviation
    # X1 = get_truncated_normal(mean=100, sd=25, low=1, upp=100)
    # # X = np.random.normal(mu, sigma, 1000)
    # # count, bins, ignored = plt.hist(X1, 30, density=True)
    # # plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
    # # plt.show()
    #
    # X2 = get_truncated_normal(mean=5.5, sd=1, low=1, upp=10)
    # X3 = get_truncated_normal(mean=8, sd=1, low=1, upp=10)
    #
    # fig, ax = plt.subplots(3, sharex=True)
    # data=X1.rvs(1000)
    # ax[0].hist(data, normed=True)
    # # ax[1].hist(X2.rvs(10000), normed=True)
    # # ax[2].hist(X3.rvs(10000), normed=True)
    # plt.show()

    # import matplotlib.pyplot as plt
    # D=tools.get_truncated_normal(0.5,0.25,0,1)
    # v=D.rvs(10000)
    # plt.hist(v,bins=100)
    # plt.show()


    W=Mundo.Mundo()


    # for j in range(0,100):
    #     min=200
    #     max=100
    #     for i in range(0,100000):
    #         a=Tools.rand(100,200)
    #         if a<min:
    #             min=a
    #         if a>max:
    #             max=a
    #         print(a)
    #     print("min:%d max:%d"%(min,max))



if __name__ == "__main__":
    main()
