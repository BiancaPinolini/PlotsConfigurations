import os
import copy
import inspect



configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2016
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}

# imported from samples.py:
# samples, signals
mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

# distance between lepton and jet
aliases['R_j1l1'] = {
        'expr': 'TMath::Sqrt(TMath::Power(Alt$(CleanJet_eta[0],-9999.)-Lepton_eta[0],2)+TMath::Power(Alt$(CleanJet_phi[0],-9999.)-Lepton_phi[0],2))',
        'samples': mc + ['DATA']
}

aliases['R_j2l1'] = {
        'expr': 'TMath::Sqrt(TMath::Power(Alt$(CleanJet_eta[1],-9999.)-Lepton_eta[0],2)+TMath::Power(Alt$(CleanJet_phi[1],-9999.)-Lepton_phi[0],2))',
        'samples': mc + ['DATA']
}

aliases['R_j1l2'] = {
        'expr': 'TMath::Sqrt(TMath::Power(Alt$(CleanJet_eta[0],-9999.)-Lepton_eta[1],2)+TMath::Power(Alt$(CleanJet_phi[0],-9999.)-Lepton_phi[1],2))',
        'samples': mc + ['DATA']
}

aliases['R_j2l2'] = {
        'expr': 'TMath::Sqrt(TMath::Power(Alt$(CleanJet_eta[1],-9999.)-Lepton_eta[1],2)+TMath::Power(Alt$(CleanJet_phi[1],-9999.)-Lepton_phi[1],2))',
        'samples': mc + ['DATA']
}

# variables
aliases['detall_al'] = {
    'expr': 'fabs(Lepton_eta[0]-Lepton_eta[1])',
    'samples': mc + ['DATA']
}
aliases['jetpt1_al'] = {
    'expr': 'Alt$(CleanJet_pt[0],-9999.)',
    'samples': mc + ['DATA']
}
aliases['jetpt2_al'] = {
    'expr': 'Alt$(CleanJet_pt[1],-9999.)',
    'samples': mc + ['DATA']
}
aliases['eta1_al'] = {
    'expr': 'Lepton_eta[0]',
    'samples': mc + ['DATA']
}
aliases['eta2_al'] = {
    'expr': 'Lepton_eta[1]',
    'samples': mc + ['DATA']
}
aliases['dphijj_al'] = {
    'expr': 'fabs(Alt$(CleanJet_phi[0],-9999.)-Alt$(CleanJet_phi[1],-9999.))',
    'samples': mc + ['DATA']
}
aliases['btag_central_al'] = {
    'expr': ' (fabs(Alt$(CleanJet_eta[0],-9999.)) <= fabs(Alt$(CleanJet_eta[1],-9999.)))* Jet_btagDeepB[CleanJet_jetIdx[0]] + (fabs(Alt$(CleanJet_eta[1],-9999.)) < fabs(Alt$(CleanJet_eta[0],-9999.))) * Jet_btagDeepB[CleanJet_jetIdx[1]]',
    'samples': mc + ['DATA']
}

aliases['dR_jl1_al'] = {
    'expr': '(R_j1l1 < R_j2l1)*R_j1l1+(R_j1l1 >= R_j2l1)*R_j2l1',
    'samples': mc + ['DATA']
}
aliases['dR_jl2_al'] = {
    'expr': '(R_j1l2 < R_j2l2)*R_j1l2+(R_j1l2 >= R_j2l2)*R_j2l2',
    'samples': mc + ['DATA']
}

# Zeppenfeld variables
aliases['Zeppll_al'] = {
    'expr' : '0.5*fabs((Lepton_eta[0]+Lepton_eta[1])-(CleanJet_eta[0]+CleanJet_eta[1]))'
}
aliases['Zepp1_al'] = {
    'expr' : 'Lepton_eta[0]-0.5*(CleanJet_eta[0]+CleanJet_eta[1])'
}
aliases['Zepp2_al'] = {
    'expr' : 'Lepton_eta[1]-0.5*(CleanJet_eta[0]+CleanJet_eta[1])'
}

