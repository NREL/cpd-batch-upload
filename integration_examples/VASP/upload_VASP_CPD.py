#!/usr/bin/env python
import os
from os.path import basename
import csv

###Bulk Properties###
BulkFormula = "Pd"
Element1 = "Pd"
Sequence1 = "1"
Coefficient1 = "1"
Element2 = ""
Sequence2 = ""
Coefficient2 = ""
PrimaryClass = "Transition metal"
SecondaryClass = ""
IsStretched = "FALSE"
IsCompressed = "FALSE"
SpaceGroup = "Fm3m"
LatticeConstant_a = "3.885"
LatticeConstant_b = ""
LatticeConstant_c = ""
NP_noAtoms = ""
NP_FirstLayer_Name = ""
NP_FirstLayer_Element1 = ""
NP_FirstLayer_Sequence1 = ""
NP_FirstLayer_Coefficient1 = ""
NP_FirstLayer_Element2 = ""
NP_FirstLayer_Sequence2 = ""
NP_FirstLayer_Coefficient2 = ""
NP_SecondLayer_Name = ""
NP_SecondLayer_Element1 = ""
NP_SecondLayer_Sequence1 = ""
NP_SecondLayer_Coefficient1 = ""
NP_SecondLayer_Element2 = ""
NP_SecondLayer_Sequence2 = ""
NP_SecondLayer_Coefficient2 = ""

###SurfaceProperties###
Facet = "(111)"
Termination = "Pd"
CellSymmetry = ""

###Methods###
Software = "VASP"
XC = "PBE-D3"
Potentials = "projector augmented wave"
BasisSet = "plane wave"
SpinPol = "TRUE"
ZPE = "TRUE" 
FixedSubstrate = "FALSE"

###AdsorptionMeasurement_ReferenceSpeciesInformation###
PathName = basename(os.path.abspath(os.getcwd()))
AdsName = PathName.split("_")[0]
Site = PathName.split("_")[1]
Path = os.path.abspath(os.getcwd())
CoverageFraction = "1/22"
CoveragePer = "Pd"

if AdsName == "h":
	AdsorbateFormula = "H"
	MolecularFormula = "H"
	SMILES = "[H]"
	ConnSMILES = "[H]"
	AdsorbateName = "hydrogen, atomic"
	StoichiometricCoefficient1 = "0.5"
	RefFormula1 = "H2"
	RefMolecularFormula1 = "H2"
	RefSMILES1 = "[H][H]"
	RefConnSMILES1 = "[H][H]"
	RefName1 = "hydrogen"
	RefEnergy = -6.7591926
	RefZPE = 0.266
elif AdsName == "co":
        AdsorbateFormula = "CO"
        MolecularFormula = "CO"
        SMILES = "[C]#[O]"
        ConnSMILES = "[C][O]"
        AdsorbateName = "carbon monoxide"
        StoichiometricCoefficient1 = "1"
        RefFormula1 = "CO"
        RefMolecularFormula1 = "CO"
        RefSMILES1 = "[C]#[O]"
        RefConnSMILES1 = "[C][O]"
        RefName1 = "carbon monoxide"
        RefEnergy = -14.795235
        RefZPE = 0.132
elif AdsName == "naphthalene":
        AdsorbateFormula = "C10H8"
        MolecularFormula = "C10H8"
        SMILES = "c1c2ccccc2ccc1"
        ConnSMILES = "[CH]1[CH]2[CH][CH][CH][CH][CH]2[CH][CH][CH]1"
        AdsorbateName = "naphthalene"
        StoichiometricCoefficient1 = "1"
        RefFormula1 = "C10H8"
        RefMolecularFormula1 = "C10H8"
        RefSMILES1 = "c1c2ccccc2ccc1"
        RefConnSMILES1 = "[CH]1[C]2[CH][CH][CH][CH][C]2[CH][CH][CH]1"
        RefName1 = "naphthalene"
        RefEnergy = -119.79112
        RefZPE = 3.838
elif AdsName == "tetralin":
        AdsorbateFormula = "C10H12"
        MolecularFormula = "C10H12"
        SMILES = "c1c2CCCCc2ccc1"
        ConnSMILES = "[CH]1[C]2CCCC[C]2[CH][CH][CH]1"
        AdsorbateName = "tetralin"
        StoichiometricCoefficient1 = "1"
        RefFormula1 = "C10H12"
        RefMolecularFormula1 = "C10H12"
        RefSMILES1 = "c1c2CCCCc2ccc1"
        RefConnSMILES1 = "[CH]1[C]2CCCC[C]2[CH][CH][CH]1"
        RefName1 = "tetralin"
        RefEnergy = -134.96931
        RefZPE = 5.111

