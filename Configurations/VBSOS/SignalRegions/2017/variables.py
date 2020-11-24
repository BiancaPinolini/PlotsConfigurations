# variables['detajj']  = {   'name': 'fabs(detajj)',
#                            'range' : (20,2,9),
#                            'xaxis' : '#Delta#eta_{jj}',
#                            'fold' : 3
#                         }
# variables['ptll']    = {    'name': 'ptll',               
#                             'range' : (20,30,200),   
#                             'xaxis' : 'pt_{ll} [GeV]',
#                             'fold' : 3 
#                         }
# variables['eta1']  = {   'name': 'Lepton_eta[0]',
#                         'range' : (20,-3.14,3.14),
#                         'xaxis' : '#eta 1^{st} lep',
#                         'fold' : 3
#                         }
# variables['eta2']  = {  'name': 'Lepton_eta[1]',
#                         'range' : (20,-3.14,3.14),
#                         'xaxis' : '#eta 2^{nd} lep',
#                         'fold' : 3
#                         }     

# variables['eta-j1']  = {   'name': 'CleanJet_eta[0]',
#                         'range' : (20,-3.14,3.14),
#                         'xaxis' : '#eta 1^{st} jet',
#                         'fold' : 3
#                         }
# variables['eta-j2']  = {  'name': 'CleanJet_eta[1]',
#                         'range' : (20,-3.14,3.14),
#                         'xaxis' : '#eta 2^{nd} lep',
#                         'fold' : 3
#                         }  


# variables['detall']  = {   'name': 'fabs(Lepton_eta[0]-Lepton_eta[1])',
#                            'range' : (15,0,5),
#                            'xaxis' : '#Delta#eta_{ll}',
#                            'fold'  : 3
#                         }

# variables['leppt1']  = {   'name': 'Lepton_pt[0]',
#                            'range' : (15,0.,300),
#                            'xaxis' : 'p_{T} 1^{st} lepton [GeV]',
#                            'fold'  : 3
#                            }

# variables['leppt2']  = {   'name': 'Lepton_pt[1]',
#                            'range' : (15,0.,300),
#                            'xaxis' : 'p_{T} 2^{nd} lepton [GeV]',
#                            'fold'  : 3
#                            }

# variables['jetpt1']  = {   'name': 'Alt$(CleanJet_pt[0],-9999.)',
#                            'range' : (15,0.,300),
#                            'xaxis' : 'p_{T} 1^{st} jet [GeV]',
#                            'fold'  : 3
#                            }

# variables['jetpt2']  = {   'name': 'Alt$(CleanJet_pt[1],-9999.)',
#                            'range' : (15,0.,300),
#                            'xaxis' : 'p_{T} 2^{nd} jet [GeV]',
#                            'fold'  : 3
#                            }

# variables['met']  = {   'name': 'MET_pt',            
#                         'range' : (30,0,250),    
#                         'xaxis' : 'MET [GeV]',
#                         'fold'  : 3
#                         }

# variables['dphill']  = {'name': 'fabs(dphill)',
#                         'range' : (20,0,3.5),
#                         'xaxis' : '#Delta#Phi_{ll}',
#                         'fold'  : 3
#                         }

# variables['dphijj']  = {'name': 'fabs(Alt$(CleanJet_phi[0],-9999.)-Alt$(CleanJet_phi[1],-9999.))',
#                         'range' : (20,0,6),
#                         'xaxis' : '#Delta#Phi_{jj}',
#                         'fold'  : 3
#                         }
# variables['Mll']  = {       'name': 'mll',
#                             'range' : (20,50,350),
#                             'xaxis' : 'm_{ll} [GeV]',
#                             'fold'  : 3
#                         }
variables['btag_central']  = {   'name'  : 'btag_central_al',
                                'range' : (20,0,1),
                                'xaxis' : 'b-tag of the central jet',
                                'fold'  : 3
                            }
variables['btag_forward']  = {   'name'  : 'btag_forward_al',
                                'range' : (20,0,1),
                                'xaxis' : 'b-tag of the forward jet',
                                'fold'  : 3
                            }

variables['btag_central_DNN'] = {   'name'  : 'btag_central_DNN',
                                'range' : (20,0,1),
                                'xaxis' : 'b-tag of the central jet used for the DNN',
                                'fold'  : 3
                            }

variables['btag_forward_DNN'] = {   'name'  : 'btag_forward_DNN',
                                'range' : (20,0,1),
                                'xaxis' : 'b-tag of the forward jet used for the DNN',
                                'fold'  : 3
                            }

variables['Zeppll_DNN'] = {   'name'  : 'Zeppll_DNN',
                              'range' : (10,0,1),
                              'xaxis' : 'Zeppenfeld_{ll} used for the DNN',
                              'fold' : 3
                           }  

