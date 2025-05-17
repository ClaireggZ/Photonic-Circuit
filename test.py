from laser_circuit import LaserCircuit
from circuit_for_testing import get_my_lasercircuit
from run import set_pulse_sequence

'''
This test program checks if the set_pulse_sequence function is implemented
correctly.

You can modify this scaffold as needed (changing function names, parameters, 
or implementations...), however, DO NOT ALTER the code in circuit_for_testing 
file, which provides the circuit. The circuit can be retrieved by calling 
get_my_lasercircuit(), and it should be used as an argument for the 
set_pulse_sequence function when testing.

Make sure to create at least six functions for testing: two for positive cases,
two for negative cases, and two for edge cases. Each function should take
different input files.

NOTE: Whenever we use ... in the code, this is a placeholder for you to
replace it with relevant code.
'''


def positive_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    '''
    Positive test case to verify the set_pulse_sequence function.

    Paramaters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)
    
    A_correct = (
        my_circuit.emitters[0].pulse_sequence_set == True and
        my_circuit.emitters[0].frequency == 25 and
        my_circuit.emitters[0].direction == 'N'
    )
    assert A_correct, "Emitter A is not correctly set"

    B_correct = (
        my_circuit.emitters[1].pulse_sequence_set == True and
        my_circuit.emitters[1].direction == 'N' and
        my_circuit.emitters[1].frequency == 30
    )
    assert B_correct, "Emitter B is not correctly set"

    C_correct = (
        my_circuit.emitters[2].pulse_sequence_set == True and
        my_circuit.emitters[2].direction == 'N' and
        my_circuit.emitters[2].frequency == 80
    )
    assert C_correct, "Emitter C is not correctly set"

    print("All emitters are correctly set.")

    file_obj.close()


def positive_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    '''
    Positive test case to verify the set_pulse_sequence function.

    Paramaters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)
    
    A_correct = (
        my_circuit.emitters[0].pulse_sequence_set == True and
        my_circuit.emitters[0].frequency == 250 and
        my_circuit.emitters[0].direction == 'E'
    )
    assert A_correct, "Emitter A is not correctly set"

    B_correct = (
        my_circuit.emitters[1].pulse_sequence_set == True and
        my_circuit.emitters[1].direction == 'S' and
        my_circuit.emitters[1].frequency == 300
    )
    assert B_correct, "Emitter B is not correctly set"

    C_correct = (
        my_circuit.emitters[2].pulse_sequence_set == True and
        my_circuit.emitters[2].direction == 'N' and
        my_circuit.emitters[2].frequency == 800
    )
    assert C_correct, "Emitter C is not correctly set"

    print("All emitters are correctly set.")

    file_obj.close()


def negative_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    '''
    Negative test case to verify the set_pulse_sequence function.

    Paramaters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)

    set_pulse_sequence(my_circuit, file_obj)

    assert my_circuit.emitters[0].pulse_sequence_set == True, "Emitter X is not in the circuit emitters"
    print("All emitters are correctly set.")

    file_obj.close()


def negative_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    '''
    Negative test case to verify the set_pulse_sequence function.

    Paramaters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)

    set_pulse_sequence(my_circuit, file_obj)
    
    assert my_circuit.emitters[0].pulse_sequence_set == True, \
    "The pulse sequence can't be set when the file is empty"
    
    print("All emitters are correctly set.")

    file_obj.close()


def negative_test_3(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    '''
    Negative test case to verify the set_pulse_sequence function.

    Paramaters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)
    
    assert not my_circuit.emitters[0].pulse_sequence_set == True, \
    "The pulse sequence is correctly set even though it has too many lines in the file."
    print("The pulse sequence is not correctly set.")

    file_obj.close()


def negative_test_4(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    '''
    Negative test case to verify the set_pulse_sequence function.

    Paramaters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)
    
    assert not my_circuit.emitters[0].pulse_sequence_set == True, \
    "The pulse sequence is correctly set even though it has insufficient lines in the file."
    print("The pulse sequence is not correctly set.")

    file_obj.close()



def edge_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    '''
    Edge test case to verify the set_pulse_sequence function.

    Paramaters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)

    set_pulse_sequence(my_circuit, file_obj)

    assert my_circuit.emitters[0].pulse_sequence_set == True, "The frequency can't be too large"

    print("The emitter's pulse sequence was correctly set.")

    file_obj.close()


def edge_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    '''
    Edge test case to verify the set_pulse_sequence function.

    Paramaters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)

    set_pulse_sequence(my_circuit, file_obj)

    assert my_circuit.emitters[0].pulse_sequence_set == True, "The frequency can't be 0"
    
    print("The first emitter's pulse sequence was correctly set.")

    file_obj.close()


def edge_test_3(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    '''
    Edge test case to verify the set_pulse_sequence function.

    Paramaters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)

    set_pulse_sequence(my_circuit, file_obj)

    assert my_circuit.emitters[0].pulse_sequence_set == True, "The frequency can't be negative"
    
    print("The first emitter's pulse sequence was correctly set.")

    file_obj.close()


if __name__ == '__main__':
    # positive test cases
    positive_test_1(get_my_lasercircuit(), '/home/input/pulse_sequence.in')
    positive_test_2(get_my_lasercircuit(), '/home/input/positive_case_2.in')

    # negative test cases
    negative_test_1(get_my_lasercircuit(), '/home/input/negative_case_1.in')
    negative_test_2(get_my_lasercircuit(), '/home/input/negative_case_2.in')
    negative_test_3(get_my_lasercircuit(), '/home/input/negative_case_3.in')
    negative_test_4(get_my_lasercircuit(), '/home/input/negative_case_4.in')
    
    # edge test cases 
    edge_test_1(get_my_lasercircuit(), '/home/input/edge_case_1.in')
    edge_test_2(get_my_lasercircuit(), '/home/input/edge_case_2.in')
    edge_test_3(get_my_lasercircuit(), '/home/input/edge_case_3.in')


