void countevents() {

    Double_t Sum = 0;

    for(Int_t i = 0; i <= 11; i++){

        char buffer[10];

	std::cout << "i = " << i << std::endl;

        sprintf(buffer, "%d", i);

	char str[200];

	strcpy (str,"/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6/nanoLatino_ST_tW_top_ext1__part");

	strcat (str, buffer);

        strcat (str,".root");

        TFile *f = new TFile(str, "READ");
        TTree *T = (TTree*)f->Get("Runs");
        Double_t N;
        T->SetBranchAddress("genEventSumw_",&N);
        T->GetEntry(0);
        std::cout << N << std::endl;

	Sum = Sum + N;

    }

    std::cout << "Somma = " << Sum << std::endl;
    
}
