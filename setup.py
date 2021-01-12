from setuptools import setup, find_packages

requires = [
    'boto3>=1.14.49,<1.15.0'
    'botocore<1.5.0,>=1.4.1',
    'jmespath>=0.7.1,<1.0.0',
    's3transfer<0.2.0,>=0.1.0'
]


setup(
    name='py_aws_helper',
    version='1.3',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Helper for AWS services like S3 written in python...',
    long_description=open('README.md').read(),
    install_requires=['boto3'],
    url='https://github.com/1CloudHub/py_aws_helper.git',
    author='Sripranav P',
    author_email='sripranav@1cloudhub.com'
)
