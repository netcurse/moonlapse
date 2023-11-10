import subprocess
import jinja2

locations = [
    "../server/app/net",
    "../tests.client.mock/tests/packets"
]

def run_shell_commands():
    commands = [f'protoc -I="." --python_out="{l}" --mypy_out="{l}" "./packets.proto"' for l in locations]

    for cmd in commands:
        process = subprocess.run(cmd, shell=True, check=True)
        if process.returncode != 0:
            print(f"Command failed with return code {process.returncode}: {cmd}")
        else:
            print(f"Command executed successfully: {cmd}")

if __name__ == "__main__":
    run_shell_commands()
