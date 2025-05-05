#20250504 convert osim model to mujoco
import os, sys
sys.path.append('F:/ncf/myoconverter')
from myoconverter.O2MPipeline import O2MPipeline
if __name__ == '__main__':
    # define pipeline configurations
    kwargs = {}  # define kwargs inputs
    kwargs['convert_steps'] = [1]    # All three steps selected
    kwargs['muscle_list'] = None           # No specific muscle selected, optimize all of them
    kwargs['osim_data_overwrite'] = True   # Overwrite the Osim model state files
    kwargs['conversion'] = True            # Yes, perform 'Cvt#' process
    kwargs['validation'] = True            # Yes, perform 'Vlt#' process
    kwargs['speedy'] = False               # Do not reduce the checking notes to increase speed
    kwargs['generate_pdf'] = True          # Do not generate validation pdf report
    kwargs['add_ground_geom'] = False       # Add ground to the model
    kwargs['treat_as_normal_path_point'] = False    # Using constraints to represent moving and conditional path points

    ############### Simple Arm 2 DoFs 6 Muscles ################ 
    osim_file = './models/osim/cotr/63_opt0504.osim'
    geometry_folder = './models/osim/cotr'
    output_folder = './models/mjc/cotr'
    O2MPipeline(osim_file, geometry_folder, output_folder, **kwargs)