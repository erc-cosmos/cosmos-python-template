# Getting started

You need Git and an internet connection. You do not need a system Python.
Supported platforms are Intel and Apple Silicon Macs with macOS 12+, Windows
x86-64, and Linux x86-64 with glibc 2.28+. Start with the root README commands.
If Windows blocks activation, open a PowerShell session with
`powershell -ExecutionPolicy Bypass`, subject to your organisation's policy,
and repeat the activation command. You can also run commands through
`powershell -ExecutionPolicy Bypass -File .\cosmos.ps1 run python -m project.main`.

## How this project works

`src/project/` is an editable Python package: edits are immediately available
without reinstalling. Keep its generic name until you have a reason to rename it.
If renaming, update pyproject.toml, the editable dependency in pixi.toml, imports,
and commands together, then regenerate the lockfile.

The environment starts with the COSMOS Python 3.14 distribution: NumPy, pandas,
Numba, SciPy, scikit-learn, and conda-forge CPU PyTorch. pytest and setuptools
support project testing and editable installation. Requirements are owned by
pixi.toml; do not maintain a separate requirements.txt with conflicting pins.
The lockfile fixes direct and indirect versions for every supported platform.

Use `pixi run --locked test` before sharing changes. GitHub Actions runs the
example tests and scientific smoke checks on Linux, Windows, and both Mac
architectures. A passing local test is not proof of identical numerical results
on all hardware. The workflow makes no deployment or publication changes.

## Updating

A repository made from a GitHub template is independent: template edits do not
arrive automatically. Follow COSMOS-TOOLS.md for setup helper updates. To update
packages inside their current version ranges, run `bash cosmos.sh upgrade`
(or `.\cosmos.ps1 upgrade`), then test and commit the lockfile.
For a new COSMOS distribution baseline, follow PYTHON-ENVIRONMENT.md: compare
and merge constraints deliberately, retaining project extras. Never replace a
customised manifest/lockfile with an unmodified standalone copy.

## Before sharing

Replace the project title, describe the research question and how to reproduce
results, and agree a suitable licence with your supervisor before distributing
project code or data. No project licence is selected by this template.
