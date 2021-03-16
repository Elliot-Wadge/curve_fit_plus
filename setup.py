#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Curve_fit_plus',
    url='https://github.com/Elliot-Wadge/curve_fit_plus',
    author='Elliot Wadge',
    author_email='ewadge@sfu.ca',
    # Needed to actually package something
    packages=['curve_fit_plus'],
    # Needed for dependencies
    install_requires=['numpy,scipy,matplotlib'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='E',
    description='a curve fitting routine to do a repetitive fitting routine',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)

