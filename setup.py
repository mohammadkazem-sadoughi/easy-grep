from setuptools import setup, find_packages

setup(
    name="easy-grep",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'click',
        'anthropic',
    ],
    extras_require={
        'dev': [
            'black',
            'pylint',
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'e-g=easy_grep.cli:cli',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="Natural language to command line converter",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mohammadkazem-sadoughi/easy-grep",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 