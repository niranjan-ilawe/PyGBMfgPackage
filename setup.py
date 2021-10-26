from setuptools import setup


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name="pygbmfg",
    version="0.1",
    description="Package for pulling GB Mfg and QC data",
    url="",
    author="Niranjan Ilawe",
    author_email="niranjan.ilawe@10xgenomics.com",
    license="MIT",
    packages=["pygbmfg"],
    install_requires=["pandas", "pybox", "pydb", "ezsheets"],
    test_suite="nose.collector",
    tests_require=["nose"],
    include_package_data=True,
    zip_safe=False,
)
