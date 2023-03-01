from setuptools import setup

setup(
    name='ezdownloader',
    version='0.1.0',
    description = 'A simple file downloading tool ',
    author = 'codemilo',
    author_email = 'milomurthy@gmail.com',
    url = 'https://github.com/codemilo-ui/ezdownloader',
    packages=['ezdownloader'],
    keywords = ['tag1', 'tag2'],
    install_requires=[
        'urllib3',
        'tqdm'
    ],
    entry_points={
        'console_scripts': [
            'ezdownloader = ezdownloader.ezdownloader:main'
        ]
    }
)
