from setuptools import setup, find_packages

setup(
    name='aicensor',
    url='https://github.com/OkaeriPoland/ai-censor-python-client',
    author='Dawid Sawicki',
    author_email='dawid@okaeri.eu',
    install_requires=['requests'],
    version='1.0',
    license='AGPLv3+',
    description='OK! AI.Censor Python Client',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: AGPLv3+ License",
        "Operating System :: OS Independent",
    ],
)
