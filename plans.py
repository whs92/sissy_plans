"""
A collection of plans intended to be called from a GUI at SISSY

Configuration of devices is seperated from the plans which do stuff

It is assumed that the following is set as metadata in the environment and attached to all plans:

sample information: Can be read from sissy1 database or entered manually

User info

Investigation info

"""

def config_kth(kth, rnge, int_time):

    """
    Configure the range or integration time of a particular keithely

    kth : Keithly Device
        The keithley to configure
    rnge : enum
        The range to set it to
    int_time : float
        The integration time

    """
    
def config_chan(chan, int_time, hv):

    """
    Configure the integration time or hv of a particular channeltron

    chan : Channeltron Device
        The Channeltron to configure
    hv : int
        The hv to set the device to
    int_time : float
        The integration time

    """


    
def config_mca(mca,int_time=None,roi_display_list=None):

    """
    Configure the integration time and roi display of a particular mca device

    mca : MCA Device
        The MCA to configure
    int_time : float
        The integration time
    roi_display : list
        A list of the rois to display
        All others will be hidden in plots

    ___________

    RE(config_mca(bruker.mca, 0.1, [0,2,3]))

    """


def config_pgm(pgm, slit_width, harmonic, order, grating, id_on):
    
    """
    Configure the a particular pgm

    pgm : PGM Device
        The PGM to configure
    slit_width : float
        The slit width in um
    harmonic : enum
        The harmonic to use
    order : int
        The order to use
    grating : enum
        The grating to use (400 l/mm or 800 l/mm)
    id_on : bool   
        Control the monochromator and undulator together

    ___________

    """
    
def config_dcm(dcm, crystal, harmonic, order, id_on):

    """
    Configure the a particular dcm

    dcm : DCM Device
        The DCM to configure
    crystal : enum
        The crystal to use
    harmonic : enum
        The harmonic to use
    order : int
        The order to use
    id_on : bool   
        Control the monochromator and undulator together

    ___________

    """
def prep_u17_dcm_s1():

    """
    Move the u17 dcm in, the pgm out
    Move m2 out
    Move m3 SMU to SISSY
    move m4 SMU to SISSY1
    """

def prep_u17_dcm_s2():
    
    """
    Move the u17 dcm in, the pgm out
    Move m2 out
    Move m3 SMU to SISSY
    move m4 SMU to SISSY2
    """

def prep_u17_pgm_s1():
    
    """
    Move the u17 pgm in, the dcm out
    Move m2 out
    Move m3 SMU to SISSY
    move m4 SMU to SISSY1
    """

def prep_u17_pgm_s2():
    
    """
    Move the u17 pgm in, the dcm out
    Move m2 out
    Move m3 SMU to SISSY
    move m4 SMU to SISSY2
    """
    
def prep_ue48_pgm_s1():
    
    """
    Move m3 SMU to SISSY
    move m4 SMU to SISSY1
    """

def prep_ue48_pgm_s2():
    
    """
    Move m3 SMU to SISSY
    move m4 SMU to SISSY1
    """
    
def dcm_change_fixed_energy(energy):

    """
    Change the dcm to a new fixed energy

    energy : float
        The energy to move to

    scan the u17 undulator and the dcm 2nd crystal pitch 
    to maximise intensity
    """
    
def dcm_change_range_energy(energy_start, energy_stop):

    """
    Commission the U17 DCM for an XAS measurement between two energies

    scan the u17 undulator and the dcm 2nd crystal pitch 
    to maximise intensity

    energy_start : float
        The start of the energy region
    energy_stop : float
        The end of the energy region
    """

def s1_xas(detectors, monochromator, start, stop, step, md=None):

    """
    A plan which moves a monochromator between start and stop energies
    with step_size step. The monochromator is moved in a stepwise fashion
    
    The plan will use the following i0 detectors:
        * bessy2 ring_current
        * m4 mirror current (dependent on monochromator chosen)

    The plan will read from the prevac sample database to determine
    information about the sample in the chamber

    detectors: list
        List of 'readable' objects from [s1_chan, s1_tfy, s1_tey, s1_pfy]
    monochromator: obj of class Mono
        The monochromator that will be scanned, either ue48_pgm.en, u17_pgm.en, u17_dcm.en
    start: float
        The first energy in the range
    stop: float
        The last energy in the range
    step: float
        The energy step size
    md:

    _____________
    Example
    
    RE(s1_xas([s1_chan, s1_tfy, s1_tey, s1_pfy], u17_dcm.en, 7900,8000,1), reason="demo of hard xas at sissy1")
            
    """

