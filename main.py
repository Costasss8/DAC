import flet as ft  # type: ignore
from Simulador1 import criaSimulador1
from Simulador2 import criaSimulador2

def main(page: ft.Page):
    page.title = "Simulador de Juros e Créditos"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    state = {"screen": 0}

    # Construtores das "views"
    def criaPrincipal():
        return ft.Column(
            [
                ft.AppBar(
                    bgcolor=ft.Colors.BLUE_100,
                    title=ft.Row(
                        [
                            ft.Image(
                                src="logo2.png",
                                height=70,  # logo maior também aumenta altura
                                fit="contain",
                            ),
                            ft.Column(
                                [
                                    ft.Text(
                                        "SIMULADOR DE JUROS E CRÉDITOS",
                                        size=24,  # texto maior contribui para altura
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    ft.Text(
                                        "Escola Secundária Padre Benjamin Salgado",
                                        size=14,
                                    ),
                                ],
                                spacing=0,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                    ),
                    # Aumenta altura do AppBar com padding interno
                    toolbar_height=80,  # Flet >=0.9.13 permite ajustar toolbar_height
                ),
                ft.Text("Página inicial", size=22, weight=ft.FontWeight.BOLD),
                ft.Text("Escolha uma opção abaixo."),
                ft.Row(
                    [
                        ft.FilledButton(
                            "Simulador Contas-Poupança",
                            on_click=lambda _: goToView(1),
                        ),
                        ft.FilledButton(
                            "Simulador Crédito Habitação",
                            on_click=lambda _: goToView(2),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Text(
                    "TRABALHO DESENVOLVIDO PELO 12ºF",
                    size=14,
                    italic=True,
                ),
            ],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )

    # Função que devolve o corpo da página com base no estado
    def criaCorpoPagina():
        if state["screen"] == 0:
            return criaPrincipal()
        if state["screen"] == 1:
            return criaSimulador1()
        return criaSimulador2()

    corpoPagina = ft.Container(content=criaCorpoPagina(), expand=True)

    # Navegação
    def goToView(index: int):
        state["screen"] = index
        corpoPagina.content = criaCorpoPagina()
        barraNavegacao.selected_index = index
        page.update()

    def changeView(e: ft.ControlEvent):
        state["screen"] = e.control.selected_index
        corpoPagina.content = criaCorpoPagina()
        page.update()

    # Barra de navegação inferior
    barraNavegacao = ft.NavigationBar(
        selected_index=state["screen"],
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Início"),
            ft.NavigationBarDestination(icon=ft.Icons.CURRENCY_EXCHANGE, label="Simulador 1"),
            ft.NavigationBarDestination(icon=ft.Icons.ACCOUNT_BALANCE_ROUNDED, label="Simulador 2"),
        ],
        on_change=changeView,
        bgcolor=ft.Colors.BLUE_100,
    )

    # Interface principal
    page.add(
        ft.Column([corpoPagina, barraNavegacao], expand=True)
    )

    page.update()

ft.run(main, view=ft.AppView.WEB_BROWSER, assets_dir="assets")