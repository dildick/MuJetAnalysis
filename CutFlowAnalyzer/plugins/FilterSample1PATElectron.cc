// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "MuJetAnalysis/AnalysisTools/interface/Helpers.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/VIDCutFlowResult.h"

//******************************************************************************
//                           Class declaration
//******************************************************************************

class FilterSample1PATElectron : public edm::EDFilter
{
public:
  explicit FilterSample1PATElectron(const edm::ParameterSet&);
  ~FilterSample1PATElectron();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  virtual void beginJob() ;
  virtual bool filter(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;

  virtual void beginRun(edm::Run const&, edm::EventSetup const&);
  virtual void endRun(edm::Run const&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

  //****************************************************************************
  //          RECO LEVEL VARIABLES, BRANCHES, COUNTERS AND SELECTORS
  //****************************************************************************

  // Labels to access
  edm::EDGetTokenT<pat::ElectronCollection > m_electrons;
  edm::EDGetToken m_electron;
  edm::EDGetTokenT<edm::ValueMap<bool> > eleIdMapToken;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
FilterSample1PATElectron::FilterSample1PATElectron(const edm::ParameterSet& iConfig)
{
  m_electrons           = consumes<pat::ElectronCollection >(edm::InputTag("patElectrons"));
  m_electron        = mayConsume<edm::View<reco::GsfElectron> >(iConfig.getParameter<edm::InputTag>("electrons"));

  // m_electron     = consumes<edm::View<pat::Electron> >(iConfig.getParameter<edm::InputTag>("electron"));
  eleIdMapToken     = (consumes<edm::ValueMap<bool> >(iConfig.getParameter<edm::InputTag>("elIdFullInfoMap")));
}


FilterSample1PATElectron::~FilterSample1PATElectron()
{
}

//
// member functions
//

// ------------ method called for each event  ------------
bool
FilterSample1PATElectron::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;

  //****************************************************************************
  //                          RECO LEVEL ANALYSIS START
  //****************************************************************************

  edm::Handle<pat::ElectronCollection > patelectrons;
  iEvent.getByToken(m_electrons, patelectrons);
  const pat::ElectronCollection& electronC = *patelectrons.product();

  edm::Handle<edm::View<reco::GsfElectron> > electrons;
  iEvent.getByToken(m_electron, electrons);

  //Get the electron ID data from the event stream.
   edm::Handle<edm::ValueMap<bool> > ele_id_decisions;
   iEvent.getByToken(eleIdMapToken, ele_id_decisions);

  // require at least 3 electrons
  int nEle = 0;
  // for (const auto& p : electronC) {
  //     if (p.pt() >= 20 and abs(p.eta())<2.5) nEle++;
  // }

  for (size_t i=0, size=electrons->size(); i<size; ++i){   
    const auto ele = electrons->ptrAt(i);          // easier if we use ptrs for the id

    // pt selection
    if (ele->pt()< 20) continue;
    // std::cout << "electron pt " << ele->pt() << std::endl;

    // std::cout << "electron eta " << ele->eta() << std::endl;
    // eta selection
    if (std::abs(ele->eta()) > 2.5) continue;
    
    // dz cut
    reco::GsfTrackRef theTrack = ele->gsfTrack();
    double dxy = std::abs(theTrack->dxy());
    double dz = std::abs(theTrack->dz());
    double eta = ele->superCluster()->eta();
    // std::cout << "electron dxy " << dxy << std::endl;
    // std::cout << "electron dz " << dz << std::endl;

    bool isPassEleId  = (*ele_id_decisions)[ele];

    /*    
    // if (!isPassEleId) continue;
    // dxy less than 0.01 for electrons in the barrel
    if (std::abs(eta)<1.479){
      if (dxy > 0.01) continue;
      if (dz > 0.4) continue;
      // if (ele->full5x5_sigmaIetaIeta() > 0.00998) continue;
      // if (dEtaInSeed(ele) > 0.00308) continue;
      // if (GsfEleConversionVetoCut::GsfEleDPhiInCut::value(ele) > 0.0816) continue;
      // if (GsfEleHadronicOverEMCut::value(ele)  > 0.0414) continue;
      // if (GsfEleEffAreaPFIsoCut::GsfEleEInverseMinusPInverseCut::value(ele)>0.0129) continue;
    }
    if (std::abs(eta)>1.479){
      if (dxy > 0.07) continue;
      if (dz > 0.6) continue;
      // if (ele->full5x5_sigmaIetaIeta() > 0.0292) continue;
      // if (dEtaInSeed(ele) > 0.00605) continue;
      // if (GsfEleConversionVetoCut::GsfEleDPhiInCut::value(ele) > 0.0394) continue;
      // if (GsfEleHadronicOverEMCut::value(ele)  > 0.0641) continue;
      // if (GsfEleEffAreaPFIsoCut::GsfEleEInverseMinusPInverseCut::value(ele)>0.0129) continue;
    }
    */
    nEle++;
  }
  return nEle >= 1;
}


// ------------ method called once each job just before starting event loop  ------------
void
FilterSample1PATElectron::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
FilterSample1PATElectron::endJob()
{
}

// ------------ method called when starting to processes a run  ------------
void
FilterSample1PATElectron::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
FilterSample1PATElectron::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
FilterSample1PATElectron::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
FilterSample1PATElectron::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
FilterSample1PATElectron::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//Indentation change
//define this as a plug-in
DEFINE_FWK_MODULE(FilterSample1PATElectron);
