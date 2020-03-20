from distutils.core import setup
setup(
  name = 'epidemic',         # How you named your package folder (MyLib)
  packages = ['epidemic'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This is a python library that can help predict when will next epidemic happen (relatively). MAY NOT BE ACCURATE',   # Give a short description about your library
  author = 'BOYUAN LIU',                   # Type in your name
  author_email = 'boyuanliu6@yahoo.com',      # Type in your E-Mail
  url = 'https://github.com/boyuan12/epidemic',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/boyuan12/epidemic/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['epidemic', 'python', 'health'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'matplotlib',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)