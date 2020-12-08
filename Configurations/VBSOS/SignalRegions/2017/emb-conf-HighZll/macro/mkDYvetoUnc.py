#!/usr/bin/env python

import os
import ROOT
import sys


###
### Applies shape of vetoed TauTau MC events as uncertainty for Embedded
### Run this after mkShapesMulti Hadd-step, and before mkPlot:
### "python scripts/mkDYvetoUnc.py configuration.py"
###

conf = sys.argv[1][:-3]

cwd = os.getcwd()
sys.path.append(".")
exec("from "+conf+" import *")

rootfile = cwd + "/" + outputDir + "/" + "plots_" + tag + ".root"
origfile = rootfile.replace(".root", "_orig.root")

if not os.path.isfile(origfile):
  print "Making safety copy of original root file.."
  os.system("cp "+rootfile+" "+origfile)
else:
  print "Retrieving safety copy of original root file.."
  os.system("cp "+origfile+" "+rootfile)
print "Copy done"

newfile = ROOT.TFile(rootfile, 'update')

for categories in newfile.GetListOfKeys(): # Cut directory
  category = newfile.GetDirectory(categories.GetName())
  for variables in category.GetListOfKeys(): # Variable directory
    variable = category.GetDirectory(variables.GetName())

    print("Ok fin qua ci siamo")

    DYvetoUp = variable.Get("histo_Dyveto_CMS_embed_veto_2017Up")
    print("DYvetoUp", DYvetoUp)
    DYvetoDn = variable.Get("histo_Dyveto_CMS_embed_veto_2017Down")
    print("DYvetoDn", DYvetoDn)
    DYuncUp = variable.Get("histo_Dyemb_CMS_embed_veto_2017Up")
    print("DYuncUp", DYuncUp)
    DYuncDn = variable.Get("histo_Dyemb_CMS_embed_veto_2017Down")
    print("DYuncDn", DYuncDn)

    DYuncUp.Add(DYvetoUp)
    DYuncDn.Add(DYvetoDn)
    newfile.GetDirectory(categories.GetName()).GetDirectory(variables.GetName()).cd()
    DYuncUp.Write()
    DYuncDn.Write()

newfile.Close()
print "Done!"
exit(0)

