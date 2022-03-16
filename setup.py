from setuptools import setup, find_packages


setup(
    name='stse',
    version='0.0.4',
    license='MIT',
    author='Jacob Gerlach',
    author_email='jwgerlach00@gmail.com',
    url='https://github.com/jwgerlach00/stuff_that_should_exist',
    description='Various extremely useful and commonly needed functions.',
    packages=find_packages('stse'),
    package_dir={'': 'stse'},
    install_requires=[
        'numpy',
        'pandas',
    ],
)
