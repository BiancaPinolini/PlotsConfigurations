#include "TTree.h"
#include "TFile.h"
#include "TSystem.h"
#include "TROOT.h"
#include "TString.h"
#include <iostream>

using namespace std; 

namespace multidraw {
  extern thread_local TTree* currentTree;
}

TString currentSampleName;




int getSampleName(){
  TString targetSampleName = "TTTo2L2Nu";

  currentSampleName = TString(multidraw::currentTree->GetCurrentFile()->GetName());

  if ( currentSampleName.Contains(targetSampleName)) {
      return 1;
  }
  else {
      return 0;
  }

  targetSampleName = "ST_s-channel_ext1";

  if ( currentSampleName.Contains(targetSampleName)) {
      return 1;
  }
  else return 0;


  targetSampleName = "ST_t-channel_antitop";

  if ( currentSampleName.Contains(targetSampleName)) {
      return 1;
  }
  else return 0;


  targetSampleName = "ST_t-channel_top";

  if ( currentSampleName.Contains(targetSampleName)) {
      return 1;
  }
  else return 0;


  targetSampleName = "ST_tW_antitop_ext1";

  if ( currentSampleName.Contains(targetSampleName)) {
      return 1;
  }
  else return 0;


  targetSampleName = "ST_tW_top_ext1";

  if ( currentSampleName.Contains(targetSampleName)) {
      return 1;
  }
  else return 0;

}