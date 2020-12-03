#!/bin/bash

## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/user/r/rdfexp/bianca/CMSSW_8_1_0/
eval `scramv1 runtime -sh`
cd -

## FIXME this is your work directory
workDir=/afs/cern.ch/user/r/rdfexp/bianca/CMSSW_10_2_15_patch2/src/PlotsConfigurations/Configurations/VBSOS/SignalRegions/2018/emb-conf/datacards
date=1203
var=DNNoutput_15

datacardDir=${workDir}/${date}
workspaceDir=${datacardDir}/workspace

combineTool.py -M Impacts -d ${workspaceDir}/combine_${var}.root -m 125 -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs --X-rtd MINIMIZER_analytic --doInitialFit
combineTool.py -M Impacts -d ${workspaceDir}/combine_${var}.root -m 125 -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs --X-rtd MINIMIZER_analytic --doFits
combineTool.py -M Impacts -d ${workspaceDir}/combine_${var}.root -m 125 -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs --X-rtd MINIMIZER_analytic -o ${workspaceDir}/impacts_2018_${var}.json 

plotImpacts.py -i ${workspaceDir}/impacts_2018_${var}.json -o ${workspaceDir}/impacts_2018_${var}

cd $workspaceDir
