#!/bin/bash
## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/user/b/bpinolin/CMSSW_8_1_0/
eval `scramv1 runtime -sh`
cd -

workDir=/afs/cern.ch/user/b/bpinolin/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBSOS/SignalRegions
    
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
    workspaceDir=${workDir}/workspace
    
    cd $workDir
    output=combine_${var}

    combineCards.py   sr_lowZ_2016=${workDir}/2016/comb_v6/datacards/210103/sr_lowZ/${var}/datacard.txt \
                      sr_lowZ_2017=${workDir}/2017/comb_v6/datacards/210103/sr_lowZ/${var}/datacard.txt \
                      sr_lowZ_2018=${workDir}/2018/comb_v6/datacards/210103/sr_lowZ/${var}/datacard.txt \
                      sr_highZ_2016=${workDir}/2016/comb_v6/datacards/210103/sr_highZ/${var}/datacard.txt \
                      sr_highZ_2017=${workDir}/2017/comb_v6/datacards/210103/sr_highZ/${var}/datacard.txt \
                      sr_highZ_2018=${workDir}/2018/comb_v6/datacards/210103/sr_highZ/${var}/datacard.txt \
                      topcr_2016=${workDir}/2016/comb_v6/datacards/210103/topcr/events/datacard.txt \
                      topcr_2017=${workDir}/2017/comb_v6/datacards/210103/topcr/events/datacard.txt \
                      topcr_2018=${workDir}/2018/comb_v6/datacards/210103/topcr/events/datacard.txt \
                      dycr_2016=${workDir}/2016/comb_v6/datacards/210103/dycr/events/datacard.txt \
                      dycr_2017=${workDir}/2017/comb_v6/datacards/210103/dycr/events/datacard.txt \
                      dycr_2018=${workDir}/2018/comb_v6/datacards/210103/dycr/events/datacard.txt \
    > ${workspaceDir}/${output}.txt

    text2workspace.py ${workspaceDir}/${output}.txt -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO 'map=.*/WWewk:r_vbs[1,-10,10]' -o ${workspaceDir}/${output}.root

    echo ${var}":" "" > ${workspaceDir}/fitdiagnostic_${output}.txt
    combine -M FitDiagnostics ${workspaceDir}/${output}.root -t -1 --setParameters r_vbs=1 --cminDefaultMinimizerStrategy 0 --redefineSignalPOIs=r_vbs --saveNormalizations --saveWithUncertainties >> ${workspaceDir}/fitdiagnostic_${output}.txt

    mv higgsCombineTest.FitDiagnostics.mH120.root ${workspaceDir}/.
    mv fitDiagnostics.root ${workspaceDir}/.
    rm combine_logger.out

    echo ${var}":" "" > ${workspaceDir}/significance_${output}.txt
    combine -M Significance ${workspaceDir}/${output}.root -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs >>  ${workspaceDir}/significance_${output}.txt

    mv higgsCombineTest.Significance.mH120.root ${workspaceDir}/.

done
