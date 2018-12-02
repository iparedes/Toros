import random
from scipy.stats import truncnorm

Constants={}


def randNormal(a,b):
    if b<a:
        a,b=b,a
    mu=(b-a)/2
    t=random.normalvariate(mu,mu/6)
    return int(t+a)

def rand(a,b):
    if b<a:
        a,b=b,a
    t=random.randint(a,b)
    return t

def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
        return truncnorm((low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

# def randTecnica(tecnica):
#     try:
#         desv=Constants['TecnicaSD']
#     except:
#         desv=10
#     X1 = get_truncated_normal(mean=tecnica, sd=desv, low=1, upp=100)
#     data=X1.rvs(1)
#     return data
