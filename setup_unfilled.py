import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


def version():
    return os.getenv('TAG_NAME')


setuptools.setup(
    name="dialog-bot-sdk",
    version=version(),
    author="Dmitry Borodkin",
    description="Python Bot SDK for Dialog Messenger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/salute-to-business-public/dialog-python-bot-sdk",
    packages=setuptools.find_packages(
        exclude=["tests"]
    ),
    license='Apache License 2.0',
    keywords='dialog messenger bot sdk',
    install_requires=[
        'protobuf==3.19.3',
        'grpcio==1.43.0',
        'grpcio-tools==1.43.0',
        'google-api-python-client==2.0.2',
        'googleapis-common-protos==1.53.0',
        'requests==2.25.1',
        'pyopenssl==22.1.0',
        'Pillow==8.4',
        'ratelimiter==1.2.0.post0',
    ],
    python_requires='>=3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
