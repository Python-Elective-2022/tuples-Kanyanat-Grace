'''
function main
    inputs the tuple
    prints the function skip_tuples with the tuple inputted

function skip_tuples
    returns every 2 skipped tuple
    
if name is 'main'
    main()
'''

def main():
    '''
    tuple is defined,
    returns the function skip_tuples with tuple
    '''
    tuple = 'I', 'am', 'a', 'test', 'tuple'
    print (skip_tuples(tuple))

def skip_tuples(tuple):
    '''
    inputs the tuple,
    skips every two tuple
    '''
    return tuple[::2]

if __name__ == "__main__":
    main()
