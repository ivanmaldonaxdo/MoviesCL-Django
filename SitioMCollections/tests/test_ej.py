import pytest 
from datetime import datetime
# print(datetime.now())
# # @pytest.mark.slow
# def test_example_pass():
#     print("TEST 1")
#     assert 1 == 1

# # @pytest.mark.xfail
# # @pytest.mark.skip
# def test_example_fail():
#     print(AssertionError())
#     assert 1 == 2   

# # @pytest.mark.skip
# def test_example_fail_2():
#     print(AssertionError())
#     assert 1 < 2

# #ACTION
# #funcion que retorna un valor
# @pytest.fixture
# def fixture_1():
#     print("Fixture 1")
#     return 1
# #ASSERT
# def test_fixture_1(fixture_1):
#     print("Test Fixture 1")
#     # print(AssertionError())
#     num = fixture_1
#     assert num == 1