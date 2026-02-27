import flet as ft  # type: ignore
from Simulador1 import criaSimulador1
from Simulador2 import criaSimulador2

def main(page: ft.Page):
    page.title = "Simulador de Juros e Créditos"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    state = { "screen": 0 }  # estados: 0 = início, 1 = turmas, 2 = alunos

    # Construtores das "views"
    def criaPrincipal():
        return ft.Column(
            [
                ft.Text("Página inicial", size=22, weight=ft.FontWeight.BOLD),
                ft.Text("Escolha uma opção abaixo."),
                ft.Row(
                    [
                        ft.FilledButton("Simulador Contas-Poupança", on_click=lambda _: goToView(1)),  # estados: 0 = início, 1 = turmas, 2 = alunos
                        ft.FilledButton("    Simulador Crédito    ", on_click=lambda _: goToView(2)),  # estados: 0 = início, 1 = turmas, 2 = alunos
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    criaSimulador1()

    criaSimulador2()

    # Função que devolve o corpo da página com base no estado
    def criaCorpoPagina():
        if state["screen"] == 0:
            return criaPrincipal()
        if state["screen"] == 1:
            return criaSimulador1()
        return criaSimulador2()

    # Contentor onde se coloca o conteúdo
    corpoPagina = ft.Container(content=criaCorpoPagina(), expand=True)

    # Tratamento da navegação
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
        bgcolor=ft.Colors.BLUE_100
    )

    # Interface principal
    page.add(
        ft.Column([ ft.AppBar(title=ft.Text("SIMULADOR DE JUROS E CRÉDITOS"), bgcolor=ft.Colors.BLUE_100), corpoPagina, barraNavegacao, ], expand=True, )
    )
    
    page.update()
    
ft.run(main, view=ft.AppView.WEB_BROWSER)




