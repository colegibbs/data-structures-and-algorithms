from data_structures.hashtable import Hashtable


def left_join(left, right):
    words_syns_ants = []
    for word in left.keys():
        word_syn_ant = []
        if word in left.keys():
            word_syn_ant.append(word)
            word_syn_ant.append(left.get(word))
            word_syn_ant.append(right.get(word))
        else:
            word_syn_ant.append(word)
            word_syn_ant.append(left.get(word))
            word_syn_ant.append(None)
        words_syns_ants.append(word_syn_ant)
    return words_syns_ants



