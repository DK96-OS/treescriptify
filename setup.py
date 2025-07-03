""" Setup Package Configuration
"""
from setuptools import setup, find_packages


setup(
    name="treescriptify",
    version="0.3.2",
    description="Create TreeScript from an existing filesystem tree.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="DK96-OS",
    url="https://github.com/DK96-OS/treescriptify",
    project_urls={
        "Issues": "https://github.com/DK96-OS/treescriptify/issues",
        "Source Code": "https://github.com/DK96-OS/treescriptify"
    },
    license="GPLv3",
    packages=find_packages(exclude=['test', 'test.*']),
    entry_points={
        'console_scripts': [
            'treescriptify=treescriptify.__main__:main',
            'treescriptify_this=treescriptify.__main__:main',
            'treescriptify-this=treescriptify.__main__:main',
        ],
    },
    python_requires='>=3.10',
    keywords=['treescript'],
    classifiers=[
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
)
