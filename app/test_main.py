import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Mango", True),
    ],
    ids=[
        "all_unique_lowercase",
        "repeated_letters",
        "case_insensitive",
        "empty_string",
        "mixed_case",
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
