variables['detajj']  = {   'name': 'TMath::Abs(detajj)',
                           'range' : (20,2,9),
                           'xaxis' : '#Delta#eta_{jj}',
                           'fold' : 3
                        }
variables['ptll']    = {    'name': 'ptll',               
                            'range' : (17,30,200),   
                            'xaxis' : 'pt_{ll} [GeV]',
                            'fold' : 3 
                        }
variables['detall']  = {   'name': 'TMath::Abs(Alt$(Lepton_eta[0],-9999.)-Alt$(Lepton_eta[1],-9999.))',
                           'range' : (15,0,5),
                           'xaxis' : '#Delta#eta_{ll}',
                           'fold'  : 3
                        }

variables['jetpt1']  = {   'name': 'Alt$(CleanJet_pt[0],-9999.)',
                           'range' : (20,30.,300),
                           'xaxis' : 'p_{T} 1^{st} jet [GeV]',
                           'fold'  : 3
                           }

variables['jetpt2']  = {   'name': 'Alt$(CleanJet_pt[1],-9999.)',
                           'range' : (20,30.,300),
                           'xaxis' : 'p_{T} 2^{nd} jet [GeV]',
                           'fold'  : 3
                           }

variables['met']  = {   'name': 'MET_pt',            
                        'range' : (25,20,250),    
                        'xaxis' : 'MET [GeV]',
                        'fold'  : 3
                        }


variables['mtw1']  = {   'name': 'mtw1',            
                        'range' : (20,0,400),    
                        'xaxis' : 'm^{T}_{W1}  [GeV]',
                        'fold'  : 3
                        }

variables['mtw2']  = {   'name': 'mtw2',            
                        'range' : (20,0,400),    
                        'xaxis' : 'm^{T}_{W2}  [GeV]',
                        'fold'  : 3
                        }

variables['dphill']  = {'name': 'TMath::Abs(dphill)',
                        'range' : (20,0,3.5),
                        'xaxis' : '#Delta#Phi_{ll}',
                        'fold'  : 3
                        }

variables['dphijj']  = {'name': 'TMath::Abs(Alt$(CleanJet_phi[0],-9999.)-Alt$(CleanJet_phi[1],-9999.))',
                        'range' : (20,0,6),
                        'xaxis' : '#Delta#Phi_{jj}',
                        'fold'  : 3
                        }
variables['Mll']  = {       'name': 'mll',
                            'range' : (30,50,350),
                            'xaxis' : 'm_{ll} [GeV]',
                            'fold'  : 3
                        }
variables['dR_jl1'] = {	'name' : '(R_j1l1 < R_j2l1)*R_j1l1+(R_j1l1 >= R_j2l1)*R_j2l1',
                        'range' : (24,0,6),
                        'xaxis' : 'R from 1^{st} lep to nearest jet',
                        'fold'  : 3
                            }
variables['dR_jl2'] = { 'name' : '(R_j1l2 < R_j2l2)*R_j1l2+(R_j1l2 >= R_j2l2)*R_j2l2',
                        'range' : (24,0,6),
                        'xaxis' : 'R from 2^{nd} lep to nearest jet',
                        'fold'  : 3
                            }
variables['Zepp1']  = {   'name': 'Alt$(Lepton_eta[0],-9999.)-0.5*(Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))',
                           'range' : (20,-5,5),
                           'xaxis' : 'Zeppenfeld_{1}',
                           'fold' :0
                           }

variables['Zepp2']  = {   'name': 'Alt$(Lepton_eta[1],-9999.)-0.5*(Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))',
                           'range' : (20,-5,5),
                           'xaxis' : 'Zeppenfeld_{2}',
                           'fold' :0
                           }

variables['mjj']  = {   'name': 'mjj',
                        'range' : (30,220,3000),
                        'xaxis' : 'm_{jj} [GeV]',
                        'fold' :3
                        }

variables['qgl_forward'] = { 'name': '(TMath::Abs(Alt$(CleanJet_eta[0],-9999.)) > TMath::Abs(Alt$(CleanJet_eta[1],-9999.))) * Alt$(Jet_qgl[CleanJet_jetIdx[0]],-9999.) + (TMath::Abs(Alt$(CleanJet_eta[1],-9999.)) >= TMath::Abs(Alt$(CleanJet_eta[0],-9999.))) * Alt$(Jet_qgl[CleanJet_jetIdx[1]],-9999.)',
                         'range' : (20, 0, 1),
                         'xaxis' : 'Quark vs Gluon likelihood discriminator Without Morphing - Forward jet',
                         'fold' : 3
                       }
                       
variables['qgl_central'] = { 'name': '(TMath::Abs(Alt$(CleanJet_eta[0],-9999.)) <= TMath::Abs(Alt$(CleanJet_eta[1],-9999.))) * Alt$(Jet_qgl[CleanJet_jetIdx[0]],-9999.) + (TMath::Abs(Alt$(CleanJet_eta[1],-9999.)) < TMath::Abs(Alt$(CleanJet_eta[0],-9999.))) * Alt$(Jet_qgl[CleanJet_jetIdx[1]],-9999.)',
                         'range' : (20, 0, 1),
                         'xaxis' : 'Quark vs Gluon likelihood discriminator Without Morphing - Central jet',
                         'fold' : 3
                       }

variables['qgl_forward_remorphed'] = { 'name': '(TMath::Abs(Alt$(CleanJet_eta[0],-9999.)) > TMath::Abs(Alt$(CleanJet_eta[1],-9999.))) * Alt$(CleanJet_qgl_morphed[0],-9999.) + (TMath::Abs(Alt$(CleanJet_eta[1],-9999.)) >= TMath::Abs(Alt$(CleanJet_eta[0],-9999.))) * Alt$(CleanJet_qgl_morphed[1],-9999.)',
                         'range' : (20, 0, 1),
                         'xaxis' : 'Quark vs Gluon likelihood discriminator - Forward jet',
                         'fold' : 3
                       }

variables['qgl_central_remorphed'] = { 'name': '(TMath::Abs(Alt$(CleanJet_eta[0],-9999.)) <= TMath::Abs(Alt$(CleanJet_eta[1],-9999.))) * Alt$(CleanJet_qgl_morphed[0],-9999.) + (TMath::Abs(Alt$(CleanJet_eta[1],-9999.)) < TMath::Abs(Alt$(CleanJet_eta[0],-9999.))) * Alt$(CleanJet_qgl_morphed[1],-9999.)',
                         'range' : (20, 0, 1),
                         'xaxis' : 'Quark vs Gluon likelihood discriminator - Central jet',
                         'fold' : 3
                       }