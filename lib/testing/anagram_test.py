import pytest
from anagram import Anagram


class TestAnagram:
    @pytest.fixture
    def detector(self):
        return Anagram("listen")

    def test_instantiates_with_word(self):
        """Test that Anagram can be instantiated with a word."""
        anagram = Anagram("word")
        assert anagram.word == "word"
        assert anagram.sorted_word == sorted("word")

    def test_has_match_method(self):
        """Test that the match method exists."""
        assert hasattr(Anagram, "match")

    def test_no_matches_returns_empty_list(self):
        """Test that no matches return an empty list."""
        detector = Anagram("word")
        result = detector.match(["hello", "goodbye"])
        assert result == []

    def test_single_match_returns_list_with_one_item(self):
        """Test matching one anagram."""
        detector = Anagram("enlist")
        result = detector.match(["listen", "poison", "hello"])
        assert result == ["listen"]

    def test_multiple_matches_returns_list_with_multiple_items(self):
        """Test matching multiple anagrams."""
        detector = Anagram("enlist")
        result = detector.match(["listen", "silent", "hippopotamus"])
        assert result == ["listen", "silent"]

    @pytest.mark.parametrize(
        "word, candidates, expected",
        [
            ("listen", ["enlists", "google", "inlets", "banana"], ["inlets"]),
            ("allergy", ["gallery", "ballerina", "regally", "clergy"], ["gallery", "regally"]),
            ("Orchestra", ["cashregister", "Carthorse", "radishes"], ["Carthorse"]),
        ],
    )
    def test_parametrized_matches(self, word, candidates, expected):
        """Test various anagram scenarios using parametrized tests."""
        detector = Anagram(word)
        result = detector.match(candidates)
        assert result == expected
