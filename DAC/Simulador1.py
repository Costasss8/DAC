import flet as ft


def calcJuros(capital, taxa, tempo, jurosSimples=True):
    """
    capital: valor inicial (float)
    taxa: taxa de juros em porcentagem (ex: 5 para 5%)
    tempo: período (anos, meses, etc.)
    jurosSimplesipo: True - simples ou False - composto
    """

    taxa_decimal = taxa / 100

    if jurosSimples:
        juros = capital * taxa_decimal * tempo
        montante = capital + juros
    #Juros Compostos
    else:
        montante = capital * (1 + taxa_decimal) ** tempo
        juros = montante - capital

    return montante, juros

def criaSimulador1():

        def slider_changed(e):
            valor_texto.value = f"Taxa de Juro Selecionada: {e.control.value:.2f}%"

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
            width=300,  # slider menor
            on_change=slider_changed,
        )
        
        valor_texto = ft.Text("Taxa de Juro Selecionada: 5.00%")

        tempo = ft.TextField(
            label="Capitalizações Por Ano",
            width=300,
            keyboard_type=ft.KeyboardType.NUMBER,
        )

        juros_escolher = [
                ft.dropdown.Option("Juros Simples"),
                ft.dropdown.Option("Juros Composto"),
                ]


        juros_tipo = ft.Dropdown(
            label="Tipo de Juros",
            width=300,
            options=juros_escolher,
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

                if juros_tipo.value == "Juros Simples":
                    js = True
                elif juros_tipo.value == "Juros Composto":
                    js = False
                else:
                    resultado.value = "Selecione o tipo de juros."
                    return

                montante, juros = calcJuros(c, t, tp, js)

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
                    ft.Text("Juros Simples e Compostos", size=22, weight=ft.FontWeight.BOLD),
                    ft.Divider(),
                    capital,
                    ft.Text("Taxa (%)"),
                    taxa,
                    valor_texto,
                    tempo,
                    juros_tipo,
                    ft.ElevatedButton("Calcular", on_click=calcular),
                    ft.Divider(),
                    resultado,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
            ),
            width=400,
            padding=20,
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
