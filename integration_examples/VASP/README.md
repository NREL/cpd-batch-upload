# Overview
<div style="text-align: justify">For a single metal surface/cluster, the Upload_VASP_CPD.py python script allows users to calculate binding energies directly from VASP output files and compile all of the data into a .csv that can be uploaded to the CPD.

# Required Subdirectory Structure
To use the Upload_VASP_CPD.py script, users must set up subdirectories for the adsorption calculations in a particular format. All calculations that the user seeks to upload to the CPD must be placed in the same parent directory, and each folder must be named in the format: <span style="color:blue">{Adsorbate}_{Site}</span>. In the example upload directories provided here, the four folders are named:

><span style="color:blue">co_fcc/ h_fcc/ naphthalene_bridge-top-bridge/ tetralin_bridge-bridge-bridge

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