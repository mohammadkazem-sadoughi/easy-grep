import subprocess

class CommandExecutor:
    def execute(self, command):
        """Execute the shell command and return output"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                check=True,
                text=True,
                capture_output=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error executing command: {e.stderr}" 