# bVeto forward
aliases['pT_forward']  = {
    'expr'  : '(fabs(Alt$(CleanJet_eta[0],-9999.)) > fabs(Alt$(CleanJet_eta[1],-9999.))) * Alt$(CleanJet_pt[0],-9999.) + (fabs(Alt$(CleanJet_eta[1],-9999.)) >= fabs(Alt$(CleanJet_eta[0],-9999.))) * Alt$(CleanJet_pt[1],-9999.)',
    'samples': mc + ['DATA']
}
aliases['eta_forward']  = {
    'expr'  : '(fabs(Alt$(CleanJet_eta[0],-9999.)) > fabs(Alt$(CleanJet_eta[1],-9999.))) * abs(Alt$(CleanJet_eta[0],-9999.)) + (fabs(Alt$(CleanJet_eta[1],-9999.)) >= fabs(Alt$(CleanJet_eta[0],-9999.))) * abs(Alt$(CleanJet_eta[1],-9999.))',
    'samples': mc + ['DATA']
}
aliases['btag_forward']  = {
    'expr'  : '(fabs(Alt$(CleanJet_eta[0],-9999.)) > fabs(Alt$(CleanJet_eta[1],-9999.))) * Jet_btagDeepB[CleanJet_jetIdx[0]] + (fabs(Alt$(CleanJet_eta[1],-9999.)) >= fabs(Alt$(CleanJet_eta[0],-9999.))) * Jet_btagDeepB[CleanJet_jetIdx[1]]',
    'samples': mc + ['DATA']
}
aliases['bVetoForward'] = {
    'expr': '(pT_forward>20. && eta_forward<2.5 && btag_forward>0.1241)==0',
    'samples': mc + ['DATA']
}

# DNN output
aliases['cut_index'] = {
    'expr': '1',
    'samples': mc + ['DATA']
}
mva_reader_path = os.getenv('CMSSW_BASE') + '/src/PlotsConfigurations/Configurations/VBSOS/SignalRegions/2018/mva/'
models_path = '/eos/home-b/bpinolin/ML_output/VBSOS'

aliases['DNNoutput'] = {
    'class': 'MVAReader_sr_v1',
    'args': ( models_path +'/sr/models/v1/', False, 1),
    'linesToAdd':[
        'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        'gSystem->Load("libDNNEvaluator.so")',
        '.L ' + mva_reader_path + 'mvareader_sr_v1.cc+', 
    ],
}

eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'

aliases['LepWPCut'] = {
    'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP,
    'samples': mc + ['DATA']
}

aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': 'VgS'
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': 'VgS'
}

# Fake leptons transfer factor 
aliases['fakeW'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP,
    'samples': ['Fake']
}
# And variations - already divided by central values in formulas !
aliases['fakeWEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleUp',
    'samples': ['Fake']
}
aliases['fakeWEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleDown',
    'samples': ['Fake']
}
aliases['fakeWMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuUp',
    'samples': ['Fake']
}
aliases['fakeWMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuDown',
    'samples': ['Fake']
}
aliases['fakeWStatEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleUp',
    'samples': ['Fake']
}
aliases['fakeWStatEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleDown',
    'samples': ['Fake']
}
aliases['fakeWStatMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuUp',
    'samples': ['Fake']
}
aliases['fakeWStatMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuDown',
    'samples': ['Fake']
}

# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1], 0)',
    'samples': mc
}

# PostProcessing did not create (anti)topGenPt for ST samples with _ext1
lastcopy = (1 << 13)

aliases['isTTbar'] = {
    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 2' % lastcopy,
    'samples': ['top']
}

aliases['isSingleTop'] = {
    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 1' % lastcopy,
    'samples': ['top']
}

# aliases['topGenPtOTF'] = {
#     'expr': 'Sum$((GenPart_pdgId == 6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
#     'samples': ['top']
# }

# aliases['antitopGenPtOTF'] = {
#     'expr': 'Sum$((GenPart_pdgId == -6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
#     'samples': ['top']
# }

aliases['Top_pTrw'] = {
    'expr': 'isTTbar * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPt) * TMath::Exp(0.0615 - 0.0005 * antitopGenPt))) + isSingleTop',
    'samples': ['top']
}
# Jet bins
# using Alt$(CleanJet_pt[n], 0) instead of Sum$(CleanJet_pt >= 30) because jet pt ordering is not strictly followed in JES-varied samples

#bjet
# No jet with pt > 30 GeV
aliases['zeroJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) < 30.'
}

# ==1 jet with pt > 30 GeV
aliases['oneJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) >= 30. && Alt$(CleanJet_pt[1], 0) < 30.'
}

# ==2 jets with pt > 30 GeV
aliases['twoJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) >= 30. && Alt$(CleanJet_pt[1], 0) >= 30. && Alt$(CleanJet_pt[2], 0) < 30.'
}

# >=2 jets with pt > 30 GeV
aliases['multiJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) >= 30. && Alt$(CleanJet_pt[1], 0) >= 30.'
}


