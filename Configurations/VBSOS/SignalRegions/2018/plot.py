# plot configuration



# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#
groupPlot['DY']  = {  
                  'nameHR' : "DY",
                  'isSignal' : 0,
                  'color': 418,    # kGreen+2
                  'samples'  : ['DY']
              }
groupPlot['VVV']  = {  
                  'nameHR' : 'VVV',
                  'isSignal' : 0,
                  'color': 857, # kAzure -3  
                  'samples'  : ['VVV']
              }
groupPlot['VZ']  = {  
                  'nameHR' : "VZ",
                  'isSignal' : 0,
                  'color'    : 617,   # kViolet + 1  
                  'samples'  : ['VZ']
              }
groupPlot['Vg']  = {  
                  'nameHR' : "V#gamma(*)",
                  'isSignal' : 0,
                  'color'    : 631, # kRed -1
                  'samples'  : ['Vg', 'VgS_H', 'VgS_L']
              }
groupPlot['Higgs']  = {  
                  'nameHR' : 'Higgs',
                  'isSignal' : 0,
                  'color': 632, 
		  'samples'  : [ 'qqH_hww', 'ggH_hww']
  

            }
groupPlot['WW']  = {  
                  'nameHR' : 'WW',
                  'isSignal' : 0,
                  'color': 851, # kAzure -9 
                  'samples'  : ['WW', 'ggWW']
              }
groupPlot['top']  = {  
                  'nameHR' : 'Top',
                  'isSignal' : 0,
                  'color': 400,   # kYellow
                  'samples'  : ['top']
              }


groupPlot['WWewk']  = {
                  'nameHR' : 'Signal',
                  'isSignal' : 1,
                  'color': 2,
		  'samples'  : [ 'WWewk']                                                                             
              }

#plot = {}

# keys here must match keys in samples.py    
#   
plot['DY']  = { 
                  'nameHR' : 'DY',
                  'color': 1 ,  
                  'isSignal' : 0,
                  'isData'   : 0 
              }
plot['top']  = { 
                  'nameHR' : 'top',
                  'color': 2 ,  
                  'isSignal' : 0,
                  'isData'   : 0 

              }
plot['VVV']  = { 
                  'nameHR' : 'VVV',
                  'color': 3 ,  
                  'isSignal' : 0,
                  'isData'   : 0 

              }
plot['VZ']  = { 
                  'nameHR' : 'VZ',
                  'color': 4 ,  
                  'isSignal' : 0,
                  'isData'   : 0 

              }

plot['Vg']  = {  
                  'nameHR' : "V#gamma",
                  'isSignal' : 0,
                  'color'    : 6,   
                  'isData'   : 0 
              }

plot['VgS_H']  = {  
                  'nameHR' : "V#gamma*",
                  'isSignal' : 0,
                  'color'    : 9,   
                  'isData'   : 0 
              }
plot['VgS_L']  = {  
                  'nameHR' : "V#gamma*",
                  'isSignal' : 0,
                  'color'    : 9,   
                  'isData'   : 0 
              }


plot['WW']  = {
                  'nameHR' : 'WW',
                  'isSignal' : 0,
                  'isData'   : 0 ,
                  'color': 7 #                                                                           
              }
plot['ggWW']  = {
                  'nameHR' : 'ggWW',
                  'isSignal' : 0,
                  'isData'   : 0 ,
                  'color': 9 #                                                                           
              }

# HWW 



plot['qqH_hww'] = {
                  'nameHR' : 'qqH',
                  'color': 632+1, # kRed+1 
                  'isSignal' : 0,
                  'isData'   : 0
                  }


plot['ggH_hww'] = {
                  'nameHR' : 'ggH',
                  'color': 632, # kRed 
                  'isSignal' : 0,
                  'isData'   : 0
                  }
plot['DATA']  = { 
                 'nameHR' : 'Data',
                'color': 1 ,  
                'isSignal' : 0,
               'isData'   : 1,
               'isBlind'  : 0
          }

          
plot['WWewk']  = {
                  'nameHR' : 'WpWmJJ_EWK_noTop',
                  'isSignal' : 1,
                  'isData'   : 0 ,
                  'color': 8                                                                             
              }


