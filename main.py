import flet as ft

def main(page: ft.Page) -> None:
    page.title = "Message Builder"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN)

    page.window.min_width = 640
    page.window.min_height = 440
    page.window.max_width = 1440
    page.window.max_height = 1040

    def create_document(event: ft.Event[ft.IconButton]) -> None:
        workspace.content = ft.Column(
            controls=[
                ft.Text(
                    "New document",
                    color=ft.Colors.ON_SURFACE_VARIANT
                )
            ]
        )

    control_panel = ft.Container(
        content=ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.CREATE_ROUNDED,
                    tooltip="Create new document",
                    style=ft.ButtonStyle(
                        bgcolor={
                            ft.ControlState.DEFAULT: ft.Colors.GREEN_200,
                            ft.ControlState.HOVERED: ft.Colors.GREEN_300
                        },
                        shape=ft.RoundedRectangleBorder(radius=8),
                        mouse_cursor=ft.MouseCursor.CLICK
                    ),
                    on_click=create_document
                )
            ]
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