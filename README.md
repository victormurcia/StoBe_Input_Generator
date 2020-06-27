# StoBe_Input_Generator

This function is used to create and organize all of the input files necessary to carry out Density Functional Theory (DFT) calculations via the software platform StoBe with the goal of simulating Near Edge X-ray Absorption Fine Structure (NEXAFS) spectra.

The program was written using Python 3.7.7

The program generates the .run files necessary for a complete transition potential calculation of a molecule/cluster for each atom of interest. The generated files include the ground state calculation, the excited/ionized state calculation, the transition potential calculation, the XAS plotting utility, and the batch files used to sequentially run the calculations. 

The user must provide two files to the program: 
1) A file with a .xyz extension containing the atom labels and X,Y,Z coordinates for each atom. The atoms in this file MUST be sorted by ELEMENT TYPE, and the first set of atoms must correspond to atoms of the element that we are calculating the NEXAFS for. For example, if we wanted to calculate the Carbon-edge NEXAFS for Pyridine (C5H5N), then the .xyz file should start with 5 Carbon atoms, followed by either the Nitrogen atom or the 5 Hydrogen atoms. An example is provided in this repository.

2) A file titled molConfig.py that contains all of the desired input parameters for the current system (an example of the contents/structure of this file for pyridine can be found in this repository). Detailed descriptions of the input keywords can be found in the StoBe Manual website: http://www.fhi-berlin.mpg.de/KHsoftware/StoBe/StoBeMAN.html

To run the program, place the .xyz file and molConfig.py file in the same directory as the StoBe_Input_Generator_v3.py file and then run the program through a terminal.
