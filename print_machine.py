import textwrap

def print_machine(machine_config):

    header = f"""
        |**************************************************************************
        |*                                                              *
        |*                      {machine_config['name']}                               *
        |*                                                              *
        |**************************************************************************
    """
    print(textwrap.dedent(header).replace("|", "").strip())
    main_info = f"""
        |Alphabet: {machine_config['alphabet']}
        |States: {machine_config['states']}
        |Initial: {machine_config['initial']}
        |Finals: {machine_config['finals']}
        |**************************************************************************
        |Transitions: 
    """
    print(textwrap.dedent(main_info).replace("|", "").strip())
    for key in machine_config['transitions'].items():
        for item in key[1]:
            print(transaction_to_string(key[0], item))
    print("**************************************************************************")

def transaction_to_string(state, item):
    return(
        f"({state}, {item['read']}) -> ({item['to_state']}, {item['write']}, {item['action']})"
    )

def print_help():
    error_msg = """
    |usage: ft_turing [-h] jsonfile input
    |
    |positional arguments:
    |   jsonfile json description of the machine
    |
    |   input input of the machine
    |
    |optional arguments:
    |-h, --help show this help message and exit
    """
    return print(textwrap.dedent(error_msg).replace("|", "").strip()), exit(1)

def print_status(tape, i, state, item):
    tape[i] = f"<{tape[i]}>"
    print("".join(tape) + " " + transaction_to_string(state, item))