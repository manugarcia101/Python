from cx_Freeze import setup, Executable

setup(name = 'python_to_exe', version = '0.1',
      description = 'Parse stuff',
      executables = [Executable("python_to_exe.py")])