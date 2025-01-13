#!/bin/bash -l        
#SBATCH --time=8:00:00
#SBATCH --ntasks=8
#SBATCH --mem=10g
#SBATCH --tmp=10g
#SBATCH --mail-type=BEGIN,END,FAIL  
#SBATCH --mail-user=reine097@umn.edu 
cd ~/program_directory
module load intel 
module load ompi/intel mpirun -np 8 program_name < inputfile > outputfile 