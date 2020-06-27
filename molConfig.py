#*****File Gnerator Script Definitions****
fname     = "CuPc_MM_Packed"
mname     = "CuPc_Packed"
aname     = "C"
nFiles    = 16
difElems  = 4
#Effective Nuclear Charge of Elements in System
element1a = 6
element1b = 4
element2  = 7
element3  = 1
element4  = 29
element5  = 0
element6  = 0
#Number of each element present in system
nElem1    = 96
nElem2    = 24
nElem3    = 48
nElem4    = 3
nElem5    = 0
nElem6    = 0
#*****StoBe SPECIFIC PARAMETERS*****
#****The keywords have been organized according to the logical grouping defined in section 2.1.1 if the StoBe Manual****
#***The StoBe manual can be found here: http://www.fhi-berlin.mpg.de/KHsoftware/StoBe/StoBeMAN.html#2.1.1.1.
#Auxiliary Basis Set Input
elem1_Abasis_a = "A-CARBON (5,2;5,2)"
elem1_Abasis_b = "A-CARBON(+4) (3,3;3,3)"
elem2_Abasis   = "A-NITROGEN (4,3;4,3)"
elem3_Abasis   = "A-HYDROGEN (3,1;3,1)"
elem4_Abasis   = "A-COPPER (5,5;5,5)"
elem5_Abasis   = ""
elem6_Abasis   = ""
#Orbital Basis Set Input
elem1_Obasis_a = "O-CARBON iii_iglo"
elem1_Obasis_b = "O-CARBON(+4) (311/211/1)"
elem2_Obasis   = "O-NITROGEN (33/3)"
elem3_Obasis   = "O-HYDROGEN (311/1) misc"
elem4_Obasis   = "O-COPPER (63321/531/41)"
elem5_Obasis   = ""
elem6_Obasis   = ""
#Model Core Potential Input
elem1_MCPbasis = "P-CARBON(+4) (3,1:8,0)"
#Electron Configuration/Occupation Input
alpha        = 346
beta         = 343
alfaOcc      = '0 1 38 0.0'
betaOcc      = '0 0'
alfaOccTP    = '0 1 38 0.5'
#GEOMETRY BASICS KEYWORDS
sym          = None
geom         = None
#ELECTRONIC STATE KEYWORDS
multiplicity    = '4'
charge          = None
potential       = None
noFSsym         = None #Not implemented yet
fsymGND         = None
fsymEXC         = None
smear           = None #Not implemented yet
conf            = None #Not implemented yet
exci            = None #Not implemented yet
field           = None #Not implemented yet
spin            = None
reorder         = None #Not implemented yet
localize        = None #Not implemented yet
#SCF ITERATION KEYWORDS
runtype         = None
scftype         = None
maxcycles       = None
econvergence    = '5.5'
dconvergence    = '0.2'
dmixing         = None
diis            = None
levelshift      = None #Not implemented yet
maxoverlap      = None #Not implemented yet
integration     = None #Not implemented yet
grid            = None
wedge           = None #Not implemented yet
slater          = None #Not implemented yet
ptcharges       = None #Not implemented yet
bsserror        = None #Not implemented yet
supsym          = None #Not implemented yet
trrh            = None #Not implemented yet
#GEOMETRY OPTIMIZATION KEYWORDS
gconvergence    = None #Not implemented yet
gstepsize       = None #Not implemented yet
maxgeometries   = None #Not implemented yet
coordinate      = None #Not implemented yet
atom            = None #Not implemented yet
group           = None #Not implemented yet
hessian         = None #Not implemented yet
gradients       = None #Not implemented yet
strbalsac       = None #Not implemented yet
#PROPERTIES KEYWORDS
mulliken        = None
lowedin         = None #Not implemented yet
mepfit          = None #Not implemented yet
balpop          = None #Not implemented yet
draw            = None #Not implemented yet
pscratch        = None #Not implemented yet
xrayspec        = None #Not implemented yet
topological     = None #Not implemented yet
nmrout          = None #Not implemented yet
eprout          = None #Not implemented yet
vibrations      = None #Not implemented yet
nebparams       = None #Not implemented yet
resinput        = None #Not implemented yet
resoutput       = None #Not implemented yet
#MISCELLANEOUS KEYWORDS
title           = mname
printout        = None #Not implemented yet
save            = None #Not implemented yet
orbi            = None
ecpread         = None #Not implemented yet
pntgen          = None #Not implemented yet
alchem          = None #Not implemented yet
mofile          = None
virt            = None
ctrlopt         = None #Not implemented yet
dosout          = None #Not implemented yet
shortres        = None #Not implemented yet
forces          = None #Not implemented yet
dynamics        = None #Not implemented yet
geoformat       = None #Not implemented yet