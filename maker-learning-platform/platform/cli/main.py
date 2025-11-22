"""Main CLI entry point for Maker Learning Platform.

This CLI demonstrates the core concept of capability-aware learning,
aligned with Principle 2 (Practical Over Perfect) by shipping a working
tool quickly, and Principle 5 (Accessibility First) by working with
just Python installed.
"""

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.tree import Tree

from core.capability_checker import CapabilityChecker

console = Console()


@click.group()
@click.version_option(version="0.1.0", prog_name="Maker Learning Platform")
def cli():
    """Maker Learning Platform - Learn by building useful things.

    A learning platform for hobbyists and tinkerers who want to
    understand and control their digital world.
    """
    pass


@cli.command()
@click.option("--verbose", "-v", is_flag=True, help="Show detailed version information")
def check(verbose):
    """Check your system capabilities.

    Detects what tools and hardware you have available, so we can
    recommend projects that match your setup.
    """
    console.print("\n[bold blue]Checking system capabilities...[/bold blue]\n")

    checker = CapabilityChecker()
    caps = checker.check_all()
    summary = caps.summary()

    # System information panel
    system_info = summary["system"]
    system_table = Table(show_header=False, box=None, padding=(0, 2))
    system_table.add_column("Property", style="cyan")
    system_table.add_column("Value")
    system_table.add_row("OS", system_info["os"])
    system_table.add_row("Python", system_info["python"])
    system_table.add_row("Architecture", system_info["architecture"])
    system_table.add_row("CPU Cores", str(system_info["cpu_cores"]))
    system_table.add_row("Memory", f"{system_info['memory_gb']} GB")

    console.print(Panel(system_table, title="[bold]System Information[/bold]", border_style="blue"))

    # Tools status
    tools = summary["tools"]
    tools_table = Table(show_header=True, header_style="bold")
    tools_table.add_column("Tool", style="cyan")
    tools_table.add_column("Status")
    if verbose:
        tools_table.add_column("Version")

    for tool, available in tools.items():
        status = "[green]Available[/green]" if available else "[dim]Not found[/dim]"
        if verbose:
            version = summary["versions"].get(tool, "-")
            tools_table.add_row(tool, status, version if available else "-")
        else:
            tools_table.add_row(tool, status)

    console.print(Panel(tools_table, title="[bold]Development Tools[/bold]", border_style="green"))

    # Unlocked projects
    projects = caps.unlocked_projects()
    project_tree = Tree("[bold]Unlocked Project Types[/bold]")
    for project in projects:
        project_tree.add(f"[green]✓[/green] {project}")

    console.print(Panel(project_tree, border_style="yellow"))

    # Summary
    tool_count = sum(1 for available in tools.values() if available)
    console.print(
        f"\n[bold green]Ready to learn![/bold green] "
        f"You have {tool_count} tools available and can work on {len(projects)} project types.\n"
    )


@cli.command()
def explore():
    """Explore available learning paths.

    Shows the skill trees and project options available to you,
    based on your interests and capabilities.
    """
    console.print("\n[bold blue]Learning Paths[/bold blue]\n")

    # Show available tracks
    tracks = Tree("[bold]Available Tracks[/bold]")

    # Python track
    python = tracks.add("[cyan]Python[/cyan] - Automation & scripting")
    python.add("[dim]Tinkerer[/dim] - File organizers, basic automation")
    python.add("[dim]Builder[/dim] - Web scraping, data processing")
    python.add("[dim]Maker[/dim] - APIs, integrations, complex automation")

    # Bash track
    bash = tracks.add("[cyan]Bash[/cyan] - System automation")
    bash.add("[dim]Tinkerer[/dim] - System info, backups")
    bash.add("[dim]Builder[/dim] - Advanced scripting, cron jobs")
    bash.add("[dim]Maker[/dim] - Infrastructure automation")

    # HTML/CSS track
    web = tracks.add("[cyan]HTML/CSS[/cyan] - Visual interfaces")
    web.add("[dim]Tinkerer[/dim] - Personal dashboards")
    web.add("[dim]Builder[/dim] - Interactive pages")
    web.add("[dim]Maker[/dim] - Full web applications")

    # Integration track
    integration = tracks.add("[yellow]Integration Projects[/yellow] - Combine skills!")
    integration.add("[dim]Morning Dashboard[/dim] - Python + HTML/CSS + Bash")
    integration.add("[dim]Home Automation Hub[/dim] - All skills")

    console.print(Panel(tracks, border_style="blue"))

    console.print(
        "\n[dim]Run [bold]maker start <track>/<level>/<project>[/bold] to begin a project.[/dim]\n"
    )


@cli.command()
@click.argument("project_path", required=False)
def start(project_path):
    """Start a learning project.

    PROJECT_PATH: The project to start (e.g., python/tinkerer/file-organizer)
    """
    if not project_path:
        console.print("\n[yellow]Available starter projects:[/yellow]\n")
        starters = [
            ("python/tinkerer/file-organizer", "Organize files by type/date"),
            ("python/tinkerer/todo-cli", "Simple command-line todo list"),
            ("bash/tinkerer/system-info", "Script to display system information"),
            ("web/tinkerer/dashboard", "Personal local dashboard"),
        ]
        for path, desc in starters:
            console.print(f"  [cyan]{path}[/cyan]")
            console.print(f"    {desc}\n")
        console.print("[dim]Usage: maker start python/tinkerer/file-organizer[/dim]\n")
        return

    # Parse project path
    parts = project_path.split("/")
    if len(parts) != 3:
        console.print(
            "[red]Invalid project path.[/red] "
            "Use format: [cyan]<language>/<level>/<project>[/cyan]"
        )
        return

    language, level, project = parts

    console.print(f"\n[bold green]Starting project:[/bold green] {project}\n")
    console.print(f"  Track: [cyan]{language}[/cyan]")
    console.print(f"  Level: [cyan]{level}[/cyan]")
    console.print()

    # Placeholder for actual project initialization
    console.print("[yellow]Project system coming soon![/yellow]")
    console.print(
        "[dim]This will create a project directory with instructions "
        "and starter code.[/dim]\n"
    )


@cli.command()
def status():
    """Show your learning progress.

    Displays your current skill levels, completed projects,
    and suggested next steps.
    """
    console.print("\n[bold blue]Your Learning Progress[/bold blue]\n")

    # Placeholder progress display
    progress_table = Table(show_header=True, header_style="bold")
    progress_table.add_column("Skill", style="cyan")
    progress_table.add_column("Track")
    progress_table.add_column("Level")
    progress_table.add_column("Progress")

    # Sample data (will be replaced with actual tracking)
    progress_table.add_row("Python", "Hobbyist", "Tinkerer 1.0", "[dim]Not started[/dim]")
    progress_table.add_row("Bash", "Hobbyist", "Tinkerer 1.0", "[dim]Not started[/dim]")
    progress_table.add_row("HTML/CSS", "Hobbyist", "Tinkerer 1.0", "[dim]Not started[/dim]")

    console.print(progress_table)
    console.print("\n[dim]Complete projects to advance your skills![/dim]\n")


def main():
    """Entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()
