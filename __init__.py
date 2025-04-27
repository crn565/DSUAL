# Import functions for converting various datasets to NILMTK format
# Converters for well-known datasets
from .redd.convert_redd import convert_redd    # Convert the REDD dataset
from .dred.convert_dred import convert_dred    # Convert the DRED dataset
from .ukdale.convert_ukdale import convert_ukdale  # Convert the UK-DALE dataset
from .ampds.convert_ampds import convert_ampds  # Convert the AMPds dataset
from .combed.convert_combed import convert_combed  # Convert the COMBED dataset
from .eco.convert_eco import convert_eco    # Convert the ECO dataset
from .greend.convert_greend import convert_greend  # Convert the GREEND dataset
from .hes.convert_hes import convert_hes    # Convert the HES dataset
from .refit.convert_refit import convert_refit  # Convert the REFIT dataset
from .iawe.convert_iawe import convert_iawe  # Convert the iAWE dataset
from .smart.convert_smart import convert_smart  # Convert the SMART dataset
from .caxe.convert_caxe import convert_caxe  # Convert the CAXE dataset
from .ideal.convert_ideal import convert_ideal # Convert the IDEAL dataset
# New dataset converters
from .ualm5.convert_ualm import convert_ualm # Convert DSUALM dataset
from .ualm5t.convert_ualmt import convert_ualmt # Convert DSUALMH dataset (harmonics support)
from .ualm10.convert_ualm10 import convert_ualm10 # Convert DSUALM10 dataset
from .ualmt10H.convert_ualmt10H import convert_ualmt10H # Convert DSUALM10H dataset (harmonics support)
from ompm.convert_ualm2 import convert_ualm2 # Convert UALM2 dataset
from ompm.convert_ualm22 import convert_ualm22 # Convert UALM3 dataset (only aggregated)
