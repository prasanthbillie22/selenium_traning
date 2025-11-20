# '''
# PYTEST
# '''
# import pytest
# def test_login():
#     print("Testing login")
#
# def test_logout():
#     print("Testing logout")
# #######################################################################################################################
# '''
# FIXTURE
# eqal to decorator
# '''
# @pytest.fixture()
# def greert():
#     print("good morning")
#
# @pytest.fixture()
# def spam():
#     print("hello world")
#
# def test_login(greet,spam)
#     print("login ok")
#
# def test_logout(greet,spam):
#     print("logout ok")
# ######################################################################################################################
# '''
# AUTOUSE
# it is use to pass the main function perameter to all class function perameter
# '''
# @pytest.fixture(autouse=True)
# def greet():
#     print("good morning")
#     yield
#     print("good evening")
#
# class TestSample:
#
#     def test_login(self):
#         print("login ok")
#
#     def test_singup(self):
#         print("singup ok")
#
#     def test_logout(self):
#         print("logout ok")
# #######################################################################################################################
# '''
# SCOPE='CLASS'
# this is use to apply fixture for entire class only once
# # '''
# import pytest
# #
# #
# @pytest.fixture(autouse=True, scope='class')
# def greet():
#     print("good morning")
#     yield
#     print("good evening")
#
# class TestSample:
#
#     def test_login(self):
#         print("login ok")
#
#     def test_singup(self):
#         print("singup ok")
#
# class TestSample1:
#     def test_reg(self):
#         print("reg ok")
#
#     def test_logout(self):
#         print("logout ok")
###########################################################################################################################






















