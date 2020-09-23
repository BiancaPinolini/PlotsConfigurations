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

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

###### START ######

# AGGIORNARE VERSIONE DEL MODELLO IN ANALISI
model_version = 'v4/'

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
    'expr' : '0.5*fabs((Lepton_eta[0]+Lepton_eta[1])-(Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.)))'
}
aliases['Zepp1_al'] = {
    'expr' : 'Lepton_eta[0]-0.5*(Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))'
}
aliases['Zepp2_al'] = {
    'expr' : 'Lepton_eta[1]-0.5*(Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))'
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
# aliases['bVetoForward'] = {
#     'expr': '(pT_forward>20. && eta_forward<2.5 && btag_forward>0.1241)==0',
#     'samples': mc + ['DATA']
# }
# aliases['bReqForward'] = {
#     'expr': '(pT_forward > 30. && eta_forward < 2.5 && btag_forward > 0.1241) >= 1'
# }

aliases['qgl_forward'] = {
    'expr'  : '(fabs(Alt$(CleanJet_eta[0],-9999.)) > fabs(Alt$(CleanJet_eta[1],-9999.))) * Alt$(Jet_qgl[0],-9999.) + (fabs(Alt$(CleanJet_eta[1],-9999.)) >= fabs(Alt$(CleanJet_eta[0],-9999.))) * Alt$(Jet_qgl[1],-9999.)',
    'samples': mc + ['DATA']
}
aliases['qgl_central'] = {
    'expr'  : '(fabs(Alt$(CleanJet_eta[0],-9999.)) > fabs(Alt$(CleanJet_eta[1],-9999.))) * Alt$(Jet_qgl[1],-9999.) + (fabs(Alt$(CleanJet_eta[1],-9999.)) >= fabs(Alt$(CleanJet_eta[0],-9999.))) * Alt$(Jet_qgl[0],-9999.)',
    'samples': mc + ['DATA']
}


aliases['bVeto'] = {
    #'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1241) == 0'
    'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.4184) == 0'
}

aliases['cut_index'] = {
    'expr': '1',
    'samples': mc + ['DATA']
}

mva_reader_path = os.getenv('CMSSW_BASE') + '/src/PlotsConfigurations/Configurations/VBSOS/SignalRegions/2018/mva/'
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

# # Fake leptons transfer factor 
# aliases['fakeW'] = {
#     'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP,
#     'samples': ['Fake']
# }
# # And variations - already divided by central values in formulas !
# aliases['fakeWEleUp'] = {
#     'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleUp',
#     'samples': ['Fake']
# }
# aliases['fakeWEleDown'] = {
#     'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleDown',
#     'samples': ['Fake']
# }
# aliases['fakeWMuUp'] = {
#     'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuUp',
#     'samples': ['Fake']
# }
# aliases['fakeWMuDown'] = {
#     'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuDown',
#     'samples': ['Fake']
# }
# aliases['fakeWStatEleUp'] = {
#     'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleUp',
#     'samples': ['Fake']
# }
# aliases['fakeWStatEleDown'] = {
#     'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleDown',
#     'samples': ['Fake']
# }
# aliases['fakeWStatMuUp'] = {
#     'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuUp',
#     'samples': ['Fake']
# }
# aliases['fakeWStatMuDown'] = {
#     'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuDown',
#     'samples': ['Fake']
# }

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
    'samples': ['top']
}

aliases['isSingleTop'] = {
    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 1' % lastcopy,
    'samples': ['top']
}

aliases['Top_pTrw'] = {
    'expr': 'isTTbar * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPt) * TMath::Exp(0.0615 - 0.0005 * antitopGenPt))) + isSingleTop',
    'samples': ['top']
}

handle = open('%s/src/PlotsConfigurations/Configurations/patches/DYrew.py' % os.getenv('CMSSW_BASE'),'r')
exec(handle)
handle.close()
aliases['DY_NLO_pTllrw'] = {
    #'expr': '1',
    'expr': '('+DYrew['2018']['NLO'].replace('x', 'gen_ptll')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}

aliases['DY_LO_pTllrw'] = {
    #'expr': '1',
    'expr': '('+DYrew['2018']['LO'].replace('x', 'gen_ptll')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}

# Jet bins
# using Alt$(CleanJet_pt[n], 0) instead of Sum$(CleanJet_pt >= 30) because jet pt ordering is not strictly followed in JES-varied samples

# No jet with pt > 30 GeV
aliases['zeroJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) < 30.'
}

aliases['oneJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) > 30.'
}

aliases['multiJet'] = {
    'expr': 'Alt$(CleanJet_pt[1], 0) > 30.'
}

# B tagging

aliases['bReq'] = {
    # 'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1241) >= 1'
    'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.4184) >= 1'
}

# CR definitions

aliases['topcr'] = {
    'expr': 'mjj > 200 && detajj > 2 && Zeppll_al < 1 && mth > 60 && ((zeroJet && !bVeto) || bReq)'
}

# SR definition

aliases['sr'] = {
    'expr': 'mjj > 200 && detajj > 2 && Zeppll_al < 1 && mth > 60 && bVeto'
}

aliases['centralVeto'] = {
    'expr': 'Sum$(CleanJet_pt > 30 && CleanJet_eta > TMath::Min(CleanJet_eta[0], CleanJet_eta[1]) && CleanJet_eta < TMath::Max(CleanJet_eta[0], CleanJet_eta[1]) && abs(CleanJet_eta - CleanJet_eta[0]) > 1 && abs(CleanJet_eta - CleanJet_eta[1]) > 1) == 0'        
}

# B tag scale factors

#btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_102XSF_V1.csv' % os.getenv('CMSSW_BASE')
#
#aliases['Jet_btagSF_shapeFix'] = {
#    'linesToAdd': [
#        'gSystem->Load("libCondFormatsBTauObjects.so");',
#        'gSystem->Load("libCondToolsBTau.so");',
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
#        '.L %s/patches/btagsfpatch.cc+' % configurations
#    ],
#    'class': 'BtagSF',
#    'args': (btagSFSource,),
#    'samples': mc
#}

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
    #aliases['Jet_btagSF_shape_up_%s' % shift] = {
    #    'class': 'BtagSF',
    #    'args': (btagSFSource, 'up_' + shift),
    #    'samples': mc
    #}
    #aliases['Jet_btagSF_shape_down_%s' % shift] = {
    #    'class': 'BtagSF',
    #    'args': (btagSFSource, 'down_' + shift),
    #    'samples': mc
    #}

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

#puidSFSource = '%s/src/LatinoAnalysis/NanoGardener/python/data/JetPUID_effcyandSF.root' % os.getenv('CMSSW_BASE')
#
#aliases['PUJetIdSF'] = {
#    'linesToAdd': [
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
#        '.L %s/patches/pujetidsf_event.cc+' % configurations
#    ],
#    'class': 'PUJetIdEventSF',
#    'args': (puidSFSource, '2018', 'loose'),
#    'samples': mc
#}

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
