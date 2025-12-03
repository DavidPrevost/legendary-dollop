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
from rich.prompt import Prompt, Confirm

from core.capability_checker import CapabilityChecker
from core.progress_tracker.tracker import ProgressTracker
from core.progress_tracker.assessments import PlacementAssessment, CommandLineAssessment

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

    tracker = ProgressTracker()
    summary = tracker.get_summary()
    subjects = tracker.get_subject_list()

    # Overall summary
    summary_table = Table(show_header=False, box=None, padding=(0, 2))
    summary_table.add_column("Metric", style="cyan")
    summary_table.add_column("Value")
    summary_table.add_row("Subjects Started", str(summary["subjects_started"]))
    summary_table.add_row("Projects Completed", str(summary["total_projects_completed"]))
    summary_table.add_row("Concepts Learned", str(summary["total_concepts_learned"]))
    summary_table.add_row("Total Time", f"{summary['total_time_hours']} hours")

    console.print(Panel(summary_table, title="[bold]Overall Progress[/bold]", border_style="blue"))

    # Subject progress
    if subjects:
        progress_table = Table(show_header=True, header_style="bold")
        progress_table.add_column("Subject", style="cyan")
        progress_table.add_column("Level")
        progress_table.add_column("Projects")
        progress_table.add_column("Concepts")

        for subject in subjects:
            progress_table.add_row(
                subject["subject_id"],
                f"{subject['current_level']} ({subject['level_name']})",
                str(subject["projects_completed"]),
                str(subject["concepts_completed"]),
            )

        console.print(Panel(progress_table, title="[bold]Subject Progress[/bold]", border_style="green"))
    else:
        console.print("\n[dim]No subjects started yet. Run 'maker subjects' to see available subjects.[/dim]")

    console.print("\n[dim]Complete projects to advance your skills![/dim]\n")


@cli.command()
def subjects():
    """List available learning subjects.

    Shows all subjects you can study, with their level counts
    and estimated completion times.
    """
    console.print("\n[bold blue]Available Subjects[/bold blue]\n")

    # Subject data (will be loaded from content files in future)
    available_subjects = [
        {
            "id": "project-foundations",
            "name": "Project Foundations",
            "description": "Documentation and planning skills",
            "levels": 5,
            "hours": "15-23",
            "status": "available",
        },
        {
            "id": "command-line-mastery",
            "name": "Command Line Mastery",
            "description": "Terminal navigation and shell scripting",
            "levels": 5,
            "hours": "30-42",
            "status": "available",
        },
    ]

    subjects_table = Table(show_header=True, header_style="bold")
    subjects_table.add_column("Subject", style="cyan")
    subjects_table.add_column("Description")
    subjects_table.add_column("Levels")
    subjects_table.add_column("Est. Hours")
    subjects_table.add_column("Status")

    for subject in available_subjects:
        status_str = "[green]Available[/green]" if subject["status"] == "available" else "[dim]Coming Soon[/dim]"
        subjects_table.add_row(
            subject["name"],
            subject["description"],
            str(subject["levels"]),
            subject["hours"],
            status_str,
        )

    console.print(subjects_table)
    console.print("\n[dim]Run 'maker assess project-foundations' to take a placement test.[/dim]\n")


@cli.command()
@click.argument("subject_id", required=False)
def assess(subject_id):
    """Take a placement assessment for a subject.

    SUBJECT_ID: The subject to assess (e.g., project-foundations)
    """
    if not subject_id:
        console.print("\n[yellow]Available assessments:[/yellow]\n")
        console.print("  [cyan]project-foundations[/cyan] - Documentation and planning skills")
        console.print("  [cyan]command-line-mastery[/cyan] - Terminal and shell scripting\n")
        console.print("[dim]Usage: maker assess project-foundations[/dim]\n")
        return

    if subject_id not in ["project-foundations", "command-line-mastery"]:
        console.print(f"\n[red]Assessment not available for '{subject_id}'[/red]\n")
        return

    # Select appropriate assessment
    if subject_id == "project-foundations":
        console.print("\n[bold blue]Project Foundations - Placement Assessment[/bold blue]\n")
        assessment = PlacementAssessment()
    else:  # command-line-mastery
        console.print("\n[bold blue]Command Line Mastery - Placement Assessment[/bold blue]\n")
        assessment = CommandLineAssessment()

    console.print("Answer these questions to find your starting level.\n")
    tracker = ProgressTracker()

    # Level names for Project Foundations
    level_names = {
        0: "Curious",
        1: "Explorer",
        2: "Tinkerer",
        3: "Builder",
        4: "Maker",
    }

    # Start the subject
    tracker.start_subject(subject_id, level_names)

    correct = 0
    total = len(assessment.questions)

    for i, question in enumerate(assessment.questions, 1):
        console.print(f"[bold]Question {i}/{total}[/bold]")
        console.print(f"{question.text}\n")

        for j, option in enumerate(question.options):
            console.print(f"  {j + 1}. {option}")

        while True:
            answer = Prompt.ask("\nYour answer", choices=["1", "2", "3", "4"])
            break

        if int(answer) - 1 == question.correct_index:
            correct += 1
            console.print("[green]Correct![/green]\n")
        else:
            console.print(f"[red]Incorrect.[/red] {question.explanation}\n")

    # Calculate level
    result = assessment.calculate_level(correct, total)
    tracker.record_assessment(subject_id, result.recommended_level, level_names)

    console.print(Panel(
        f"Score: {result.score}/{result.total} ({result.percentage}%)\n"
        f"Recommended Level: [bold]{result.recommended_level}[/bold] ({level_names[result.recommended_level]})",
        title="[bold]Assessment Complete[/bold]",
        border_style="green",
    ))

    console.print(f"\n[dim]You can start at Level {result.recommended_level} or begin from Level 0 for a complete experience.[/dim]\n")


def main():
    """Entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()
