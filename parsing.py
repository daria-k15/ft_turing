
def check_alphabet(alphabet: tuple, blank: str)->tuple:
    if is_not_str(alphabet):
        raise TypeError("Should be a string!")
    if is_duplicate(alphabet):
        raise ValueError("Shouldn't contain duplicates")
    if not all(map(lambda x: len(x) == 1, alphabet)):
        raise TypeError("Invalid length of the alphabet characters")
    if blank not in alphabet:
        raise ValueError("Blank should be in alphabet")

def check_states(states: tuple, initial: str, finals: tuple)->tuple:
    if not finals:
        raise ValueError("Finals shouldn't be empty")
    if is_not_str(states) or is_not_str(finals):
        raise TypeError("Should be a string")
    if is_duplicate(states) or is_duplicate(finals):
        raise ValueError("Shouldn't containt duplicates")
    if not is_value_in_states(initial, states):
        raise ValueError("Initial should be in states")
    is_final_in_states(finals, states)

def check_transitions(state_keys: tuple, transitions: dict, alphabet: tuple, states: tuple) -> dict:
    def get_trans():
        return transitions[state_keys[0]]
 
    if not state_keys: return
    if state_keys[0] not in states:
        raise ValueError(f"Transition '{state_keys[0]}' not in states list")
    if is_duplicate(tuple(map(lambda i: get_trans()[i]["read"], range(len(get_trans()))))):
        raise ValueError(f"state '{state_keys[0]}' contain duplicates")
    check_t_lines(get_trans(), alphabet, states)
    check_transitions(state_keys[1:], transitions, alphabet, states)

def check_t_lines(t:tuple[dict[str, str]], alphabet, states)-> None:
    if not t: return

    if t[0]["read"] not in alphabet or t[0]["write"] not in alphabet:
        raise ValueError(f"'read' | 'write': '{t[0]['read']}' must be in 'alphabet'")
    if t[0]["to_state"] not in states:
        raise ValueError(f"'{t[0]['to_state']}' must be in 'states'")
    if t[0]["action"] not in {"LEFT", "RIGHT"}:
        raise ValueError("'action' must be 'LEFT' or 'RIGHT'")
    check_t_lines(t[1:], alphabet, states)

def is_value_in_states(value:str, states:tuple)->bool:
    if not states: return False
    return value == states[0] or is_value_in_states(value, states[1:])

def is_final_in_states(finals:tuple, states:tuple)->None:
    if not finals:
        return
    if not is_value_in_states(finals[0], states):
        raise ValueError("Finals should be in States")
    is_final_in_states(finals[1:], states)

def is_not_str(iterable)->bool:
    match iterable:
        case []:
            return False
        case [hd, *tl]:
            if not isinstance(hd, str):
                return True
            return is_not_str(tl)
        
def is_duplicate(iterable: tuple)->bool:
    match iterable:
        case []:
            return False
        case [hd, *tl]:
            return hd in tl or is_duplicate(tl)

def parse_data(data):
    check_alphabet(data['alphabet'], data['blank'])
    check_states(data["states"], data["initial"], data["finals"])
    check_transitions((tuple(data["transitions"].keys())), data["transitions"], data["alphabet"], data["states"])

def check_input_tape(input: str, alphabet: tuple[str], blank: str):
    def check_validity(i):
        if input[i] not in alphabet:
            raise ValueError(f"Character '{input[i]}' must be in alphabet")
        if input[i] == blank:
            raise ValueError(f"Character {input[i]} is blank and shouldn't be in input")
        return (i, input[i])
    return dict(map(check_validity, range(len(input))))
    