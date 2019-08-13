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


cutFlowAnalyzer = cms.EDAnalyzer('CutFlowAnalyzer_AOD',
    analyzerDebug = cms.int32(100),
#    muons = cms.InputTag("cleanPatTrackerMuonsTriggerMatch"),
#    muJets = cms.InputTag("TrackerMuJetProducer05"),
    muons = cms.InputTag("cleanPatPFMuonsTriggerMatch"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    muJets = cms.InputTag("PFMuJetProducer05"),
    muJetOrphans = cms.InputTag("PFMuJetProducer05", "Orphans"),
    triggerEvent = cms.InputTag("patTriggerEvent"),
    tracks = cms.InputTag("generalTracks"),
    TriggerResults = cms.InputTag("TriggerResults","","HLT"),
    TrackRefitter = cms.InputTag("TrackRefitter"),
    genParticles = cms.InputTag("genParticles"),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    electrons = cms.InputTag("gedGsfElectrons"),
    patJet = cms.InputTag("patJets"),##
    patMET = cms.InputTag("patMETs"),
    DiMuons_Iso_Max = cms.double(2.0),
    nThrowsConsistentVertexesCalculator = cms.int32(0),
    barrelPixelLayer = cms.int32(1),
    endcapPixelLayer = cms.int32(1),
    runDisplacedVtxFinder = cms.bool(False),
    runPixelHitRecovery = cms.bool(False),
    Traj = cms.InputTag("TrackRefitter"),
    NavigationSchool   = cms.string('SimpleNavigationSchool'),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag('MeasurementTrackerEvent'),
    Propagator = cms.string("RungeKuttaTrackerPropagator"),
    runBBestimation = cms.bool(False),
    #elIdFullInfoMap  = cms.InputTag(vid_el_loose),
    elIdFullInfoMapM = cms.InputTag(vid_el_medium),
    elIdFullInfoMap = cms.InputTag(vid_el_tight),
    #elIdFullInfoMap = cms.InputTag(vid_el_tight),
    skimOutput = cms.bool(False),
    signalHltPaths = cms.vstring(
        'HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v1',
        'HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v2',
        'HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v3',
        'HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v4',
        'HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v5',
        'HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v6',
    ),
    backupHltPaths = cms.vstring(
        'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v1',
        'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v2',
        'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v3',
        'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v4',
        'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v5',
        'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v6',
    ),
    otherMuHltPaths = cms.vstring(
        'HLT_DoubleMu18NoFiltersNoVtx_v3',
        'HLT_DoubleMu23NoFiltersNoVtxDisplaced_v3',
        'HLT_DoubleMu28NoFiltersNoVtxDisplaced_v3',
        'HLT_DoubleMu33NoFiltersNoVtx_v3',
        'HLT_DoubleMu38NoFiltersNoVtx_v3',
        'HLT_DoubleMu8_Mass8_PFHT250_v2',
        'HLT_DoubleMu8_Mass8_PFHT300_v5',
        'HLT_L2DoubleMu23_NoVertex_v3',
        'HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10_v3',
        'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_Mass10_v3',
        'HLT_Mu10_CentralPFJet30_BTagCSV_p13_v2',
        'HLT_Mu17_Mu8_DZ_v3',
        'HLT_Mu17_Mu8_SameSign_DZ_v2',
        'HLT_Mu17_Mu8_SameSign_v2',
        'HLT_Mu17_Mu8_v2',
        'HLT_Mu17_TkMu8_DZ_v3',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v3',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v3',
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v3',
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v3',
        'HLT_Mu17_TrkIsoVVL_v3',
        'HLT_Mu17_v3',
        'HLT_Mu20_Mu10_DZ_v2',
        'HLT_Mu20_Mu10_SameSign_DZ_v2',
        'HLT_Mu20_Mu10_SameSign_v1',
        'HLT_Mu20_Mu10_v2',
        'HLT_Mu27_TkMu8_v3',
        'HLT_Mu30_TkMu11_v3',
        'HLT_Mu3_PFJet40_v2',
        'HLT_Mu40_TkMu11_v3',
        'HLT_Mu8_TrkIsoVVL_v4',
        'HLT_Mu8_v4',
        'HLT_TripleMu_12_10_5_v3',
        'HLT_TripleMu_5_3_3_v1',
    )
)
