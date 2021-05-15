from setuptools import setup


def readme():
    with open("README.md") as file:
        return file.read()


setup(
    name="Python Project Template",
    version="0.1",
    description="Python Project Template with GitHub actions",
    license="MIT",
    packages=["project_dir"],
    install_requires=[],
    zip_safe=False,
    entry_points={"console_scripts": []},
)
