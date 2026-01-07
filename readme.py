from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("😄 [link=https://www.linkedin.com/in/cor-zuurmond/]Cor Zuurmond[/]", style="bright_black", guide_style="bold bright_black")

python_tree = tree.add("📦 Open Source")

legend_tree = python_tree.add("legend")
legend_tree.add("🚀 = creator and/or maintainer", )
legend_tree.add("✨ = contributor")

databricks_tree = python_tree.add("[bold link=https://github.com/databrickslabs/]Databricks labs[/] \t     - Labs projects to accelerate use cases on the Databricks")
databricks_tree.add("✨ [bold link=https://github.com/databrickslabs/ucx]UCX[/] \t\t\t - Your best companion for upgrading to Unity Catalog")
databricks_tree.add("✨ [bold link=https://github.com/databrickslabs/lsql]lsq[/] \t\t\t - Lightweight SQL execution wrapper")

dbt_tree = python_tree.add("[bold link=https://www.getdbt.com/]dbt[/] - data transformation tool")
dbt_tree.add(f"🚀 [bold link=https://github.com/godatadriven/dbt-excel]dbt-excel[/] \t\t - April fools' joke about a [bold link=https://dbt-excel.com/]dbt adapter for Excel[/]")
dbt_tree.add(f"🚀 [bold link=https://github.com/godatadriven/pytest-dbt-core]pytest-dbt-core[/] \t - Pytest plugin for dbt core")
dbt_tree.add(f"✨ [bold link=https://github.com/dbt-labs/dbt-spark/]dbt-spark[/] \t\t - dbt adapter for Spark")
dbt_tree.add(f"✨ [bold link=https://github.com/dbt-labs/spark-utils]spark-utils[/] \t\t - Utility functions for dbt-spark")
dbt_tree.add(f"✨ [bold link=https://github.com/dbt-labs/dbt-core/]dbt-core[/] \t\t - dbt core")
dbt_tree.add(f"✨ [bold link=https://github.com/dbt-labs/dbt-external-tables]dbt-external-tables[/] \t - dbt macros to stage external sources")
dbt_tree.add(f"✨ [bold link=https://github.com/dbt-labs/docs.getdbt.com]docs.getdbt.com[/] \t - dbt documentation")
dbt_tree.add(f"✨ [bold link=https://github.com/dbt-msft/dbt-sqlserver]dbt-sqlserver[/] \t - dbt adapter for Microsoft SQL server")
dbt_tree.add(f"✨ [bold link=https://github.com/dbt-msft/dbt-synapse]dbt-synapse[/] \t\t - dbt adapter for Microsoft Synapse")


soda_tree = python_tree.add("[bold link=https://www.soda.io/]Soda[/] - data quality tool")
soda_tree.add(f"🚀 [bold link=https://github.com/sodadata/soda-spark]soda-spark[/] \t\t - PySpark library for Soda")
soda_tree.add(f"✨ [bold link=https://github.com/sodadata/soda-core]soda-core[/] \t\t - Soda core")
soda_tree.add(f"✨ [bold link=https://github.com/sodadata/docs]docs[/] \t\t - Soda documentation")

protein_tree = python_tree.add("[bold link=https://github.com/ProteinGym]ProteinGym[/] - benchmarks for protein fitness prediction and design")
protein_tree.add(f"✨ [bold link=https://github.com/ProteinGym/proteingym-base]proteingym-base[/] \t - Base package for ProteinGym")
protein_tree.add(f"✨ [bold link=https://github.com/ProteinGym/proteingym-benchmark]proteingym-benchmark[/]  - Benchmarks for protein fitness prediction")

data_science_tree = python_tree.add("data science tools")
data_science_tree.add(f"✨ [bold link=https://github.com/koaning/scikit-lego]scikit-lego[/] \t\t - Extra blocks for scikit-learn pipelines")
data_science_tree.add(f"🚀 [bold link=https://github.com/JCZuurmond/smelly-rats]smelly-rats[/] \t\t - scikit-learn implementation of paper about IPLS")

misc_tree = python_tree.add("Miscellaneous")
misc_tree.add(f"🚀 [bold link=https://github.com/JCZuurmond/dotfiles]dotfiles[/] \t\t - My settings files")
misc_tree.add(f"🚀 [bold link=https://github.com/JCZuurmond/pyjpeg]pyjpeg[/] \t\t - Python implementation of the JPEG algorithm")
misc_tree.add(f"✨ [bold link=https://github.com/emacs-openai/openai]emacs-openai[/] \t - Emacs integration with OpenAI")

knowledge_sharing_tree = tree.add("📚 Knowledge sharing")

legend_tree = knowledge_sharing_tree.add("legend")
legend_tree.add("🎙 = spoken", )
legend_tree.add("✏️ = written")

knowledge_sharing_tree.add(f"🎙 [bold link=https://www.youtube.com/watch?v=IJQ-PpSU1kY]PyData Global (2021)[/] \t  - Wisdom of the Crowd: Amplifying Human Intelligence With AI")
knowledge_sharing_tree.add(f"✏️ [bold link=https://scripties.uba.uva.nl/search?id=record_27376]University of Amsterdam[/] - Height estimation from aerial imagery with stereo CNNs")
knowledge_sharing_tree.add(f"✏️ [bold link=https://godatadriven.com/blog/dbts-missing-software-engineering-piece-unit-tests/]GoDataDriven blog[/] \t  - dbt’s missing software engineering piece: unit tests")

console.print(tree)
console.print("")

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
