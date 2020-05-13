from distutils.core import setup
#from distutils.extension import Extension

def readme():
    with open('README.md') as readme:
        return readme.read()

setup(name='pyiocontrol',
    version='0.0.1',
    description='iarduino.ru module for Raspberry Pi',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    url='http://github.com/tremaru/pyiocontrol',
    author='iarduino.ru',
    author_email='shop@iarduino.ru',
    license='MIT',
)
