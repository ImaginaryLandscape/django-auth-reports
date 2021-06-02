from setuptools import setup, find_packages

setup(
    name='django-auth-reports',
    version='1.0.2',
    description='Adds csv reports for auth groups, right-side filtering for filter_horizontal m2m widgets',
    license='BSD',
    author='Imaginary Landscape',
    author_email='dbertrand@imagescape.com',

    install_requires=[
        'Django<2.0',
    ],

    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
)
