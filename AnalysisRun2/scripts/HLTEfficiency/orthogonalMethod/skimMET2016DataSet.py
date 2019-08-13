from ROOT import *


Samples_2016_BH_SingleElectron = {
  '2016B' : [
    ], 
  '2016C' : [
    "/fdata/hepx/store/user/dildick/SingleElectron/crab_SingleElectron-Run2016C-07Aug17-v1-20180519_v2/180519_155843/0000/out_ana*.root",
    "/fdata/hepx/store/user/dildick/SingleElectron/crab_SingleElectron-Run2016C-07Aug17-v1-20180519_v2/180519_155843/0001/out_ana*.root",
    ],
  '2016D' : [
    "/fdata/hepx/store/user/dildick/SingleElectron/crab_SingleElectron-Run2016D-07Aug17-v1-20180519_v2/180519_155902/0000/out_ana*.root",
    "/fdata/hepx/store/user/dildick/SingleElectron/crab_SingleElectron-Run2016D-07Aug17-v1-20180519_v2/180519_155902/0001/out_ana*.root",
    ],
  '2016E' : [
    "/fdata/hepx/store/user/dildick/SingleElectron/crab_SingleElectron-Run2016E-07Aug17-v1-20180519_v2/180519_155924/0000/out_ana*.root",
    "/fdata/hepx/store/user/dildick/SingleElectron/crab_SingleElectron-Run2016E-07Aug17-v1-20180519_v2/180519_155924/0001/out_ana*.root",
    "/fdata/hepx/store/user/dildick/SingleElectron/crab_SingleElectron-Run2016E-07Aug17-v1-20180519_v2/180519_155924/0002/out_ana*.root",
    ],
  '2016F' : [
    "/fdata/hepx/store/user/dildick/SingleElectron/crab_SingleElectron-Run2016F-07Aug17-v1-20180519_v2/180519_155943/0000/out_ana*.root",
    ],
  '2016G' : [
    "/fdata/hepx/store/user/dildick/SingleElectron/crab_SingleElectron-Run2016G-07Aug17-v1-20180519_v2/180519_160001/0000/out_ana*.root",
    "/fdata/hepx/store/user/dildick/SingleElectron/crab_SingleElectron-Run2016G-07Aug17-v1-20180519_v2/180519_160001/0001/out_ana*.root",
    "/fdata/hepx/store/user/dildick/SingleElectron/crab_SingleElectron-Run2016G-07Aug17-v1-20180519_v2/180519_160001/0002/out_ana*.root",
    "/fdata/hepx/store/user/dildick/SingleElectron/crab_SingleElectron-Run2016G-07Aug17-v1-20180519_v2/180519_160001/0003/out_ana*.root",
    ],
  '2016H' : [
    "/fdata/hepx/store/user/dildick/SingleElectron/crab_SingleElectron-Run2016H-07Aug17-v1-20180519_v2/180519_160027/0000/out_ana*.root",
    "/fdata/hepx/store/user/dildick/SingleElectron/crab_SingleElectron-Run2016H-07Aug17-v1-20180519_v2/180519_160027/0001/out_ana*.root",
    "/fdata/hepx/store/user/dildick/SingleElectron/crab_SingleElectron-Run2016H-07Aug17-v1-20180519_v2/180519_160027/0002/out_ana*.root",
    "/fdata/hepx/store/user/dildick/SingleElectron/crab_SingleElectron-Run2016H-07Aug17-v1-20180519_v2/180519_160027/0003/out_ana*.root",
    "/fdata/hepx/store/user/dildick/SingleElectron/crab_SingleElectron-Run2016H-07Aug17-v1-20180519_v2/180519_160027/0004/out_ana*.root",
    ],
  }

def makeSkim(era, date="20180520"):

  chain = TChain("cutFlowAnalyzerPXBL3PXFL2/Events");

  for p in Samples_2016_BH_SingleElectron[era]:
      chain.Add(p)
      print p

  ## save to file
  newFile = TFile.Open("out_ana_selected_SingleElectron_" + era + "_" + date + ".root","RECREATE") 
  newChain = chain.CopyTree("nRecoMu>=3")
  newChain.AutoSave()
  newFile.Close()

  print "Processed", era


def makeSkims():

  for p in Samples_2016_BH_SingleElectron:
      makeSkim(p)

makeSkims()




