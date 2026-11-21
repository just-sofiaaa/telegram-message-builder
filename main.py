import flet as ft

def main(page: ft.Page) -> None:
    message = ft.Text("[MESSAGE] Application started!")
    page.add(message)

ft.run(main)