import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2016
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}

# imported from samples.py:
# samples, signals

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]
btag_algo="deepcsv"#deepcsv

###### START ######

# AGGIORNARE VERSIONE DEL MODELLO IN ANALISI
model_version = 'v0/'

# distance between lepton and jet
aliases['R_j1l1'] = {
        'expr': 'TMath::Sqrt(TMath::Power(Alt$(CleanJet_eta[0],-9999.)-Lepton_eta[0],2)+TMath::Power(Alt$(CleanJet_phi[0],-9999.)-Lepton_phi[0],2))'
}

aliases['R_j2l1'] = {
        'expr': 'TMath::Sqrt(TMath::Power(Alt$(CleanJet_eta[1],-9999.)-Lepton_eta[0],2)+TMath::Power(Alt$(CleanJet_phi[1],-9999.)-Lepton_phi[0],2))'
}

aliases['R_j1l2'] = {
        'expr': 'TMath::Sqrt(TMath::Power(Alt$(CleanJet_eta[0],-9999.)-Lepton_eta[1],2)+TMath::Power(Alt$(CleanJet_phi[0],-9999.)-Lepton_phi[1],2))'
}

aliases['R_j2l2'] = {
        'expr': 'TMath::Sqrt(TMath::Power(Alt$(CleanJet_eta[1],-9999.)-Lepton_eta[1],2)+TMath::Power(Alt$(CleanJet_phi[1],-9999.)-Lepton_phi[1],2))'
}

# TRAINING VARIABLES
aliases['detall_al'] = {
    'expr': 'fabs(Lepton_eta[0]-Lepton_eta[1])'
}
aliases['jetpt1_al'] = {
    'expr': 'Alt$(CleanJet_pt[0],-9999.)'
}
aliases['jetpt2_al'] = {
    'expr': 'Alt$(CleanJet_pt[1],-9999.)'
}
aliases['eta1_al'] = {
    'expr': 'Lepton_eta[0]'
}
aliases['eta2_al'] = {
    'expr': 'Lepton_eta[1]'
}
aliases['dphijj_al'] = {
    'expr': 'fabs(Alt$(CleanJet_phi[0],-9999.)-Alt$(CleanJet_phi[1],-9999.))'
}

aliases['dR_jl1_al'] = {
    'expr': '(R_j1l1 < R_j2l1)*R_j1l1+(R_j1l1 >= R_j2l1)*R_j2l1'
}
aliases['dR_jl2_al'] = {
    'expr': '(R_j1l2 < R_j2l2)*R_j1l2+(R_j1l2 >= R_j2l2)*R_j2l2'
}

aliases['Zeppll_al'] = {
    'expr' : '0.5*fabs((Lepton_eta[0]+Lepton_eta[1])-(Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.)))'
}
aliases['Zepp1_al'] = {
    'expr' : 'Lepton_eta[0]-0.5*(Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))'
}
aliases['Zepp2_al'] = {
    'expr' : 'Lepton_eta[1]-0.5*(Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))'
}

aliases['btag_central_al'] = {
    'expr': ' (fabs(Alt$(CleanJet_eta[0],-9999.)) <= fabs(Alt$(CleanJet_eta[1],-9999.)))* Jet_btagDeepB[CleanJet_jetIdx[0]] + (fabs(Alt$(CleanJet_eta[1],-9999.)) < fabs(Alt$(CleanJet_eta[0],-9999.))) * Jet_btagDeepB[CleanJet_jetIdx[1]]'
}

aliases['btag_forward_al']  = {
    'expr'  : '(fabs(Alt$(CleanJet_eta[0],-9999.)) > fabs(Alt$(CleanJet_eta[1],-9999.))) * Jet_btagDeepB[CleanJet_jetIdx[0]] + (fabs(Alt$(CleanJet_eta[1],-9999.)) >= fabs(Alt$(CleanJet_eta[0],-9999.))) * Jet_btagDeepB[CleanJet_jetIdx[1]]'
}

