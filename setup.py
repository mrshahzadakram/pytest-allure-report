"""Setup for pytest-nice plugin."""
from setuptools import setup

setup(
    name='pytest-allure-report',
    version='0.1.0',
    description='A pytest plugin to take screenshots for allure report',
    author='Shahzad Akram',
    author_email='shahzad.akram@newpage.io',
    license='proprietary',
    py_modules=['pytest-all5ure-report'],
    install_requires=['pytest'],
    entry_points={'pytest11': ['report_image_resize_to_percent = pytest_allure_report',
                               'report_image_resize_width = pytest_allure_report',
                               'report_image_resize_height = pytest_allure_report'], },
    classifiers=["Framework :: Pytest"],
)