def s2_xas(detectors, monochromator, start, stop, step, shutter=False ):
    
    """
    A plan which moves a monochromator between start and stop energies
    with step_size step. The monochromator is moved in a stepwise fashion
    
    The plan will use the following i0 detectors:
        * bessy2 ring_current
        * m4 mirror current (dependent on monochromator chosen)
        * s2_mesh

    detectors: list
        List of 'readable' objects from [s2_chan, s2_tfy, s2_pfy]
    monochromator: obj of class Mono
        The monochromator that will be scanned, either ue48_pgm.en, u17_pgm.en, u17_dcm.en
    start: float
        The first energy in the range
    stop: float
        The last energy in the range
    step: float
        The energy step size
    shutter: bool, default = False
        if asserted then a shutter will be open and closed around each reading
  
    _____________
    Example
    
    RE(s2_xas([s2_chan, s2_tfy,s2_pfy], u17_dcm.en, 7900,8000,1), reason="demo of hard xas at sissy2")
            
    """

def s1_xas_fly(detectors, monochromator, start, stop, vel, md=None):
    
    """
    A plan which moves a monochromator between start and stop energies
    with velocity vel. 
    
    The monochromator is moved continuously

    The detectors are sampled as quickly as the slowest detector in the list
    
    The plan will use the following i0 detectors:
        * bessy2 ring_current
        * m4 mirror current (dependent on monochromator chosen)

    The plan will read from the prevac sample database to determine
    information about the sample in the chamber

    ----------------

    detectors: list
        List of 'readable' objects from [s1_chan, s1_tfy, s1_tey, s1_pfy]
    monochromator: obj of class Mono
        The monochromator that will be scanned, either ue48_pgm.en, u17_pgm.en
    start: float
        The first energy in the range
    stop: float
        The last energy in the range
    vel: float
        The velocity to drive the monochromator at
   
    __________
    Example
    
    RE(config_mca(s1_mca,int_time=0.1))
    RE(config_kth(s1_tfy,int_time=0.1, rnge="20 nA"))
    RE(s1_xas([s1_chan, s1_tfy, s1_tey, s1_pfy], ue48_pgm.en, 790,800,0.1), reason="demo of soft flyscan xas at sissy1")
            
    """

def s2_xas_fly(detectors, monochromator, start, stop, vel):

    """
    A plan which moves a monochromator between start and stop energies
    with velocity vel. 
    
    The monochromator is moved continuously

    The detectors are sampled as quickly as the slowest detector in the list
    
    The plan will use the following i0 detectors:
        * bessy2 ring_current
        * m4 mirror current (dependent on monochromator chosen)
        * s2_mesh

    detectors: list
        List of 'readable' objects from [s2_chan, s2_tfy, s2_pfy]
    monochromator: obj of class Mono
        The monochromator that will be scanned, either ue48_pgm.en, u17_pgm.en
    start: float
        The first energy in the range
    stop: float
        The last energy in the range
    vel: float
        The rate of change of energy

    _____________
    Example
    
    RE(s2_xas_fly([s2_chan, s2_tfy,s2_pfy], ue48_pgm.en, 790,800,0.1), reason="demo of soft flyscan xas at sissy2")
            
    """

def xas(detectors, end_station, mono, slit_width, harmonic, order, mode, start, stop,  step, vel, shutter, md=None):

    """
    A different style of plan which tries to put everthing together

    The users wants to perform xas at at a particular end station

    detectors: list
        List of 'readable' objects dependent on end station and mono
    end_station : enum (S1, S2)
        The end station to use
    mono: obj of class Mono
        The monochromator that will be scanned, u17_dcm.en, u17_pgm.en or ue48_pgm.en
    slit_width : float
        The slit width to set if a pgm is selected
    harmonic : enum
        The harmonic to use
    order : int
        The order to use
    mode : enum (continuous, step)
        The measurement mode to use. Depends on the pgm selected
    start: float
        The first energy in the range
    stop: float
        The last energy in the range
    step : float
        The step size to use if mode = step
    vel: float
        The rate of change of energy to use if mode = continuous
    shutter: bool
        if the end station is s2 and the mode is step, then allow to use a shutter
    """

def s2_fexrav(detectors, md=None):

    """
    The biologic detector at s2 is triggered (it's waiting with a TI technique)

    The detectors in the list are triggered and read as quickly as possible

    This continues until the biologic issues a trigger (TO)

    All of the parameters from the biologic plans are also read and available in 
    different streams. The data from the detectors list and biologic will use the same
    timestamp source so you can collate the data

    The plan will use the following i0 detectors:
        * bessy2 ring_current
        * m4 mirror current (dependent on monochromator chosen)
        * s2_mesh

    detectors: list
        List of 'readable' objects from [s2_chan, s2_tfy, s2_pfy]
   
    _____________
    Example
    
    RE(s2_fexrav([s2_chan, s2_tfy,s2_pfy]), reason="demo of fexrav at sissy2")

    """

