#!/bin/bash
## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/user/r/rdfexp/bianca/CMSSW_8_1_0/
eval `scramv1 runtime -sh`
cd -

## work directory
date=1124
var=DNNoutput_40

workDir=datacards
datacardDir=${workDir}/${date}  datacards/1123
workspaceDir=${datacardDir}/workspace   datacards/1123/workspace

output=combine_${var}
cd $workDir cd datacards

combineCards.py   sr=${datacardDir}/sr/${var}/datacard.txt \
                  cr_top=${datacardDir}/top_cr/events/datacard.txt \
                  cr_dy=${datacardDir}/dy_cr/events/datacard.txt \
> ${workspaceDir}/${output}.txt

text2workspace.py ${workspaceDir}/${output}.txt -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO 'map=.*/WWewk:r_vbs[1,-10,10]' -o ${workspaceDir}/${output}.root

echo ${var}":" "" > ${workspaceDir}/fitdiagnostic_${output}.txt
combine -M FitDiagnostics ${workspaceDir}/${output}.root -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs --saveNormalizations --saveWithUncertainties >> ${workspaceDir}/fitdiagnostic_${output}.txt


echo ${var}":" "" > ${workspaceDir}/significance_${output}.txt
combine -M Significance ${workspaceDir}/${output}.root -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs >>  ${workspaceDir}/significance_${output}.txt