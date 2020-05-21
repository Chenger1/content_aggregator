import pytest

from request_content import get_content, res_data, url_base

class TestClass:
    def test_one(self):
        """
        .json file contains 6 urls. 
        Test proves that url_base equil it
        """
        assert len(url_base) == 6, 'Should be 6'

    def test_two(self):
        """
        Test proves that 'get_content' returns right data
        """
        result = get_content()
        assert 'Habr' in result, 'There is no "Habr"'
        assert 'TechCrunch' in result, 'There is no "TechCrunch"'
        assert 'Techmeme' in result, 'There is no "TechMeme"'
        assert 'Kanobu' in result, 'There is no "Kanobu"'
        assert 'Strana.ua' in result, 'There is no "Strana.ua"'
        assert 'Hacker News' in result, 'There is no "Hacker News"'

    def test_three(self):
        """
        One page can contain 20 articles from each source
        Test proves that "get_content" returns right count of articles
        """
        result = get_content()
        assert len(result['Habr']) <= 20,'Result contains too much articles'
        assert len(result['Strana.ua'])  <= 20, 'Result contains too much articles'
        assert len(result['Hacker News']) <= 20,'Result contains too much articles'
