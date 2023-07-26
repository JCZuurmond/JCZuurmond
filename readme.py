from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("😄 [link=https://www.linkedin.com/in/cor-zuurmond/]Cor Zuurmond[/]", style="bright_black", guide_style="bold bright_black")

python_tree = tree.add("📦 Open Source")

legend_tree = python_tree.add("legend")
legend_tree.add("🚀 = creator and/or maintainer", )
legend_tree.add("✨ = contributor")

dbt_tree = python_tree.add("[bold link=https://www.getdbt.com/]dbt[/] - data transformation tool")
dbt_tree.add(f"🚀 [bold link=https://github.com/godatadriven/dbt-excel]dbt-excel[/] \t\t - April fools' joke about a [bold link=https://dbt-excel.com/]dbt adapter for Excel[/]")
dbt_tree.add(f"🚀 [bold link=https://github.com/godatadriven/pytest-dbt-core]pytest-dbt-core[/] \t - pytest plugin for dbt core")
dbt_tree.add(f"✨ [bold link=https://github.com/dbt-labs/dbt-spark/]dbt-spark[/] \t\t - dbt adapter for Spark")
dbt_tree.add(f"✨ [bold link=https://github.com/dbt-labs/dbt-core/]dbt-core[/] \t\t - dbt core")
dbt_tree.add(f"✨ [bold link=https://github.com/dbt-labs/dbt-core/]dbt-external-tables[/] \t - dbt macros to stage external sources")
dbt_tree.add(f"✨ [bold link=https://github.com/dbt-labs/docs.getdbt.com]docs.getdbt.com[/] \t - dbt documentation")
dbt_tree.add(f"✨ [bold link=https://github.com/dbt-msft/dbt-sqlserver]dbt-sqlserver[/] \t - dbt adapter for SQL server")


soda_tree = python_tree.add("[bold link=https://www.soda.io/]Soda[/] - data quality tool")
soda_tree.add(f"🚀 [bold link=https://github.com/sodadata/soda-spark]soda-spark[/] \t\t - PySpark library for Soda")
soda_tree.add(f"✨ [bold link=https://github.com/sodadata/soda-core]soda-core[/] \t\t - Soda core")
soda_tree.add(f"✨ [bold link=https://github.com/sodadata/docs]docs[/] \t\t\t - Soda documentation")

console.print(tree)
console.print("")

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
