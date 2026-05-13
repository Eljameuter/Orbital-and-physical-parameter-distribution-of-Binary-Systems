# change scope to
Which bias do we have in physical properties of stars (thin Kroupa INF and e propto P^eta) and what is observational bias
- SB9
- ORB6
Game plan: research distributions from theory -> subtract found distribution from observational data -> result is observational bias
# Description of column names
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
In SB9 consistently lower eccentricities are observed more than expected.
[Proof](https://watermark02.silverchair.com/stag351.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAAA1wwggNYBgkqhkiG9w0BBwagggNJMIIDRQIBADCCAz4GCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMMqbVa-uKOhE60uuXAgEQgIIDDxO07YZzDgITOpMIwL6YdAOVpcJoFeaqmwZkqa5dUWKPBJ-qKVPt-laYJ-blYaMuknLfpPKPwmOyOw5sWa3KE6qhaBZPvaAQXXH_pHqACWq2A2hp-luYDwO1ZfTwAn5rsnisiWG_v0k8CHbqNX6t0DfUJ3no0Uj9B3Ql-DLjEJLvjfulAEdHf2EE5QBcmF6f1pNj9LPJtAbqn4pdygOaNiJulLM705RVkVVO6HBxaWgjZDQm2pq2j24tgEM3NzX78OgOIk5ZCsZgwz8h3wEGVrsjghN2GHTbXYU3-23MsO60iCR_EbVdpLDP7tXLcoCExmnizJp9cAPqnlt2Vmnj50B_LEcW9XvqKUyyzHhDfKCTq2ffHPyRqYUl_WUyiVTHlB6UDSihwYhTZW4DddCB1DnLIA8RNcBVXYghBmMEPKlL7-FtEiKn1WHLp33R9MH5CQgOsw0h_-4Wg6jlTmjX04msCZjIsfLWgZMJpIOlCPLH6SOgsGxVIFYnahn6E8TnpPSYal73nQ1HW0Aa6Usa3vT1vWwNFPUO6gDBFfMsnFYbyLO-d97hNmCcVAFyU8E9nG-v2eYZYEV-Gh2Wcx0oLo0jzicmVxJdCey5rxL39Pfud4RRCBfjBk1139bltG4RWb3Q7AWXqcD-nX7auUdhHrYJbjjmSZNN6PiHSlD0ChV0NRKe3URrhFcu1ZkWjHYNTruBbTeoCRIG5kEG9UF0S5pZxBPgQyKQlDj_EfLopCAvaXxRXQfAt1aci9ApnNkSkQzjgF3CmT3D9ocBzE0DSgjAgOennHCY5eaEQdPlUZId34ycS8SQiKpNfQKH_JyfuidS_YW5Xv0mHnCBC1fAwz2t8Lm4DdPw3W3dG1vlc4CAK0IVm5UtdFZ3eCEvy-o0OmjyHnNIZmAOO3jDUGKb0x9iyfMDSQqvGL3MydttYROXoctpdSNmkYycGLeVguKFf92f59GJW8hEPJuWcapwrwdpd4EAmZWPeqzez6B8YXeSuzRJKssBH_DGtYL3470EMNHZP8U4JHi5VxsnX_Aivg) that that makes sense: 
Observational bias against high Periods -> supresses high eccentricity systems
The RV curve is more sinusoidal for e = 0, hence strongly biased towards e = 0 for spectroscopic systems since they are easier to detect

Maybe also in comparison to T < 7 days -> circulization almost certain and since we are also biased 
towards lower T we see a bunch of circular eccentricities

In ORB6 strongly biased towards lower eccentricities, but not as extremely towards e = 0
We find that the catalogue of visual orbits is strongly biased against large eccentricities. (https://academic.oup.com/mnras/article/456/2/2070/1071036)
ORB only includes characterized orbits -> computational selection bias -> smaller e are easier to compute, up to e = 0.5 
The computational selection is less of a problem for spectroscopic binaries.