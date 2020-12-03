#!/bin/bash
## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/user/r/rdfexp/bianca/CMSSW_8_1_0/
eval `scramv1 runtime -sh`
cd -

date=1203
workDir=/afs/cern.ch/user/r/rdfexp/bianca/CMSSW_10_2_15_patch2/src/PlotsConfigurations/Configurations/VBSOS/SignalRegions/2018/emb-conf/datacards
    
points=(
10
15
20
25
30
)

for pi in "${points[@]}"
do
    var=DNNoutput_${pi}

    datacardDir=${workDir}/${date}
    workspaceDir=${datacardDir}/workspace

    output=combine_${var}
    cd $workDir

    combineCards.py   sr=${datacardDir}/sr/${var}/datacard.txt \
                    cr_top=${datacardDir}/top_cr/events/datacard.txt \
                    cr_dy=${datacardDir}/dy_cr/events/datacard.txt \
    > ${workspaceDir}/${output}.txt

    text2workspace.py ${workspaceDir}/${output}.txt -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO 'map=.*/WWewk:r_vbs[1,-10,10]' -o ${workspaceDir}/${output}.root

    echo ${var}":" "" > ${workspaceDir}/fitdiagnostic_${output}.txt
    combine -M FitDiagnostics ${workspaceDir}/${output}.root -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs --saveNormalizations --saveWithUncertainties >> ${workspaceDir}/fitdiagnostic_${output}.txt


    echo ${var}":" "" > ${workspaceDir}/significance_${output}.txt
    combine -M Significance ${workspaceDir}/${output}.root -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs >>  ${workspaceDir}/significance_${output}.txt
done