aliases['qgl_central'] = {
    'expr'  : '(fabs(Alt$(CleanJet_eta[0],-9999.)) > fabs(Alt$(CleanJet_eta[1],-9999.))) * Alt$(Jet_qgl[0],-9999.) + (fabs(Alt$(CleanJet_eta[1],-9999.)) >= fabs(Alt$(CleanJet_eta[0],-9999.))) * Alt$(Jet_qgl[1],-9999.)'
}

aliases['qgl_forward'] = {
    'expr'  : '(fabs(Alt$(CleanJet_eta[0],-9999.)) <= fabs(Alt$(CleanJet_eta[1],-9999.))) * Alt$(Jet_qgl[0],-9999.) + (fabs(Alt$(CleanJet_eta[1],-9999.)) < fabs(Alt$(CleanJet_eta[0],-9999.))) * Alt$(Jet_qgl[1],-9999.)'
}

aliases['area_central'] = {
    'expr'  : '(fabs(Alt$(CleanJet_eta[0],-9999.)) > fabs(Alt$(CleanJet_eta[1],-9999.))) * Alt$(Jet_area[0],-9999.) + (fabs(Alt$(CleanJet_eta[1],-9999.)) >= fabs(Alt$(CleanJet_eta[0],-9999.))) * Alt$(Jet_area[1],-9999.)'
}

aliases['area_forward'] = {
    'expr'  : '(fabs(Alt$(CleanJet_eta[0],-9999.)) <= fabs(Alt$(CleanJet_eta[1],-9999.))) * Alt$(Jet_area[0],-9999.) + (fabs(Alt$(CleanJet_eta[1],-9999.)) < fabs(Alt$(CleanJet_eta[0],-9999.))) * Alt$(Jet_area[1],-9999.)'
}

aliases['Jet_nConst_central'] = {
    'expr'  : '(fabs(Alt$(CleanJet_eta[0],-9999.)) > fabs(Alt$(CleanJet_eta[1],-9999.))) * Alt$(Jet_nConstituents[0],-9999.) + (fabs(Alt$(CleanJet_eta[1],-9999.)) >= fabs(Alt$(CleanJet_eta[0],-9999.))) * Alt$(Jet_nConstituents[1],-9999.)'
}

