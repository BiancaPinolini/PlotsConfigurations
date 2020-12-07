#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "NNEvaluation/DNNTensorflow/interface/DNNEvaluator.hh"

#include "TMath.h"

#include <cmath>
#include <string>
#include <iostream>

using namespace std;
using namespace NNEvaluation;

#ifndef MVAReader_sr_v2_H
#define MVAReader_sr_v2_H

class MVAReader_sr_v2 : public multidraw::TTreeFunction {
public:
  
  MVAReader_sr_v2(const char* model_path, bool verbose, int cut);

  char const* getName() const override { return "MVAReader_sr_v2"; }
  TTreeFunction* clone() const override { return new MVAReader_sr_v2(model_path_.c_str(), verbose, cut_); }

  std::string model_path_;
  int cut_;
  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:  
 
  bool verbose;
  void bindTree_(multidraw::FunctionLibrary&) override;
  
  DNNEvaluator* dnn_tensorflow;
  
  TTreeReaderValue<Double_t>* cut_index{};
  FloatValueReader* detajj{};
  FloatValueReader* ptll{};
  TTreeReaderValue<Double_t>* eta1{};
  TTreeReaderValue<Double_t>* eta2{};
  TTreeReaderValue<Double_t>* detall{};
  TTreeReaderValue<Double_t>* jetpt1{};
  TTreeReaderValue<Double_t>* jetpt2{};
  FloatValueReader* met{};
  FloatValueReader* dphill{};
  TTreeReaderValue<Double_t>* dphijj{};
  FloatValueReader* Mll{};
  TTreeReaderValue<Double_t>* btag_central{};
  TTreeReaderValue<Double_t>* btag_forward{};
  TTreeReaderValue<Double_t>* dR_jl1{};
  TTreeReaderValue<Double_t>* dR_jl2{};
  TTreeReaderValue<Double_t>* Zeppll{};
  TTreeReaderValue<Double_t>* Zepp1{};
  TTreeReaderValue<Double_t>* Zepp2{};
  FloatValueReader* mjj{};
  TTreeReaderValue<Double_t>* qgl_forward{};
  TTreeReaderValue<Double_t>* qgl_central{};

  TTreeReaderValue<Double_t>* topcr{};
  TTreeReaderValue<Double_t>* dycr{};
  TTreeReaderValue<Double_t>* srr{};
  
};

MVAReader_sr_v2::MVAReader_sr_v2(const char* model_path, bool verbose, int cut):
    model_path_(model_path), 
    verbose(verbose),
    cut_(cut)
{
    dnn_tensorflow = new DNNEvaluator(model_path_, verbose);
}


double 
MVAReader_sr_v2::evaluate(unsigned)
{
  // Run only if 
  if ((int)(*(cut_index->Get())) != cut_) {
    return -999.;
  }
  // std::cout << "cut_index = " << (int)(*(cut_index->Get())) << "; cut =  " << cut_ << std::endl;

  std::vector<float> input{};

  input.push_back( TMath::Abs(*(detajj->Get())));
  input.push_back( *(ptll->Get()) );
  input.push_back( *(detall->Get()) );
  input.push_back( TMath::Log(*(jetpt1->Get()) ));
  input.push_back( TMath::Log(*(jetpt2->Get()) ));
  input.push_back( *(met->Get()) );
  input.push_back( TMath::Abs(*(dphill->Get())));
  input.push_back( *(dphijj->Get()) );
  input.push_back( *(Mll->Get()) );
  if (*(topcr->Get())) input.push_back( (float) 0.7);
  else                 input.push_back(*(btag_central->Get()));
  if (*(topcr->Get())) input.push_back( (float) 0.7);
  else                 input.push_back(*(btag_forward->Get()));
  input.push_back( *(dR_jl1->Get()) );
  input.push_back( *(dR_jl2->Get()) );
  if (*(srr->Get())) input.push_back(*(Zeppll->Get()));
  else               input.push_back( (float) 0.5);
  input.push_back( TMath::Log(*(mjj->Get()) ));
  input.push_back( *(Zepp1->Get()) );
  input.push_back( *(Zepp2->Get()) );
  input.push_back( *(eta1->Get()) );
  input.push_back( *(eta2->Get()) );
  input.push_back( *(qgl_forward->Get()) );
  input.push_back( *(qgl_central->Get()) );
  
  // std::cout << "srr = " << *(srr->Get()) << std::endl;
  // std::cout << "btag = " << btag << std::endl;
  // std::cout << "btag_central = " << *(btag_central->Get()) << std::endl;

  //if(*(topcr->Get())) {
    // std::cout << "btag_central = " << *(btag_central->Get()) << std::endl;
    // std::cout << "btag_forward = " << *(btag_forward->Get()) << std::endl;
    // std::cout << "Jet_nConst_central = " << *(Jet_nConst_central->Get()) << std::endl;
    // std::cout << "output = " << dnn_tensorflow->analyze(input) << std::endl;
  //}

  return dnn_tensorflow->analyze(input);
  
}

void
MVAReader_sr_v2::bindTree_(multidraw::FunctionLibrary& _library)
{  
  _library.bindBranch(cut_index, "cut_index");
  _library.bindBranch(detajj, "detajj");
  _library.bindBranch(ptll, "ptll");
  _library.bindBranch(eta1, "eta1_al");
  _library.bindBranch(eta2, "eta2_al");
  _library.bindBranch(detall, "detall_al");
  _library.bindBranch(jetpt1, "jetpt1_al");
  _library.bindBranch(jetpt2, "jetpt2_al");
  _library.bindBranch(met, "MET_pt");
  _library.bindBranch(dphill, "dphill");
  _library.bindBranch(dphijj, "dphijj_al");
  _library.bindBranch(Mll, "mll");
  _library.bindBranch(btag_central, "btag_central_DNN");
  _library.bindBranch(btag_forward, "btag_forward_DNN");
  _library.bindBranch(dR_jl1, "dR_jl1_al");
  _library.bindBranch(dR_jl2, "dR_jl2_al");
  _library.bindBranch(Zeppll, "Zeppll_DNN");
  _library.bindBranch(Zepp1, "Zepp1_al");
  _library.bindBranch(Zepp2, "Zepp2_al");
  _library.bindBranch(mjj, "mjj");
  _library.bindBranch(qgl_forward, "qgl_forward");
  _library.bindBranch(qgl_central, "qgl_central");

  _library.bindBranch(topcr, "topcr");
  _library.bindBranch(dycr, "dycr");
  _library.bindBranch(srr, "srr");
}


#endif
