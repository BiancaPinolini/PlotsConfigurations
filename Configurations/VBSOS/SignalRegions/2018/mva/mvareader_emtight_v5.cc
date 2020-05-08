#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "NNEvaluation/DNNTensorflow/interface/DNNEvaluator.hh"

#include "TMath.h"

#include <cmath>
#include <string>
#include <iostream>

using namespace std;
using namespace NNEvaluation;

#ifndef MVAReader_emtight_v5_H
#define MVAReader_emtight_v5_H

class MVAReader_emtight_v5 : public multidraw::TTreeFunction {
public:
  
  MVAReader_emtight_v5(const char* model_path, bool verbose, int cut);

  char const* getName() const override { return "MVAReader_emtight_v5"; }
  TTreeFunction* clone() const override { return new MVAReader_emtight_v5(model_path_.c_str(), verbose, cut_); }

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
  TTreeReaderValue<Double_t>* eta1{};
  TTreeReaderValue<Double_t>* eta2{};
};


MVAReader_emtight_v5::MVAReader_emtight_v5(const char* model_path, bool verbose, int cut):
    model_path_(model_path), 
    verbose(verbose),
    cut_(cut)
{
    dnn_tensorflow = new DNNEvaluator(model_path_, verbose);
}


double 
MVAReader_emtight_v5::evaluate(unsigned)
{
  // Run only if 
  if ((int)(*(cut_index->Get())) != cut_) {
    return -999.;
  }

  std::vector<float> input{};

  input.push_back( TMath::Abs(*(detajj->Get())));
  input.push_back( *(eta1->Get()) );
  input.push_back( *(eta2->Get()) );

  // std::cout << "output = " << dnn_tensorflow->analyze(input) << std::endl;

  return dnn_tensorflow->analyze(input);
  
}

void
MVAReader_emtight_v5::bindTree_(multidraw::FunctionLibrary& _library)
{  
  _library.bindBranch(cut_index, "cut_index");
  _library.bindBranch(detajj, "detajj");
  _library.bindBranch(eta1, "eta1");
  _library.bindBranch(eta2, "eta2");
}


#endif 
