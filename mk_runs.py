#! /usr/bin/env python3

import os
import sys

from lmtoy import runs

project="2024-S1-DM-2"

# Dictionary of sources, each with a list of obsnum's in this project
# negative obsnums are ignored in the combinations. See also comments.txt
# for obsnum specific comments and parameters!
on = {}

on["MWC1_freq1"] = \
 [ 155800, 155801, 155802, 155804, 155805, 155806, 155810, 155811, 155812,]

on["MWC1_freq2"] = \
 [ 156134, 156138, 156141, 156145, 156159, 156161, 156163,
   156495, 156497, 156499, # May-4-26 + May-8-26
  ]

on["MWC1_c18o"] = on["MWC1_freq1"] + on["MWC1_freq2"]
on["MWC1_13co"] = on["MWC1_freq1"] + on["MWC1_freq2"]
on["MWC1_wide"] = on["MWC1_freq1"] + on["MWC1_freq2"]


# parameters for the first pass of the pipeline (restart=1 is automatically enforced here)
# optionally speeding up with:    meta=0 srdp=0 sdfits=0
fast = " meta=0 srdp=0 sdfits=0"

pars1 = {}

pars1["MWC1_freq1"] = "vlsr=163  dv=50  dw=100 pix_list=-13,15 bank=1   oid=__CO    %s" % fast
pars1["MWC1_freq2"] = "vlsr=163  dv=100 dw=100 pix_list=-13,15 bank=1   oid=__CN    %s" % fast
pars1["MWC1_13co"]  = "vlsr=-406 dv=50  dw=100 pix_list=-13    bank=0   oid=__13CO  %s" % fast
pars1["MWC1_c18o"]  = "vlsr=+736 dv=50  dw=100 pix_list=-13    bank=0   oid=__C18O  %s" % fast
pars1["MWC1_wide"]  = "vlsr=163  dv=50  dw=950 pix_list=-15             oid=__wide  %s" % fast

# parameters for the (optional) second pass of the pipeline (e.g. for bank=0)
pars2 = {}

pars2["MWC1_freq1"] = "bank=1  oid=__CO"
pars2["MWC1_freq2"] = "bank=1  oid=__CN"
pars2["MWC1_13co"]  = "bank=0  oid=__13CO"
pars2["MWC1_c18o"]  = "bank=0  oid=__C18O"


# parameters for the (optional) third pass of the pipeline (usually for bank=1)
pars3 = {}

# Found 2 source(s) for 2024-S1-DM-2

if __name__ == "__main__":
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)

# see also /nese/toltec/dataprod_lmtslr/work_lmt/tmp/2024-S1-DM-2.obsnums.log
