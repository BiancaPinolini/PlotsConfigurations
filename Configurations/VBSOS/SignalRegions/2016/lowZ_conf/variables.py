variables['events']  = {'name': '1',
                        'range' : (1,0,2),
                        'xaxis' : 'events',
                        'fold' : 3
                        } 


variables['DNNoutput_10'] = { 
                        'name' : 'DNNoutput',
                        'range' : (10,0,1),
                        'xaxis' : 'DNN score',
                        'fold' : 3,
                        'blind' : {
                            "sr": [0.5,1]
                            }
                        }
variables['DNNoutput_15'] = { 
                        'name' : 'DNNoutput',
                        'range' : (15,0,1),
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

# variables['qgl_central'] = { 'name': 'qgl_central',
#                          'range' : (20, 0, 1),
#                          'xaxis' : 'Quark vs Gluon likelihood discriminator - Central jet',
#                          'fold' : 3
#                        }

# variables['qgl_forward'] = { 'name': 'qgl_forward',
#                          'range' : (20, 0, 1),
#                          'xaxis' : 'Quark vs Gluon likelihood discriminator - Forward jet',
#                          'fold' : 3
#                        }

# VARIABILE BDT
#variables['readBDT'] = {
#	'name': 'readBDT(PuppiMET_pt,Lepton_pt,mll,ptll,dphillmet)',
#	'range' : (100,-1,1),
#	'xaxis': 'MVA discriminant',
#	'linesToAdd' : ['.L /afs/cern.ch/user/r/rdfexp/bianca/CMSSW_10_2_15_patch2/src/BDT_plot/readBDT.C+', 'initmyreaderBDT()']
#}
