import flet as ft


def calcJuros(capital, taxa, tempo, capitalizacoes=1, jurosSimples=True):
    """
    capital: valor inicial (float)
    taxa: taxa de juros em porcentagem (ex: 5 para 5%)
    tempo: período (anos)
    capitalizacoes: número de capitalizações por ano
    jurosSimples: True - simples | False - composto
    """

    taxa_decimal = taxa / 100

    if jurosSimples:
        juros = capital * taxa_decimal * tempo
        montante = capital + juros
    else:
        # Juros Compostos
        montante = capital * (1 + taxa_decimal / capitalizacoes) ** (capitalizacoes * tempo)
        juros = montante - capital

    return montante, juros


def criaSimulador1():

    def slider_changed(e):
        valor_texto.value = f"Taxa de Juro Selecionada: {e.control.value:.2f}%"
        valor_texto.update()

    capital = ft.TextField(
        label="Capital de Entrada (€)",
        width=300,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    taxa = ft.Slider(
        min=0,
        max=10,
        divisions=200,
        value=5,
        width=300,
        on_change=slider_changed,
    )

    valor_texto = ft.Text("Taxa de Juro Selecionada: 5.00%")

    tempo = ft.TextField(
        label="Número de Anos",
        width=300,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    capitalizacoes = ft.TextField(
        label="Capitalizações Por Ano",
        width=300,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    juros_tipo = ft.Dropdown(
        label="Tipo de Juros",
        width=300,
        options=[
            ft.dropdown.Option("Juros Simples"),
            ft.dropdown.Option("Juros Composto"),
        ],
    )

    resultado = ft.Text(
        "O Resultado Aparecerá Aqui",
        size=16,
        weight=ft.FontWeight.W_500,
        text_align=ft.TextAlign.CENTER,
    )

    def calcular(e):
        try:
            c = float(capital.value)
            t = float(taxa.value)
            tp = float(tempo.value)
            cap = float(capitalizacoes.value) if capitalizacoes.value else 1

            if juros_tipo.value == "Juros Simples":
                js = True
            elif juros_tipo.value == "Juros Composto":
                js = False
            else:
                resultado.value = "Selecione o tipo de juros."
                resultado.update()
                return

            montante, juros = calcJuros(c, t, tp, cap, js)

            resultado.value = (
                f"Capital Final: {montante:,.2f} €\n"
                f"Juros: {juros:,.2f} €"
            )

            resultado.update()

        except ValueError:
            resultado.value = "Erro: Insira valores numéricos válidos."
            resultado.update()

    card = ft.Container(
        content=ft.Column(
            [
                ft.Text("Juros Simples e Compostos", size=16, weight=ft.FontWeight.BOLD),
                ft.Divider(color=ft.Colors.GREY_800),
                capital,
                ft.Text("Taxa (%)"),
                taxa,
                valor_texto,
                tempo,
                capitalizacoes,
		ft.Text(
            spans=[
                ft.TextSpan("Caso pretendas calcular "),
                ft.TextSpan(
                    "JUROS SIMPLES",
                    style=ft.TextStyle(weight=ft.FontWeight.BOLD),
                ),
                ft.TextSpan("\nDeixa a caixa acima "),
                ft.TextSpan(
                    "VAZIA",
                    style=ft.TextStyle(weight=ft.FontWeight.BOLD),
                ),
            ],
            size=14,
            text_align=ft.TextAlign.CENTER,
        ),
                juros_tipo,
                ft.ElevatedButton("Calcular", on_click=calcular),
                ft.Divider(color=ft.Colors.GREY_800),
                resultado,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        ),
        width=400,
        padding=20,
        border=ft.border.all(2, ft.Colors.BLACK),
        border_radius=15,
        bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors.BLACK12,
            offset=ft.Offset(0, 5),
        ),
    )

    return ft.Row(
        [
            ft.Column(
                [card],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )