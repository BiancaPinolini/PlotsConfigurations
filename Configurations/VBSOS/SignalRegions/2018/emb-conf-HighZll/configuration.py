# example of configuration file

tag = 'DNN_HighZll_2018'
outputDir = 'RootFiles'
treeName = 'Events'

date='201206'

# luminosity to normalize to
lumi = 59.74

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py'

# file with list of samples
samplesFile = 'samples.py'

# file with list of plot
plotFile = 'plot/plot_topcr.py'

# file with list of nuisances
nuisancesFile = 'nuisances.py'

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = '/eos/home-b/bpinolin/www/VBSOS/emb-conf-HighZll/'+date

# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards/'+date

# structure file for datacard
structureFile = 'structure.py'