aliases['Jet_nConst_forward'] = {
    'expr'  : '(fabs(Alt$(CleanJet_eta[0],-9999.)) <= fabs(Alt$(CleanJet_eta[1],-9999.))) * Alt$(Jet_nConstituents[0],-9999.) + (fabs(Alt$(CleanJet_eta[1],-9999.)) < fabs(Alt$(CleanJet_eta[0],-9999.))) * Alt$(Jet_nConstituents[1],-9999.)'
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

aliases['srr'] = {
    'expr':'bVeto && Zeppll_al < 1 && mth > 60'
}

aliases['topcr'] = {
     'expr': '((zeroJet && !bVeto) || bReq)'
}

aliases['btag_central_DNN'] = {
    'expr': ' topcr * 0.7 + (!topcr) * ((fabs(Alt$(CleanJet_eta[0],-9999.)) <= fabs(Alt$(CleanJet_eta[1],-9999.)))* Jet_btagDeepB[CleanJet_jetIdx[0]] + (fabs(Alt$(CleanJet_eta[1],-9999.)) < fabs(Alt$(CleanJet_eta[0],-9999.))) * Jet_btagDeepB[CleanJet_jetIdx[1]])'
}

aliases['btag_forward_DNN']  = {
    'expr'  : 'topcr * 0.7 + (!topcr) *((fabs(Alt$(CleanJet_eta[0],-9999.)) > fabs(Alt$(CleanJet_eta[1],-9999.))) * Jet_btagDeepB[CleanJet_jetIdx[0]] + (fabs(Alt$(CleanJet_eta[1],-9999.)) >= fabs(Alt$(CleanJet_eta[0],-9999.))) * Jet_btagDeepB[CleanJet_jetIdx[1]])'
}

aliases['Zeppll_DNN'] = {
    'expr' : '(!srr) * 0.5 + srr *(0.5*fabs((Lepton_eta[0]+Lepton_eta[1])-(Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))))'
}

## DNN

aliases['cut_index'] = {
    'expr': '1'
}

mva_reader_path = os.getenv('CMSSW_BASE') + '/src/PlotsConfigurations/Configurations/VBSOS/SignalRegions/2016/mva/'
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

eleWP = 'mva_90p_Iso2016'
muWP = 'cut_Tight80x'

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

aliases['Top_pTrw'] = {
    'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPt) * TMath::Exp(0.0615 - 0.0005 * antitopGenPt))) + (topGenPt * antitopGenPt <= 0.)',
    'samples': ['top']
}

aliases['nCleanGenJet'] = {
    'linesToAdd': ['.L %s/src/PlotsConfigurations/Configurations/Differential/ngenjet.cc+' % os.getenv('CMSSW_BASE')],
    'class': 'CountGenJet',
    'samples': mc
}

handle = open('%s/src/PlotsConfigurations/Configurations/patches/DYrew.py' % os.getenv('CMSSW_BASE'),'r')
exec(handle)
handle.close()
aliases['DY_NLO_pTllrw'] = {
    #'expr': '1',
    'expr': '('+DYrew['2016']['NLO'].replace('x', 'gen_ptll')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}
aliases['DY_LO_pTllrw'] = {
    #'expr': '1',
    'expr': '('+DYrew['2016']['LO'].replace('x', 'gen_ptll')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
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

# B tagging
# if btag_algo == "deepcsv":
#     aliases['bVeto'] = {
#         'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.4184) == 0'
#     }

#     aliases['bReq'] = {
#         'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.4184) >= 1'
#     }
# elif btag_algo == "deepflav":
#     aliases['bVeto'] = {
#         'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepFlavB[CleanJet_jetIdx] >  0.0614) == 0'
#     }        
    
#     aliases['bReq'] = {
#         'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepFlavB[CleanJet_jetIdx] >  0.0614) >= 1'
#     }

# Flavour definitions

# aliases['SameFlav'] = {
#     'expr': '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)',
#     'samples': mc
# }

# aliases['DiffFlav'] = {
#     'expr': 'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
#     'samples': mc
# }

# CR definitions

# aliases['topcr'] = {
#     'expr': '((zeroJet && !bVeto) || bReq)'
# }

# aliases['centralVeto'] = {
#     'expr': 'Sum$(CleanJet_pt > 30 && CleanJet_eta > TMath::Min(CleanJet_eta[0], CleanJet_eta[1]) && CleanJet_eta < TMath::Max(CleanJet_eta[0], CleanJet_eta[1]) && abs(CleanJet_eta - CleanJet_eta[0]) > 1 && abs(CleanJet_eta - CleanJet_eta[1]) > 1) == 0'        
# }

# aliases['lowZ'] = {
#     'expr':  '0.5*abs((Lepton_eta[0] + Lepton_eta[1]) - (CleanJet_eta[0] + CleanJet_eta[1])) < 1'        
# }

# aliases['highZ'] = {
#     'expr':  '0.5*abs((Lepton_eta[0] + Lepton_eta[1]) - (CleanJet_eta[0] + CleanJet_eta[1])) >= 1'
# }

# B tag scale factors

#btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_2016LegacySF_V1.csv' % os.getenv('CMSSW_BASE')

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
if btag_algo == "deepcsv":
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
# elif btag_algo == "deepflav":
#     btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepJet_2016LegacySF_V1.csv' % os.getenv('CMSSW_BASE')
#     aliases['Jet_btagSF_deepflav_shape'] = {
#         'linesToAdd': [
#             'gSystem->Load("libCondFormatsBTauObjects.so");',
#             'gSystem->Load("libCondToolsBTau.so");',
#             'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
#             '.L %s/src/PlotsConfigurations/Configurations/patches/btagsfpatch.cc+' % os.getenv('CMSSW_BASE') 
#         ],
#         'class': 'BtagSF',
#         'args': (btagSFSource,'central','deepjet'),
#         'samples': mc
#     }
        
#     aliases['bVetoSF'] = {
#         'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepflav_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
#         'samples': mc
#     }
    
#     aliases['bReqSF'] = {
#         'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepflav_shape[CleanJet_jetIdx]+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
#         'samples': mc
#     }
    
#     aliases['btagSF'] = {
#         'expr': '(bVeto || (topcr && zeroJet))*bVetoSF + (topcr && !zeroJet)*bReqSF',
#         'samples': mc
#     }
    
#     for shift in ['jes', 'lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
#         aliases['Jet_btagSF_deepflav_shape_up_%s' % shift] = {
#             'class': 'BtagSF',
#             'args': (btagSFSource, 'up_' + shift,'deepjet'),
#             'samples': mc
#         }
#         aliases['Jet_btagSF_deepflav_shape_down_%s' % shift] = {
#             'class': 'BtagSF',
#             'args': (btagSFSource, 'down_' + shift,'deepjet'),
#             'samples': mc
#         }
    
#         for targ in ['bVeto', 'bReq']:
#             alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
#             alias['expr'] = alias['expr'].replace('btagSF_deepflav_shape', 'btagSF_deepflav_shape_up_%s' % shift)
    
#             alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
#             alias['expr'] = alias['expr'].replace('btagSF_deepflav_shape', 'btagSF_deepflav_shape_down_%s' % shift)
    
#         aliases['btagSF%sup' % shift] = {
#             'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
#             'samples': mc
#         }
    
#         aliases['btagSF%sdown' % shift] = {
#             'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
#             'samples': mc
#         }

# data/MC scale factors
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l', 'LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'LepWPCut', 'btagSF', 'PrefireWeight']),
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


