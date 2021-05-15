from setuptools import setup


def readme():
    with open("README.md") as file:
        return file.read()


setup(
    name="Python Project Template",
    version="0.1",
    description="Python Project Template with GitHub actions",
    long_description=readme(),
    long_description_content_type="markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "Topic :: System :: Archiving :: Packaging",
    ],
    keywords=[
        "template",
        "project structure",
        "github actions",
        "continious integration",
    ],
    url="https://github.com/maximilianwassink/python-project-template",
    author="Maximilian Wassink",
    author_email="wassink.maximilian@protonmail.com",
    license="MIT",
    packages=["project_dir"],
    install_requires=[],
    zip_safe=False,
    entry_points={},
)
