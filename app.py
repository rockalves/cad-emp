from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Vertical
from textual.reactive import reactive
from textual.widgets import DataTable, Footer, Header, Static

# Dados de exemplo para iniciar
COMPANIES = [
    ("001", "Google", "https://www.google.com"),
    ("002", "Textualize", "https://www.textualize.io"),
    ("003", "Microsoft", "https://www.microsoft.com"),
]


class DetailsPane(Static):
    """Um widget para exibir os detalhes da empresa."""

    # Reage a mudanças nos detalhes da empresa e atualiza o layout
    company_details = reactive(("", "", ""), layout=True)

    def watch_company_details(self, details: tuple[str, str, str]) -> None:
        """Observa as mudanças em 'company_details' e atualiza o conteúdo."""
        code, name, url = details
        self.update(f"[b]Código:[/b] {code}\n[b]Nome:[/b] {name}\n[b]URL:[/b] {url}")


class CompanyApp(App):
    """Um aplicativo TUI para gerenciar empresas."""

    CSS_PATH = "app.css"
    BINDINGS = [
        Binding("f3", "toggle_sidebar", "Lista de Empresas"),
        Binding("q", "quit", "Sair"),
    ]

    def compose(self) -> ComposeResult:
        """Cria os widgets filhos para o aplicativo."""
        with Container():
            with Vertical(id="sidebar", classes="-hidden"):
                yield DataTable(id="company-list")
            with Vertical(id="main-pane"):
                yield Header(name="Cadastro de Empresas")
                yield DetailsPane("Selecione uma empresa na lista (F3)", id="details")
                yield Footer()

    def on_mount(self) -> None:
        """Chamado quando o aplicativo é montado no DOM."""
        table = self.query_one(DataTable)
        table.add_columns("Código", "Nome")
        for code, name, _ in COMPANIES:
            table.add_row(code, name, key=code)

    def on_data_table_row_highlighted(self, event: DataTable.RowHighlighted) -> None:
        """Chamado quando uma linha da tabela de dados é destacada."""
        if event.row_key.value:
            company_data = next((c for c in COMPANIES if c[0] == event.row_key.value), None)
            if company_data:
                details_pane = self.query_one(DetailsPane)
                details_pane.company_details = company_data

    def action_toggle_sidebar(self) -> None:
        """Alterna a visibilidade da barra lateral."""
        sidebar = self.query_one("#sidebar")
        sidebar.toggle_class("-hidden")


if __name__ == "__main__":
    app = CompanyApp()
    app.run()