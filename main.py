import flet as ft

def main(page: ft.Page) -> None:
    page.title = "Message Builder"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN)

    page.window.min_width = 640
    page.window.min_height = 440
    page.window.max_width = 1440
    page.window.max_height = 1040

    control_panel = ft.Container(
        content=ft.Text(
            "Control panel",
            color=ft.Colors.ON_SURFACE_VARIANT
        ),
        padding=12,
        bgcolor=ft.Colors.SURFACE_CONTAINER,
        border_radius=8
    )

    workspace = ft.Container(
        content=ft.Text(
            "No open document",
            color=ft.Colors.ON_SURFACE_VARIANT
        ),
        padding=12,
        bgcolor=ft.Colors.SURFACE_CONTAINER,
        border_radius=8,
        expand=True
    )

    layout = ft.Column(
        controls=[control_panel, workspace],
        spacing=8,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        expand=True
    )

    page.add(layout)

ft.run(main)