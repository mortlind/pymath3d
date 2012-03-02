"""
Utility function and definitions library for PyMath3D.
"""

__author__ = "Morten Lind"
__copyright__ = "Morten Lind 2009-2012"
__credits__ = ["Morten Lind"]
__license__ = "GPL"
__maintainer__ = "Morten Lind"
__email__ = "morten@lind.no-ip.org"
__status__ = "Production"

import numpy as np

## Possibly replace by 1000*np.finfo(float).resolution
_eps = np.finfo(np.float64).eps

## Tuple of types considered sequences 
_seqTypes = (list, tuple, np.ndarray)

def isSequence(s):
    return type(s) in _seqTypes

def isThreeSequence(s):
    return type(s) in _seqTypes and len(s) == 3

## Standard numeric types
_numTypes = [float, int]
## Get numeric types from numpy
for i in np.typeDict:
    if type(i) == type('') and (i.find('int') >= 0 or i.find('float') >= 0):
        _numTypes.append(np.typeDict[i])
        
def isNumType(val):
    return type(val) in _numTypes

def isNumTypes(lst):
    for li in lst:
        if type(li) not in _numTypes:
            return False
    return True