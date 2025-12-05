import flet as ft

# Custom color palette to keep the UI clean and consistent
PRIMARY = ft.Colors.BLUE_600
BG = ft.Colors.BLUE_50

def main(page: ft.Page):
    # Basic page setup: window size, theme, background color
    page.title = "Exercise 5 - Navigation"
    page.window_width = 450
    page.window_height = 800
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = BG

    # This dictionary will store the form input data
    user_data = {
        "name": "",
        "dob": "",
        "gender": "",
        "address": "",
        "country": ""
    }

    # -------------------------------
    #            LOGIN PAGE
    # -------------------------------

    # Input fields + error message text
    email_field = ft.TextField(label="Email", width=320, border_radius=12)
    password_field = ft.TextField(label="Password", password=True, width=320, border_radius=12)
    login_error = ft.Text("", color=ft.Colors.RED_600)

    # Logic for the login button
    def login_click(e):
        # If email or password is missing, show an error message
        if not email_field.value or not password_field.value:
            login_error.value = "Please enter both email and password."
            page.update()
        else:
            # If everything is OK → navigate to home page
            login_error.value = ""
            page.go("/home")

    # Visual layout of the login page
    login_page = ft.View(
        route="/",
        bgcolor=BG,
        controls=[
            ft.Column(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Login", size=36, weight="bold", color=PRIMARY),
                                ft.Text("Please sign in to continue", size=16),

                                email_field,
                                password_field,
                                login_error,

                                ft.Container(height=10),

                                # Login button with rounded design
                                ft.ElevatedButton(
                                    "Login",
                                    on_click=login_click,
                                    bgcolor=PRIMARY,
                                    color=ft.Colors.WHITE,
                                    width=200,
                                    height=45,
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12))
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=30,
                        border_radius=20,
                        bgcolor=ft.Colors.WHITE,

                        # Add a light shadow to make the card stand out
                        shadow=ft.BoxShadow(blur_radius=16, spread_radius=2, color=ft.Colors.BLACK12),
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ]
    )

    # -------------------------------
    #            HOME PAGE
    # -------------------------------

    # Navigation to the form page
    def go_to_form(e):
        page.go("/form")

    # Layout of the home page
    home_page = ft.View(
        route="/home",
        bgcolor=BG,

        # App bar for simple navigation indication
        appbar=ft.AppBar(title=ft.Text("Home"), bgcolor=PRIMARY, color=ft.Colors.WHITE),

        controls=[
            ft.Column(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Welcome!", size=34, weight="bold", color=PRIMARY),
                                ft.Text("Navigate to the form page below.", size=16),

                                ft.Container(height=20),

                                # Button that takes the user to the form
                                ft.ElevatedButton(
                                    "Go to Form",
                                    on_click=go_to_form,
                                    bgcolor=PRIMARY,
                                    color=ft.Colors.WHITE,
                                    width=200,
                                    height=45,
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12))
                                )
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=30,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=20,
                        shadow=ft.BoxShadow(blur_radius=12, spread_radius=1, color=ft.Colors.BLACK12),
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ]
    )

    # -------------------------------
    #            FORM PAGE
    # -------------------------------

    # Input fields for the form page
    name_field = ft.TextField(label="Full Name", width=320, border_radius=12)
    address_field = ft.TextField(label="Address", width=320, border_radius=12)

    gender_dropdown = ft.Dropdown(
        label="Gender",
        width=320,
        options=[
            ft.dropdown.Option("Male"),
            ft.dropdown.Option("Female"),
            ft.dropdown.Option("Other"),
        ]
    )

    country_dropdown = ft.Dropdown(
        label="Country",
        width=320,
        options=[
            ft.dropdown.Option("Finland"),
            ft.dropdown.Option("Hungary"),
            ft.dropdown.Option("Germany"),
            ft.dropdown.Option("USA"),
        ]
    )

    # Date picker for selecting DOB
    dob_picker = ft.DatePicker()

    # Logic for the submit button
    def submit_form(e):
        # Store the user’s input
        user_data["name"] = name_field.value
        user_data["dob"] = dob_picker.value.strftime("%Y-%m-%d") if dob_picker.value else ""
        user_data["gender"] = gender_dropdown.value
        user_data["address"] = address_field.value
        user_data["country"] = country_dropdown.value

        # Navigate to the details page
        page.go("/details")

    # Form page layout
    form_page = ft.View(
        route="/form",
        bgcolor=BG,

        # App bar with a back button
        appbar=ft.AppBar(
            title=ft.Text("Form"),
            bgcolor=PRIMARY,
            color=ft.Colors.WHITE,
            leading=ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=lambda _: page.go("/home"))
        ),

        controls=[
            ft.Column(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Fill in your details", size=26, weight="bold", color=PRIMARY),

                                name_field,
                                ft.Container(height=12),

                                ft.ElevatedButton(
                                    "Select Date of Birth",
                                    on_click=lambda _: page.open(dob_picker)
                                ),

                                gender_dropdown,
                                address_field,
                                country_dropdown,

                                ft.Container(height=20),

                                ft.ElevatedButton(
                                    "Submit",
                                    on_click=submit_form,
                                    bgcolor=PRIMARY,
                                    color=ft.Colors.WHITE,
                                    width=200,
                                    height=45,
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12))
                                )
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=30,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=20,
                        shadow=ft.BoxShadow(blur_radius=12, spread_radius=1, color=ft.Colors.BLACK12),
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll="auto"
            )
        ]
    )

    # -------------------------------
    #          DETAILS PAGE
    # -------------------------------

    # Creating the details card separately keeps the code cleaner
    def build_details():
        return ft.Card(
            elevation=10,
            content=ft.Container(
                padding=20,
                content=ft.Column(
                    [
                        ft.Text("User Details", size=28, weight="bold", color=PRIMARY),
                        ft.Divider(),

                        # Displaying all captured form data
                        ft.Text(f"Name: {user_data['name']}", size=18),
                        ft.Text(f"Date of Birth: {user_data['dob']}", size=18),
                        ft.Text(f"Gender: {user_data['gender']}", size=18),
                        ft.Text(f"Address: {user_data['address']}", size=18),
                        ft.Text(f"Country: {user_data['country']}", size=18),
                    ]
                )
            )
        )

    # Layout of the details page
    details_page = ft.View(
        route="/details",
        bgcolor=BG,

        appbar=ft.AppBar(
            title=ft.Text("Details"),
            bgcolor=PRIMARY,
            color=ft.Colors.WHITE,
            leading=ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=lambda _: page.go("/form"))
        ),

        controls=[
            ft.Column(
                [
                    build_details(),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll="auto"
            )
        ]
    )

    # -------------------------------
    #            ROUTING
    # -------------------------------

    # This function updates which view is shown based on the current route
    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(login_page)
        elif page.route == "/home":
            page.views.append(home_page)
        elif page.route == "/form":
            page.views.append(form_page)
        elif page.route == "/details":
            page.views.append(details_page)

        page.update()

    page.on_route_change = route_change
    page.go("/")


# Run the app
ft.app(
    target=main,
    view=ft.AppView.WEB_BROWSER
)
