# My Python project

Replace this heading and sentence with your project title and purpose.

## Create your repository

1. Open [cosmos-python-template](https://github.com/erc-cosmos/cosmos-python-template).
2. Select **Use this template → Create a new repository**.
3. Choose your account or organisation, a project name, and public or private visibility.
4. Clone your new repository and enter its directory:

```sh
git clone https://github.com/YOUR-ACCOUNT/YOUR-PROJECT.git
cd YOUR-PROJECT
```

## Install and run

Mac/Linux:

```sh
bash install.sh
source ./activate.sh
pixi run --locked python -m project.main
pixi run --locked test
```

Windows PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1
. .\activate.ps1
pixi run --locked python -m project.main
pixi run --locked test
```

Repeat the activation command in each new terminal. See
[getting started](docs/getting-started.md) for Windows policy troubleshooting.

## Start your work

- Edit `src/project/main.py` and add code under `src/project/`.
- Add tests under `tests/` and notes under `docs/`.
- Run a separate script with `pixi run --locked python path/to/script.py`.
- Keep notebooks in `notebooks/`; see its README to install notebook tools.

## Add a package

Edit `pixi.toml` to add a package under `[dependencies]`, then run:

```sh
bash update.sh
pixi run --locked test
```

Windows: run `.\update.ps1` instead. Commit `pixi.toml` and `pixi.lock` together.
You can also use `bash cosmos.sh add` (Windows: `.\cosmos.ps1 add`) for an exact-version prompt.

## Get a colleague's changes

```sh
git pull --ff-only
bash install.sh
```

Windows: use `.\install.ps1`. See [environment details](PYTHON-ENVIRONMENT.md)
and [updating setup tools](COSMOS-TOOLS.md) for maintenance instructions.
