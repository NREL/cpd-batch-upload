# Overview
<div style="text-align: justify">For a single metal surface/cluster, the Compile_Upload_CPD_VAPS.py python script allows users to calculate binding energies directly from VASP output files and compile all of the data into a .csv that can be uploaded to the CPD. Modifications will be necessary if ZPE corrections are added to the calculation to account for these values in the adsorption energy calculation.

# Required Subdirectory Structure
To use the Compile_Upload_CPD_VASP.py script, users must set up subdirectories for the adsorption calculations in a particular format. All calculations that the user seeks to upload to the CPD must be placed in the same parent directory, and each folder must correspond to an adsorbate species and be named in the format: <span style="color:blue">{Adsorbate}_{RefCoefficient}_{RefSpecies}</span>. In its current form, the script only handles a single reference species for the adsorption energy calculation, but simple modifications to the script can be made to allow it to handle multiple reference species. In this example, Cl adsorption was calculated on Ag(100). The parent directory is:

><span style="color:blue">Ag100/

Inside this parent directory are directories for the Cl adsorption calculation:
><span style="color:blue">Cl_1_Cl/

and the clean-surface calculation:
><span style="color:blue">Clean/
        
Within the Cl adsorption folder, the periodic surface unit cell and coverage information for the calculation is provided in the following format:
><span style="color:blue">1.9_Ag_3x3
        
1.9 is the Coverage fraction (1/9), Ag is the Coverage per (Ag surface atom), and 3x3 is the surface unit cell size.
        
Within this subdirectory are the unique converged adsorption sites direcroties. In this case,
><span style="color:blue">4f_x/ b/
        
The "_x" indicates the most-stable adsorption energy.

# Required files
### VASP Files
To use this script, the OSZICAR for the converged calculations must be present both the Clean/ subdirectory, as well as in each adsorption site subdirectory. In addition, the directory path containing the gas-phase energies should be provided in the Compile_Upload_CPD_VASP.py file (line 10). The directory containing the gas-phase energy calculation must have the same name as {RefSpecies} in the adsorbate subdirectory, and should contain the corresponding OSZICAR file.

### CSV file
The path must be set in Compile_Upload_CPD_VASP.py for writing the .csv file (line 152)

# Supplementary Files
To compile the species data for both the adsorbate and reference species, the Species_Dictionary.py file should be placed in the same directory as the Compile_Upload_CPD_VASP.py file. If the species studied is not currently within the Species_Dictionary.py file, the user should add this information.
        
Within the parent directory (here, Ag100/), three files should be present:
><span style="color:green">BulkSurfaceProperties, Metadata, and Methods

These files contain all of the data pertaining to the surface/cluster material, the metadata associated with the calculation, and the methods used to perform the calculation. See https://cpd.chemcatbio.org/parameter-guide for more information.
        
# Running the script
To run the Compile_Upload_CPD_VASP.py script, simply cd into the parent directory (here Ag100/) and run the Compile_Upload_CPD_VASP.py script. Running this script will create the .csv file and populate the required entries. This populated Database_empty_template.csv file can then be uploaded to the CPD (see **NREL/cpd-batch-upload/cpdupload** folder).

</div>
