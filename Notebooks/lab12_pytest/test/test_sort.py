#!/usr/bin/python
# -*- coding: utf-8 -*-

import sort
import pytest

positivetestdata = [[2, 5, 7, 1, 4], [7, 5, 4, 2, 1]]


@pytest.mark.parametrize('sample', positivetestdata)
def test_positive(sample):

    sorted = sort.bubblesort(sample)

    assert sorted == [1, 2, 4, 5, 7]


negativetestdata = [1, 'a', (2, 1, 3)]


@pytest.mark.parametrize('sample', negativetestdata)
def test_negative(sample):

    sorted = sort.bubblesort(sample)

    assert sorted == [1, 2, 4, 5, 7]


def test_catch_exception():

    exceptiontestdata = [1, 2, 'a']
    with pytest.raises(Exception):
        sort.bubblesort(exceptiontestdata)


def test_exception_message():

    exceptiontestdata = {1: 1, 2: 2, 3: 3}
    with pytest.raises(Exception) as exc:
        sort.bubblesort(exceptiontestdata)
    assert'Data type is dict' in str(exc.value)


if __name__ == '__main__':
    pytest.main()
