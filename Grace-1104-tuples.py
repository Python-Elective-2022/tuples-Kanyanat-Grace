'''
function skip_tuples
    returns every 2 skipped tuple

function main
    inputs the tuple
    prints the function skip_tuples with the tuple inputted

print main()
'''

def skip_tuples(tuple):
    '''
    inputs the tuple,
    skips every two tuple
    '''
    return tuple[::2]

def main():
    '''
    tuple is defined,
    returns the function skip_tuples with tuple
    '''
    tuple = 'I', 'am', 'a', 'test', 'tuple'
    return (skip_tuples(tuple))

print(main())