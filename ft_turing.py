import sys
import json
import time
from print_machine import print_machine
from print_status import print_status

def turing_machine(tape, machine_config):
    tape_as_list = list(tape)
    i = 0
    state = machine_config['initial']
    transitions = machine_config['transitions']
    #print_status(tape_as_list.copy(), i, state, item)

    while (state not in machine_config['finals']):
        for item in transitions[state]:
            if (item['read'] == tape[i]):
                (i, state) = transition(i, tape_as_list, item, machine_config['blank'])
                print_status(tape_as_list.copy(), i, state, item)
                break
        else:
            print("here")
            print_status(tape_as_list.copy(), i, state, item)
            raise Exception("Woooow smth happened")
    print("".join(tape_as_list))

def transition(i, tape, item, blank):
    time.sleep(2)
    
    #print("BEFORE change tape i = ", tape[i])
    tape[i] = item["write"]
    #print("AFTER change tape i = ", tape[i])
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
           # print(data)
            return data
    except Exception as error:
        print("Error while loading json file: {error}")
        sys.exit(1)

def main():
    if len(sys.argv) < 3:
        print("usage: ft_turing jsonfile input\n")
        print("positional arguments:")
        print(" jsonfile       json description of the machine")
        print(" input          input of the machine")
        sys.exit(1)

    transitions_file = sys.argv[1]
    initial_tape = sys.argv[2]

    machine_config = open_and_parse_file(transitions_file)
    print_machine(machine_config)
    turing_machine(initial_tape, machine_config)

if __name__ == "__main__":
    main()