import re

class InvalidSetFormatError(Exception):
    pass

def parse_set_input(user_input : str) -> tuple[int, float]:
    pattern = r"^\s*(\d+)\s*[xX]\s*(\d+(?:\.\d+)?)\s*$"
    match = re.match(pattern, user_input)

    if not match:
        raise InvalidSetFormatError(f"Wrong set format: '{user_input}. Change it to (e.g : 8x60) (reps, weight)'")
    
    reps = int(match.group(1))
    load = float(match.group(2))

    return reps, load