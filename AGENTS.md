# Project guidance

Read README.md and PYTHON-ENVIRONMENT.md before changing the environment.
Use the committed Pixi environment and `pixi run --locked test`.
Keep research code in src/project and tests in tests. Preserve the COSMOS
baseline unless a requested requirement needs a deliberate, tested change.
Add dependencies to pixi.toml and regenerate pixi.lock; preserve project extras.
Do not overwrite managed helpers: follow COSMOS-TOOLS.md for updates.
Do not upload data, run private notebooks, publish, commit, or push without
user authorisation. Never commit local installations, credentials, or data.
Report test failures and unavailable datasets instead of silently skipping them.
