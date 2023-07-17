from time import sleep
from typing import List
from rich.console import Console, OverflowMethod
from rich.panel import Panel
from rich import inspect
from rich.table import Table
from rich.tree import Tree
from rich.progress import Progress
from rich.syntax import Syntax

console = Console()
tasks = [f"Task {n}" for n in range(1, 4)]

console.rule("[b yellow]Demonstration Start", align='center')

console.print(Panel('[blue]This is a panel[/]'))

###############################################
console.rule("[b yellow]Table", align='center')

table = Table(title="Star Wars Movies")

table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")

table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

console.print(table)

###############################################
console.rule("[b magenta]Tree", align='center')

tree = Tree("Programming Languages")
python_tree = tree.add("[b green]Python[/]")
python_tree.add("Numpy")
python_tree.add("Pandas")
python_tree.add("Django")
python_tree.add("Flask")
  
java_tree = tree.add("[b dark_orange3]Java[/]")
java_tree.add("Spring")
java_tree.add("Apache")
  
frameworks = ["Express", "React", "Next", "Vue", "Angular"]
js_tree = tree.add("[b yellow]Javascript[/]")
for framework in frameworks:
    js_tree.add(framework)
  
console.print(tree)

##############################################
console.rule("[b cyan]Progress", align='center')

with console.status("[b dark_orange]Processing tasks...") as status:
    while tasks:
        task = tasks.pop(0)
        console.out(f"{task} complete")
        sleep(0.3)

with console.status("Monkeying around...", spinner="monkey"):
    sleep(0.5)

with Progress() as progress:
  
    task1 = progress.add_task("[red]Doing Task 1", total=60)
    task2 = progress.add_task("[blue]Doing Task 2", total=30)
    task3 = progress.add_task("[green]Doing Task 3", total=100)
  
    while not progress.finished:
        progress.update(task1, advance=0.1)
        progress.update(task2, advance=0.3)
        progress.update(task3, advance=0.6)
        sleep(0.01)

##############################################
console.rule("[b purple]Rich print", align='center')

inspect(tasks, methods=True)

console = Console()
syntax = Syntax.from_path('rich_templates.py', line_numbers=True)
console.print(syntax)