# In WpWmJJ_EWK and WpWmJJ_QCD events, partons [0] and [1] are always the decay products of the first W
aliases['lhe_mW1'] = {
    'expr': 'TMath::Sqrt(2. * LHEPart_pt[0] * LHEPart_pt[1] * (TMath::CosH(LHEPart_eta[0] - LHEPart_eta[1]) - TMath::Cos(LHEPart_phi[0] - LHEPart_phi[1])))',
    'samples': ['WWewk', 'WW']
}

# and [2] [3] are the second W
aliases['lhe_mW2'] = {
    'expr': 'TMath::Sqrt(2. * LHEPart_pt[2] * LHEPart_pt[3] * (TMath::CosH(LHEPart_eta[2] - LHEPart_eta[3]) - TMath::Cos(LHEPart_phi[2] - LHEPart_phi[3])))',
    'samples': ['WWewk', 'WW']
}

# use HTXS_njets30 when moving to NanoAODv5 for all trees
#aliases['nCleanGenJet'] = {
#    'linesToAdd': ['.L %s/Differential/ngenjet.cc+' % configurations],
#    'class': 'CountGenJet',
#    'samples': signals
#}

# GGHUncertaintyProducer wasn't run for 2016 nAODv5 non-private
#thus = [
#    'ggH_mu',
#    'ggH_res',
#    'ggH_mig01',
#    'ggH_mig12',
#    'ggH_VBF2j',
#    'ggH_VBF3j',
#    'ggH_pT60',
#    'ggH_pT120',
#    'ggH_qmtop'
#]

#for thu in thus:
#    aliases[thu] = {
#        'linesToAdd': ['.L %s/Differential/gghuncertainty.cc+' % configurations],
#        'class': 'GGHUncertainty',
#        'args': (thu,),
#        'samples': ['ggH_hww'],
#        'nominalOnly': True
#    }