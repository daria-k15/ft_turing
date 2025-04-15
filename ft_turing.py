import sys
import json
from print_machine import print_machine
from print_machine import print_help
from print_machine import print_status
from parsing import check_input_tape, parse_data

def execute_turing_machine(tape, machine_config, i = 0, state = None):
    if state is None:
        state = machine_config["initial"]

    if state in machine_config['finals']:
        return print("".join(tape))

    transitions = machine_config['transitions']

    for item in transitions[state]:
        if item['read'] == tape[i]:
            new_i, new_state, new_tape = transition(i, tape, item, machine_config['blank'], state)
            return execute_turing_machine(new_tape, machine_config, new_i, new_state)

def transition(i, tape, item, blank, current_state):
    print_status(tape.copy(), i, current_state, item)
    new_tape = list(tape)
    new_tape[i] = item['write']
    new_i = i - 1 if item["action"] == "LEFT" else i+1
    if new_i < 0:
        new_tape = [blank] + new_tape
        new_i = 0
    elif new_i >= len(new_tape):
        new_tape = new_tape + [blank]
    
    return new_i, item['to_state'], new_tape

def open_and_parse_file(transitions_file):
    try:
        with open(transitions_file) as json_data:
            data = json.load(json_data)
            parse_data(data)
            return data
    except Exception as error:
        print(f"{__name__}: {type(error).__name__}: {error}")
        sys.exit(1)  

def main():
    if (len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help")):
        print_help()
    if (len(sys.argv) != 3):
        return print("ft_turing [-h] jsonfile input"), exit(1)

    transitions_file, initial_tape = sys.argv[1], sys.argv[2]
    machine_config = open_and_parse_file(transitions_file)
    check_input_tape(initial_tape, machine_config['alphabet'], machine_config['blank'])

    print_machine(machine_config)
    execute_turing_machine(list(initial_tape), machine_config)

if __name__ == "__main__":
    ERRORS = (FileNotFoundError, PermissionError, ValueError, IsADirectoryError, 
                      KeyError, TypeError, AttributeError, RecursionError, KeyboardInterrupt)
    try:
        main()
    except ERRORS as error:
        print(f"{__name__}: {type(error).__name__}: {error}")
        exit(1)