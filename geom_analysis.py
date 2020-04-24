"""
This module has functions associated with analyzing the geometry of a molecule.

It can be run as a script with an xyz file.
"""

import os
import argparse
import numpy

    
def open_xyz(xyz_filename):
    """
    This function opens xyz file, separates the coordinates and the symbols and recasts the coordinates as floats.
    """
    xyz_filename = numpy.genfromtxt(fname=xyz_filename, skip_header=2, dtype='unicode')
    symbols = xyz_filename[:,0]
    coordinates = xyz_filename[:,1:]
    coordinates = coordinates.astype(numpy.float)
    return symbols, coordinates

def calculate_distance(atom1_coord, atom2_coord):
    """
    Calculates the distances between two points in 3D spcae.
    Inputs: Coordinates of two atoms
    Return: distance between the atoms
    """
    x_distance = atom1_coord[0] - atom2_coord[0]
    y_distance = atom1_coord[1] - atom2_coord[1]
    z_distance = atom1_coord[2] - atom2_coord[2]
    atom_distance = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return atom_distance

def bond_check(distance, minimum_length =0, maximum_length=1.5):
    """
    This function checks the atom distance and assigns as a bond if it falls within the minimum_length 
    and maximum_length 
    """
    if distance > minimum_length and distance <= maximum_length:
        return True
    else:
        return False

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='The script analyses a user given xyz file and outputs the length of the bond')
    parser.add_argument('xyz_file', help="The file path for xyz file")
    args = parser.parse_args()                                

    xyzfilename = args.xyz_file                                 
    symbols, coords = open_xyz(xyzfilename)
    num_atoms = len(symbols)
    for num1 in range(0,num_atoms):
        for num2 in range(0,num_atoms):
            if num1<num2:
                atom_distance = calculate_distance(coords[num1], coords[num2])
                if bond_check(atom_distance) is True:
                    print(F'{symbols[num1]} to {symbols[num2]} : {atom_distance: .3f}')