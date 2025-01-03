# from calculator import square

# # def test_square():
# #     if square(2) != 4:
# #         print("2 squared was not 4")
# #     if square(3) != 9:
# #         print("3 squared was not 9")
# #     if square(-2) != 4:
# #         print("-2 squared was not 4")
# #     if square(-3) != 9:
# #         print("-3 squared was not 9")
# #     if square(0) != 0:
# #         print("0 squared was not 0")


# #we can use assert to check if the function is working correctly
# def test_square():
#     try:
#         assert square(2) == 4
#         assert square(3) == 9
#         assert square(-2) == 4
#         assert square(-3) == 9
#         assert square(0) == 0
#     except AssertionError:
#         print("Test failed")
#     else:
#         print("All tests passed")

# def main():
#     test_square()

# if __name__ == "__main__":
#     main()


from calculator import square
import pytest

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0

#instead of having one big function, we can have multiple small functions
def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_string():
    with pytest.raises(TypeError):
        square("cat")



