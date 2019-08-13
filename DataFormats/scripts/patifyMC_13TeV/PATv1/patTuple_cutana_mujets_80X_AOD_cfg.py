import FWCore.ParameterSet.Config as cms

process = cms.Process("MUONJET")

isData = True

## MessageLogger
process.load("FWCore.MessageLogger.MessageLogger_cfi")

# verbose flags for the PF2PAT modules
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.options.allowUnscheduled = cms.untracked.bool(False)

## Geometry and Detector Conditions (needed for a few patTuple production steps)
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
if isData:
    process.GlobalTag = GlobalTag(process.GlobalTag, '80X_dataRun2_2016LegacyRepro_v4')
else:
    process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_2016_TrancheIV_v8')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("MuJetAnalysis.DataFormats.RECOtoPAT_cff")
process.load("MuJetAnalysis.MuJetProducer.MuJetProducer_cff")
process.load("MuJetAnalysis.CutFlowAnalyzer.CutFlowAnalyzer_cff")
process.load("MuJetAnalysis.CutFlowAnalyzer.FilterSample3RecoMu_cfi")
process.load("MuJetAnalysis.CutFlowAnalyzer.FilterSample3RecoMu_PAT_cfi")
process.load("MuJetAnalysis.CutFlowAnalyzer.FilterSample1PATElectron_cfi")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'file:/fdata/hepx/store/user/dildick/009A0C3D-1A91-E711-89D3-24BE05BDBE61.root',
        #'file:/fdata/hepx/store/user/dildick/009A0C3D-1A91-E711-89D3-24BE05BDBE61.root',
        #'file:/fdata/hepx/store/user/dildick/02F3508B-1D91-E711-AE56-24BE05BD4F81.root'
        #'file:/fdata/hepx/store/user/dildick/084A7351-CE90-E711-A0B5-008CFA0A5844.root',
        #'file:/fdata/hepx/store/user/dildick/12778F8B-1D91-E711-BA95-5065F3812261.root',
        #'file:/fdata/hepx/store/user/dildick/1AF0BFA7-1D91-E711-9B99-4C79BA3201D9.root',
        #'file:/fdata/hepx/store/mc/RunIISummer16DR80Premix/WZTo3LNu_0Jets_MLL-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0CFEE63A-7AD0-E611-A9DF-C81F66B7EBF5.root'
        #'file:/fdata/hepx/store/user/lpernie/DarkSUSY_mH_125_mN1_10_mGammaD_0p25_cT_0_13TeV_20k_MG452_BR224_LHE_pythia8_GEN_SIM_MINIAOD_V2_v1/DarkSUSY_mH_125_mN1_10_mGammaD_0p25_cT_0_13TeV_20k_PAT_ANA_V2_v1/170124_224445/0000/out_pat_17.root'
    )
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )

process.dump=cms.EDAnalyzer('EventContentAnalyzer')

from PhysicsTools.SelectorUtils.tools.vid_id_tools import *

if isData:
    patifyChoice = process.patifyData
else:
    patifyChoice = process.patifyMC

switchOnVIDElectronIdProducer(process, DataFormat.AOD)

# define which IDs we want to produce                                                                                                                                                                                              
my_id_modules = ['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Summer16_80X_V1_cff',
                 'RecoEgamma.ElectronIdentification.Identification.heepElectronID_HEEPV60_cff']

#add them to the VID producer                                                                                                                                                                                                      
for idmod in my_id_modules:
    setupAllVIDIdsInModule(process,idmod,setupVIDElectronSelection)

process.p = cms.Path(
    process.tripleRecoMuFilter *
    patifyChoice *
    process.tripleRecoMuFilterPAT *
#    process.singleElectronFilterPAT *
    process.MuJetProducers *
#    process.dump*
    process.cutFlowAnalyzers
)

process.out = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string('/fdata/hepx/store/user/dildick/patTuple.root'),
    SelectEvents = cms.untracked.PSet( 
        SelectEvents = cms.vstring("p")
    )
)

### Add MuJet Dataformats
from MuJetAnalysis.DataFormats.EventContent_version10_cff import *
process = customizePatOutput(process)

process.outpath = cms.EndPath(process.out)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("out_ana.root")
)

