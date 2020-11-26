# variables['detajj']  = {   'name': 'detajj',
#                            'range' : (20,2,9),
#                            'xaxis' : '#Delta#eta_{jj}',
#                            'fold' : 3
#                         }
# variables['ptll']    = {    'name': 'ptll',               
#                             'range' : (20,30,200),   
#                             'xaxis' : 'pt_{ll} [GeV]',
#                             'fold' : 3 
#                         }
# variables['eta1']  = {   'name': 'eta1_al',
#                         'range' : (20,-3.14,3.14),
#                         'xaxis' : '#eta 1^{st} lep',
#                         'fold' : 3
#                         }
# variables['eta2']  = {  'name': 'eta2_al',
#                         'range' : (20,-3.14,3.14),
#                         'xaxis' : '#eta 2^{nd} lep',
#                         'fold' : 3
#                         }     

# variables['detall']  = {   'name': 'detall_al',
#                            'range' : (15,0,5),
#                            'xaxis' : '#Delta#eta_{ll}',
#                            'fold'  : 3
#                         }

# variables['jetpt1']  = {   'name': 'jetpt1_al',
#                            'range' : (15,0.,300),
#                            'xaxis' : 'p_{T} 1^{st} jet [GeV]',
#                            'fold'  : 3
#                            }

# variables['jetpt2']  = {   'name': 'jetpt2_al',
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

# variables['dphijj']  = {'name': 'dphijj_al',
#                         'range' : (20,0,6),
#                         'xaxis' : '#Delta#Phi_{jj}',
#                         'fold'  : 3
#                         }
# variables['Mll']  = {       'name': 'mll',
#                             'range' : (20,50,350),
#                             'xaxis' : 'm_{ll} [GeV]',
#                             'fold'  : 3
#                         }
# variables['btag_central']  = {   'name'  : 'btag_central_al',
#                                 'range' : (20,0,1),
#                                 'xaxis' : 'b-tag of the central jet',
#                                 'fold'  : 3
#                             }
# variables['btag_forward']  = {   'name'  : 'btag_forward_al',
#                                 'range' : (20,0,1),
#                                 'xaxis' : 'b-tag of the forward jet',
#                                 'fold'  : 3
#                             }

# variables['btag_central_DNN'] = {   'name'  : 'btag_central_DNN',
#                                 'range' : (20,0,1),
#                                 'xaxis' : 'b-tag of the central jet used for the DNN',
#                                 'fold'  : 3
#                             }

# variables['btag_forward_DNN'] = {   'name'  : 'btag_forward_DNN',
#                                 'range' : (20,0,1),
#                                 'xaxis' : 'b-tag of the forward jet used for the DNN',
#                                 'fold'  : 3
#                             }

# variables['Zeppll_DNN'] = {   'name'  : 'Zeppll_DNN',
#                               'range' : (10,0,1),
#                               'xaxis' : 'Zeppenfeld_{ll} used for the DNN',
#                               'fold' : 3
#                            }  

# variables['dR_jl1'] = {	'name' : 'dR_jl1_al',
#                         'range' : (20,0,6),
#                         'xaxis' : 'R from 1^{st} lep to nearest jet',
#                         'fold'  : 3
#                             }
# variables['dR_jl2'] = { 'name' : 'dR_jl2_al',
#                         'range' : (20,0,6),
#                         'xaxis' : 'R from 2^{nd} lep to nearest jet',
#                         'fold'  : 3
#                             }
# variables['Zeppll']  = {   'name': 'Zeppll_al',
#                            'range' : (10,0,1),
#                            'xaxis' : 'Zeppenfeld_{ll}',
#                            'fold' : 3
#                            }  
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

# variables['mjj']  = {   'name': 'mjj',
#                         'range' : (20,220,3000),
#                         'xaxis' : 'm_{jj} [GeV]',
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
                       
# variables['area_forward'] = { 'name': 'area_forward',
#                          'range' : (20, 0, 1),
#                          'xaxis' : 'area forward',
#                          'fold' : 3
#                        }

# variables['area_central'] = { 'name': 'area_central',
#                          'range' : (20, 0, 1),
#                          'xaxis' : 'area central',
#                          'fold' : 3
#                        }
# variables['Jet_nConst_forward'] = { 'name': 'Jet_nConst_forward',
#                          'range' : (20, -1, 100),
#                          'xaxis' : 'Jet_nConst_forward',
#                          'fold' : 3
#                        }

# variables['Jet_nConst_central'] = { 'name': 'Jet_nConst_central',
#                          'range' : (20, -1, 100),
#                          'xaxis' : 'Jet_nConst_central',
#                          'fold' : 3
#                        }
variables['DNNoutput_10'] = { 
                        'name' : 'DNNoutput',
                        'range' : (10,0,1),
                        'xaxis' : 'DNN score',
                        'fold' : 3,
                        'blind' : {
                            "sr": [0.5,1]
                            }
                        }
variables['DNNoutput_20'] = { 
                        'name' : 'DNNoutput',
                        'range' : (20,0,1),
                        'xaxis' : 'DNN score',
                        'fold' : 3,
                        'blind' : {
                            "sr": [0.5,1]
                            }
                        }
variables['DNNoutput_25'] = { 
                        'name' : 'DNNoutput',
                        'range' : (25,0,1),
                        'xaxis' : 'DNN score',
                        'fold' : 3,
                        'blind' : {
                            "sr": [0.5,1]
                            }
                        }
variables['DNNoutput_30'] = { 
                        'name' : 'DNNoutput',
                        'range' : (30,0,1),
                        'xaxis' : 'DNN score',
                        'fold' : 3,
                        'blind' : {
                            "sr": [0.5,1]
                            }
                        }

variables['DNNoutput_40'] = { 
                        'name' : 'DNNoutput',
                        'range' : (40,0,1),
                        'xaxis' : 'DNN score',
                        'fold' : 3,
                        'blind' : {
                            "sr": [0.5,1]
                            }
                        }


# VARIABILE BDT
#variables['readBDT'] = {
#	'name': 'readBDT(PuppiMET_pt,Lepton_pt,mll,ptll,dphillmet)',
#	'range' : (100,-1,1),
#	'xaxis': 'MVA discriminant',
#	'linesToAdd' : ['.L /afs/cern.ch/user/r/rdfexp/bianca/CMSSW_10_2_15_patch2/src/BDT_plot/readBDT.C+', 'initmyreaderBDT()']
#}
