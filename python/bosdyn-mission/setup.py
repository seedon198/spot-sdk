# Copyright (c) 2019 Boston Dynamics, Inc.  All rights reserved.
#
# Downloading, reproducing, distributing or otherwise using the SDK Software
# is subject to the terms and conditions of the Boston Dynamics Software
# Development Kit License (20191101-BDSDK-SL).

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bosdyn-mission",
    version="1.1.2",
    author="Boston Dynamics",
    author_email="support@bostondynamics.com",
    description="Boston Dynamics mission code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.bostondynamics.com/",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['bosdyn-api>=1.1.2', 'six'],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Private :: Do Not Upload",
    ],
)
