from data_structures.linked_list import TargetError

def zip_lists(a, b):

    if b.head == None and a.head == None:
        raise TargetError

    if b.head == None:
        return a

    if a.head == None:
        return b

    current_one = a.head
    current_two = b.head

    while current_one and current_two:
        first_broken = current_one.next
        second_broken = current_two.next
        current_one.next = current_two
        if first_broken == None:
            break
        current_two.next = first_broken
        current_one = first_broken
        current_two = second_broken

    return a
