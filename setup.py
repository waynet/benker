import io
import os
import re

from setuptools import find_packages
from setuptools import setup

install_requires = [
    'lxml',
]

tests_require = [
    'Tox',
    'PyTest             ; python_version >= "3.6"',
    'PyTest < 5         ; python_version < "3"',
    'PyTest-Cov         ; python_version >= "3.6"',
    'PyTest-Cov < 2.6   ; python_version < "3"',
    'py',
    'isort',
    'check-manifest',
    'Sphinx'
]

extras_require = {"dev": tests_require}


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name="Benker",
    version='0.3.1',

    author="Laurent LAPORTE",
    author_email="laurent.laporte.pro@gmail.com",

    description="Organize your data in a spatial grid system for CALS, HTML, Office Open XML tables conversion",
    long_description=read("README.rst"),
    long_description_content_type='text/x-rst',

    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    exclude_package_data={'benker': []},
    zip_safe=True,

    url="https://github.com/laurent-laporte-pro/benker",
    license='MIT',
    platforms=['posix', 'nt'],
    keywords='Office, Word, Excel, PowerPoint, docx, xlsx, pptx, CALS, HTML, table, converter, conversion',

    install_requires=install_requires,
    extras_require=extras_require,

    # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Markup',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Text Processing :: Markup :: XML',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Manufacturing',
        'Topic :: Printing',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Other',
        'Operating System :: Unix',
    ],
)
