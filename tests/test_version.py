import pytest
import tax_pipeline 

def test_version_length():
    dotted_triplet = tax_pipeline.__version__.split('.')
    assert len(dotted_triplet) == 3

def test_three_ints():
    dotted_triplet = tax_pipeline.__version__.split('.')
    error = False
    try:
        maj = dotted_triplet[0]
        min = dotted_triplet[1]
        hot = dotted_triplet[2]
        print(f'version fail: "{maj}.{min}.{hot}"')
    except ValueError:
        error = True
    assert not error
