from setuptools import setup, find_packages

setup(
    name="yamtimes", 
    version="0.0.1", 
    description="Modern Date and Time Handling library for Python",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="svidaniya",
    author_email="svidaniyafg@gmail.com",
    url="https://github.com/svidaniya/yamtimes",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["python-dateutil==2.9.0.post0","six==1.17.0"],
    python_requires=">=3.6",
)
