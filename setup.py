from setuptools import setup, find_packages

setup(
    name='py_ios',  # Replace with your project's name
    version='0.1.0',  # Initial version
    author='Your Name',  # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    description='A brief description of your project',
    long_description=open('README.md').read(),  # Ensure you have a README.md file
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/yourproject',  # Replace with your project's URL
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=[
        # List your project's dependencies here, e.g.,
        # 'requests>=2.25.1',
    ],
     package_data={
        'py_ios': ['lib/windows/*']
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Choose your license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the Python version requirement
    entry_points={
        'console_scripts': [
            'idb=py_ios.execute_cmd:main',  # Replace with your command and module
        ],
    },
)