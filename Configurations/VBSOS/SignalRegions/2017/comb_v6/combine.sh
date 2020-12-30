#!/bin/bash
## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/user/b/bpinolin/CMSSW_8_1_0/
eval `scramv1 runtime -sh`
cd -

date=201230
workDir=/afs/cern.ch/user/b/bpinolin/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBSOS/SignalRegions/2017/comb_v6/datacards
    
points=(
10
15
20
25
30
35
40
)

for pi in "${points[@]}"
do
    var=DNNoutput_${pi}

    datacardDir=${workDir}/${date}
    workspaceDir=${datacardDir}/workspace
    
    cd $workDir
    output=combine_${var}

    combineCards.py   sr=${datacardDir}/sr/${var}/datacard.txt \
                      topcr=${datacardDir}/topcr/events/datacard.txt \
                      dycr=${datacardDir}/dycr/events/datacard.txt \
    > ${workspaceDir}/${output}.txt

    text2workspace.py ${workspaceDir}/${output}.txt -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO 'map=.*/WWewk:r_vbs[1,-10,10]' -o ${workspaceDir}/${output}.root

    echo ${var}":" "" > ${workspaceDir}/fitdiagnostic_${output}.txt
    combine -M FitDiagnostics ${workspaceDir}/${output}.root -t -1 --setParameters r_vbs=1 --cminDefaultMinimizerStrategy 0 --redefineSignalPOIs=r_vbs --saveNormalizations --saveWithUncertainties >> ${workspaceDir}/fitdiagnostic_${output}.txt

    mv higgsCombineTest.FitDiagnostics.mH120.root ${workspaceDir}/.
    mv fitDiagnostics.root ${workspaceDir}/.
    rm combine_logger.out

    echo ${var}":" "" > ${workspaceDir}/significance_${output}.txt
    combine -M Significance ${workspaceDir}/${output}.root -t -1 --freezeParameters allConstrainedNuisances --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs >>  ${workspaceDir}/significance_${output}.txt

    mv higgsCombineTest.Significance.mH120.root ${workspaceDir}/.

done
