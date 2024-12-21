from setuptools import setup, find_packages
import io

# 使用 io.open() 并指定 UTF-8 编码读取 README
with io.open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="city-distance-calculator",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.20.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python tool for calculating distances between city districts and city centers in China",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/city-distance-calculator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
