import subprocess

from setuptools import setup
from setuptools.command.build_py import build_py


# metadata lives in pyproject.toml; this shim only drives the Makefile build of glafic.so
class BuildPy(build_py):
    def run(self):
        subprocess.run("make clean; make python", shell = True, check = True)
        super().run()


setup(cmdclass = {'build_py': BuildPy})
