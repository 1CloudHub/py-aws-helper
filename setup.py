from setuptools import setup, find_packages

requires = [
    'boto3>=1.16.52,<1.17.0'
    'botocore>=1.19.52,<1.20.0',
    'jmespath>=0.10.0,<0.11.0',
    's3transfer>=0.3.4,<0.4.0'
]


setup(
    name='py_aws_helper',
    version='1.7',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Helper for AWS services like S3 written in python...',
    long_description=open('README.md').read(),
    install_requires=requires,
    url='https://github.com/1CloudHub/py_aws_helper.git',
    author='Sripranav P',
    author_email='sripranav@1cloudhub.com'
)
