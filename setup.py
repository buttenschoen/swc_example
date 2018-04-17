from setuptools import setup,find_packages

setup(
	name='newton',
	version='0.1',
	description='a mass/weight converter',
#	for GitHub:
#	download_url=url + '/tarball/' + 0.1,
	author='B. Buttenschoen',
#	for PyPI:
#	author_email= 
	license='MIT',
	packages=find_packages(),
	test_require=['nose'],
#	for installation prerequisites:
#	install_requires=['numpy'],
	entry_points={
		'console_scripts': ['newton = newton.app:main']
	}
)