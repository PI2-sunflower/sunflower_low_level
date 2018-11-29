import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sunflower_low_level",
    version="0.0.5",
    author="sunflower team - pi2",
    author_email="alex@sunflower.com",
    description="sunflower low level",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PI2-sunflower",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
