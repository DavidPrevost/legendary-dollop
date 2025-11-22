"""System capability detection for the Maker Learning Platform.

This module detects what hardware and software the user has available,
enabling personalized project recommendations.

Supports Principle 5 (Accessibility First) by working on any system
and Principle 3 (Flexible Paths) by enabling hardware-aware recommendations.
"""

import os
import platform
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class SystemCapabilities:
    """Container for detected system capabilities."""

    # System info
    os_name: str = ""
    os_version: str = ""
    python_version: str = ""
    architecture: str = ""

    # Core tools (required for platform)
    has_python: bool = False
    has_git: bool = False

    # Development tools
    has_docker: bool = False
    has_node: bool = False
    has_npm: bool = False

    # Databases
    has_sqlite: bool = False
    has_postgres: bool = False

    # Shell capabilities
    has_bash: bool = False
    has_powershell: bool = False

    # Network tools
    has_curl: bool = False
    has_ssh: bool = False

    # Editor/IDE indicators
    has_vscode: bool = False

    # Hardware indicators (basic)
    cpu_cores: int = 0
    memory_gb: float = 0.0

    # Tool versions (for detailed info)
    tool_versions: dict = field(default_factory=dict)

    def summary(self) -> dict:
        """Return a summary of capabilities for display."""
        return {
            "system": {
                "os": f"{self.os_name} {self.os_version}",
                "python": self.python_version,
                "architecture": self.architecture,
                "cpu_cores": self.cpu_cores,
                "memory_gb": round(self.memory_gb, 1),
            },
            "tools": {
                "git": self.has_git,
                "docker": self.has_docker,
                "node": self.has_node,
                "sqlite": self.has_sqlite,
                "postgres": self.has_postgres,
                "bash": self.has_bash,
                "powershell": self.has_powershell,
                "curl": self.has_curl,
                "ssh": self.has_ssh,
                "vscode": self.has_vscode,
            },
            "versions": self.tool_versions,
        }

    def unlocked_projects(self) -> list[str]:
        """Return list of project types this system can support."""
        projects = ["python-basics", "file-automation", "web-scraping"]

        if self.has_git:
            projects.append("version-control")

        if self.has_docker:
            projects.extend(["containerization", "homelab-services"])

        if self.has_node:
            projects.extend(["web-development", "frontend-projects"])

        if self.has_sqlite:
            projects.append("local-databases")

        if self.has_postgres:
            projects.append("production-databases")

        if self.has_bash:
            projects.extend(["shell-scripting", "system-automation"])

        if self.has_ssh:
            projects.extend(["remote-management", "server-admin"])

        if self.has_curl:
            projects.append("api-integration")

        return sorted(projects)


