
from setuptools import setup

requires = [
    'flask'
]

setup(
    name='dStatus-Server',
    version='0.0.1',
    description='dStatus monitor resource utilization.',
    author='Amit Ghadge',
    author_email='amitg.b14@gmail.com',
    url='https://github.com/Amitgb14/dStatus/Server',
    install_requires=requires,
    packages=['dServer'],
    scripts=['dServer/app.py']
)
