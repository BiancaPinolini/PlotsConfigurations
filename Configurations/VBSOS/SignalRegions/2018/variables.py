variables['detajj']  = {   'name': 'fabs(detajj)',
                           'range' : (20,0,9),
                           'xaxis' : '#Delta#eta_{jj}',
                           'fold' : 3
                        }
variables['eta1']  = {   'name': 'Lepton_eta[0]',
                        'range' : (40,-3.14,3.14),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold' : 3
                        }
variables['eta2']  = {  'name': 'Lepton_eta[1]',
                        'range' : (40,-3.14,3.14),
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold' : 3
                        }     
variables['detall']  = {   'name': 'fabs(Lepton_eta[0]-Lepton_eta[1])',
                           'range' : (20,0,6),
                           'xaxis' : '#Delta#eta_{ll}',
                           'fold'  : 3
                        }

variables['jetpt1']  = {   'name': 'Alt$(CleanJet_pt[0],-9999.)',
                           'range' : (15,0.,300),
                           'xaxis' : 'p_{T} 1^{st} jet',
                           'fold'  : 3
                           }

variables['jetpt2']  = {   'name': 'Alt$(CleanJet_pt[1],-9999.)',
                           'range' : (15,0.,300),
                           'xaxis' : 'p_{T} 2^{nd} jet',
                           'fold'  : 3
                           }

variables['met']  = {   'name': 'MET_pt',            
                        'range' : (50,0,250),    
                        'xaxis' : 'MET [GeV]',
                        'fold'  : 3
                        }

variables['dphill']  = {'name': 'fabs(dphill)',
                        'range' : (20,0,3.5),
                        'xaxis' : '#Delta#Phi_{ll}',
                        'fold'  : 3
                        }

variables['dphijj']  = {'name': 'fabs(Alt$(CleanJet_phi[0],-9999.)-Alt$(CleanJet_phi[1],-9999.))',
                        'range' : (20,0,9),
                        'xaxis' : '#Delta#Phi_{jj}',
                        'fold'  : 3
                        }
variables['Mll']  = {       'name': 'mll',
                            'range' : (20,0,350),
                            'xaxis' : 'm_{ll} [GeV]',
                            'fold'  : 3
                        }
variables['btag_first']  = {   'name'  : 'btag_first_al',
                                'range' : (20,0,1),
                                'xaxis' : 'b-tag of the 1^{st} most central jet',
                                'fold'  : 3
                            }
variables['dR_jl1'] = {	'name' : '(R_j1l1 < R_j2l1)*R_j1l1+(R_j1l1 >= R_j2l1)*R_j2l1',
                        'range' : (50,0,10),
                        'xaxis' : 'R from 1^{st} lep to nearest jet',
                        'fold'  : 3
                            }
variables['dR_jl2'] = { 'name' : '(R_j1l2 < R_j2l2)*R_j1l2+(R_j1l2 >= R_j2l2)*R_j2l2',
                        'range' : (50,0,10),
                        'xaxis' : 'R from 2^{nd} lep to nearest jet',
                        'fold'  : 3
                            }

# variables['DNNoutput_emloose'] = { 'name' : 'DNNoutput_emloose',
#                         'cuts' : ['em_loose'],
#                         'range' : (30,0,1),
#                         'xaxis' : 'DNN output em_loose'
#                             }
# variables['DNNoutput_emmedium'] = { 'name' : 'DNNoutput_emmedium',
#                         'cuts' : ['em_medium'],
#                         'range' : (30,0,1),
#                         'xaxis' : 'DNN output em_medium'
                        # }
variables['DNNoutput_emtight'] = { 
                        'name' : 'DNNoutput_emtight',
                        'cuts' : ['em_tight'],
                        'range' : (30,0,1),
                        'xaxis' : 'DNN output em_tight'
                        }

# VARIABILE BDT
#variables['readBDT'] = {
#	'name': 'readBDT(PuppiMET_pt,Lepton_pt,mll,ptll,dphillmet)',
#	'range' : (100,-1,1),
#	'xaxis': 'MVA discriminant',
#	'linesToAdd' : ['.L /afs/cern.ch/user/r/rdfexp/bianca/CMSSW_10_2_15_patch2/src/BDT_plot/readBDT.C+', 'initmyreaderBDT()']
#}
