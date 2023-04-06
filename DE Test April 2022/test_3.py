import pytest

# The below function doesn't work correctly. It should sum all the numbers at the
# current time. For example, 01:02:03 should return 6. Improve and fix the function,
# and write unit test(s) for it. Use any testing framework you're familiar with.


def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""
    if not time_str.replace(":", "").isnumeric():
        raise ValueError("Not in the expected format of HH:MM:SS.")
    if not all(len(chars) == 2 for chars in [i for i in time_str.split(":")]):
        raise ValueError("Not in the expected format of HH:MM:SS.")

    list_of_nums = [int(num) for num in time_str.split(":")]
    if not 0 <= list_of_nums[0] < 24:  # Presuming 24hr clock
        raise ValueError("Invalid hour.")
    if not all(0 <= nums < 60 for nums in list_of_nums[1:]):
        raise ValueError("Invalid minute/second.")
    return sum(list_of_nums)


def test_wrong_format():
    with pytest.raises(ValueError):
        sum_current_time('12,32,12')
    with pytest.raises(ValueError):
        sum_current_time('023:00:00')


def test_invalid_time():
    with pytest.raises(ValueError):
        sum_current_time('24:00:00')
    with pytest.raises(ValueError):
        sum_current_time('23:60:00')
    with pytest.raises(ValueError):
        sum_current_time('23:00:60')


def test_non_number():
    with pytest.raises(ValueError):
        sum_current_time('aa:bb:cc')


def test_correct_sum():
    assert sum_current_time('01:02:03') == 6
    assert sum_current_time('12:15:17') == 44
    assert sum_current_time('13:13:13') == 39
