import sys
import os
import builtins
import DEVS.AtomicDEVS
import DEVS.CoupledDEVS
import Simulator


sys.path.append(os.path.join('..','DEVSKernel','PyDEVS'))
sys.path.append(os.path.join('..'))
builtins.__dict__['DEFAULT_DEVS_DIRNAME'] = 'PyDEVS'
builtins.__dict__['DEVS_DIR_PATH_DICT'] = {'PyDEVS':os.path.join(os.pardir,'DEVSKernel','PyDEVS'),'PyPDEVS':os.path.join(os.pardir,'DEVSKernel','PyPDEVS')}


class Diagram0(CoupledDEVS):
    def __init__ (self, name):
        CoupledDEVS.__init__(self, name)



################### Model Hierarchy #####################
# Model_Diagram0
#########################################################