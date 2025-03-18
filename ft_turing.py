import sys
import json

def turing_machine(tape, machine_config):
    tap_as_list = list(tape)
    initial_state = machine_config["initial"]
    transitions = machine_config["transitions"]
    #print(initial_state)
    #print(transitions)
    print(tap_as_list)

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
    turing_machine(initial_tape, machine_config)

if __name__ == "__main__":
    main()