#!/usr/bin/env dumbo

def mapper(key,value): 
    """ Each record is a line of text. """
    valarray = [float(v) for v in value.split()]
    for col,val in enumerate(valarray):
        yield col, val

def reducer(key,values):
    yield key, sum(values)
   
if __name__=='__main__':
    import dumbo
    import dumbo.lib
    dumbo.run(mapper,reducer)

