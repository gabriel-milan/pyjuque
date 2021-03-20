from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
	name='pyjuque',
	packages=find_packages(),
	version='0.1.1.4',
	description="'Juju' Quant Engine for Python",
	long_description=long_description,
	long_description_content_type="text/markdown",
	author='Tudor Barbulescu',
	author_email='hello@tudorbarbulescu.com',
	license='MIT',
    url='https://github.com/tudorelu/pyjuque',
	install_requires=['yaspin', 'ccxt', 'pyyaml', 'numpy', 'pandas', 'plotly', 'python-dotenv' ,'requests', 'SQLAlchemy', 'websocket', 'websocket-client'],
	setup_requires=['nose2==0.9.2'],
	tests_require=['alchemy-mock==0.4.3', 'coverage==5.1', 'freezegun==0.3.15', 'mock==4.0.2', 'nose2==0.9.2']
)
