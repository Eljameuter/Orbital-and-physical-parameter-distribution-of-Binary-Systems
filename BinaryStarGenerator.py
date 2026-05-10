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
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.interpolate import interp1d


class BinaryStarGenerator:

    def generate_single(self, pdf, limit, number):

        xmin, xmax = limit
        x = np.linspace(xmin, xmax, 10000)
        # calc pdf for x
        p = pdf(x)
        p = np.clip(p, 0, None)
        #integrate to get cdf
        cdf = cumulative_trapezoid(p, x, initial=0)
        cdf /= cdf[-1] #normalize

        # Inverse CDF interpolation
        inv_cdf = interp1d(cdf, x)

        # Uniform random numbers
        u = np.random.rand(number)

        # Samples
        samples = inv_cdf(u)

        return samples



