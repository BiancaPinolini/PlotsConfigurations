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

variables['DNNoutput_50'] = { 
                        'name' : 'DNNoutput',
                        'range' : (50,0,1),
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
