from print_machine import transaction_to_string

def print_status(tape, i, state, item):
    tape[i] = f"<{tape[i]}>"
    print("".join(tape) + " " + transaction_to_string(state, item))