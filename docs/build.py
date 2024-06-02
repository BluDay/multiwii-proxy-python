from subprocess import run

run('sphinx-build -b html . _build/html', shell=True)
