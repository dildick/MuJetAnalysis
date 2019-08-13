import FWCore.ParameterSet.Config as cms


year=2016

vid_el_loose  = ''
vid_el_medium = ''
vid_el_tight  = ''
if year==2016:
    vid_el_loose  = "egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-loose"
    vid_el_medium = "egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-medium"
    vid_el_tight  = "egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-tight"
elif year==2017:
    vid_el_loose  = "egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-loose"
    vid_el_medium = "egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-medium"
    vid_el_tight  = "egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-tight"

singleElectronFilterPAT = cms.EDFilter("FilterSample1PATElectron",
    electrons = cms.InputTag("gedGsfElectrons"),
    #elIdFullInfoMap  = cms.InputTag(vid_el_loose),
    #elIdFullInfoMap = cms.InputTag(vid_el_medium),
    elIdFullInfoMap = cms.InputTag(vid_el_tight)                                  
)
