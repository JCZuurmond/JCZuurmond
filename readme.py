from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("😄 [link=https://www.linkedin.com/in/cor-zuurmond/]Cor Zuurmond", guide_style="bold bright_black")

python_tree = tree.add("📦 Open Source Packages", guide_style="bright_black")
python_tree.add("[bold link=https://github.com/godatadriven/dbt-excel]dbt-excel[/]           - [bright_black]simple bulk labelling interface")

console.print(tree)
console.print("")

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
