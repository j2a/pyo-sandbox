from setuptools import setup, find_packages

setup(
    name = 'BlogTut',

    version = "",

    description = '',

    long_description = """
    """,
    
    classifiers = [
    ],

    author = '',
    
    author_email = '',
    
    url = '',
    
    install_requires = [
    'Schevo==dev,>=3.0b4dev-r2831',
    ],
    
    tests_require = [
    'nose >= 0.9.0',
    ],

    test_suite = 'nose.collector',

    extras_require = {
    },
    
    dependency_links = [
    ],
    
    packages=find_packages(),

    include_package_data=True,

    package_data={},

    entry_points="""
    """,
    )
