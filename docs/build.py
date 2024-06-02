from subprocess import run

run('sphinx-build -a -b html . _build/html', shell=True)
