# verify_installation.py
import sys
import importlib
import subprocess

modules = ["numpy", "pandas", "matplotlib", "sklearn"]

print("=== Python version ===")
print(sys.version)
print("\n=== Try imports ===")

success = []
failed = []
for m in modules:
    try:
        importlib.import_module(m)
        success.append(m)
    except Exception as e:
        failed.append((m, str(e)))

print("Imported OK:", ", ".join(success))
if failed:
    print("\nFailed imports:")
    for name, err in failed:
        print(f"- {name}: {err}")
else:
    print("\nAll imports OK")

# Check Jupyter availability (optional)
try:
    ver = subprocess.check_output(["jupyter", "--version"], text=True)
    print("\nJupyter version:\n", ver)
except Exception as e:
    print("\nJupyter not available or jupyter command not found:", e)
