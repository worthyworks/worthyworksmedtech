from setuptools import setup, find_packages

setup(
    name='worthyworksmedtech',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'worthyworksmedtech= app:main',
        ],
    },
)
