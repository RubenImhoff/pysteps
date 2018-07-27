
from . import conversion
from . import transformation
from . import dimension

def get_method(name):
    """Return a callable function for the bandpass filter or decomposition method 
    corresponding to the given name.\n\
    
    Conversion methods:
    +-------------------+--------------------------------------------------------+
    |     Name          |              Description                               |
    +===================+========================================================+
    | mm/h or rainrate  | convert to rain rate [mm/h]                            |
    +-------------------+--------------------------------------------------------+
    | mm or raindepth   | convert to rain depth [mm]                             |
    +-------------------+--------------------------------------------------------+
    | dBZ or reflectivity  | convert to reflectivity [dBZ]                       |
    +-------------------+--------------------------------------------------------+
    
    Transformation methods:
    +-------------------+--------------------------------------------------------+
    |     Name          |              Description                               |
    +===================+========================================================+
    |  dB, decibel      | transform to units of decibel                          |
    +-------------------+--------------------------------------------------------+
    |  BoxCox           | apply one-parameter Box-Cox transform                  |
    +-------------------+--------------------------------------------------------+
    
    Dimension methods:
    +-------------------+--------------------------------------------------------+
    |     Name          |              Description                               |
    +===================+========================================================+
    |  aggregate        | aggregate fields in time                               |
    +-------------------+--------------------------------------------------------+
    |  square           | either pad or crop the data to get a square domain     |
    +-------------------+--------------------------------------------------------+
    """
    if name is None:
        def donothing(R, metadata, *args, **kwargs):
            return R.copy(), metadata.copy()
        return donothing
    elif name.lower() == "mm/h" or name.lower() == "rainrate":
        return conversion.to_rainrate
    elif name.lower() == "mm" or name.lower() == "raindepth":
        return conversion.to_raindepth
    elif name.lower() == "dbz" or name.lower() == "reflectivity":
        return conversion.to_reflectivity
    elif name.lower() == "db" or name.lower() == "decibel":
        return transformation.dB_transform
    elif name.lower() == "boxcox":
        return transformation.boxcox_transform
    elif name.lower() == "aggregate":
        return dimension.aggregate_fields_time
    elif name.lower() == "square":
        return dimension.square_domain
    else:
        raise ValueError("unknown method %s" % name)