from beartype import beartype


@beartype
def note_khe_to_sci(note: str):
    if len(note) != 2:
        raise ValueError()
    if not note[1].isdigit():
        raise ValueError()
    if not note[0].isascii():
        raise ValueError()

    letter = note[0]
    if letter.islower():
        return letter.upper() + '#' + note[1]
    return note


@beartype
def note_sci_to_khe(note: str):
    if len(note) < 2 or len(note) > 3:
        raise ValueError()
    if not note[-1].isdigit():
        raise ValueError()
    if not note[0].isascii():
        raise ValueError()
    if len(note) == 3 and note[1] != "#":
        raise ValueError()

    middle = note[1]
    if middle == "#":
        return note[0].lower() + note[2]
    return note


@beartype
def katieshiqihe2pytheory(note_name: str):
    """ katie code use lowercase for black keys """
    return note_name.replace("a", "A#").replace("c", "C#").replace("d", "D#").replace("f", "F#").replace("g", "G#")