# Notebooks with marimo

Use [marimo](https://docs.marimo.io/) for notebooks in this project. A marimo
notebook is a `.py` file: edit it in your browser and commit it like other Python
code. When you change a cell or a control, marimo reruns the cells that depend on it.

Run the commands below from the repository root.

## Install marimo once per project

First install and activate the project environment:

```sh
bash install.sh
source ./activate.sh
```

On Windows PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1
. .\activate.ps1
```

Add marimo to the project's Pixi environment:

```sh
pixi add marimo
```

This updates `pixi.toml` and `pixi.lock`. Commit both files so collaborators get
the same marimo version when they run the installation script. No Jupyter or
ipykernel installation is needed. Repeat the activation command in new terminals.

## Open the example

```sh
pixi run --locked marimo edit notebooks/example.py
```

Open the local address shown in the terminal if your browser does not open
automatically. Move the sample-size slider to regenerate a reproducible set of
measurements and update the mean and data table. The example uses NumPy, pandas,
and the project's `mean_measurement` function from `src/project/main.py`.

Save changes in the editor. Press **Ctrl+C** in the terminal to stop the server.

## Create a notebook

```sh
pixi run --locked marimo edit notebooks/my_analysis.py
```

Add Python and Markdown cells in the editor. Define each shared variable in only
one cell; read it in other cells to establish dependencies. Read a slider's
`.value` in a separate cell from the one that creates it.

Keep reusable functions in `src/project/` and import them into notebooks, for
example `from project.main import mean_measurement`. Add any extra packages
through Pixi and commit the updated manifest and lockfile. Use the project
Pixi environment rather than marimo's separate sandbox environment.

## Run without editing

Open the notebook as an interactive app with the code hidden:

```sh
pixi run --locked marimo run notebooks/example.py
```

Or execute its cells as a Python script, using the controls' default values:

```sh
pixi run --locked python notebooks/example.py
```

Script execution does not open the notebook interface or display its tables.

## Share your work

Commit notebook `.py` files alongside your source code. Keep generated files in
`results/` and document data sources in `data/`. Do not embed private data or
credentials in notebook code or exported outputs. Colleagues clone the project,
run its installation script, and use the same `marimo edit` command.

See marimo's [key concepts](https://docs.marimo.io/getting_started/key_concepts/)
and [interactive apps guide](https://docs.marimo.io/guides/apps/) for more examples.
