#!/bin/bash

## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/user/b/bpinolin/CMSSW_8_1_0/
eval `scramv1 runtime -sh`
cd -

## FIXME this is your work directory
date=201224/v3_plus_v6
workDir=/afs/cern.ch/user/b/bpinolin/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBSOS/SignalRegions/2017/lowZ_conf/datacards
var=DNNoutput_20

datacardDir=${workDir}/${date}
workspaceDir=${datacardDir}/workspace

combineTool.py -M Impacts -d ${workspaceDir}/combine_${var}.root -m 125 -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs --X-rtd MINIMIZER_analytic --doInitialFit
combineTool.py -M Impacts -d ${workspaceDir}/combine_${var}.root -m 125 -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs --X-rtd MINIMIZER_analytic --doFits
combineTool.py -M Impacts -d ${workspaceDir}/combine_${var}.root -m 125 -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs --X-rtd MINIMIZER_analytic -o ${workspaceDir}/impacts_2017_${var}.json 

cd $workspaceDir

plotImpacts.py -i impacts_2017_${var}.json -o impacts_2017_${var}