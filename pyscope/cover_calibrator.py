from . import _import_driver

def CoverCalibrator(driver_name, ascom=True):
    '''Return a cover calibrator object.

    Parameters
    ----------
    driver_name : str
        Name of the cover calibrator driver to use.
    ascom : bool
        If True, use the ASCOM driver.

    Returns
    -------
    cover_calibrator : CoverCalibrator
        Cover calibrator object.
    '''

    return _import_driver(driver_name, 'CoverCalibrator', ascom=ascom)