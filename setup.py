from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="EQTransformer",
    author="S. Mostafa Mousavi",
    version="0.1.58",
    author_email="smousavi05@gmail.com",
    description="A python package for making and using attentive deep-learning models for earthquake signal detection and phase picking.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/smousavi05/EQTransformer",
    licence="MIT",
    packages=find_packages(),
    keywords='Seismology, Earthquakes Detection, P&S Picking, Deep Learning, Attention Mechanism',
    install_requires=[
	'pytest', 
	'keyring>=15.1', 
	'pkginfo>=1.4.2',
	'scipy>=1.4.1', 
	'tensorflow>=2.12', 
	'keras>=2.12', 
	'matplotlib', 
	'pandas',
	'tqdm', 
	'h5py>=3.8', 
	'obspy'], 

    python_requires='>=3.6',
)


