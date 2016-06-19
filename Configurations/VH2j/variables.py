# variables

#variables = {}
    
#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
   
variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                         'fold' : 3
                        }


variables['mjj']  = {  'name': 'mjj',
                       'range': (20,0,200),  #for 500 < mjj < 1000
                     # 'range': (15,1000,2000),  #for  mjj > 1000
                       'xaxis': 'mjj [GeV]',
                       'fold': 3
                       }

variables['mll']  = {   'name': 'mll',            #   variable name
                        'range' : (4, 0,200),    #   variable range
                        #'range' : (7,10,210),    #   variable range
                      # 'range' : (12,90,300),    #   control region: mll > 90
                        'xaxis' : 'mll [GeV]',  #   x axis name
                        'fold' : 3
                        }

variables['detajj']  = {  'name': 'detajj',
                       'range': (7,0.0,3.5),
                     # 'range': (10,3.5,8.5),
                       'xaxis': 'detajj',
                       'fold': 3
                       }

variables['ptll']  = {  'name': 'ptll',            #   variable name
                        'range' : (20,30,200),    #   variable range
                        'xaxis' : 'ptll [GeV]',  #   x axis name
                        'fold' : 3
                        }
