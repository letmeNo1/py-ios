import os
import platform
import subprocess
import argparse


def run_exe(*cmd_args):
    os_name = platform.system()
    current_dir = os.path.dirname(__file__)
    if os_name == "Darwin":
        exe_path = os.path.join(current_dir, "lib", "mac", "go-ios")
        command = f'{exe_path} ' + ' '.join(cmd_args)

    elif os_name == "Windows":

        # Get the full path of the executable
        exe_path = os.path.join(current_dir, "lib", "windows", "go-ios.exe")
        print(cmd_args)

        # Construct the command with the executable path and the variable arguments
        if all(arg in cmd_args for arg in ("start", "tunnel")):

            command = f'{exe_path} --userspace ' + ' '.join(cmd_args)
        else:
            command = f'{exe_path} ' + ' '.join(cmd_args)

    # Execute the command
    subprocess.run(command, shell=True)


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Run go-ios with specified arguments.")

    # Add arguments to the parser
    parser.add_argument('cmd_args', nargs=argparse.REMAINDER, help="Arguments to pass to go-ios.exe")

    # Parse the arguments
    args = parser.parse_args()

    # Call run_exe with the parsed arguments
    run_exe(*args.cmd_args)