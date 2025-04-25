from setuptools import setup, find_packages

setup(
    name="interval_arithmetic",
    version="0.1",
    packages=find_packages(),
    description="Interval arithmetic and symbolic computation",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Ismingiz",
    author_email="email@example.com",
    url="https://github.com/username/interval_arithmetic",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
