from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
#config.General.transferOutputs = True
config.General.transferLogs=True
config.General.requestName = 'REQUESTNAME'
config.section_('JobType')
config.JobType.psetName = '../runFlatTreeMINIAOD_cfg.py'
config.JobType.pluginName = 'Analysis'
config.JobType.inputFiles = ['../conf.xml','../Fall17_17Nov2017BCDEF_V6_DATA.db','../Fall17_17Nov2017_V6_MC.db']
#config.JobType.outputFiles = ['output.root']
config.JobType.pyCfgParams = ['privateMC=True','isData=0','runAK10=0']
config.JobType.maxMemoryMB = 4000
config.JobType.maxJobRuntimeMin = 2630
#config.JobType.pyCfgParams = ['isData=1','runAK10=0']
config.section_('Data')
#config.Data.splitting='LumiBased'
config.Data.splitting='FileBased'
config.Data.totalUnits = -1 #nof files (or lumisection) to analyze in total
#config.Data.unitsPerJob = 100 #nof files (or lumisections) in each job
config.Data.unitsPerJob = 1
#config.Data.lumiMask = 'GRL/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt'

config.Data.allowNonValidInputDataset = True
config.Data.publication = False
config.Data.inputDataset = 'INPUTDATASET'
config.Data.inputDBS = 'phys03'
config.Data.outputDatasetTag = 'PUBLISHDATANAME'
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter'
config.Data.outLFNDirBase = 'OUTLFN'


config.section_('User')
config.User.voGroup = 'becms'
config.section_('Site')
config.Site.storageSite = 'T2_BE_IIHE'
config.Site.whitelist = ['T2_BE_IIHE']

#config.Data.ignoreLocality = True
