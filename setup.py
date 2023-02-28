from setuptools import setup

setup(
    name='ezdownloader',
    version='0.1.0',
    packages=['ezdownloader'],
    install_requires=[
        'urllib3',
    ],
    entry_points={
        'console_scripts': [
            'ezdownloader = ezdownloader.__main__:main'
        ]
    }
)
