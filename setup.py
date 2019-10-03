from setuptools import setup

requires = ['memoized_property']


setup(
    name='vsx2_change_layout',
    version='1.1.1',
    description='Change keyboard layout lib by VSx2',
    author='Vladyslav Samotoy',
    author_email='svevladislav@gmail.com',
    url="https://github.com/mcwladkoe/vsx2_change_layout",
    license="GNU GPL-3.0",
    install_requires=requires,
    packages=["vsx2_change_layout"],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU GPL-3.0 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
