import sys
import input_parser
from emitter import Emitter
from receiver import Receiver
from mirror import Mirror
from laser_circuit import LaserCircuit
from board_displayer import BoardDisplayer

'''
run - Runs the entire program. It needs to take in the inputs and process them
into setting up the circuit. The user can specify optional flags to perform
additional steps, such as -RUN-MY-CIRCUIT to run the circuit and -ADD-MY-MIRRORS
to include mirrors in the circuit.

You are free to add more functions, as long as you aren't modifying the
existing scaffold.
'''


def is_run_my_circuit_enabled(args: list[str]) -> bool:
    # only requires implementation once you reach RUN-MY-CIRCUIT
    '''
    Returns whether or not '-RUN-MY-CIRCUIT' is in args.
    
    Parameters
    ----------
    args - the command line arguments of the program
    '''
    i = 0
    while i < len(args):
        if args[i] == '-RUN-MY-CIRCUIT':
            return True  
        i += 1
    return False


def is_add_my_mirrors_enabled(args: list[str]) -> bool:
    # only requires implementation once you reach ADD-MY-MIRRORS
    '''
    Returns whether or not '-ADD-MY-MIRRORS' is in args.
    
    Parameters
    ----------
    args - the command line arguments of the program
    '''
    i = 0
    while i < len(args):
        if args[i] == '-ADD-MY-MIRRORS':
            return True  
        i += 1
    return False



def initialise_circuit() -> LaserCircuit:
    # only requires implementation once you reach GET-MY-INPUTS
    '''
    Gets the inputs for the board size, emitters and receivers and processes
    it to create a LaserCircuit instance and return it. You should be using
    the functions you have implemented in the input_parser module to handle
    validating each input.

    Returns
    -------
    A LaserCircuit instance with a width and height specified by the user's
    inputted size. The circuit should also include each emitter and receiver
    the user has inputted.
    '''
    print('Creating circuit board...')
    while True:
        board_size = input('> ')
        size = input_parser.parse_size(board_size)
        if size is not None:
            width, height = size
            print(f'{width}x{height} board created.')
            break
    
    circuit = LaserCircuit(width, height)

    print('\nAdding emitter(s)...')

    count_emitters = 0
    while count_emitters < 10:
        emitters = input('> ')
        if emitters == 'END EMITTERS':
            break
        emitter = input_parser.parse_emitter(emitters)
        if emitter is None:
            continue
        if emitter and circuit.add_emitter(emitter):
            count_emitters += 1
 
    print(f'{count_emitters} emitter(s) added.')

    print('\nAdding receiver(s)...')
 
    count_receivers = 0
    while count_receivers < 10:
        receivers = input('> ')
        if receivers == 'END RECEIVERS':
            break
        receiver = input_parser.parse_receiver(receivers)
        if receiver and circuit.add_receiver(receiver):
            count_receivers += 1

    print(f'{count_receivers} receiver(s) added.\n')
    return circuit


def set_pulse_sequence(circuit: LaserCircuit, file_obj) -> None:
    # only requires implementation once you reach RUN-MY-CIRCUIT
    '''
    Handles setting the pulse sequence of the circuit. 
    The lines for the pulse sequence will come from the a file named
    /home/input/<file_name>.in. 
    You should be using the functions you have implemented in the input_parser module 
    to handle validating lines from the file.

    Parameter
    ---------
    circuit - The circuit to set the pulse sequence for.
    file_obj - A file like object returned by the open()
    '''
    print('\nSetting pulse sequence...')

    def print_remaining_emitters():
        remaining_emitters = ''
        i = 0
        while i < len(circuit.emitters):
            if not circuit.emitters[i].pulse_sequence_set:
                remaining_emitters += circuit.emitters[i].symbol + ', '
            i += 1
        if remaining_emitters.strip():
            print(f"-- ({remaining_emitters.strip(', ')})")

    print_remaining_emitters()

    line_number = 1
    line = file_obj.readline()
    while line:
        line = line.strip()
        result = input_parser.parse_pulse_sequence(line)
        if result is None:
            line_number += 1
            line = file_obj.readline()
            continue

        symbol, frequency, direction = result

        emitter_found = False
        already_set = False
        i = 0
        while i < len(circuit.emitters):
            if circuit.emitters[i].symbol == symbol:
                emitter_found = True
                if circuit.emitters[i].pulse_sequence_set:
                    already_set = True
                else:
                    circuit.emitters[i].set_pulse_sequence(frequency, direction)
                    circuit.emitters[i].pulse_sequence_set = True
                break
            i += 1

        print(f'Line {line_number}: {symbol} {frequency} {direction}')
        if not emitter_found:
            print(f'Error: emitter \'{symbol}\' does not exist')
        elif already_set:
            print(f'Error: Emitter \'{symbol}\' already has its pulse sequence set')
        
        print_remaining_emitters()

        line_number += 1
        line = file_obj.readline()
    print('Pulse sequence set.\n')


def add_mirrors(circuit: LaserCircuit) -> None:
    # only requires implementation once you reach ADD-MY-MIRRORS
    '''
    Handles adding the mirrors into the circuit. You should be using the
    functions you have implemented in the input_parser module to handle
    validating each input. 
    
    Parameters
    ----------
    circuit - the laser circuit to add the mirrors into
    '''
    print("Adding mirror(s)...")
    count_mirrors = 0

    while True:
        mirrors = input("> ")
        if mirrors == "END MIRRORS":
            break

        mirror = input_parser.parse_mirror(mirrors)
        if (mirror is not None) and circuit.add_mirror(mirror):
            count_mirrors += 1
        else:
            continue
    
    print(f"{count_mirrors} mirror(s) added.")
    


def main(args: list[str]) -> None:
    # only requires implementation once you reach GET-MY-INPUTS
    # will require extensions in RUN-MY-CIRCUIT and ADD-MY-MIRRORS
    '''
    Responsible for running all code related to the program.

    Parameters
    ----------
    args - the command line arguments of the program
    '''
    circuit = initialise_circuit()
    if is_add_my_mirrors_enabled(args):
        print('<ADD-MY-MIRRORS FLAG DETECTED!>\n')
        add_mirrors(circuit)
        print('')
        circuit.print_board()
        print('')
    else:
        circuit.print_board()
        print('')



    if is_run_my_circuit_enabled(args):
        print('<RUN-MY-CIRCUIT FLAG DETECTED!>')
        try:
            with open('/home/input/pulse_sequence.in', 'r') as file:
                set_pulse_sequence(circuit, file)
                circuit.run_circuit()
        except FileNotFoundError:
            print('\nError: -RUN-MY-CIRCUIT flag detected but /home/input/pulse_sequence.in does not exist')
            return

        

if __name__ == '__main__':
    '''
    Entry point of program. We pass the command line arguments to our main
    program. We do not recommend modifying this.
    '''
    main(sys.argv)
