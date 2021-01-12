from setuptools import setup, find_packages

setup(
    name='py-aws-helper',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Helper for AWS services like S3 written in python...',
    long_description=open('README.md').read(),
    install_requires=['boto3'],
    url='https://github.com/1CloudHub/py_aws_helper.git',
    author='Sripranav P',
    author_email='sripranav@1cloudhub.com'
)