#bVeto and central veto

aliases['centralVeto'] = {
    'expr': 'Sum$(CleanJet_pt > 30 && CleanJet_eta > TMath::Min(CleanJet_eta[0], CleanJet_eta[1]) && CleanJet_eta < TMath::Max(CleanJet_eta[0], CleanJet_eta[1]) && abs(CleanJet_eta - CleanJet_eta[0]) > 1 && abs(CleanJet_eta - CleanJet_eta[1]) > 1)==0'
}

aliases['bVeto'] = {
    'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1241) == 0'
    #'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.4184) == 0'
}

# aliases['bVetoT'] = {
#     'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] >  0.7527  ) == 0'
# }

#bReq

aliases['bReq'] = {
    'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1241) >= 1'
    #'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.4184) >= 1'
}



# B tagging
aliases['btag0'] = {
    'expr': 'zeroJet && !bVeto'
}

aliases['btag1'] = {
    'expr': 'oneJet && bReq'
}

aliases['btag2'] = {
    'expr': 'twoJet && bReq'
}

# CR definitions

aliases['topcr'] = {
      'expr': '((zeroJet && !bVeto) || bReq) && !bVetoForward'
}

# aliases['dycr'] = {
#     'expr': 'mth<60 && mll>70 && mll<120 && bVeto'
# }

# aliases['wwcr'] = {
#     'expr': 'mth>60 && mtw2>30 && mll>100 && bVeto'
# }

# SR definition

aliases['sr'] = {
    'expr': 'mjj > 200 && fabs(detajj) > 2 && mth > 60 && bVetoForward'
}

# B tag scale factors
aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}

# aliases['btag0SF'] = {
#     #'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && CleanJet_pt<30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || CleanJet_pt>30 || abs(CleanJet_eta)>2.5))))',
#     'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && CleanJet_pt<30 && abs(CleanJet_eta)<2.5)*Jet_btagSF[CleanJet_jetIdx]+1*(CleanJet_pt<20 || CleanJet_pt>30 || abs(CleanJet_eta)>2.5))))',
#     'samples': mc
# }

# aliases['btagnSF'] = {
#     #'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx] + (CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
#     'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF[CleanJet_jetIdx] + (CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
#     'samples': mc
# }

aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx]+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}

aliases['btagSF'] = {
    'expr': '(bVeto || (topcr && zeroJet))*bVetoSF + (topcr && !zeroJet)*bReqSF',
    'samples': mc
}

for shift in ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']:

    for targ in ['bVeto', 'bReq']:
        alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_up_%s' % shift)

        alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_down_%s' % shift)

    aliases['btagSF%sup' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
        'samples': mc
    }

    aliases['btagSF%sdown' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
        'samples': mc
    }
# PU jet Id SF

puidSFSource = '%s/src/LatinoAnalysis/NanoGardener/python/data/JetPUID_effcyandSF.root' % os.getenv('CMSSW_BASE')

aliases['PUJetIdSF'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
        '.L %s/patches/pujetidsf_event.cc+' % configurations
    ],
    'class': 'PUJetIdEventSF',
    'args': (puidSFSource, '2018', 'loose'),
    'samples': mc
}

# data/MC scale factors
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l', 'LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'LepWPCut', 'btagSF']),
    'samples': mc
}

# variations
aliases['SFweightEleUp'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Up',
    'samples': mc
}
aliases['SFweightEleDown'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Do',
    'samples': mc
}
aliases['SFweightMuUp'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Up',
    'samples': mc
}
aliases['SFweightMuDown'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Do',
    'samples': mc
}

# In WpWmJJ_EWK events, partons [0] and [1] are always the decay products of the first W
# aliases['lhe_mW1'] = {
#     'expr': 'TMath::Sqrt(2. * LHEPart_pt[0] * LHEPart_pt[1] * (TMath::CosH(LHEPart_eta[0] - LHEPart_eta[1]) - TMath::Cos(LHEPart_phi[0] - LHEPart_phi[1])))',
#     'samples': ['WWewk_limW']
# }

# # and [2] [3] are the second W
# aliases['lhe_mW2'] = {
#     'expr': 'TMath::Sqrt(2. * LHEPart_pt[2] * LHEPart_pt[3] * (TMath::CosH(LHEPart_eta[2] - LHEPart_eta[3]) - TMath::Cos(LHEPart_phi[2] - LHEPart_phi[3])))',
#     'samples': ['WWewk_limW']
# }