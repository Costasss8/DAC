import flet as ft

def criaSimulador2():

    capital = ft.TextField(
        label="Valor do Empréstimo (€)",
        width=300,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    taxa = ft.Slider(
        min=0,
        max=10,
        divisions=200,
        value=3,
        width=300,
    )

    valor_taxa = ft.Text("Taxa de Juro: 3.00%")

    def slider_changed(e):
        valor_taxa.value = f"Taxa de Juro: {e.control.value:.2f}%"
        valor_taxa.update()

    taxa.on_change = slider_changed

    anos = ft.TextField(
        label="Duração (anos)",
        width=300,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    resultado = ft.Text(
        "A prestação aparecerá aqui",
        size=16,
        weight=ft.FontWeight.W_500,
        text_align=ft.TextAlign.CENTER,
    )

    def calcular(e):
        try:
            c = float(capital.value)
            t = float(taxa.value)
            a = float(anos.value)

            prestacao = credito_habitacao(c, t, a)
            juros_mes = c * (t/100) / 12
            total_pago = prestacao * (a * 12)

            resultado.value = (
                f"Prestação Mensal: {prestacao:,.2f} €\n"
                f"Juros 1º Mês: {juros_mes:,.2f} €\n"
                f"Total A Pagar: {total_pago:,.2f} €\n"
            )

            resultado.update()

        except ValueError:
            resultado.value = "Erro: Insira valores válidos."
            resultado.update()

    card = ft.Container(
        content=ft.Column(
            [
                ft.Text("Crédito Habitação", size=16, weight=ft.FontWeight.BOLD),
                ft.Divider(color=ft.Colors.GREY_800),
                capital,
                ft.Text("Taxa (%)"),
                taxa,
                valor_taxa,
                anos,
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

def credito_habitacao(capital, taxa_anual, anos):
    """
    capital: valor do empréstimo (€)
    taxa_anual: taxa de juro anual (%) (ex: 3 para 3%)
    anos: duração do empréstimo (anos)
    """

    # converter taxa anual para mensal (decimal)
    i = (taxa_anual / 100) / 12

    # número total de prestações (meses)
    n = anos * 12

    if i == 0:  # caso especial sem juros
        return capital / n

    prestacao = capital * ((i * (1 + i)**n) / ((1 + i)**n - 1))
    return prestacao