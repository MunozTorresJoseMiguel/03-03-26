import flet as ft
def main(page=ft.Page):
    page.title = "Tu evento"

    page.add(ft.Text("Hola desde UV y Flet!"))

    page.add(ft.TextField(
label="Nombre Del Evento",
hint_text="Nombre Del evento",
value="",
prefix_icon=ft.Icons.PERSON,
suffix=ft.Text(".com"),
error=ft.Text("Campo obligatorio"),
password=False,
can_reveal_password=False,
multiline=False,
max_length=50,
keyboard_type=ft.KeyboardType.TEXT,
border=ft.InputBorder.OUTLINE,
border_color=ft.Colors.BLUE,
focused_border_color=ft.Colors.RED,
filled=True,
bgcolor=ft.Colors.GREY_100,
on_change=lambda e: print(e.control.value),
on_submit=lambda e: print("Enter presionado")
))
    page.add(ft.Dropdown(
    label="Tipo de evento",
    width=220,
    value="Evento",
    options=[
        ft.DropdownOption(key="Reunion", text="Reunion"),
        ft.DropdownOption(key="Conferencia", text="Conferencia"),
        ft.DropdownOption(key="Taller", text="Taller")
    ],
))
    page.add(ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="Precencial",label="Presencial"),
            ft.Radio(value="Online",label="Online")
        ])
    ))
    
    ft.Checkbox(
        label="Requiere confirmacion",
        value=False
    )
    
    page.add(ft.Image(
src="https://picsum.photos/200/200",
width=200,
height=200,

fit="cover",
border_radius=ft.BorderRadius.all(10),
repeat=ft.ImageRepeat.NO_REPEAT

))
 
ft.run(main)