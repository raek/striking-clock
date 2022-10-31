import setuptools


setuptools.setup(
    name="striking_clock",
    version="1.0.0",
    description="A service that goes BONG! BONG! BONG! every hour.",
    long_description = open("README.md").read(),
    long_description_content_type = "text/markdown",
    home_page="https://github.com/raek/striking-clock/",
    author="Rasmus Bondesson",
    author_email="raek@raek.se",
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    py_modules=[
        "striking_clock",
    ],
    python_requires=">=3.5, <4",
    install_requires=[
        "appdirs",
    ],
    entry_points={
        "console_scripts": [
            "striking-clock = striking_clock:main"
        ],
    },
    data_files=[
        ("share/systemd/user", [
            "striking-clock.service",
            "striking-clock.timer",
        ]),
    ]
)
