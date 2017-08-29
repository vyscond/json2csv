from setuptools import setup, find_packages

setup(
    name='json2csv',
    description='convert json to csv format',
    author='Ramon Moraes',
    author_email='ramon@vyscond.io',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'console_scripts': [
            'json2csv=json2csv:main',
        ],
    },
)
