from setuptools import setup

__about__ = {}

with open("yoda/__about__.py") as fp:

    exec(fp.read(), None, __about__)

setup(
    name="AppNexus-client",
    version=__about__["__version__"],
    license="MIT",
    author="numberly",
    author_email="alexys@1000mercis.com",
    description="General purpose Python client for the AppNexus API",
    url="https://github.com/numberly/appnexus-client",
    download_url="https://github.com/numberly/appnexus-client/tags",
    platforms="any",
    packages=["appnexus"],
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
