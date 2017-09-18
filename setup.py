from setuptools import find_packages, setup

with open('exsort/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.0.1'

with open('README.rst', 'rb') as f:
    readme = f.read().decode('utf-8')

REQUIRES = []

setup(
    name='exsort',
    version=version,
    description='',
    long_description=readme,
    author='Andy Hung',
    author_email='andyhorng168@gmail.com',
    maintainer='Andy Hung',
    maintainer_email='andyhorng168@gmail.com',
    url='https://github.com/andyhorng/exsort',
    download_url='https://github.com/andyhorng/exsort/archive/0.1.tar.gz',
    license='MIT',

    keywords=[
        'external sorting',
        'sorting',
        'utility'
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    install_requires=REQUIRES,
    tests_require=['coverage', 'pytest'],

    packages=find_packages(),
)
