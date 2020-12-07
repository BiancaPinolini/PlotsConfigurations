# example of configuration file

tag = 'DNN_emb_comb_2016'
outputDir = 'RootFiles'
treeName = 'Events'

date='201208'

# luminosity to normalize to
lumi = 35.867

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py'

# file with list of samples
samplesFile = 'samples.py'

# file with list of plot
plotFile = 'plot.py'

# file with list of nuisances
nuisancesFile = 'nuisances.py'

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = '/eos/home-b/bpinolin/www/VBSOS/'+date+'/2016/emb-conf/'

# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards/'+date

# # structure file for datacard
structureFile = 'structure.py'
