import cx_Freeze
executables = [cx_Freeze.Executable(script="game.py", icon="assets/livroIcon.png")]

cx_Freeze.setup(
    name="Desvie das bebidas Alcólicas",
    options={"build_exe": {
        "packages": ["pygame"],
        "include_files":["assets"]
    }},
    executables = executables
)