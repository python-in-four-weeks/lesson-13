import pytest

import challenges


@pytest.mark.parametrize("sorted_numbers, target, expected_index", [
    ([12], 12, 0),
    ([1, 3, 6, 10, 15, 21, 28], 15, 4),
])
def test_binary_search_with_target_present(sorted_numbers: list[int], target: int, expected_index: int) -> None:
    index = challenges.binary_search(sorted_numbers, target)
    assert index == expected_index, f"{target} should have been found at index {expected_index}"


@pytest.mark.parametrize("sorted_numbers, target, expected_error_message", [
    ([], 12, "Target not found in list"),
    ([1, 3, 6, 10, 15, 21], 16, "Target not found in list"),
])
def test_binary_search_with_target_absent(sorted_numbers: list[int], target: int, expected_error_message: str) -> None:
    with pytest.raises(ValueError) as error:
        challenges.binary_search(sorted_numbers, target)
    assert str(error.value) == expected_error_message, f"Trying to find {target} should have resulted in message \"{expected_error_message}\""


@pytest.mark.parametrize("numbers, expected_sorted_numbers", [
    ([], []),
    ([3], [3]),
    ([2, 4, 6, 8], [2, 4, 6, 8]),
    ([5, 1, 9, 7], [1, 5, 7, 9]),
])
def test_selection_sort(numbers: list[int], expected_sorted_numbers: list[int]) -> None:
    challenges.selection_sort(numbers)
    assert numbers == expected_sorted_numbers, f"Sorted numbers should have been {expected_sorted_numbers}"


@pytest.mark.parametrize("numbers, expected_sorted_numbers", [
    ([], []),
    ([3], [3]),
    ([2, 4, 6, 8], [2, 4, 6, 8]),
    ([5, 1, 9, 7], [1, 5, 7, 9]),
])
def test_insertion_sort(numbers: list[int], expected_sorted_numbers: list[int]) -> None:
    challenges.insertion_sort(numbers)
    assert numbers == expected_sorted_numbers, f"Sorted numbers should have been {expected_sorted_numbers}"


@pytest.mark.parametrize("numbers, target, expected_pairs", [
    (set(), 6, set()),
    ({3}, 6, set()),
    ({1, 3, 7, 9}, 6, set()),
    ({4, 2, 7, 3, 8}, 9, {frozenset({2, 7})}),
    ({2, -6, 16, 8}, 10, {frozenset({2, 8}), frozenset({-6, 16})}),
])
def test_two_number_sum(numbers: set[int], target: int, expected_pairs: set[frozenset[int]]) -> None:
    pairs = challenges.two_number_sum(numbers, target)
    assert pairs == expected_pairs, f"Number pairs should have been {expected_pairs}"


@pytest.mark.parametrize("numbers, target, expected_triples", [
    (set(), 6, set()),
    ({2}, 6, set()),
    ({1, 2, 4, 8}, 6, set()),
    ({4, 1, 7, 3, 8}, 8, {frozenset({1, 3, 4})}),
    ({-4, 1, 2, 3, 6, 12}, 10, {frozenset({-4, 2, 12}), frozenset({1, 3, 6})}),
])
def test_three_number_sum(numbers: set[int], target: int, expected_triples: set[frozenset[int]]) -> None:
    triples = challenges.three_number_sum(numbers, target)
    assert triples == expected_triples, f"Number triples should have been {expected_triples}"


@pytest.mark.parametrize("numbers, expected_result", [
    ([], False),
    ([2], False),
    ([2, 2], False),
    ([2, 2, 2], True),
    ([1, 2, 3, 4, 5, 4, 3, 2, 1], False),
    ([1, 2, 3, 4, 5, 4, 5, 4, 3, 2, 1], True),
])
def test_contains_triples(numbers: list[int], expected_result: bool) -> None:
    result = challenges.contains_triples(numbers)
    assert result == expected_result, f"Expected numbers {'to' if expected_result else 'not to'} contain triples"


@pytest.mark.parametrize("words, expected_groups", [
    ([], set()),
    (["name"], {frozenset({"name"})}),
    (["name", "name"], {frozenset({"name"})}),
    (["name", "mane"], {frozenset({"name", "mane"})}),
    (["name", "gnome"], {frozenset({"name"}), frozenset({"gnome"})}),
    (["name", "age", "city"], {frozenset({"name"}), frozenset({"age"}), frozenset({"city"})}),
    (["name", "age", "city", "mean"], {frozenset({"name", "mean"}), frozenset({"age"}), frozenset({"city"})}),
    (["name", "ages", "mane", "city", "mean", "sage", "amen"], {frozenset({"name", "mane", "mean", "amen"}), frozenset({"ages", "sage"}), frozenset({"city"})}),
])
def test_group_anagrams(words: list[str], expected_groups: set[frozenset[str]]) -> None:
    groups = challenges.group_anagrams(words)
    assert groups == expected_groups, f"Expected anagram groups to be {expected_groups}"
