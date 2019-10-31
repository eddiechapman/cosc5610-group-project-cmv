from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='cosc5610-group-project-cmv',
    version='0.1',
    packages=['cmv'],
    entry_points={
        'console_scripts': ['download=cmv.cmv_data:download'],
    }
    install_requires=[
        'requests'
    ],
    description='Network analysis of the ChangeMyView dataset',
    long_description=readme(),
    author='Noah Asaria, David Reddy, Eddie Chapman',
    url='https://github.com/eddiechapman/cosc5610-group-project-cmv',
)

