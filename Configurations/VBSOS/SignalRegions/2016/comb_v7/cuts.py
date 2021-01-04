# cuts

supercut = '   mll>50 \
            && Lepton_pt[0]>25 \
            && Lepton_pt[1]>13 \
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && ptll>30 \
            && PuppiMET_pt > 20 \
            && Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*13 \
            && mjj > 220 \
            && detajj > 2 \
            && multiJet \
           '

##signal region
cuts['sr'] = {
   'expr': 'bVeto && mth > 60',
   'categories' : {
      'lowZ'   : 'Zeppll_al < 1', 
      'highZ'  : 'Zeppll_al >=1',
    }
}    

# Top control region
cuts['topcr']  = {
   'expr': '((zeroJet && !bVeto) || bReq)'
   'categories' : {
      'lowZ'   : 'Zeppll_al < 1', 
      'highZ'  : 'Zeppll_al >=1',
    }
}

# DY control region
cuts['dycr'] = {
   'expr': 'mth < 60 && bVeto && mll < 80'
   'categories' : {
      'lowZ'   : 'Zeppll_al < 1', 
      'highZ'  : 'Zeppll_al >=1',
    }
}