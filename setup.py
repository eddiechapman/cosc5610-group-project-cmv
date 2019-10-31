from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='cosc5610-group-project-cmv',
    version='0.1',
    packages=['cmv'],
    install_requires=[],  # TODO: How to autoload from requirements.txt?
    description='Network analysis of the ChangeMyView dataset',
    long_description=readme(),
    author='Noah Asaria, David Reddy, Eddie Chapman',
    url='https://github.com/eddiechapman/cosc5610-group-project-cmv',
)

