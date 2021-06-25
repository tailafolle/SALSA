import cx_Freeze
executables = [cx_Freeze.Executable(script="game.py", icon="assets/livroIcon.ico")]

cx_Freeze.setup(
    name="Desvie das bebidas Alcólicas",
    options={"build_exe": {
        "package": ["pygame"],
        "include_files":["assets"]
    }},
    executables = executables
)