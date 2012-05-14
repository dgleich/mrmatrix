#!/usr/bin/env dumbo

def mapper(key,value): 
    """ Each record is a line of text. 
    key=<byte that the line starts in the file>
    value=<line of text>
    """
    valarray = [float(v) for v in value.split()]
    yield key, sum(valarray)

if __name__=='__main__':
    import dumbo
    import dumbo.lib
    dumbo.run(mapper,dumbo.lib.identityreducer)
