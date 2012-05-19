#!/usr/bin/env dumbo

import os

def mapper(key,value):
    """ Each record in the tempdata files is params, timestep, node, value. 
    
    We output: (node,timestep), (param,value)
    """
    data = value.split()
    p = int(data[0])
    t = int(data[1])
    n = int(data[2])
    val = float(data[3])
    yield (t,n), (p,val)

def reducer(key,values):
    """ Each key is a (node,timestep) pair.  Each value is (param,value) pair.
    
    We want to make an array of all the values over the parameters. """
    
    # TODO optimize this routine
    valarray = [val for val in values] # realize the 
    array = [0. for _ in xrange(len(valarray))]
    for val in valarray:
        pi = val[0]
        v = val[1]
        assert(pi >= 0)
        assert(pi < len(array))
        array[pi] = v
    
    yield key, array
    
def starter(prog):
    tempfiles = prog.delopt('tempfiles')
    if not tempfiles:
        return '-tempfiles not specified'
        
    prog.addopt('input',tempfiles)
    
    output = prog.getopt('output')
    if output is None:
        dirpath = os.path.split(tempfiles)
        prog.addopt('output',dirpath + '.mseq')
        
    prog.addopt('overwrite','yes')
    
    numreducers = prog.getopt('numreducetasks')
    if not numreducers:
        prog.addopt('numreducetasks','256')
        
        
def runner(job):
    job.additer(mapper, reducer)
    
if __name__ == '__main__':
    import dumbo
    dumbo.main(runner,starter)
        
        
    
