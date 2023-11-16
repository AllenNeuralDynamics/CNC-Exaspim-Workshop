#Functions for loading data

import pandas as pd
import json
import os
import glob

def load_annotation(mouse_id, neuron_id, complete=True):
    """Loads axon and dendrite annotations for a neuron
    Parameters
    ----------
    mouse_id : string 
        mouse id
    neuron_id: string
        neuron id
    complete: Boolean, default True
        indicates whether to use "Complete" or "Incomplete" annotations
    
    Returns
    -------
    axons : pandas DataFrame
        DataFrame of the axon annotations
    dendrites : pandas DataFrame
        DataFrame of the axon annotations
    """

    tracing_path = r'/data/neuron_tracings'
    if complete:
        dendrite_file = glob.glob(os.path.join(tracing_path,'*' + mouse_id + '*', 'Complete', neuron_id+'*', '*'+'dendrite'+'*'))[0]
        axon_file = glob.glob(os.path.join(tracing_path,'*' + mouse_id + '*', 'Complete', neuron_id+'*', '*'+'axon'+'*'))[0]
    else:
        dendrite_file = glob.glob(os.path.join(tracing_path,'*' + mouse_id + '*', 'Incomplete', neuron_id+'*', '*'+'dendrite'+'*'))[0]
        axon_file = glob.glob(os.path.join(tracing_path,'*' + mouse_id + '*', 'Incomplete', neuron_id+'*', '*'+'axon'+'*'))[0]
    axons = pd.read_table(axon_file, sep='\s', header=None, skiprows=[0,1,2], engine='python',
                          names=('sampleNumber', 'structureIdentifier', 'x', 'y', 'z', 'radius', 'parentNumber'))
    dendrites = pd.read_table(dendrite_file, sep='\s', header=None, skiprows=[0,1,2], engine='python', 
                              names=('sampleNumber', 'structureIdentifier', 'x', 'y', 'z', 'radius', 'parentNumber'))
    return(axons, dendrites)

def load_mouselight(neuron_id):
    """Loads axon and dendrite annotations for a neuron from the mouselight annotations
    Parameters
    ----------
    neuron_id: string
        neuron id
    
    Returns
    -------
    axons : pandas DataFrame
        DataFrame of the axon annotations
    dendrites : pandas DataFrame
        DataFrame of the axon annotations
    """
    
    tracing_path = r'/data/neuron_tracings/mouselight'
    file_path = os.path.join(tracing_path, neuron_id+'.json')
    with open(file_path) as json_data:
        d = json.load(json_data)
        json_data.close()
    axons = pd.DataFrame(d['neuron']['axon'])
    dendrites = pd.DataFrame(d['neuron']['dendrite'])
    return(axons, dendrites)