import sys
import json
import time
from print_machine import print_machine
from print_machine import print_help
from print_status import print_status

def turing_machine(tape, machine_config):
    tape_as_list = list(tape)
    i = 0
    state = machine_config['initial']
    transitions = machine_config['transitions']

    while (state not in machine_config['finals']):
        for item in transitions[state]:
            if (item['read'] == tape_as_list[i]):
                (i, state) = transition(i, tape_as_list, item, machine_config['blank'], state)
                break
        else:
            print_status(tape_as_list.copy(), i, state, item)
            raise Exception("Woooow smth happened")
    print("".join(tape_as_list))

def transition(i, tape, item, blank, current_state):
    print_status(tape.copy(), i, current_state, item)
    tape[i] = item["write"]
    i = i - 1 if item["action"] == "LEFT" else i+1
    if (i == -1):
        i += 1
        tape.insert(0, blank)
    elif i >= len(tape):
        tape.append(blank)
    return (i, item["to_state"])

def open_and_parse_file(transitions_file):
    try:
        with open(transitions_file) as json_data:
            data = json.load(json_data)
            return data
    except Exception as error:
        print("Error while loading json file: {error}")
        sys.exit(1)

def main():
    if (len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help")):
        print_help()
    if (len(sys.argv) != 3):
        return print("ft_turing [-h] jsonfile input"), exit(1)

    transitions_file, initial_tape = sys.argv[1], sys.argv[2]

    machine_config = open_and_parse_file(transitions_file)
    print_machine(machine_config)
    turing_machine(initial_tape, machine_config)

if __name__ == "__main__":
    main()