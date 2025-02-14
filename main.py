import flet as ft

def main(page: ft.Page):
    page.title = "Interfaz con Entrada y Botón"
    nombre = ft.TextField(label="Introduce tu nombre")
    resultado = ft.Text()
    def enviar_click(e):
        resultado.value = f"¡Hola, {nombre.value}!"
        page.update()
    page.add(nombre, ft.ElevatedButton("Enviar", on_click=enviar_click), resultado)

if __name__ == '__main__':
    ft.app(target=main)
