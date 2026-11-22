import flet as ft

def main(page: ft.Page) -> None:
    page.title = "Message Builder"
    page.theme_mode = ft.ThemeMode.LIGHT

    uniform_style = ft.TextStyle(size=14)
    page.theme = ft.Theme(
        color_scheme_seed=ft.Colors.GREEN,
        text_theme=ft.TextTheme(
            display_large=uniform_style,
            display_medium=uniform_style,
            display_small=uniform_style,
            headline_large=uniform_style,
            headline_medium=uniform_style,
            headline_small=uniform_style,
            title_large=uniform_style,
            title_medium=uniform_style,
            title_small=uniform_style,
            body_large=uniform_style,
            body_medium=uniform_style,
            body_small=uniform_style,
            label_large=uniform_style,
            label_medium=uniform_style,
            label_small=uniform_style
        )
    )
    page.theme.hover_color = ft.Colors.TRANSPARENT

    page.window.min_width = 640
    page.window.min_height = 440
    page.window.max_width = 1440
    page.window.max_height = 1040

    ###

    def create_document(event: ft.Event[ft.IconButton]) -> None:
        document_title = ft.Text(
            "New document",
            color=ft.Colors.ON_SURFACE_VARIANT,
        )

        def on_message_name_change(inner_event: ft.Event[ft.TextField]) -> None:
            message_name = inner_event.control.value.strip()
            document_title.value = message_name or "New document"

        message_name_field = ft.TextField(
            label="Message name",
            label_style=ft.TextStyle(color=ft.Colors.ON_SURFACE_VARIANT),
            color=ft.Colors.ON_SURFACE_VARIANT,

            filled=True,
            fill_color=ft.Colors.SURFACE,

            border_radius=8,
            border_color=ft.Colors.ON_SURFACE_VARIANT,
            border_width=1,

            width=600,

            mouse_cursor=ft.MouseCursor.CLICK,
            on_change=on_message_name_change
        )

        message_type_field = ft.Dropdown(
            label="Message type",
            label_style=ft.TextStyle(color=ft.Colors.ON_SURFACE_VARIANT),
            color=ft.Colors.ON_SURFACE_VARIANT,

            filled=True,
            fill_color=ft.Colors.SURFACE,
            bgcolor=ft.Colors.SURFACE,

            border_radius=8,
            border_color=ft.Colors.ON_SURFACE_VARIANT,
            border_width=1,

            width=600,

            options=[
                ft.DropdownOption(key="standard_message", text="Standard message"),
                ft.DropdownOption(key="rich_message", text="Rich message")
            ],
            menu_style=ft.MenuStyle(
                bgcolor=ft.Colors.SURFACE,
                max_size=ft.Size.from_width(200),
                shape=ft.RoundedRectangleBorder(radius=12),
                elevation=3
            )
        )

        workspace.content = ft.Column(
            controls=[
                document_title,
                ft.Divider(),
                message_name_field,
                message_type_field
            ],
            spacing=8,
            expand=True
        )

    ###

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
        content=ft.Column(
            controls=[
                ft.Text(
                    "No open document",
                    color=ft.Colors.ON_SURFACE_VARIANT
                ),
                ft.Divider()
            ],
            spacing=8
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