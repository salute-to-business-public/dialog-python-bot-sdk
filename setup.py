import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dialog-bot-sdk",
    version="1.1.0",
    author="Andrey Skiba, Dialog LLC",
    author_email="a.skiba@dlg.im",
    description="Python Bot SDK for Dialog Messenger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dialogs/python-bot-sdk",
    packages=setuptools.find_packages(),
    license='Apache License 2.0',
    keywords='dialog messenger bot sdk',
    install_requires=[
        'protobuf',
        'google-api-python-client',
        'googleapis-common-protos',
        'gevent',
        'grpcio',
        'grpcio-tools',
        'requests',
        'pyopenssl',
        'Pillow'
    ],
    python_requires='>=3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)