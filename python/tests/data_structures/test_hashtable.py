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

@pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


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
