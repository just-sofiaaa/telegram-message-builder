import flet as ft

def main(page: ft.Page) -> None:
    page.title = "Message Builder"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN)

    page.window.min_width = 640
    page.window.min_height = 440
    page.window.max_width = 1440
    page.window.max_height = 1040

    message = ft.Text("[MESSAGE] Application started!")
    page.add(message)

    another_message = ft.Text("[MESSAGE] All works well!")
    page.add(another_message)

ft.run(main)