## Important Links
[Proposal](https://www.overleaf.com/read/hstttxpzgdtk#62cb08)

Report

Poster
## Research Question

What is the distribution of eccentricity, mass ratio, radius ratio, orbital period and semi-major axis for a large number of binary stars, and how are these influenced by tidal effects?

---

## Timeline

* **11 April** – Project start, dataset check, task division
* **18 April** – Data cleaning complete
* **25 April** – Bias research completed (per parameter)
* **2 May** – Bias corrections implemented
* **5 May** – Corrected distributions generated
* **11 May** – Interpretation & tidal analysis complete
* **14 May** – Draft report complete
* **16 May** – Poster finalized
* **18 May** – Final report + presentation

---

## ToDo

| Deadline | Task                             | Owner  | Support | Progress | Notes                                                                                           |
| -------- | -------------------------------- |--------|---------|----------|-------------------------------------------------------------------------------------------------|
| 18 Apr   | Data cleaning & validation       | Wouter | All     | 🔴 0%    | Maintains final cleaned dataset                                                                 |
| 20 Apr   | Identify catalogues & sources    | Elja      | Tobias  | 🟢 100%  | Document sources clearly -> catalogues are in quick_read_out_data                               |
| 25 Apr   | Bias research (eccentricity)     | Elja   | —       | 🟢 95%   | Literary study in doc.md, also plan on how to implement                                         |
| 25 Apr   | Bias research (mass ratio + P)   | Tobias | —       | 🔴 0%    | Summary required                                                                                |
| 25 Apr   | Bias research (radius ratio)     | Damian | —       | 🔴 0%    | Depends partly on Teff                                                                          |
| 25 Apr   | Bias research (semi-major axis)  | Wouter | —       | 🔴 0%    | Summary required                                                                                |
| 27 Apr   | Define correction methods        | Tobias | All     | 🔴 0%    | Leads method consistency                                                                        |
| 2 May    | Implement bias correction (e)    | Elja   | —       | 🟡 10%   | Code + notes -> made binary star generator, generates binary star populations based on Moe & Di Stefano (2017)  |
| 2 May    | Implement bias correction (q, P) | Tobias | —       | 🔴 0%    | Code + notes                                                                                    |
| 2 May    | Implement bias correction (R)    | Damian | —       | 🔴 0%    | Needs Teff                                                                                      |
| 2 May    | Implement bias correction (a)    | Wouter | —       | 🔴 0%    | Code + notes                                                                                    |
| 5 May    | Generate distributions (e)       | Elja   | —       | 🔴 0%    | Raw vs corrected                                                                                |
| 5 May    | Generate distributions (q, P)    | Tobias | —       | 🔴 0%    | —                                                                                               |
| 5 May    | Generate distributions (R)       | Damian | —       | 🔴 0%    | —                                                                                               |
| 5 May    | Generate distributions (a)       | Wouter | —       | 🔴 0%    | —                                                                                               |
| TBD      | Obtain Teff + spectral type      | Damian | Tobias  | 🔴 0%    | Critical dependency                                                                             |
| 11 May   | Interpretation (eccentricity)    | Elja   | All     | 🔴 0%    | Focus on tidal effects                                                                          |
| 11 May   | Interpretation (q, P)            | Tobias | All     | 🔴 0%    | Link to formation scenarios                                                                     |
| 11 May   | Interpretation (R)               | Damian | All     | 🔴 0%    | Depends on data completeness                                                                    |
| 11 May   | Interpretation (a)               | Wouter | All     | 🔴 0%    | —                                                                                               |
| 11 May   | Global tidal analysis            | Wouter | Elja    | 🔴 0%    | Cross-parameter synthesis                                                                       |
| 14 May   | Draft report (methods)           | Tobias | All     | 🔴 0%    | Bias + methodology                                                                              |
| 14 May   | Draft report (results)           | Damian   | All     | 🔴 0%    | Figures + trends                                                                                |
| 14 May   | Draft report (discussion)        | Wouter | All     | 🔴 0%    | Physical interpretation                                                                         |
| 16 May   | Poster design                    | Elja | All     | 🔴 0%    | Visual clarity focus                                                                            |
| 18 May   | Final report + presentation      | All    | —       | 🔴 0%    | Final integration                                                                               |

---
## Progress Legend

* 🔴 Not started (0%)
* 🟡 In progress (25–75%)
* 🟢 Completed (100%)

---
## Data Status

**Available:**

* Eccentricity (e)
* Period
* Semi-major axis (a)
* Parallax
* Inclination (i)
* Catalogue IDs

**Pending:**

* Spectral type
* Effective temperature (Teff) *(needed for radius ratio)*
* Luminocity (L) *(needed for radius ratio)*

---

## Task Distribution

* **Elja** → Eccentricity distribution
* **Tobias** → Mass ratio + Orbital period distribution
* **Damian** → Radius ratio *(depends on Teff, L)*
* **Wouter** → Semi-major axis distribution

---

## Workflow

### 1. Data Preparation (11–18 April)

* Clean dataset (remove NaNs, invalid entries)
* Ensure consistent units
* Prepare shared dataset

---

### 2. Bias Research (18–25 April)

Each member investigates biases affecting their parameter:

* Selection effects
* Detection limits
* Catalogue-specific biases
* Relevant literature

➡ Output: short written summary per parameter

---

### 3. Bias Correction (25 April – 2 May)

* Define correction methods (cuts, weighting, etc.)
* Apply corrections to dataset
* Document assumptions clearly

---

### 4. Distribution Analysis (2–5 May)

* Generate corrected distributions
* Compare raw vs corrected results
* Quick identification of major features

---

### 5. Interpretation & Tidal Effects (5–11 May)

*(Expanded — this is the hard part)*

* Analyse relationships between parameters
* Focus on eccentricity vs orbital period
* Identify tidal circularization signatures
* Cross-compare parameters (e.g. mass ratio vs period)
* Interpret physical meaning of distributions

---

### 6. Report Writing (11–14 May)

* Combine all results
* Clearly explain:

  * Methods
  * Bias corrections
  * Key interpretations
* Draft figures + captions early

---

### 7. Poster Preparation (14–16 May)

* Create visual summary of results
* Focus on:

  * Clean plots
  * Clear takeaway messages

---

