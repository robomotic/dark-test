import os
import sys
import getopt
import numpy as np
from dark_magic import FileParser

def check_if_file_exits(file):
    '''
        Checks if a file exists. Prints an error and exits if it does not exist.
    '''
    if not os.path.exists(file):
        print('File \'{}\' does not exist'.format(file))
        exit()


def parse_files(parser):
    # Check if the files exist.
    for f in [x_file, a_file, b_file, c_file]:
        check_if_file_exits(f)

    # Parse the files.
    try:
        signs = parser.parseXFile(x_file)
        A = parser.parseAFile(a_file)
        directions, bvals = parser.parseBFile(b_file)
        max_or_min, cvals = parser.parseCFile(c_file)
        return signs, A, directions, bvals, max_or_min, cvals
    except Exception as e:
        if verbose:
            # Verbose messages may include a reason why the file is malformed.
            exit_with_message(str(e))
        else:
            exit_with_message('Malformed input file. Exiting.')

def exit_with_message(msg, exitcode=0):
    ''' Prints a message and exits. '''
    print(msg)
    exit(exitcode)

if __name__ == '__main__':
    # Check and parse arguments
    if len(sys.argv) == 7 and sys.argv[6] == '--verbose':
        verbose = True

        # It's useful to have a greater linewidth for verbose printing.
        np.set_printoptions(linewidth=200)
        _, command, x_file, a_file, b_file, c_file, _ = sys.argv
    elif len(sys.argv) == 6:
        verbose = False
        _, command, x_file, a_file, b_file, c_file = sys.argv
    else:
        print('Incorrect Number of Arguments.')
        exit_with_message('Usage: ./runMyLPSolver <command> x_FILEPATH A_FILEPATH b_FILEPATH c_FILEPATH')

    # Parse Files
    parser = FileParser()
    var_signs, A, directions, bvals, max_or_min, cvals = parse_files(parser)