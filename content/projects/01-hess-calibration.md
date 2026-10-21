---
title: ML-based calibration of a large-domain hydrology model
when: HESS 2025
filters:
- ml
tags:
- Emulators
- Optimization
- SUMMA
links:
- label: Paper
  url: https://doi.org/10.5194/hess-29-4515-2025
- label: Code
  url: https://github.com/MozhganFarahani/lse_landhydro
---

An AI-driven calibration workflow for the SUMMA process-based hydrology model. Machine-learning emulators are coupled with genetic-algorithm optimization to search high-dimensional parameter spaces across 627 CAMELS basins, refining estimates through successive emulator-guided model runs. Median streamflow accuracy (KGE′) rose from 0.30 to 0.76, compared with 0.69 for per-basin calibration, and spatial cross-validation tested how well the approach regionalizes to unseen basins.

The framework now extends to the larger CAMELS-X dataset with an improved optimization strategy, a global emulator, and a complementary regional emulator trained with federated learning (manuscript in preparation).
