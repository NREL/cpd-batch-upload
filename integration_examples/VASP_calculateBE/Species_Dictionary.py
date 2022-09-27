#!/usr/bin/env python

#import argparse
#
#parser = argparse.ArgumentParser(description='Provide species adsorbate and reference species information')
#parser.add_argument('--species',help='Adsorbate formula of species')

def species_info(species):
	if species=='Al':
	    MolecularFormula='Al'
	    SMILES='[Al]'
	    ConnectivitySMILES='[Al]'
	    Name='aluminum, atomic'
	elif species=='B':
	    MolecularFormula='B'
	    SMILES='[B]'
	    ConnectivitySMILES='[B]'
	    Name='boron, atomic'
	elif species=='Ca':
	    MolecularFormula='Ca'
	    SMILES='[Ca]'
	    ConnectivitySMILES='[Ca]'
	    Name='calcium, atomic'
	elif species=='Cl':
	    MolecularFormula='Cl'
	    SMILES='[Cl]'
	    ConnectivitySMILES='[Cl]'
	    Name='chlorine, atomic'
	elif species=='Fe':
	    MolecularFormula='Fe'
	    SMILES='[Fe]'
	    ConnectivitySMILES='[Fe]'
	    Name='iron, atomic'
	elif species=='K':
	    MolecularFormula='K'
	    SMILES='[K]'
	    ConnectivitySMILES='[K]'
	    Name='potassium, atomic'
	elif species=='Mg':
	    MolecularFormula='Mg'
	    SMILES='[Mg]'
	    ConnectivitySMILES='[Mg]'
	    Name='magnesium, atomic'
	elif species=='Mn':
	    MolecularFormula='Mn'
	    SMILES='[Mn]'
	    ConnectivitySMILES='[Mn]'
	    Name='manganese, atomic'
	elif species=='Na':
	    MolecularFormula='Na'
	    SMILES='[Na]'
	    ConnectivitySMILES='[Na]'
	    Name='sodium, atomic'
	elif species=='N':
	    MolecularFormula='N'
	    SMILES='[N]'
	    ConnectivitySMILES='[N]'
	    Name='nitrogen, atomic'
	elif species=='P':
	    MolecularFormula='P'
	    SMILES='[P]'
	    ConnectivitySMILES='[P]'
	    Name='phosphorus, atomic'
	elif species=='S':
	    MolecularFormula='S'
	    SMILES='[S]'
	    ConnectivitySMILES='[S]'
	    Name='sulfur, atomic'
	elif species=='Si':
	    MolecularFormula='Si'
	    SMILES='[Si]'
	    ConnectivitySMILES='[Si]'
	    Name='silicon, atomic'
	elif species=='Zn':
	    MolecularFormula='Zn'
	    SMILES='[Zn]'
	    ConnectivitySMILES='[Zn]'
	    Name='zinc, atomic'
	elif species=='COS':
	    MolecularFormula='COS'
	    SMILES='O=C=S'
	    ConnectivitySMILES='[O][C][S]'
	    Name='carbonyl sulfide'
	elif species=='H2S':
	    MolecularFormula='H2S'
	    SMILES='S'
	    ConnectivitySMILES='S'
	    Name='hydrogen sulfide'
	elif species=='HCl':
	    MolecularFormula='HCl'
	    SMILES='Cl'
	    ConnectivitySMILES='Cl'
	    Name='hydrogen chloride'
	elif species=='HCN':
	    MolecularFormula='HCN'
	    SMILES='C#N'
	    ConnectivitySMILES='[CH][N]'
	    Name='hydrogen cyanide'
	elif species=='K2O':
	    MolecularFormula='K2O'
	    SMILES='[K+].[O2-].[K+]'
	    ConnectivitySMILES='[K+].[O2-].[K+]'
	    Name='potassium oxide'
	elif species=='KCl':
	    MolecularFormula='KCl'
	    SMILES='[Cl-].[K+]'
	    ConnectivitySMILES='[Cl-].[K+]'
	    Name='potassium chloride'
	elif species=='NH3':
	    MolecularFormula='NH3'
	    SMILES='N'
	    ConnectivitySMILES='N'
	    Name='ammonia'

	return MolecularFormula, SMILES, ConnectivitySMILES, Name
