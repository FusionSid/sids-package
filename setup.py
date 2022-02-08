from setuptools import setup, find_packages
 
VERSION = '0.0.3'
DESCRIPTION = ""

setup(
    name='sidspackage',
    version=VERSION,
    author='Siddhesh Zantye',
    author_email='siddheshadsv@icloud.com',
    url='https://github.com/FusionSid/sids-package',
    description=DESCRIPTION,
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
    packages=find_packages()
)
