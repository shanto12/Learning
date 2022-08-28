# from py_package.package_file import print_package
# from py_package.py_subpackage.sub_package_file import print_sub_package
from py_package import package_file
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    package_file.print_package()
    print_sub_package()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
