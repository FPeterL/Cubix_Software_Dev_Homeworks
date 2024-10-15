from setuptools import setup, find_packages

setup(
    name='Build',
    version='0.1',
    author='Fehér Péter',
    author_email='feher.peter.lazlo@gmail.com',
    description='Build automazizálás házi feladat',
    url='https://github.com/FPeterL/Cubix_Software_Dev_Homeworks',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Python verzió
    install_requires=open('requirements.txt').read().splitlines(),  # Függőségek a requirements.txt-ből
)