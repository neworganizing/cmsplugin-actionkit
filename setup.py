from distutils.core import setup

setup(
    name='CMSPlugins for Actionkit',
    version='0.1',
    pacakges=['cmsplugin-actionkit'],
    license='copyright NOI',
    long_description="""
        A set of plugins for DjangoCMS that interact with Actionkit.
    """,
    install_requires=[
        'django>=1.6.5',
        'south>=0.8.4',
        'django-cms>=3.0.0'
    ],
)