StoichiometricCoefficient2 = ""
RefFormula2 = ""
RefMolecularFormula2 = ""
RefSMILES2 = ""
RefConnSMILES2 = ""
RefName2 = ""
StoichiometricCoefficient3 = ""
RefFormula3 = ""
RefMolecularFormula3 = ""
RefSMILES3 = ""
RefConnSMILES3 = ""
RefName3 = ""
StoichiometricCoefficient4 = ""
RefFormula4 = ""
RefMolecularFormula4 = ""
RefSMILES4 = ""
RefConnSMILES4 = ""
RefName4 = ""

###AdsorptionEnergy###
CleanEnergy = -471.61791
oszicar = open("OSZICAR", "r")
lastMatch = None
for line in oszicar:
	if 'E0' in line:
		lastMatch = str(line)
oszicar.close
AdsTotalEnergy = lastMatch.split()[4]
zpefile = open("zpe","r")
for line in zpefile:
	AdsZPE = line
zpefile.close
EBcalc = float(AdsTotalEnergy) + float(AdsZPE) - CleanEnergy - float(StoichiometricCoefficient1)*(RefEnergy + RefZPE)
EB = str(round(EBcalc,2))
MostStable = "TRUE"

###External Metadata###
ExtNotes = ""
DOI = "10.1021/acscatal.1c02101"

###InternalMetaData
IntComments = ""
UploaderFirstName = "Sean"
UploaderLastName = "Tacey"
UploaderAffiliation = "NREL"
UploaderEmail = "Sean.Tacey@nrel.gov"

#####WRITE TO CSV#####
with open('/projects/ccpc/stacey/ald/adsorption/pbe_d3+u/bare_pd111/upload/Upload-ALD-FY21-Q4.csv', 'a') as csv_file:
	file_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	file_writer.writerow([BulkFormula, \
		Element1, \
		Sequence1, \
		Coefficient1, \
		Element2, \
		Sequence2, \
		Coefficient2, \
		PrimaryClass, \
		SecondaryClass, \
		IsStretched, \
		IsCompressed, \
		SpaceGroup, \
		LatticeConstant_a, \
		LatticeConstant_b, \
		LatticeConstant_c, \
		NP_noAtoms, \
		NP_FirstLayer_Name, \
		NP_FirstLayer_Element1, \
		NP_FirstLayer_Sequence1, \
		NP_FirstLayer_Coefficient1, \
		NP_FirstLayer_Element2, \
		NP_FirstLayer_Sequence2, \
		NP_FirstLayer_Coefficient2, \
		NP_SecondLayer_Name, \
		NP_SecondLayer_Element1, \
		NP_SecondLayer_Sequence1, \
		NP_SecondLayer_Coefficient1, \
		NP_SecondLayer_Element2, \
		NP_SecondLayer_Sequence2, \
		NP_SecondLayer_Coefficient2, \
		Facet, \
		Termination, \
		CellSymmetry, \
		Software, \
		XC, \
		Potentials, \
		BasisSet, \
		SpinPol, \
		ZPE, \
		FixedSubstrate, \
		AdsorbateFormula, \
		MolecularFormula, \
		SMILES, \
		ConnSMILES, \
		AdsorbateName, \
		CoverageFraction, \
		CoveragePer, \
		Site, \
		StoichiometricCoefficient1, \
		RefFormula1, \
		RefMolecularFormula1, \
		RefSMILES1, \
		RefConnSMILES1, \
		RefName1, \
		StoichiometricCoefficient2, \
		RefFormula2, \
		RefMolecularFormula2, \
		RefSMILES2, \
		RefConnSMILES2, \
		RefName2, \
		StoichiometricCoefficient3, \
		RefFormula3, \
		RefMolecularFormula3, \
		RefSMILES3, \
		RefConnSMILES3, \
		RefName3, \
		StoichiometricCoefficient4, \
		RefFormula4, \
		RefMolecularFormula4, \
		RefSMILES4, \
		RefConnSMILES4, \
		RefName4, \
		EB, \
		MostStable, \
		ExtNotes, \
		DOI, \
		IntComments, \
		UploaderFirstName, \
		UploaderLastName, \
		UploaderAffiliation, \
		UploaderEmail])
