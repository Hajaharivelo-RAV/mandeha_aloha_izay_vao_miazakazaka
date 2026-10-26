# pip is a package manager
# a package is a libraries of code like module but much more elaborated
# need an internet connexion to download some
# with pip we can download and install package withing our python 
# If you do not have PIP installed, you can download and install it from this page: https://pypi.org/project/pip/
# pip install  <name package> for installing packages
# pip uninstall <name package> for uninstall packages
# pip list to see every packages that already installed
# Find Packages at https://pypi.org/.
# let's download and install a package and use it
# first on the terminal we type pip install camelcase
import camelcase

print(dir(camelcase))

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))