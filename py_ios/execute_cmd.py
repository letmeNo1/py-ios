import os
import subprocess
import argparse
from loguru import logger


def run_exe(*cmd_args):
    current_dir = os.path.dirname(__file__)

    # Get the full path of the executable
    exe_path = os.path.join(current_dir, "lib", "windows", "go-ios.exe")

    # Construct the command with the executable path and the variable arguments
    if cmd_args == ('tunnel', 'start'):
        command = f'{exe_path} --userspace ' + ' '.join(cmd_args)
    else:
        command = f'{exe_path} ' + ' '.join(cmd_args)
    logger.debug(command)

    # Execute the command
    subprocess.run(command, shell=True)


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Run go-ios.exe with specified arguments.")

    # Add arguments to the parser
    parser.add_argument('cmd_args', nargs=argparse.REMAINDER, help="Arguments to pass to go-ios.exe")

    # Parse the arguments
    args = parser.parse_args()

    # Call run_exe with the parsed arguments
    run_exe(*args.cmd_args)