---
title: 'CTSM-CONUS: high-resolution land and river modeling'
when: Aug–Sep 2026
filters:
- hpc
- tools
tags:
- CTSM
- mizuRoute
- Xarray · Dask
links:
- label: Project site
  url: https://project.cgd.ucar.edu/projects/ctsm-conus
- label: Technical note
  url: https://project.cgd.ucar.edu/projects/ctsm-conus/note/
- label: Code
  url: https://github.com/MozhganFarahani/ctsm_conus
---

Which CTSM configuration choices matter most for fine-scale hydrology over the contiguous U.S.? This project ran the Community Terrestrial Systems Model (CTSM 5.4, CLM6 physics) coupled to the mizuRoute river model on the NLDAS-2 1/8° grid: 80,439 land cells, 227,247 MERIT-Hydro river reaches, and 38 water years of NLDAS-2 forcing. Starting from a control configuration, each experiment changes one process option: irrigation, evolving land cover, hillslope hydrology, or prognostic phenology.

Routed streamflow was evaluated against 2,286 USGS, USACE, and USBR gauges (monthly NSE, KGE, percent bias). Hillslope hydrology is the only option that changes skill substantially, roughly doubling median NSE, with the largest gains across the West and the Missouri basin. The work was a two-month Science Innovation Fund (SIF-T) project, published as a project website, an interactive dashboard, a Jupyter Book technical note, and a code repository.

It was also my first time running CTSM. I used Claude as a working assistant throughout: learning the model with my proposal as context, adapting my SUMMA evaluation code to CTSM and mizuRoute, diagnosing setup and routing errors, keeping a project log, and building the website and dashboard. I reviewed and tested every step as I would my own code.
