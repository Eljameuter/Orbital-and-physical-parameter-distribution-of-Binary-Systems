# Binary Star Distribution Analysis

## Important Links

* [Proposal](https://www.overleaf.com/read/hstttxpzgdtk#62cb08)

## Deliverables

* Poster

---

## Research Question

What observational biases are present in the SB9 and ORB6 binary star catalogues when compared to theoretically expected binary star populations? Specifically, do the differences between observed and theoretical distributions of eccentricity, mass ratio, radius ratio, orbital period, and semi-major axis match the observational biases expected from the detection methods used in these catalogues?




## Timeline

* **11 April** – Project start, dataset check, task division
* **18 April** – Data cleaning complete
* **25 April** – Literature research on expected distributions complete
* **2 May** – Expected population models implemented
* **5 May** – Observed vs expected distributions generated
* **8 May** – Poster planning & figure selection
* **16 May** – Poster finalized
* **22 May** – Poster Presentation

---

## ToDo

## ToDo

| Deadline | Task                                                           | Owner  | Support | Progress | Notes                                       |
| -------- | -------------------------------------------------------------- | ------ | ------- | -------- | ------------------------------------------- |
| 8 May    | Finalize cleaned SB9 + ORB6 datasets                           | Wouter | All     | 🔴 0%    | Maintains final analysis dataset            |
| 8 May    | Finalize catalogue documentation & sources                     | Elja   | Tobias  | 🟢 100%  | Catalogues documented clearly               |
| 9 May    | Literature summary: expected eccentricity distribution         | Elja   | —       | 🟢 95%   | Includes implementation ideas               |
| 9 May    | Literature summary: expected mass ratio + period distributions | Tobias | —       | 🔴 0%    | Focus on observational selection effects    |
| 9 May    | Literature summary: expected radius ratio distribution         | Damian | —       | 🟡 40%   | Depends partly on Teff + luminosity         |
| 9 May    | Literature summary: expected semi-major axis distribution      | Wouter | —       | 🔴 0%    | Summary required                            |
| 10 May   | Define observed vs theoretical comparison method               | Tobias | All     | 🔴 0%    | Includes subtraction/normalization strategy |
| 10 May   | Implement theoretical population generator (e)                 | Elja   | —       | 🟡 70%   | Moe & Di Stefano (2017)-based generator, making a class out of it still wip     |
| 10 May   | Implement theoretical population generator (q, P)              | Tobias | —       | 🔴 0%    | Code + notes                                |
| 10 May   | Implement theoretical population generator (R)                 | Damian | —       | 🔴 0%    | Requires Teff + luminosity                  |
| 10 May   | Implement theoretical population generator (a)                 | Wouter | —       | 🔴 0%    | Code + notes                                |
| 11 May   | Generate observed vs expected distributions (e)                | Elja   | —       | 🟡 70%     | Compare catalogue vs model populations  -> done for one distribution still need to analyse if its all theoretical.    |
| 11 May   | Generate observed vs expected distributions (q, P)             | Tobias | —       | 🔴 0%    | —                                           |
| 11 May   | Generate observed vs expected distributions (R)                | Damian | —       | 🔴 0%    | —                                           |
| 11 May   | Generate observed vs expected distributions (a)                | Wouter | —       | 🔴 0%    | —                                           |
| 11 May   | Obtain Teff + spectral type + luminosity                       | Damian | Tobias  | 🟢 100%    | Critical dependency                         |
| 13 May   | Analyse observational biases in SB9 and ORB6                   | All    | —       | 🔴 0%    | Compare against expected detection biases   |
| 14 May   | Select final figures for poster                                | All    | —       | 🔴 0%    | Focus on strongest comparisons              |
| 15 May   | Assemble poster                                                | Elja   | All     | 🔴 20%    | Minimal text, strong visuals                |
| 22 May   | Poster presentation                                            | All    | —       | 🔴 0%    | Final presentation                          |


---

## Progress Legend

* 🔴 Not started (0%)
* 🟡 In progress (25–75%)
* 🟢 Completed (100%)

---

## Data Status

### Available

* Eccentricity (e)
* Orbital period (P)
* Semi-major axis (a)
* Parallax
* Inclination (i)
* Catalogue IDs
* SB9 catalogue data
* ORB6 catalogue data
* Spectral type
* Luminosity (L) *(needed for radius ratio)*

### Not Available
* Effective temperature (Teff) *(needed for radius ratio)*
---

## Task Distribution

* **Elja** → Eccentricity distributions
* **Tobias** → Mass ratio + orbital period distributions
* **Damian** → Radius ratio distributions *(depends on Teff, L)*
* **Wouter** → Semi-major axis distributions

---

## Workflow

### 1. Data Preparation (11–18 April)

* Clean SB9 and ORB6 datasets
* Remove invalid entries and NaNs
* Ensure consistent units
* Prepare shared analysis dataset

---

### 2. Literature Research on Expected Distributions (18–25 April)

Each member investigates expected intrinsic distributions for their parameter:

* Population synthesis models
* Binary formation literature
* Selection effects
* Detection biases
* Catalogue incompleteness

➡ Output: short literature summary + expected model assumptions

---

### 3. Population Modelling & Comparison Methods (25 April – 2 May)

* Define expected binary population models
* Implement synthetic population generators
* Define subtraction/comparison methods
* Document assumptions clearly

---

### 4. Distribution Analysis (2–5 May)

* Generate observed catalogue distributions
* Generate expected synthetic distributions
* Compare observed vs expected populations
* Identify major discrepancies and trends

---

### 5. Interpretation & Tidal Effects (5–11 May)

* Analyse deviations between observed and expected populations
* Focus on eccentricity vs orbital period
* Identify signatures of tidal circularization
* Cross-compare parameters
* Interpret physical meaning of discrepancies

---

### 6. Poster Preparation (8–16 May)

* Create concise visual summary
* Focus on:

  * Observed vs expected comparisons
  * Key tidal effects
  * Clear plots and takeaway messages
  * Minimal text, strong visuals
