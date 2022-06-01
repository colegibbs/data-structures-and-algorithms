import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


def test_hash():
    hash_table = Hashtable()
    key = "blue"
    actual = hash_table.hash(key)
    expected = 424
    assert actual == expected


def test_set():
    hash_table = Hashtable()
    key = "blue"
    value = "favorite"
    hash_table.set(key, value)
    actual = hash_table.buckets[424].head.value[1]
    expected = value
    assert actual == expected


def test_set_update():
    hash_table = Hashtable()
    key = "blue"
    value = "favorite"
    hash_table.set(key, value)
    hash_table.set(key, "not favorite")
    actual = hash_table.buckets[424].head.value[1]
    expected = "not favorite"
    assert actual == expected

def test_set_linked_list():
    hash_table = Hashtable()
    key = "blue"
    value = "favorite"
    hash_table.set(key, value)
    hash_table.set( "bule", "not favorite")
    actual = hash_table.buckets[424].head.value[1]
    expected = "not favorite"
    assert actual == expected
    actual = hash_table.buckets[424].head.next.value[1]
    expected = "favorite"


def test_get():
    hash_table= Hashtable()
    hash_table.set("blue", "favorite")
    actual = hash_table.get("blue")
    expected = "favorite"
    assert actual == expected


def test_get_None():
    hash_table= Hashtable()
    hash_table.set("blue", "favorite")
    actual = hash_table.get("red")
    expected = None
    assert actual == expected


def test_contains():
    hash_table= Hashtable()
    hash_table.set("blue", "favorite")
    actual = hash_table.contains("blue")
    assert actual

def test_contains_does_not_contain():
    hash_table= Hashtable()
    hash_table.set("blue", "favorite")
    actual = hash_table.contains("red")
    assert not actual


def test_keys():
    hash_table= Hashtable()
    hash_table.set("blue", "favorite")
    hash_table.set("red", "no favorite")
    actual = hash_table.keys()
    expected = ["blue", "red"]
    assert actual == expected



def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


# This test does not match my LinkedList implementation
@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected
