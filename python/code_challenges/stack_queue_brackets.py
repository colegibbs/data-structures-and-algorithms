from data_structures.queue import Queue


def multi_bracket_validation(string):
    openings = ["(", "[", "{"]
    closings = [")", "]", "}"]
    check_open = []
    for char in string:
        if char in openings:
            check_open.append(char)

        if char in closings:
            if check_open == []:
                return False
            if char == closings[0] and check_open[len(check_open) - 1] == openings[0]:
                check_open.remove(openings[0])
                continue
            elif char == closings[1] and check_open[len(check_open) - 1] == openings[1]:
                check_open.remove(openings[1])
                continue
            elif char == closings[2] and check_open[len(check_open) - 1] == openings[2]:
                check_open.remove(openings[2])
                continue

    return True if check_open == [] else False
