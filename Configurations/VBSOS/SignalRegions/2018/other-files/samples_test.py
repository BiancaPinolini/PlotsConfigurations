
import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # 2018
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, sample):
    try:
        if _samples_noload:
            return []
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

# samples

try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()
    
################################################
################# SKIMS ########################
################################################

mcProduction = 'Autumn18_102X_nAODv6_Full2018v6'

mcSteps = 'MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6{var}'


##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

mcDirectory = makeMCDirectory()

#########################################
############ MC COMMON ##################
#########################################

# SFweight does not include btag weights
mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'

###########################################
#############  BACKGROUNDS  ###############
###########################################

###### Top usato per allenare la DNN #######

samples['top_DNN'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'TT_DiLept'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}

addSampleWeight(samples,'top_DNN','TT_DiLept','Top_pTrw')

###### Top Latinos #######

files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ST_s-channel_ext1') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop_ext1') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_top_ext1')

samples['top_latinos'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}

addSampleWeight(samples,'top_latinos','TTTo2L2Nu','Top_pTrw')


###########################################
#############   SIGNALS  ##################
###########################################

# signals = []

# #### WWewk ### 
# samples['WWewk'] = {
#     'name': nanoGetSampleFiles(mcDirectory, 'WpWmJJ_EWK'),
#     'weight': mcCommonWeight + '*(0.08875/0.3452)*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)', #filter tops and Higgs, factor to adjust the XS
#     'FilesPerJob': 4
# }


# signals.append('WpWmJJ_EWK')