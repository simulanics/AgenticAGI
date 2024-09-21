from setuptools import setup, find_packages

# Read the contents of the README file
with open("README.md", "r", encoding="utf-8") as fh:  # Explicitly specify UTF-8 encoding
    long_description = fh.read()

setup(
    name="AgenticAGI",      # The name of your package on PyPI
    version="0.1.3",        # Package version
    description="Python wrapper for AGI executable",  # Short description
    long_description=long_description,  # Detailed description (optional, use README.md)
    long_description_content_type="text/markdown",
    author="Simulanics Technologies",        # Your name
    author_email="mcombatti@simulanics.org",  # Your contact email
    url="https://github.com/simulanics/AgenticAGI",  # Project URL
    packages=find_packages(),  # Automatically find package folders
    include_package_data=True,  # Include additional non-code files (like executables)
    package_data={
        'agenticagi': [],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum version of Python required
)
