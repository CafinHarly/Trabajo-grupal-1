from setuptools import setup

setup(
    name='Harlybreria',
    version='0.1',
    author='Harly, Raul, Fabricio, Megumi',
    description='Librería de análisis estadístico orientada a objetos',
    py_modules=['Harlybreria'],  # 👈 porque solo hay 1 archivo .py
    install_requires=['pandas', 'matplotlib'],
)
