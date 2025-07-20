from scipy.stats import poisson

guests_threshold = 7 # укажите лимит посетителей
lmbd = 5 # укажите или рассчитайте параметр лямбда

# выведите на экран получившуюся вероятность
print(1 - poisson.cdf(guests_threshold, lmbd))