def s2_gridscan(detectors, motor1=es_man.x, start1, stop1, step1, motor2=es_man.z, start2, stop2, step2,snake=False, md=None):

    """
    Scan over a mesh; each motor is on an independent trajectory

    At each position trigger and read from all detectors

    Optionally snake motors which might be quicker but will introduce backlash problems

    The plan will use the following i0 detectors:
        * bessy2 ring_current
        * m4 mirror current (dependent on light incident on end station)

    detectors: list
        List of 'readable' objects from [s1_chan, s1_tfy, s1_pfy, s1_ana_counts]
    motor1 : A setable device, default=es_man.x
        The first axis
    start1 : float
        The first position of axis 1
    stop1 : float 
        The final position of axis 1
    step1 : float
        The step size of axis 1
    motor2 : A setable device, default=es_man.z
        The second axis axis
    start2 : float
        The first position of axis 2
    stop2 : float 
        The final position of axis 2
    step2 : float
        The step size of axis 2
    snake : Bool
        which axes should be snaked
    

    ___________
    Example
    
    RE(s1_gridscan([s2_chan, s2_tfy,s2_pfy]),oaese.x,-100,100,1,oaese.z,-100,100,1,snake=False), reason="demo of fexrav at sissy2")

    """

def s2_gridscan(detectors, motor1=oaese.x, start1, stop1, step1, motor2=oaese.z, start2, stop2, step2,snake=False,shutter=False, md=None):

    """
    Scan over a mesh; each motor is on an independent trajectory

    At each position trigger and read from all detectors

    Optionally snake motors which might be quicker but will introduce backlash problems

    The plan will use the following i0 detectors:
        * bessy2 ring_current
        * m4 mirror current (dependent on light incident on end station)
        * s2_mesh

    detectors: list
        List of 'readable' objects from [s2_chan, s2_tfy, s2_pfy]
    motor1 : A setable device, default=oaese.x
        The first axis
    start1 : float
        The first position of axis 1
    stop1 : float 
        The final position of axis 1
    step1 : float
        The step size of axis 1
    motor2 : A setable device
        The second axis axis
    start2 : float
        The first position of axis 2
    stop2 : float 
        The final position of axis 2
    step2 : float
        The step size of axis 2
    snake : Bool
        which axes should be snaked
    shutter: bool, default = False
        if asserted then a shutter will be open and closed around each reading

    ___________
    Example
    
    RE(s2_gridscan([s2_chan, s2_tfy,s2_pfy]),oaese.x,-100,100,1,oaese.z,-100,100,1,snake=False, shutter=True), reason="demo of fexrav at sissy2")

    """
    
def s2_fly_gridscan(detectors, motor1, start1, stop1, vel1, motor2, start2, stop2, step2, md=None):

    """
    Scan over a mesh; each motor is on an independent trajectory

    motor1 will be moved continuously with velocity vel1 between the start and stop points
    There will be  short ramp up and ramp down period between the points

    Between points motor1 will move at it's normal velocity

    Optionally snake motors which might be quicker but will introduce backlash problems

    While motor1 is moving the detectors will be read out as quickly as possible.

    The plan will use the following i0 detectors:
        * bessy2 ring_current
        * m4 mirror current (dependent on light incident on end station)
        * s2_mesh

    you will end up with a collection of unevenly spaced points that will require interpolation 
    onto a regular grid or plotting as a scatter

    detectors: list
        List of 'readable' objects from [s2_chan, s2_tfy, s2_pfy]
    motor1 : A setable device, default=oaese.x
        The first axis
    start1 : float
        The first position of axis 1
    stop1 : float 
        The final position of axis 1
    vel1 : float
        egu/s to move the motor in
    motor2 : A setable device
        The second axis axis
    start2 : float
        The first position of axis 2
    stop2 : float 
        The final position of axis 2
    step2 : float
        The step size of axis 2
    snake : Bool
        which axes should be snaked
    
    ___________
    Example
    
    RE(s2_fly_gridscan([s2_chan, s2_tfy,s2_pfy]),oaese.x,-100,100,1,oaese.z,-100,100,1,snake=False), reason="demo of flying gridscan at sissy2")

    """

def scan(detectors, motor, start, stop, step, md=None):

    """
    A 1D scan of a motor between start and stop with step size step

    detectors: list
        List of 'readable' objects
    motor1 : A setable device
        The  axis
    start : float
        The first position 
    stop : float 
        The final position
    step : float
        The step size

    """

def xps(pass_energy, start_energy, stop_energy, step_size, steps,repeats, region_name, md=None):

    """
    Perform a single XPS measurement in swept mode at sissy1.

    If the monochromator needs to be configured or the energy changed that should be done
    with other plans

    pass_energy: float
        The pass energy to set the the analyser to
    start_energy: float
        The start energy of the sweep
    stop_energy: float
        The stop energy of the sweep
    step_size: float
        The step that the window will be swept across
    steps: int
        The number of steps in each sweep
    repeats: int
        The number of repeats of the sweep to perform

    """

