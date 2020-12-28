#!/bin/bash
## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/user/b/bpinolin/CMSSW_8_1_0/
eval `scramv1 runtime -sh`
cd -

date=201217
workDir=/afs/cern.ch/user/b/bpinolin/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBSOS/SignalRegions/2018/lowZ_conf/datacards
datacardDir=${workDir}/${date}
workspaceDir=${datacardDir}/workspace
var=DNNoutput_10

cd $workDir
output=combine_${var}

echo ${var}":" "" > ${workspaceDir}/fitdiagnostic_${output}.txt
combine -M FitDiagnostics ${workspaceDir}/${output}.root -t -1 --setParameters r_vbs=1 --cminDefaultMinimizerStrategy 0 --redefineSignalPOIs=r_vbs --saveNormalizations \
  --saveWithUncertainties >> ${workspaceDir}/fitdiagnostic_${output}.txt

mv higgsCombineTest.FitDiagnostics.mH120.root ${workspaceDir}/fitdiagnostic_${output}.root
mv fitDiagnostics.root ${workspaceDir}/fitDiagnostic_4diffNuis_${output}.root
rm combine_logger.out

python /afs/cern.ch/user/b/bpinolin/CMSSW_8_1_0/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py \
  ${workspaceDir}/fitDiagnostic_4diffNuis_${output}.root -f text -g ${workspaceDir}/diffNuis_out_${output}.root -p r_vbs
