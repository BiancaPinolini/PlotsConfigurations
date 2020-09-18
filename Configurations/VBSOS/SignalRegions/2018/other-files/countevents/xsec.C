void xsec() {

    TFile *f = new TFile("/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6/nanoLatino_WpWmJJ_EWK_noTop__part0.root", "READ");

    TTree *T = (TTree*)f->Get("Events");
    Float_t xsec;
    T->SetBranchAddress("Xsec",&xsec);
    T->GetEntry(0);
    std::cout << xsec << std::endl;

}



