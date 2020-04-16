# variables['detajj']  = {   'name': 'fabs(detajj)',
#                            'range' : (20,0,9),
#                            'xaxis' : '#Delta#eta_{jj}',
#                            'fold'  : 3
#                         }

# variables['detall']  = {   'name': 'detall_alias',
#                            'range' : (20,0,6),
#                            'xaxis' : '#Delta#eta_{ll}',
#                            'fold'  : 3
#                         }

# variables['jetpt1']  = {   'name': 'jetpt1',
#                            'range' : (15,0.,300),
#                            'xaxis' : 'p_{T} 1^{st} jet',
#                            'fold'  : 3
#                            }

# variables['jetpt2']  = {   'name': 'jetpt2',
#                            'range' : (15,0.,300),
#                            'xaxis' : 'p_{T} 2^{nd} jet',
#                            'fold'  : 3
#                            }

# variables['eta1']  = {  'name': 'eta1',
#                         'range' : (40,-3.14,3.14),
#                         'xaxis' : '#eta 1^{st} lepton',
#                         'fold'  : 3
#                         }


# variables['eta2']  = {  'name': 'eta2',
#                         'range' : (40,-3.14,3.14),
#                         'xaxis' : '#eta 2^{nd} lepton',
#                         'fold'  : 3
#                         }

# variables['met']  = {   'name': 'MET_pt',            
#                         'range' : (50,0,250),    
#                         'xaxis' : 'MET [GeV]',
#                         'fold'  : 3
#                         }

# variables['dphill']  = {'name': 'fabs(dphill)',
#                         'range' : (20,0,3.5),
#                         'xaxis' : '#Delta#Phi_{ll}',
#                         'fold'  : 3
#                         }

# variables['dphijj']  = {'name': 'dphijj_alias',
#                         'range' : (20,0,9),
#                         'xaxis' : '#Delta#Phi_{jj}',
#                         'fold'  : 3
#                         }
# variables['Zlep1']  = {  'name': 'Zlep1',
#                          'range': (20,-1.5,1.5),
#                          'xaxis': 'Z^{lep}_{1}',
#                          'fold'  : 3
#                          }

# variables['Zlep2']  = {  'name': 'Zlep2',
#                          'range': (20,-1.5,1.5),
#                          'xaxis': 'Z^{lep}_{2}',
#                          'fold'  : 3
#                          }
# variables['Mll']  = {       'name': 'mll',             
#                             'range' : (20,0,350),
#                             'xaxis' : 'm_{ll} [GeV]',
#                             'fold'  : 3
#                         }
# variables['btag_first']  = {   'name'  : 'btag_first',
#                                 'range' : (20,0,1),
#                                 'xaxis' : 'b-tag of the 1^{st} most central jet',
#                                 'fold'  : 3
#                             }
# variables['btag_second']  = {   'name'  : 'btag_second',
#                                'range' : (20,0,1),
#                                 'xaxis' : 'b-tag of the 2^{nd} most central jet',
#                                 'fold'  : 3
#                             }
variables['dR_jl1'] = {	'name' : 'dR_jl1',
                        'range' : (100,0,10),
                        'xaxis' : 'R from 1^{st} lep to nearest jet',
                        'fold'  : 3
                            }
variables['dR_jl2'] = { 'name' : 'dR_jl2',
                        'range' : (100,0,10),
                        'xaxis' : 'R from 2^{nd} lep to nearest jet',
                        'fold'  : 3
                            }

variables['DNNoutput_emloose'] = { 'name' : 'DNNoutput_emloose',
                        'cuts' : ['em_loose'],
                        'range' : (30,0,1),
                        'xaxis' : 'DNN output em_loose',
                        'fold'  : 3
                            }
variables['DNNoutput_emmedium'] = { 'name' : 'DNNoutput_emmedium',
                        'cuts' : ['em_medium'],
                        'range' : (30,0,1),
                        'xaxis' : 'DNN output em_medium',
                        'fold'  : 3
                        }
variables['DNNoutput_emtight'] = { 'name' : 'DNNoutput_emtight',
                        'cuts' : ['em_tight'],
                        'range' : (30,0,1),
                        'xaxis' : 'DNN output em_tight',
                        'fold'  : 3
                        }

# VARIABILE BDT
#variables['readBDT'] = {
#	'name': 'readBDT(PuppiMET_pt,Lepton_pt,mll,ptll,dphillmet)',
#	'range' : (100,-1,1),
#	'xaxis': 'MVA discriminant',
#	'linesToAdd' : ['.L /afs/cern.ch/user/r/rdfexp/bianca/CMSSW_10_2_15_patch2/src/BDT_plot/readBDT.C+', 'initmyreaderBDT()']
#}
