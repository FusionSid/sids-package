from setuptools import setup
 
VERSION = '0.0.1'
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
    packages=[],
    install_requires=['py-cord==2.0.0b1'],
)
