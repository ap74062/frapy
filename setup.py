from distutils.core import setup
setup(
  name = 'sandpy',         # How you named your package folder (MyLib)
  packages = ['sandpy'],   # Chose the same as "name"
  version = '1.0.0',      # Start with a small number and increase it with every change you make
  license='apache-2.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Client for sandpy cloud',   # Give a short description about your library
  author = 'Aleksander Peczot',                   # Type in your name
  author_email = 'peczot.a@gmail.com',      # Type in your E-Mail
  url = 'sandpy.com',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['CLOUD', 'COMPUTING', 'CLOUDCOMPUTING'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'System :: Distributed Computing',
    'License :: OSI Approved :: Apache 2.0 License',   # Again, pick a license
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
)
