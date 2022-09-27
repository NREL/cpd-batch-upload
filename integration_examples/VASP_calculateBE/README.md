# Overview
<div style="text-align: justify">For a single metal surface/cluster, the Compile_Upload_CPD_VAPS.py python script allows users to calculate binding energies directly from VASP output files and compile all of the data into a .csv that can be uploaded to the CPD.

# Required Subdirectory Structure
To use the Compile_Upload_CPD_VASP.py script, users must set up subdirectories for the adsorption calculations in a particular format. All calculations that the user seeks to upload to the CPD must be placed in the same parent directory, and each folder must correspond to an adsorbate species and be named in the format: <span style="color:blue">{Adsorbate}_{RefCoefficient}_{}</span>. In its current form, the script only handles a single reference species for the adsorption energy calculation, but simple modifications to the script can be made to allow it to handle multiple reference species. In this example, Cl adsorption was calculated on Ag(100). The parent directory is:

><span style="color:blue">Ag100/

Inside this parent directory are directories for the Cl adsorption calculation:
><span style="color:blue">Cl_1_Cl/

and the clean-surface calculation:
><span style="color:blue">Clean/
        
Within the Cl adsorption folder, the periodic surface unit cell and coverage information for the calculation is provided in the following format:
><span style="color:blue">1.9_Ag_3x3
        
1.9 is the Coverage fraction (1/9), Ag is the Coverage per (Ag surface atom), and 3x3 is the surface unit cell size.
        
Within this subdirectory are the unique converged adsorption sites direcroties. In this case,
><span style="color:blue">4f_x/
><span style="color:blue">b/
        
The "_x" indicates the most-stable adsorption energy.

# Required files
### VASP Files
To use this script, the OSZICAR must be present in each subdirectory. Also, if zero-point energy (ZPE) corrections were included in the calculation (ZPE="TRUE" in line 49 of the provided upload_VASP_CPD.py file), an additional file titled "zpe" must be included in the subdirectory, which contains the ZPE value in eV.

### CSV Template
To populate the provided template CSV file (DatabaseUpload_BlankTemplate.csv), users should copy the file to the parent directory. The path to this CSV file must be specified in line 165 of the providedupload_VASP_CPD.py file.

# Manual Entries
In the current version of the upload_VASP_CPD.py script, only the total energy and ZPE from the adsorption calculation are extracted. All other entries must be manually entered. Also, reference species information will need to be added/changed in the script (lines 60-115) to account for additional reference species and to mark which reference species are associated with each adsorbate. If multiple reference species are used for a particular adsorbate, then the information for each reference species has to be provided in the associated if/elif statement.

# Running the script
To run the upload_VASP_CPD.py script, run a for loop over all subdirectories where the upload_VASP_CPD script is run in each subdirectory. An example for a bash shell workflow is provided below.

        cdir=$PWD #Set path to parent directory
        for name in */; do #For loop over all subdirectories  
            cd $name #change directory to subdirectory  
            upload_VASP_CPD.py #Run python script
            cd $cdir #change directory back to parent directory
        done #end for loop
    
Running this for loop will append a row of data for each subdirectory to the blank Database_empty_template.csv file. This populated Database_empty_template.csv file can then be uploaded to the CPD (see **NREL/cpd-batch-upload/cpdupload** folder).

</div>
