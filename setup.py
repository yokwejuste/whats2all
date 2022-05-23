from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

classifiers  =  [
  'Development Status :: 1 - Planning',
  'Intended Audience :: Developers',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]


setup(
    name = 'whats2all',
    version = '1.0.0',
    description = 'Python sdk for Whatsapp cloud api',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/whats2all/whats2all',
    author = 'whats2all',
    author_email = '',
    install_requires = ['requests'],
    packages = find_packages('src'),
    license = 'MIT',
    classifiers = classifiers
)