# variables['dR_jl1'] = {	'name' : '(R_j1l1 < R_j2l1)*R_j1l1+(R_j1l1 >= R_j2l1)*R_j2l1',
#                         'range' : (20,0,6),
#                         'xaxis' : 'R from 1^{st} lep to nearest jet',
#                         'fold'  : 3
#                             }
# variables['dR_jl2'] = { 'name' : '(R_j1l2 < R_j2l2)*R_j1l2+(R_j1l2 >= R_j2l2)*R_j2l2',
#                         'range' : (20,0,6),
#                         'xaxis' : 'R from 2^{nd} lep to nearest jet',
#                         'fold'  : 3
#                             }
variables['Zeppll']  = {   'name': 'Zeppll_al',
                           'range' : (10,0,1),
                           'xaxis' : 'Zeppenfeld_{ll}',
                           'fold' : 3
                           }  
# variables['Zepp1']  = {   'name': 'Zepp1_al',
#                            'range' : (10,-5,5),
#                            'xaxis' : 'Zeppenfeld_{1}',
#                            'fold' :0
#                            }

# variables['Zepp2']  = {   'name': 'Zepp2_al',
#                            'range' : (10,-5,5),
#                            'xaxis' : 'Zeppenfeld_{2}',
#                            'fold' :0
#                            }

# variables['mjj_100']  = {   'name': 'mjj',
#                         'range' : (100,200,3000),
#                         'xaxis' : 'm_{jj} [GeV]',
#                         'fold' :3
#                         } 
# variables['mjj_200']  = {   'name': 'mjj',
#                         'range' : (200,200,3000),
#                         'xaxis' : 'm_{jj} [GeV]',
#                         'fold' :3
#                         } 
# variables['mjj_20']  = {   'name': 'mjj',
#                         'range' : (100,200,3000),
#                         'xaxis' : 'm_{jj} [GeV]',
#                         'fold' :3
#                         }     
                        
# variables['mth']  = {   'name': 'mth',
#                         'range' : (20,0,300),
#                         'xaxis' : 'm_{T} [GeV]',
#                         'fold' :3
#                         } 

variables['events']  = {'name': '1',
                        'range' : (1,0,2),
                        'xaxis' : 'events',
                        'fold' : 3
                        } 



# variables['qgl_forward'] = { 'name': 'qgl_forward',
#                          'range' : (20, 0, 1),
#                          'xaxis' : 'Quark vs Gluon likelihood discriminator - Forward jet',
#                          'fold' : 3
#                        }
                       
# variables['qgl_central'] = { 'name': 'qgl_central',
#                          'range' : (20, 0, 1),
#                          'xaxis' : 'Quark vs Gluon likelihood discriminator - Central jet',
#                          'fold' : 3
#                        }
                       
  
variables['DNNoutput_15'] = { 
                        'name' : 'DNNoutput',
                        'range' : (15,0,1),
                        'xaxis' : 'DNN output',
                        'fold' : 3,
                        'blind' : {
                            "sr": [0.5,1]
                            }
                        }
variables['DNNoutput_25'] = { 
                        'name' : 'DNNoutput',
                        'range' : (25,0,1),
                        'xaxis' : 'DNN output',
                        'fold' : 3,
                        'blind' : {
                            "sr": [0.5,1]
                            }
                        }
variables['DNNoutput_30'] = { 
                        'name' : 'DNNoutput',
                        'range' : (30,0,1),
                        'xaxis' : 'DNN output',
                        'fold' : 3,
                        'blind' : {
                            "sr": [0.5,1]
                            }
                        }
variables['DNNoutput_35'] = { 
                        'name' : 'DNNoutput',
                        'range' : (35,0,1),
                        'xaxis' : 'DNN output',
                        'fold' : 3,
                        'blind' : {
                            "sr": [0.5,1]
                            }
                        }
variables['DNNoutput_50'] = { 
                        'name' : 'DNNoutput',
                        'range' : (50,0,1),
                        'xaxis' : 'DNN output',
                        'fold' : 3,
                        'blind' : {
                            "sr": [0.5,1]
                            }
                        }
variables['DNNoutput_70'] = { 
                        'name' : 'DNNoutput',
                        'range' : (70,0,1),
                        'xaxis' : 'DNN output',
                        'fold' : 3,
                        'blind' : {
                            "sr": [0.5,1]
                            }
                        }
# variables['DNNoutput_var'] = { 
#                         'name' : 'DNNoutput',
#                         'range' : ([0,0.03,0.06,0.09,0.12,0.15,0.18,0.21,0.24,0.27,0.3,0.35,0.40,0.45,0.50,0.60,0.70,0.80,0.83,0.86,0.89,0.92,0.95,0.98,1],),
#                         'xaxis' : 'DNN output',
#                         'fold' : 3,
#                         'blind' : {
#                             "sr": [0.5,1]
#                             }
#                         }



# VARIABILE BDT
#variables['readBDT'] = {
#	'name': 'readBDT(PuppiMET_pt,Lepton_pt,mll,ptll,dphillmet)',
#	'range' : (100,-1,1),
#	'xaxis': 'MVA discriminant',
#	'linesToAdd' : ['.L /afs/cern.ch/user/r/rdfexp/bianca/CMSSW_10_2_15_patch2/src/BDT_plot/readBDT.C+', 'initmyreaderBDT()']
#}
