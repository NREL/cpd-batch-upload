#!/bin/bash 

#SBATCH --nodes=1                   # Number of nodes
#SBATCH --ntasks-per-node=36        # This is a number we should do some benchmarking for
#SBATCH --time=48:00:00            
#SBATCH --account=ccpc             # Allocation, use ccpc or electrochem

module purge
module load mkl/2020.1.217
module load intel-mpi
module load vasp/5.4.4_centos77
vasp='vasp_std'              # use ‘vasp_gam’ for gamma point calculations

date > a
srun $vasp>out
date > b
