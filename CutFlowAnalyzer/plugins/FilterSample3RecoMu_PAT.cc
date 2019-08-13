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

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "MuJetAnalysis/AnalysisTools/interface/Helpers.h"

//******************************************************************************
//                           Class declaration
//******************************************************************************

class FilterSample3RecoMu_PAT : public edm::EDFilter
{
public:
  explicit FilterSample3RecoMu_PAT(const edm::ParameterSet&);
  ~FilterSample3RecoMu_PAT();

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
  edm::EDGetTokenT<pat::MuonCollection > m_muons;
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
FilterSample3RecoMu_PAT::FilterSample3RecoMu_PAT(const edm::ParameterSet& iConfig)
{
  m_muons           = consumes<pat::MuonCollection >(edm::InputTag("patMuons"));
}


FilterSample3RecoMu_PAT::~FilterSample3RecoMu_PAT()
{
}

//
// member functions
//

// ------------ method called for each event  ------------
bool
FilterSample3RecoMu_PAT::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;

  //****************************************************************************
  //                          RECO LEVEL ANALYSIS START
  //****************************************************************************

  edm::Handle<pat::MuonCollection > muons;
  iEvent.getByToken(m_muons, muons);
  const pat::MuonCollection& muonC = *muons.product();

  // require at least 3 muons
  int nMu8 = 0;
  int nMu17 = 0;
  for (const auto& p : muonC) {
    std::cout << p.pt() << " " << p.eta() << " " << p.phi() << std::endl;
    if ( tamu::helpers::isPFMuonLoose( &p ) ) {
      if (p.pt() >= 8 and std::abs(p.eta())<2.4) nMu8++;
      if (p.pt() >= 17 and std::abs(p.eta())<2.4) nMu17++;
    }
  }
  if (nMu8 >= 3 and nMu17 >= 1)
    std::cout << "Pass" << std::endl;
  return nMu8 >= 3  and nMu17 >= 1;
}


// ------------ method called once each job just before starting event loop  ------------
void
FilterSample3RecoMu_PAT::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
FilterSample3RecoMu_PAT::endJob()
{
}

// ------------ method called when starting to processes a run  ------------
void
FilterSample3RecoMu_PAT::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
FilterSample3RecoMu_PAT::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
FilterSample3RecoMu_PAT::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
FilterSample3RecoMu_PAT::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
FilterSample3RecoMu_PAT::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//Indentation change
//define this as a plug-in
DEFINE_FWK_MODULE(FilterSample3RecoMu_PAT);
