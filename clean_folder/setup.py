from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    author='Alona Boholiepova',
    author_email='flyingcircus@example.com',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:start']}
)