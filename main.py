import flet as ft

def main(page: ft.Page):
    page.title = "Tu evento"

    
    nombre_evento = ft.TextField(
        label="Nombre Del Evento",
        hint_text="Ej: Conferencia Tech",
        max_length=50,
        border_color=ft.Colors.BLUE,
    )

    tipo_evento = ft.Dropdown(
        label="Tipo de evento",
        width=220,
        options=[
            ft.DropdownOption(key="Reunion", text="Reunion"),
            ft.DropdownOption(key="Conferencia", text="Conferencia"),
            ft.DropdownOption(key="Taller", text="Taller")
        ],
    )

    modalidad = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="Presencial", label="Presencial"),
            ft.Radio(value="Online", label="Online")
        ])
    )
    
    asistencia = ft.Checkbox(label="Confirmar Asistencia", value=False)
    
    duracion = ft.Slider(
        min=1, max=8, divisions=7,
        label="{value} horas", value=1
    )

    
    resumen_text = ft.Text(size=16, color=ft.Colors.BLUE_GREY_700, weight=ft.FontWeight.BOLD)

   
    def mostrar_resumen(e):
        confirmado = "Sí" if asistencia.value else "No"
        resumen_text.value = (
            f"📋 RESUMEN DEL EVENTO:\n"
            f"Evento: {nombre_evento.value}\n"
            f"Tipo: {tipo_evento.value}\n"
            f"Modalidad: {modalidad.value}\n"
            f"Duración: {int(duracion.value)} horas\n"
            f"Asistencia confirmada: {confirmado}"
        )
        page.update() 

    
    boton_enviar = ft.ElevatedButton("Mostrar Resumen", icon=ft.Icons.SEND, on_click=mostrar_resumen)

    
    page.add(
        ft.Text("Hola desde UV y Flet!", size=20),
        nombre_evento,
        tipo_evento,
        ft.Text("Selecciona modalidad:"),
        modalidad,
        asistencia,
        ft.Text("Duración estimada:"),
        duracion,
        ft.Image(src="https://picsum.photos", width=200, height=100, fit="cover"),
        ft.Divider(), 
        boton_enviar,
        resumen_text
    )

ft.app(target=main)
