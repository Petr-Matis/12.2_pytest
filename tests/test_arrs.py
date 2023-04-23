from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1) == 2
    assert arrs.get(["test"], 0) == "test"
    assert arrs.get([1, 2, 3], -1) is None


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], 0) == [1, 2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4], -1) == [4]
    assert arrs.my_slice([1, 2, 3, 4], 0, -1) == [1, 2, 3]
