import os
import json
from pathlib import Path

class Config:
    def __init__(self):
        self.config_dir = os.path.expanduser('~/.config/easy-grep')
        self.config_file = os.path.join(self.config_dir, 'config.json')
        self._ensure_config_dir()

    def _ensure_config_dir(self):
        """Ensure configuration directory exists"""
        Path(self.config_dir).mkdir(parents=True, exist_ok=True)

    def is_configured(self):
        """Check if API key is configured"""
        return os.path.exists(self.config_file)

    def save_api_key(self, api_key):
        """Save API key to config file"""
        config_data = {'api_key': api_key}
        with open(self.config_file, 'w') as f:
            json.dump(config_data, f)
        os.chmod(self.config_file, 0o600)  # Secure file permissions

    def get_api_key(self):
        """Get API key from config file"""
        if not self.is_configured():
            return None
        with open(self.config_file, 'r') as f:
            config_data = json.load(f)
        return config_data.get('api_key') 