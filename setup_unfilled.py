import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dialog-bot-sdk",
    version="$CIRCLE_TAG",
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
        'dialog_api==0.0.50',
        'protobuf==3.10.0',
        'google-api-python-client==1.7.11',
        'googleapis-common-protos==1.6.0',
        'gevent==1.4.0',
        'grpcio==1.24.1',
        'grpcio-tools==1.24.1',
        'requests==2.22.0',
        'pyopenssl==19.0.0',
        'Pillow==6.2.0',
        'opencv-python==4.1.1.26',
        'audioread==2.1.8'
    ],
    python_requires='>=3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
