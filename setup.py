from setuptools import setup
import setuptools


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name="pygbmfg",
    version="0.1.6",
    description="Package for pulling GB Mfg and QC data",
    url="https://github.com/niranjan-ilawe/PyGBMfgPackage",
    author="Niranjan Ilawe",
    author_email="niranjan.ilawe@10xgenomics.com",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=["pandas", "pybox", "pydb", "ezsheets", "termcolor"],
    test_suite="nose.collector",
    tests_require=["nose"],
    include_package_data=True,
    package_data={"": ["data/*.pickle", "data/*.json"]},
    zip_safe=False,
)
