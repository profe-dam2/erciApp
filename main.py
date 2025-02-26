import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "Mi primera aplicación con Flet"

    def abrir_dialog(mensaje):
        dialog.content = ft.Text(mensaje)
        dialog.open = True
        page.update()

    def cerrar_dialog(e):
        dialog.open = False
        page.update()

    def seleccionar_fecha(e):
        fecha_tx.value = f"Fecha: {fecha_dp.value.day}/{fecha_dp.value.month}/{fecha_dp.value.year}"
        page.update()

    def abrir_selector(e):
        fecha_dp.open = True
        page.update()

    def obtener_valores(e):
        minutos = minutos_drop.value
        hora = horas_drop.value
        dia = fecha_dp.value.day
        mes = fecha_dp.value.month
        evento = evento_tf.value
        print(f'Minutos: {minutos}, Hora: {hora}, Dia: {dia}, Mes: {mes}, evento: {evento}')
        if minutos is None:
            abrir_dialog("Tienes que seleccionar los minutos")
            return
        elif hora is None:
            abrir_dialog("Tienes que seleccionar hora")
            return
        elif evento == "" or evento is None:
            abrir_dialog("Indica el evento")
            return


    def obtener_horas():
        # Crear una lista vacia para almacenar las opciones
        lista_horas = []

        for i in range(0,24):
            hora_str = str(i).zfill(2)
            opcion = ft.dropdown.Option(text=hora_str,
                                        key=hora_str)
            lista_horas.append(opcion)

        return lista_horas

    def obtener_minutos():
        # Crear una lista vacia para almacenar las opciones
        lista_minutos = []

        for i in range(1,60):
            minutos_str = str(i).zfill(2)
            opcion = ft.dropdown.Option(text=minutos_str,
                                        key=minutos_str)
            lista_minutos.append(opcion)

        return lista_minutos

    contenedor = ft.Container(
        padding=10,
        bgcolor=ft.Colors.GREEN_50,
        width=page.width,
        height=page.height,
    )
    # Objetos textfield

    minutos_drop = ft.Dropdown(label="Minutos",
                               options=obtener_minutos(),
                               width=300, max_menu_height=200)
    horas_drop = ft.Dropdown(label="Hora",
                               options=obtener_horas(),
                               width=300, max_menu_height=200)

    fecha_dp = ft.DatePicker(value=datetime.datetime.now(),on_change=seleccionar_fecha)
    fecha_tx = ft.Text(f"Fecha: {fecha_dp.value.day}/{fecha_dp.value.month}/{fecha_dp.value.year}")
    boton_fecha = ft.ElevatedButton("Selecciona la fecha", on_click=abrir_selector)

    evento_tf = ft.TextField(label="Evento")

    dialog = ft.AlertDialog(modal=True, title=ft.Text("Información"), content=ft.Text("Hola"),
                       actions=[ft.TextButton("Aceptar", on_click=cerrar_dialog)])


    columna = ft.Column(
        alignment=ft.CrossAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("PROGRAMADOR DE TAREAS"),
            minutos_drop,
            horas_drop,
            fecha_tx,
            boton_fecha,
            evento_tf,
            ft.ElevatedButton("CREAR TAREA", on_click=obtener_valores),

        ]
    )

    fila = ft.Row(controls=[columna],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    contenedor.content = fila
    page.overlay.append(fecha_dp)
    page.overlay.append(dialog)
    page.add(contenedor)

ft.app(target=main, view=ft.WEB_BROWSER)