class CapabilityChecker:
    """Detects system capabilities for personalized recommendations."""

    def __init__(self):
        self.capabilities = SystemCapabilities()

    def check_all(self) -> SystemCapabilities:
        """Run all capability checks and return results."""
        self._check_system_info()
        self._check_core_tools()
        self._check_dev_tools()
        self._check_databases()
        self._check_shell()
        self._check_network_tools()
        self._check_editors()
        self._check_hardware()

        return self.capabilities

    def _check_system_info(self) -> None:
        """Detect basic system information."""
        self.capabilities.os_name = platform.system()
        self.capabilities.os_version = platform.release()
        self.capabilities.python_version = platform.python_version()
        self.capabilities.architecture = platform.machine()
        self.capabilities.has_python = True  # We're running Python!

    def _check_command(self, command: str, version_flag: str = "--version") -> Optional[str]:
        """Check if a command exists and get its version."""
        if shutil.which(command):
            try:
                result = subprocess.run(
                    [command, version_flag],
                    capture_output=True,
                    text=True,
                    timeout=5,
                )
                # Return first line of output as version
                output = result.stdout or result.stderr
                if output:
                    return output.strip().split("\n")[0]
                return "installed"
            except (subprocess.TimeoutExpired, subprocess.SubprocessError):
                return "installed"
        return None

    def _check_core_tools(self) -> None:
        """Check for core development tools."""
        # Git
        git_version = self._check_command("git")
        if git_version:
            self.capabilities.has_git = True
            self.capabilities.tool_versions["git"] = git_version

    def _check_dev_tools(self) -> None:
        """Check for development tools."""
        # Docker
        docker_version = self._check_command("docker")
        if docker_version:
            self.capabilities.has_docker = True
            self.capabilities.tool_versions["docker"] = docker_version

        # Node.js
        node_version = self._check_command("node")
        if node_version:
            self.capabilities.has_node = True
            self.capabilities.tool_versions["node"] = node_version

        # npm
        npm_version = self._check_command("npm")
        if npm_version:
            self.capabilities.has_npm = True
            self.capabilities.tool_versions["npm"] = npm_version

    def _check_databases(self) -> None:
        """Check for database availability."""
        # SQLite (usually bundled with Python)
        try:
            import sqlite3
            self.capabilities.has_sqlite = True
            self.capabilities.tool_versions["sqlite"] = sqlite3.sqlite_version
        except ImportError:
            pass

        # PostgreSQL client
        psql_version = self._check_command("psql")
        if psql_version:
            self.capabilities.has_postgres = True
            self.capabilities.tool_versions["postgres"] = psql_version

    def _check_shell(self) -> None:
        """Check for shell capabilities."""
        # Bash
        bash_version = self._check_command("bash")
        if bash_version:
            self.capabilities.has_bash = True
            self.capabilities.tool_versions["bash"] = bash_version

        # PowerShell
        # Try pwsh (PowerShell Core) first, then powershell
        for ps_cmd in ["pwsh", "powershell"]:
            ps_version = self._check_command(ps_cmd)
            if ps_version:
                self.capabilities.has_powershell = True
                self.capabilities.tool_versions["powershell"] = ps_version
                break

    def _check_network_tools(self) -> None:
        """Check for network-related tools."""
        # curl
        curl_version = self._check_command("curl")
        if curl_version:
            self.capabilities.has_curl = True
            self.capabilities.tool_versions["curl"] = curl_version

        # SSH
        ssh_version = self._check_command("ssh", "-V")
        if ssh_version:
            self.capabilities.has_ssh = True
            self.capabilities.tool_versions["ssh"] = ssh_version

    def _check_editors(self) -> None:
        """Check for editors/IDEs."""
        # VS Code
        code_version = self._check_command("code")
        if code_version:
            self.capabilities.has_vscode = True
            self.capabilities.tool_versions["vscode"] = code_version

    def _check_hardware(self) -> None:
        """Check basic hardware capabilities."""
        # CPU cores
        try:
            self.capabilities.cpu_cores = os.cpu_count() or 0
        except Exception:
            pass

        # Memory (cross-platform approach)
        try:
            if self.capabilities.os_name == "Linux":
                with open("/proc/meminfo") as f:
                    for line in f:
                        if line.startswith("MemTotal"):
                            # Value is in kB
                            kb = int(line.split()[1])
                            self.capabilities.memory_gb = kb / (1024 * 1024)
                            break
            elif self.capabilities.os_name == "Darwin":  # macOS
                result = subprocess.run(
                    ["sysctl", "-n", "hw.memsize"],
                    capture_output=True,
                    text=True,
                    timeout=5,
                )
                if result.returncode == 0:
                    bytes_mem = int(result.stdout.strip())
                    self.capabilities.memory_gb = bytes_mem / (1024**3)
            elif self.capabilities.os_name == "Windows":
                # Use wmic on Windows
                result = subprocess.run(
                    ["wmic", "computersystem", "get", "totalphysicalmemory"],
                    capture_output=True,
                    text=True,
                    timeout=5,
                )
                if result.returncode == 0:
                    lines = result.stdout.strip().split("\n")
                    if len(lines) > 1:
                        bytes_mem = int(lines[1].strip())
                        self.capabilities.memory_gb = bytes_mem / (1024**3)
        except Exception:
            pass
