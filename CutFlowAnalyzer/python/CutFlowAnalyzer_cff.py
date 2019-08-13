import FWCore.ParameterSet.Config as cms

from MuJetAnalysis.CutFlowAnalyzer.CutFlowAnalyzer_cfi import *

cutFlowAnalyzerPXBL2PXFL2 = cutFlowAnalyzer.clone(
    barrelPixelLayer = cms.int32(2),
    endcapPixelLayer = cms.int32(2),
    muJets = cms.InputTag("PFMuJetProducer05PXBL2PXFL2"),
    muJetOrphans = cms.InputTag("PFMuJetProducer05PXBL2PXFL2", "Orphans"),
)
cutFlowAnalyzerPXBL3PXFL2 = cutFlowAnalyzer.clone(
    barrelPixelLayer = cms.int32(3),
    endcapPixelLayer = cms.int32(2),
    muJets = cms.InputTag("PFMuJetProducer05PXBL3PXFL2"),
    muJetOrphans = cms.InputTag("PFMuJetProducer05PXBL3PXFL2", "Orphans"),
)
cutFlowAnalyzers = cms.Sequence(
#    cutFlowAnalyzer * 
#    cutFlowAnalyzerPXBL2PXFL2
    cutFlowAnalyzerPXBL3PXFL2
)
