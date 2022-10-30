from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="graphic_analysis",
    version="0.0.4",
    author="João",
    author_email="joaov.amorim02@gmail.com",
    description="Análise de gráfico simples",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joviamorim/graphic-analysis.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)