# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


def main() -> None:
    setup(
        name='DatasetListGenerator',
        version='0.0.1',
        description=('Dataset List Generator'),
        author='Jack Rao',
        author_email='raoxi36@foxmail.com',
        maintainer='Jack Rao',
        maintainer_email='raoxi36@foxmail.com',
        license='MIT License',
        platforms=['any'],
        # platforms=["linux", "osx"],
        url='https://github.com/Archaic-Atom/DatasetListGenerator',
        packages=find_packages(),
        entry_points={
            'console_scripts': [
                'DatasetListGenerator = DatasetListGenerator.main:main',
            ]
        },
        package_data={
            'DatasetListGenerator': ['./*']
        },
        classifiers=[
            'Operating System :: OS Independent',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3'
        ],
        python_requires='>=3'
    )


if __name__ == '__main__':
    main()
