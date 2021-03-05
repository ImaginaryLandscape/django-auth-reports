from setuptools import setup, find_packages

setup(
    name='django-auth-reports',
    version='2.0.2',
    description='Adds csv reports for auth groups, right-side filtering for filter_horizontal m2m widgets',

    author='Imaginary Landscape',
    author_email='dbertrand@imagescape.com',

    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
)
