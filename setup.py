from setuptools import setup

__about__ = {}

with open("appnexus/__about__.py") as fp:

    exec(fp.read(), None, __about__)

setup(
    name="appNexus-client",
    version=__about__["__version__"],
    license="MIT",
    author="Ben Michael Hayward",
    author_email="ben.hayward@kindredgroup.com",
    description="General purpose Python client for the AppNexus API",
    long_description=open("README.md").read(),
    url="https://github.com/SirBenJammin/appnexus-client",
    download_url="https://github.com/SirBenJammin/appnexus-client",
    install_requires=["requests>=2.25.0",
                      "Thingy>=0.8.3"],
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
