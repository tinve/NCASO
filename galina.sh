#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -pe orte 1
#cd $SGE_O_WORKER
python Monte_Carlo.py