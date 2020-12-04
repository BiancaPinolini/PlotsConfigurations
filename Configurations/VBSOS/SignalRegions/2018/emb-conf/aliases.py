import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2018
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}

# imported from samples.py:
# samples, signals
mc = [skey for skey in samples if skey not in ('Fake', 'DATA', 'Dyemb')]
mc_emb = [skey for skey in samples if skey not in ('Fake', 'DATA')]

###### START ######

# AGGIORNARE VERSIONE DEL MODELLO IN ANALISI
model_version = 'v2/'

# distance between lepton and jet
aliases['R_j1l1'] = {
        'expr': 'TMath::Sqrt(TMath::Power(Alt$(CleanJet_eta[0],-9999.)-Alt$(Lepton_eta[0],-9999.),2)+TMath::Power(Alt$(CleanJet_phi[0],-9999.)-Alt$(Lepton_phi[0],-9999.),2))'
}

aliases['R_j2l1'] = {
        'expr': 'TMath::Sqrt(TMath::Power(Alt$(CleanJet_eta[1],-9999.)-Alt$(Lepton_eta[0],-9999.),2)+TMath::Power(Alt$(CleanJet_phi[1],-9999.)-Alt$(Lepton_phi[0],-9999.),2))'
}

aliases['R_j1l2'] = {
        'expr': 'TMath::Sqrt(TMath::Power(Alt$(CleanJet_eta[0],-9999.)-Alt$(Lepton_eta[1],-9999.),2)+TMath::Power(Alt$(CleanJet_phi[0],-9999.)-Alt$(Lepton_phi[1],-9999.),2))'
}

aliases['R_j2l2'] = {
        'expr': 'TMath::Sqrt(TMath::Power(Alt$(CleanJet_eta[1],-9999.)-Alt$(Lepton_eta[1],-9999.),2)+TMath::Power(Alt$(CleanJet_phi[1],-9999.)-Alt$(Lepton_phi[1],-9999.),2))'
}

# TRAINING VARIABLES
aliases['detall_al'] = {
    'expr': 'TMath::Abs(Alt$(Lepton_eta[0],-9999.)-Alt$(Lepton_eta[1],-9999.))'
}
aliases['jetpt1_al'] = {
    'expr': 'Alt$(CleanJet_pt[0],-9999.)'
}
aliases['jetpt2_al'] = {
    'expr': 'Alt$(CleanJet_pt[1],-9999.)'
}
aliases['eta1_al'] = {
    'expr': 'Alt$(Lepton_eta[0],-9999.)'
}
aliases['eta2_al'] = {
    'expr': 'Alt$(Lepton_eta[1],-9999.)'
}
aliases['dphijj_al'] = {
    'expr': 'TMath::Abs(Alt$(CleanJet_phi[0],-9999.)-Alt$(CleanJet_phi[1],-9999.))'
}

aliases['dR_jl1_al'] = {
    'expr': '(R_j1l1 < R_j2l1)*R_j1l1+(R_j1l1 >= R_j2l1)*R_j2l1'
}
aliases['dR_jl2_al'] = {
    'expr': '(R_j1l2 < R_j2l2)*R_j1l2+(R_j1l2 >= R_j2l2)*R_j2l2'
}

aliases['Zeppll_al'] = {
    'expr' : '0.5*TMath::Abs((Alt$(Lepton_eta[0],-9999.)+Alt$(Lepton_eta[1],-9999.))-(Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.)))'
}

aliases['Zepp1_al'] = {
    'expr' : 'Alt$(Lepton_eta[0],-9999.)-0.5*(Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))'
}
aliases['Zepp2_al'] = {
    'expr' : 'Alt$(Lepton_eta[1],-9999.)-0.5*(Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))'
}

aliases['btag_central_al'] = {
    'expr': ' (TMath::Abs(Alt$(CleanJet_eta[0],-9999.)) <= TMath::Abs(Alt$(CleanJet_eta[1],-9999.)))* Alt$(Jet_btagDeepB[CleanJet_jetIdx[0]], -9999.)  + (TMath::Abs(Alt$(CleanJet_eta[1],-9999.)) < TMath::Abs(Alt$(CleanJet_eta[0],-9999.))) * Alt$(Jet_btagDeepB[CleanJet_jetIdx[1]], -9999.)'
}

aliases['btag_forward_al']  = {
    'expr'  : '(TMath::Abs(Alt$(CleanJet_eta[0],-9999.)) > TMath::Abs(Alt$(CleanJet_eta[1],-9999.))) * Alt$(Jet_btagDeepB[CleanJet_jetIdx[0]], -9999.) + (TMath::Abs(Alt$(CleanJet_eta[1],-9999.)) >= TMath::Abs(Alt$(CleanJet_eta[0],-9999.))) * Alt$(Jet_btagDeepB[CleanJet_jetIdx[1]], -9999.)'
}

