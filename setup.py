import setuptools
from pathlib import Path
import os
import subprocess
from setuptools import setup, find_packages
from setuptools.command.install import install

README = (Path(__file__).parent/"README.md").read_text(encoding="utf8")


class InstallWithFrontend(install):
    """Custom install command to build frontend before installation."""

    def run(self):
        # Build the frontend
        frontend_path = os.path.join(os.path.dirname(__file__), "streamlit_oauth_ich_app", "frontend")
        print(frontend_path)
        if os.path.exists(frontend_path):
            print("Building frontend...")
            subprocess.check_call(["npm", "install"], cwd=frontend_path)
            subprocess.check_call(["npm", "run", "build"], cwd=frontend_path)

        install.run(self)  # Continue with normal installation


setuptools.setup(
    name="streamlit-oauth-ich-app",
    version="0.1.15",
    author="Dylan Lu",
    author_email="dnplus@gmail.com",
    description="Simple OAuth2 authorization code flow for Streamlit",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/dnplus/streamlit-oauth",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.9",
    license_files=("LICENSE",),
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit>=1.28.1",
        "httpx-oauth==0.15.1",
        "python-dotenv==1.0.1"
    ],
    cmdclass={
        "install": InstallWithFrontend,  # Use the custom install class
    },
)
