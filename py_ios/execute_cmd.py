import os
import subprocess
import argparse

def run_exe(*cmd_args):
    # Get the full path of the executable
    exe_path = os.path.join(os.getcwd(), "lib", "windows","go-ios.exe")
    
    # Construct the command with the executable path and the variable arguments
    command = f'"{exe_path}" --userspace ' + ' '.join(cmd_args)
    
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