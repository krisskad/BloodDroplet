from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Operating System :: POSIX :: Linux',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='BloodDroplet',
    version='0.0.1',
    description='Image Preprocessing Module to extract BloodDroplet from Microscopic Image',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Krishna Kadam',
    author_email='krisskad0@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='Image Processing, Preprocessing Module, Extract Blood Droplet, Masking Image',
    packages=find_packages(),
    install_requires=["opencv-python>=4.5.2.54", "numpy>=1.21.0"]
)