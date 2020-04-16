#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "NNEvaluation/DNNTensorflow/interface/DNNEvaluator.hh"

#include "TMath.h"

#include <cmath>
#include <string>
#include <iostream>

using namespace std;
using namespace NNEvaluation;

#ifndef MVAReader_emtight_v1_H
#define MVAReader_emtight_v1_H

class MVAReader_emtight_v1 : public multidraw::TTreeFunction {
public:
  
  MVAReader_emtight_v1(const char* model_path, bool verbose, int cut);

  char const* getName() const override { return "MVAReader_emtight_v1"; }
  TTreeFunction* clone() const override { return new MVAReader_emtight_v1(model_path_.c_str(), verbose, cut_); }

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
  TTreeReaderValue<Double_t>* detall{};
  TTreeReaderValue<Double_t>* jetpt1{};
  TTreeReaderValue<Double_t>* jetpt2{};
  TTreeReaderValue<Double_t>* eta1{};
  TTreeReaderValue<Double_t>* eta2{};
  FloatValueReader* MET_pt{};
  FloatValueReader* dphill{};
  TTreeReaderValue<Double_t>* dphijj{};
  TTreeReaderValue<Double_t>* Zlep1{};
  TTreeReaderValue<Double_t>* Zlep2{};
  FloatValueReader* mll{};
  TTreeReaderValue<Double_t>* btag_first{};
  TTreeReaderValue<Double_t>* btag_second{};
  TTreeReaderValue<Double_t>* dR_jl1{};
  TTreeReaderValue<Double_t>* dR_jl2{};
};


MVAReader_emtight_v1::MVAReader_emtight_v1(const char* model_path, bool verbose, int cut):
    model_path_(model_path), 
    verbose(verbose),
    cut_(cut)
{
    dnn_tensorflow = new DNNEvaluator(model_path_, verbose);
}


double
MVAReader_emtight_v1::evaluate(unsigned)
{
  // Run only if 
  if ((int)(*(cut_index->Get())) != cut_) {
    return -999.;
  }

  //std::cout << "TIGHT = " << (int)(*(cut_index->Get())) << " " << cut_ << std::endl;
  
  std::vector<float> input{};
  input.push_back( TMath::Abs(*(detajj->Get())));
  input.push_back( *(detall->Get()) );
  input.push_back( *(jetpt1->Get()) );
  input.push_back( *(jetpt2->Get()) );
  input.push_back( *(eta1->Get()) );
  input.push_back( *(eta2->Get()) );
  input.push_back( *(MET_pt->Get()) );
  input.push_back( TMath::Abs(*(dphill->Get())));
  input.push_back( *(dphijj->Get()) );
  input.push_back( *(Zlep1->Get()) );
  input.push_back( *(Zlep2->Get()) );
  input.push_back( *(mll->Get()) );
  input.push_back( *(btag_first->Get()) );
  input.push_back( *(btag_second->Get()) );
  input.push_back( *(dR_jl1->Get()) );
  input.push_back( *(dR_jl2->Get()) );

  std::cout << "output = " << dnn_tensorflow->analyze(input) << std::endl;

  return dnn_tensorflow->analyze(input);
  
}

void
MVAReader_emtight_v1::bindTree_(multidraw::FunctionLibrary& _library)
{  
  _library.bindBranch(cut_index, "cut_index");
  _library.bindBranch(detajj, "detajj");
  _library.bindBranch(detall, "detall_alias");
  _library.bindBranch(jetpt1, "jetpt1");
  _library.bindBranch(jetpt2, "jetpt2");
  _library.bindBranch(eta1, "eta1");
  _library.bindBranch(eta2, "eta2");
  _library.bindBranch(MET_pt, "MET_pt");
  _library.bindBranch(dphill, "dphill");
  _library.bindBranch(dphijj, "dphijj_alias");
  _library.bindBranch(Zlep1, "Zlep1");
  _library.bindBranch(Zlep2, "Zlep2");
  _library.bindBranch(mll, "mll");
  _library.bindBranch(btag_first, "btag_first");
  _library.bindBranch(btag_second, "btag_second");
  _library.bindBranch(dR_jl1, "dR_jl1");
  _library.bindBranch(dR_jl2, "dR_jl2");
}


#endif 