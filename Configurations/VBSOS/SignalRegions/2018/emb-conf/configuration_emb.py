# example of configuration file

tag = 'DNN_comb_emb_2018'
outputDir = 'RootFiles'
treeName = 'Events'

# luminosity to normalize to
lumi = 59.74

# file with TTree aliases
aliasesFile = 'aliases_emb.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py'

# file with list of samples
samplesFile = 'samples_emb.py'

# file with list of plot
plotFile = 'plot_emb.py'

# file with list of nuisances
nuisancesFile = 'nuisances_emb.py'

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'output-plots'

# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards/1202'

# structure file for datacard
structureFile = 'structure_emb.py'
