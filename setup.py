import pathlib
from setuptools import setup
from imaugtools import __version__

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="imaugtools",
    version=__version__,
    description="imaugtools contains tools used for image augmentation: translate, rotate, crop. This library is for "
                "you if you do NOT want to stretch or skew, or pad pixels when doing any of these operations.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/saravanabalagi/imaugtools",
    author="Saravanabalagi Ramachandran",
    author_email="saravanabalagi@hotmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["imaugtools"],
    include_package_data=True,
    install_requires=["numpy", "opencv-python"]
)
