import flet as ft

def main(page: ft.Page) -> None:
    message = ft.Text("[MESSAGE] Application started!")
    page.add(message)

    another_message = ft.Text("[MESSAGE] All works well!")
    page.add(another_message)

ft.run(main)