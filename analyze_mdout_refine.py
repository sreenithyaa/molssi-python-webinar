import os
import sys
import argparse
import glob

def inp_file(fname):
    file_in = open(fname, 'r')
    file_in_lines = file_in.readlines()
    file_in.close()
    return file_in_lines

if __name__ == "__main__" :
    
    parser = argparse.ArgumentParser(description='This script analyses the mdout and returs number of steps and energy')
    parser.add_argument('fname', help='give input file path')
    args = parser.parse_args()
    
    filenames = glob.glob(args.filepath)
    
    for file in filenames:
        f=open(file, 'r')
        inp_name = os.path.basename(filename).split('.')[0]
        in_lines = inp_file(name)
        out_file = open(F'{inp_name}_Etot.txt', 'w+')
        for line in in_lines:
            if 'NSTEP' in line:
                step_line = line
                step_num = step_line.split()[2]
            if 'Etot' in line:
                energy_line = line
                energy = energy_line.split()[2]
                out_file.write(F'Nstep{step_num} : Etot{energy} \n')
        out_file.close()