#!/usr/bin/env python

import numpy as np
import os
import os.path as basename
#import mmap
import csv
import Species_Dictionary as sd

gas_dir = "/home/stacey/gas/pbe-d3/" #Set pathway to gas-phase calculation directory. Species subfolders in this directory must match the Species text used in adsorbate calculation folders.
parent_dir = os.getcwd() #Set a path for the working directory, should be for a given surface and have all of the adsorbate folders to loop over
largeUnitCell = 0 #In this specific case, one of the larger adsorbates required a larger unit cell, parameter to check which energies/metadata to use.

##Obtain methods from Methods file##
with open('Methods', 'r') as file_:
	methods = file_.readlines()

Software = str(methods[0]).split(' #')[0]
XC = str(methods[1]).split(' #')[0]
Potentials = str(methods[2]).split(' #')[0]
BasisSet = str(methods[3]).split(' #')[0]
SpinPol = str(methods[4]).split(' #')[0]
ZPE = str(methods[5]).split(' #')[0]
FixedSubstrate = str(methods[6]).split(' #')[0]

##Obtain bulk and surface properties from BulkSurfaceProperties file##
with open('BulkSurfaceProperties', 'r') as file_:
	bulksurfprop = file_.readlines()

BulkFormula = str(bulksurfprop[0]).split(' #')[0]
Element1 = str(bulksurfprop[1]).split(' #')[0]
Sequence1 = str(bulksurfprop[2]).split(' #')[0]
Coefficient1 = str(bulksurfprop[3]).split(' #')[0]
Element2 = str(bulksurfprop[4]).split(' #')[0]
Sequence2 = str(bulksurfprop[5]).split(' #')[0]
Coefficient2 = str(bulksurfprop[6]).split(' #')[0]
PrimaryClass = str(bulksurfprop[7]).split(' #')[0]
SecondaryClass = str(bulksurfprop[8]).split(' #')[0]
IsStretched = str(bulksurfprop[9]).split(' #')[0]
IsCompressed = str(bulksurfprop[10]).split(' #')[0]
SpaceGroup = str(bulksurfprop[11]).split(' #')[0]
a = str(bulksurfprop[12]).split(' #')[0]
b = str(bulksurfprop[13]).split(' #')[0]
c = str(bulksurfprop[14]).split(' #')[0]
NanoparticleSize_noAtoms = str(bulksurfprop[15]).split(' #')[0]
Layer1_Name = str(bulksurfprop[16]).split(' #')[0]
Layer1_Element1 = str(bulksurfprop[17]).split(' #')[0]
Layer1_Sequence1 = str(bulksurfprop[18]).split(' #')[0]
Layer1_Coefficient1 = str(bulksurfprop[19]).split(' #')[0]
Layer1_Element2 = str(bulksurfprop[20]).split(' #')[0]
Layer1_Sequence2 = str(bulksurfprop[21]).split(' #')[0]
Layer1_Coefficient2 = str(bulksurfprop[22]).split(' #')[0]
Layer2_Name = str(bulksurfprop[23]).split(' #')[0]
Layer2_Element1 = str(bulksurfprop[24]).split(' #')[0]
Layer2_Sequence1 = str(bulksurfprop[25]).split(' #')[0]
Layer2_Coefficient1 = str(bulksurfprop[26]).split(' #')[0]
Layer2_Element2 = str(bulksurfprop[27]).split(' #')[0]
Layer2_Sequence2 = str(bulksurfprop[28]).split(' #')[0]
Layer2_Coefficient2 = str(bulksurfprop[29]).split(' #')[0]
Facet = str(bulksurfprop[30]).split(' #')[0]
Termination = str(bulksurfprop[31]).split(' #')[0]
#CellSymmetry = str(bulksurfprop[32]).split(' #')[0] ### Had this determined in this master script here instead because unit cell size changed.

##Obtain metadata from Metadata file##
with open('Metadata', 'r') as file_:
        metadata = file_.readlines()

ExternalNotes = str(metadata[0]).split(' #')[0]
DOI = str(metadata[1]).split(' #')[0]
InternalComments = str(metadata[2]).split(' #')[0]
FirstName = str(metadata[3]).split(' #')[0]
LastName = str(metadata[4]).split(' #')[0]
Affiliation = str(metadata[5]).split(' #')[0]
Email = str(metadata[6]).split(' #')[0]

##Extract clean-surface energetics from OSZICAR##
with open('Clean/OSZICAR', 'r') as file_:
	line_list = list(file_)
	line_list.reverse()
	for line in line_list:
		if line.find('E0') != -1:
			E_clean = line.split()[4]
			#print(E_clean)
			break

