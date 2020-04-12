# cuts

#cuts = {}
### supercut is added to all the other cuts

supercut = 'mll>50  \
            && ptll > 30 \
            && (Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*13 || Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*11 || Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-13*13)\
            && Lepton_pt[0]>25 \
            && Lepton_pt[1]>10 \
            && Alt$(Lepton_pt[2],0.)<10 \
            && (MET_pt > 20 || PuppiMET_pt>20) \
            && Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*13 \
            && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 \
'   

##signal region personalized
cuts['em_loose'] = 'em_loose'

cuts['em_medium'] = 'em_medium'

cuts['em_tight'] = 'em_tight'
