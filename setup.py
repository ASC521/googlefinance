from setuptools import setup, find_packages

setup(name='googlefinance',
      version='0.2',
      description='Package to retrive current quotes, historical prices, and descriptive details from Google Finance.',
      author='Alex Curto',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'beautifulsoup4',
      ],
      zip_safe=False,
     )
