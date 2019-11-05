import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='fastaread',
    version='1.0',
    scripts=['fasta-read'],
    author="Adolfo Esparza",
    author_email="esparzasordoadolfo@gmail.com",
    description="A small library for reading FASTA files",
    long_description=long_description,
    url="https://github.com/aesparzas/fasta-reader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
