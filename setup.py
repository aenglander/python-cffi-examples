from setuptools import setup, find_packages

setup(
    name='python-cffi-examples',
    version='0.1.0',
    package_dir={"": "src"},
    packages=find_packages(exclude=["src/_cffi_src", "src/_cffi_src/*"]),
    cffi_modules=[
        "src/_cffi_src/build_reference_md5.py:ffi",
        "src/_cffi_src/build_xkcp_sha3.py:ffi",
    ],
    install_requires=["cffi~=1.4"],
    python_requires="~=3.6",
    url='https://github.com/aenglander/python-cffi-examples',
    license='MIT',
    author='Adam Englander',
    author_email='adamenglander@yahoo.com',
    description='Examples of CFFI in Python',
)
