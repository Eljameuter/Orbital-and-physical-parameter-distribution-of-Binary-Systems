# change scope to
Which bias do we have in physical properties of stars (thin Kroupa INF and e propto P^eta) and what is observational bias
- SB9
- ORB6
Game plan: research distributions from theory -> subtract found distribution from observational data -> result is observational bias
# Description of collumn names
bsdb: BSDB identifier
ref_idsys: identification system from the original catalog (see the catalogue, filename, and line fields)
id: identifier from the original catalog
e: eccentricity
q: mass ratio
period: period
a: semi-major axis
catalogue: name of the original catalog from which the data was taken
filename: file in the original catalog
line: line number in the original catalog file
# Poster colour scheme
https://lospec.com/palette-list/retro-space

# Catalogue overview

LIST OF PARAMETERS AND SOURCES 

e (3): {'J/A+A/546/A69, ORB6, SB9'}

q (5): {'II/150A, J/A+A/417/263, V/115, V/118, V/119 '}

period (18): {'B/gcvs, CEV, II/150A, J/A+A/311/523, J/A+A/417/263, J/A+A/546/A69, J/MNRAS/491/5489, LiuHMXB, LiuLMXB, ORB6, SB9, Svechnikov84, Svechnikov99, V/115, V/118, V/119 , V/120, V/123A'}

a (4): {'J/A+A/546/A69, J/MNRAS/491/5489, ORB6, V/120'}

parallax (8): {'Hipparcos, II/150A, J/A+A/417/263, J/A+A/546/A69, J/MNRAS/349/1069, J/MNRAS/357/497, V/119 , V/120'}

i (6): {'J/A+A/417/263, ORB6, Svechnikov84, Svechnikov99, V/115, V/119 '}

| Observing Type                       | Catalogues                                |
| ------------------------------------ | ----------------------------------------- |
| **Visual / Astrometric binaries**    | ORB6, Hipparcos, V/119, V/120             |
| **Spectroscopic binaries**           | SB9                                       |
| **Eclipsing / Photometric binaries** | CEV, Svechnikov84, Svechnikov99           |
| **Variable stars**                   | B/gcvs, V/123A                            |
| **X-ray binaries**                   | LiuHMXB, LiuLMXB                          |
| **Literature mixed binary studies**  | J/A+A/*, J/MNRAS/*, II/150A, V/115, V/118 |

# Bias research
## Eccentricity
**Sources**

J/A+A/546/A69, ORB6, SB9

### Tactic
* Generate large set of binaries, with some possible distributions
* apply same bias as databases have
* compare simulation with real data 
* extract original distribution

[Mind your P's and Q's](https://iopscience.iop.org/article/10.3847/1538-4365/aa6fb6/pdf)
Mass distribution today (fig 2)

eccentricity probability  distribution  according to a power law. Note that
η = 1 is a Maxwellian “thermal” eccentricity distribution
$p \propto e^\eta$

For a given P and Q

$e_{max}(P)=1-\frac{P}{2 days}^{-2/3}$ for P > 2 days

We assume that all binaries with
P < 2 days are circularized,


Only **spectroscopic (Section 3) and eclipsing
(Section 4) binaries** can currently be utilized to quantify an
**unbiased eccentricity distribution** for early-type binaries

#### Overview of parameters like $gamma_{small}$ etc in Table 13!!

### ORB6
* long/intermediate P
* resolved systems
* nearby
* bright pairs
### SB9
[Twins like to be seen: observational biases affecting spectroscopically selected binary stars](https://academic.oup.com/mnras/article/445/2/2028/1416743)


[What a local sample of spectroscopic binaries can tell us about the field binary population](https://academic.oup.com/mnras/article/361/2/495/1057458)


[Single-lined Spectroscopic Binary Star Candidates from RAVE and Gaia DR2](https://iopscience.iop.org/article/10.3847/1538-3881/ab3cc1)
* short P
* high RV amplitude
* decent inclination
* bright primaries
### Comments on eccentricity distributions
Close binaries:
uniform f(e) = 1
Wide binaries
thermal f(e) = 2e
Very wide binaries
combination of thermal, superthermal and uniform dependent on seperation [Source](https://www.researchgate.net/publication/355872510_The_eccentricity_distribution_of_wide_binaries_and_their_individual_measurements):
![img.png](
Media/img.png)
[Source](https://academic.oup.com/mnras/article/456/2/2070/1071036)

e > 0.5

It is generally recognized that dynamical interactions in stellar systems produce binaries with ‘thermal’ eccentricity distribution f(e) = 2e


[Source](https://www.aanda.org/articles/aa/pdf/2004/35/aa1213.pdf) :

The constraints on eccentricity derived by Hut (1981) from
dissipative tidal evolution lead to a lower limit on the angular momentum h. Given that h2 ∝ a(1 − e2), we get the upper
envelope P(1 − e2)
3/2 = const. 
## Interpretation eccentricity observation bias
