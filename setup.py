from setuptools import setup,find_packages

setup(
    name='pbench-agent',
    version='1.0',
    packages=['lib','pbench_cli'],
    py_modules=['pbench'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pbench=pbench_cli.main:cli
        pbench-tools-register=pbench_cli.tools.tools:register
        pbench-tools-list=pbench_cli.tools.tools:list
        pbench-tools-clean=pbench_cli.tools.tools:clean
        pbench-results-move=pbench_cli.results.results:move
        pbench-results-copy=pbench_cli.results.results:copy
        pbench-results-clean=pbench_cli.results.results:clean
    ''',
)