##Extract clean surface energetics from OSZICAR for larger surface unit cell##
if os.path.exists('Clean/4x4/'):
	largeUnitCell = 1
	with open('Clean/4x4/OSZICAR', 'r') as file_:
		line_list = list(file_)
		line_list.reverse()
	for line in line_list:
		if line.find('E0') != -1:
			E_clean_largeuc = line.split()[4]
			#print(E_clean_largeuc)
			break

##Loop over adsorbate directories to get adsorption calculation, adsorption species, and reference species data
for ads in sorted(os.listdir(parent_dir)):
	if os.path.isdir(ads) and ads != "Clean":
		species = ads.split('_')
		ads_species = species[0]
		ads_species_data = sd.species_info(ads_species)
		ref_coefficient1 = species[1]
		ref_species = species[2]
		ref_species_data = sd.species_info(ref_species)
		## Calculate gas-phase reference energy with gas-phase energy and stoichiometric coefficient
		gas_oszicar = os.path.join(gas_dir, ref_species, 'OSZICAR')
		with open(gas_oszicar, 'r') as file_:
			line_list = list(file_)
			line_list.reverse()
		for line in line_list:
			if line.find('E0') != -1:
				E_ref = float(ref_coefficient1) * float(line.split()[4])
				break
		ads_dir = os.path.join(parent_dir, ads)
		os.chdir(ads_dir)
		##Get surface coverage and cell symmetry information##
		for cov in os.listdir(ads_dir):
			if os.path.isdir(cov):
				cov_base = cov.split('_')
				cov_frac_base = cov_base[0].split('.')
				CoverageFraction =  str(cov_frac_base[0]) + "/" + str(cov_frac_base[1])
				CoveragePer = cov_base[1]
				CellSymmetry = cov_base[2]
				cov_dir = os.path.join(ads_dir, cov)
				os.chdir(cov_dir)
				##Get adsorption site and calculate adsorption energy, determine if most stable energy##
				for site in os.listdir(cov_dir):
					if os.path.isdir(site):
						AdsSite_base = site.split('_')
						AdsSite = AdsSite_base[0]
						if len(AdsSite_base) == 2:
							MostStable = "TRUE"	
						else:
							MostStable = "FALSE"
						ads_oszicar = os.path.join(cov_dir, site, 'OSZICAR')
						with open(ads_oszicar, 'r') as file_:
							line_list = list(file_)
							line_list.reverse()
						for line in line_list:
							if line.find('E0') != -1:
								E_tot = line.split()[4]
								break
						if ads_species == 'K2O' and largeUnitCell == 1:
							BEcalc = float(E_tot) - float(E_ref) - float(E_clean_largeuc)
							BE = str(round(BEcalc,2))	
						else:
							BEcalc = float(E_tot) - float(E_ref) - float(E_clean)
							BE = str(round(BEcalc,2))
						###Write all data to the .csv file###
						with open('/home/stacey/test.csv', 'a') as csv_file:
							file_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
							file_writer.writerow([BulkFormula, \
								PrimaryClass, \
								SecondaryClass, \
								IsStretched, \
								IsCompressed, \
								SpaceGroup, \
								a, \
								b, \
								c, \
								NanoparticleSize_noAtoms, \
								Layer1_Name, \
								#Layer1_Element1, \
								#Layer1_Sequence1, \
								#Layer1_Coefficient1, \
								#Layer1_Element2, \
								#Layer1_Sequence2, \
								#Layer1_Coefficient2, \
								Layer2_Name, \
								#Layer2_Element1, \
								#Layer2_Sequence1, \
								#Layer2_Coefficient1, \
								#Layer2_Element2, \
								#Layer2_Sequence2, \
								#Layer2_Coefficient2, \
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
								ads_species, \
								ads_species_data[0], \
								ads_species_data[1], \
								ads_species_data[2], \
								ads_species_data[3], \
								f'"{CoverageFraction}"', \
								CoveragePer, \
								AdsSite, \
								ref_coefficient1, \
								ref_species, \
								ref_species_data[0], \
								ref_species_data[1], \
								ref_species_data[2], \
								ref_species_data[3], \
								'', \
								'', \
								'', \
								'', \
								'', \
								'', \
								'', \
								'', \
								'', \
								'', \
								'', \
								'', \
								'', \
								'', \
								'', \
								'', \
								'', \
								'', \
								BE, \
								MostStable, \
								ExternalNotes, \
								DOI, \
								InternalComments, \
								FirstName, \
								LastName, \
								Affiliation, \
								Email])
		os.chdir(parent_dir)
