#!/bin/bash -l        
#SBATCH --time=8:00:00
#SBATCH --ntasks=8
#SBATCH --mem=10g
#SBATCH --tmp=10g
#SBATCH --mail-type=BEGIN,END,FAIL  
#SBATCH --mail-user=reine097@umn.edu 
cd /users/9/reine097/projects/graph-theory/
/usr/bin/env /users/9/reine097/projects/graph-theory/.venv/bin/python /users/9/reine097/.vscode/extensions/ms-python.debugpy-2024.14.0-linux-x64/bundled/libs/debugpy/adapter/../../debugpy/launcher 48509 -- /users/9/reine097/projects/graph-theory/genetic_algorithm.py
