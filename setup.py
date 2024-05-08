from setuptools import setup, find_packages

setup(
    name="stock",
    version="0.0.1",
    description="股票查詢API",
    author="Paxton Li",
    author_email="paxton900222@gmail.com",
    url="git+https://github.com/Paxton0222/stock.git",
    install_requires=[
        "certifi==2024.2.2"
        "charset-normalizer==3.3.2"
        "idna==3.7"
        "lxml==5.2.1"
        "requests==2.31.0"
        "twstock @ git+https://github.com/Paxton0222/twstock.git@branch#egg=twstock"
        "urllib3==2.2.1"
    ],
    dependency_links=["https://github.com/Paxton0222/twstock.git#egg=twstock"],
    packages=find_packages(),
    package_dir={},
    package_data={},
    license="MIT license",
    zip_safe=False,
    keywords="taiwan stock api",
    classifiers=[],
)
