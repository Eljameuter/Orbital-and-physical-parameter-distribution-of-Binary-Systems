"""
Class Binary Star Generator
Input: probability distribution (joint or single), number of binary stars to be generated
Output: dataframe with Binary star population

distributions I want to try
f(e) = 1 (uniform)
f(e) = 2e (thermal distribution)

Mind you P's and Q's:
P (3-10 days)
circulized e = 0
logP = 1.5-5 (intermediate, solar type)
η ≈ 0.4
lgoP = 1.5-4.5
η ≈ 0.8 (similar to thermal, early type)



"""
import imf
import numpy as np
from matplotlib import pyplot as plt


class BinaryStarGenerator:
    def __init__(self):
        x=1

    def generate_single(self, pdf_vals, limit, number):
        dx = limit / len(pdf_vals)

        # build proper CDF
        cdf = np.cumsum(pdf_vals) * dx
        cdf /= cdf[-1]

        def get_sample():
            u = np.random.uniform(0, 1)
            return np.searchsorted(cdf, u)

        samples = []

        for _ in range(number):
            idx = get_sample()
            e = idx * dx
            samples.append(e)

        plt.hist(samples, bins=50)
        plt.show()

        return samples



