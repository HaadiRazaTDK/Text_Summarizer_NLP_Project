import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="Text_Summarizer_NLP_Project",
    version="0.0.0",
    author="Syed Haadi Raza",
    author_email="Karrar.haider128@gmail.com",
    description="A simple Python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/my_package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
