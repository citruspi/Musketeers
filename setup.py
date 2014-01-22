from distutils.core import setup

long_description = \
'''Github_.

.. _Github: http://github.com/citruspi/Musketeers
'''

setup(
    name='Musketeers',
    version='0.1.0',
    author='Mihir Singh',
    author_email='me@mihirsingh.com',
    packages=['musketeers'],
    url='http://pypi.python.org/pypi/musketeers/',
    license='MIT License',
    description='All for one, one for all!',
    long_description=long_description,
    install_requires=[
                        'requests',
                        'pyyaml'
                     ],
    classifiers=[
                    'Development Status :: 3 - Alpha',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: MIT License',
                    'Programming Language :: Python',
                    'Topic :: System :: Networking',
                    'Topic :: Internet'
                ]
)