aliases['qgl_central'] = {
    'expr'  : '(TMath::Abs(Alt$(CleanJet_eta[0],-9999.)) <= TMath::Abs(Alt$(CleanJet_eta[1],-9999.))) * Alt$(Jet_qgl[CleanJet_jetIdx[0]],-9999.) + (TMath::Abs(Alt$(CleanJet_eta[1],-9999.)) < TMath::Abs(Alt$(CleanJet_eta[0],-9999.))) * Alt$(Jet_qgl[CleanJet_jetIdx[1]],-9999.)'
}
                        
aliases['qgl_forward'] = {
    'expr'  : '(TMath::Abs(Alt$(CleanJet_eta[0],-9999.)) > TMath::Abs(Alt$(CleanJet_eta[1],-9999.))) * Alt$(Jet_qgl[CleanJet_jetIdx[0]],-9999.) + (TMath::Abs(Alt$(CleanJet_eta[1],-9999.)) >= TMath::Abs(Alt$(CleanJet_eta[0],-9999.))) * Alt$(Jet_qgl[CleanJet_jetIdx[1]],-9999.)'
}

## Variables for DNN

aliases['bVeto'] = {
    'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.4184) == 0'
}

aliases['bReq'] = {
    'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.4184) >= 1'
}

aliases['zeroJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) < 30.'
}

## cuts

aliases['srr'] = {
    'expr':'bVeto && Zeppll_al < 1 && mth > 60'
}

aliases['topcr'] = {
     'expr': '((zeroJet && !bVeto) || bReq)'
}

aliases['dycr'] = {
     'expr': 'mth < 60 && bVeto && mll < 80'
}

## DNN

aliases['cut_index'] = {
    'expr': '1'
}

mva_reader_path = os.getenv('CMSSW_BASE') + '/src/PlotsConfigurations/Configurations/VBSOS/SignalRegions/2018/emb-conf/mva/'
models_path = '/eos/home-b/bpinolin/ML_output/VBSOS'

aliases['DNNoutput'] = {
    'class': 'MVAReader_sr_v2',
    'args': ( models_path +'/sr/models/' + model_version, False, 1),
    'linesToAdd':[
        'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        'gSystem->Load("libDNNEvaluator.so")',
        '.L ' + mva_reader_path + 'mvareader_sr_v2.cc+', 
    ],
}

###### END ######

eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'

aliases['LepWPCut'] = {
    'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP,
    'samples': mc_emb + ['DATA']
}

aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': 'VgS'
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': 'VgS'
}
aliases['embedtotal'] = {
    'expr': 'embed_total_WP90V1',  # wrt. eleWP
    'samples': 'Dyemb'
}


######## OLD
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

#nCleanGenJet
aliases['nCleanGenJet'] = {
    'linesToAdd': ['.L %s/src/PlotsConfigurations/Configurations/Differential/ngenjet.cc+' % os.getenv('CMSSW_BASE')],
    'class': 'CountGenJet',
    'samples': mc
}

# PostProcessing did not create (anti)topGenPt for ST samples with _ext1
lastcopy = (1 << 13)

aliases['isTTbar'] = {
    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 2' % lastcopy,
    'samples': ['top','Dyveto']
}

aliases['isSingleTop'] = {
    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 1' % lastcopy,
    'samples': ['top','Dyveto']
}

aliases['topGenPtOTF'] = {
   'expr': 'Sum$((GenPart_pdgId == 6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
   'samples': ['top']
}

aliases['antitopGenPtOTF'] = {
   'expr': 'Sum$((GenPart_pdgId == -6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
   'samples': ['top']
}

aliases['Top_pTrw'] = {
    'expr': 'isTTbar * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPtOTF) * TMath::Exp(0.0615 - 0.0005 * antitopGenPtOTF))) + isSingleTop',
    'samples': ['top', 'DYveto']
}

handle = open('%s/src/PlotsConfigurations/Configurations/patches/DYrew.py' % os.getenv('CMSSW_BASE'),'r')
exec(handle)
handle.close()
aliases['DY_NLO_pTllrw'] = {
    #'expr': '1',
    'expr': '('+DYrew['2018']['NLO'].replace('x', 'gen_ptll')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY', 'DYtt']
}

aliases['DY_LO_pTllrw'] = {
    #'expr': '1',
    'expr': '('+DYrew['2018']['LO'].replace('x', 'gen_ptll')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY', 'DYtt']
}

# Jet bins
# using Alt$(CleanJet_pt[n], 0) instead of Sum$(CleanJet_pt >= 30) because jet pt ordering is not strictly followed in JES-varied samples

# No jet with pt > 30 GeV
# aliases['zeroJet'] = {
#     'expr': 'Alt$(CleanJet_pt[0], 0) < 30.'
# }

aliases['oneJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) > 30.'
}

aliases['multiJet'] = {
    'expr': 'Alt$(CleanJet_pt[1], 0) > 30.'
}


# B tag scale factors

aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}

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

# data/MC scale factors
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l', 'LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'LepWPCut', 'btagSF']),
    'samples': mc
}
# variations
aliases['SFweightEleUp'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Up',
    'samples': mc_emb
}
aliases['SFweightEleDown'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Do',
    'samples': mc_emb
}
aliases['SFweightMuUp'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Up',
    'samples': mc_emb
}
aliases['SFweightMuDown'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Do',
    'samples': mc_emb
}