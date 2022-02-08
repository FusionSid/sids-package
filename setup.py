from setuptools import setup, find_packages
 
VERSION = '0.0.4'
DESCRIPTION = "This is my first PyPi package, so its mainly a test"

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

# commands cause I keep forgetting:

# python3 setup.py bdist_wheel
# twine upload --skip-existing dist/*