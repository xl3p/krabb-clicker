import flet as ft
import json, os
import pyautogui
import time
import threading
from pynput import keyboard
import pynput

class Autoclicker:
    def __init__(self, keyy='left', gap_time=0.5):
        self.is_start_clicks = False
        self.key_click = keyy
        self.gap_time = gap_time

    def start_clicks(self):
        """ Включает кликер """

        if self.is_start_clicks:
            print(f"Start click {self.key_click}")

            if self.key_click in ("left", "middle", "right"):
                while self.is_start_clicks == True:
                    print(self.key_click)
                    pyautogui.click(button=self.key_click)
                    time.sleep(self.gap_time if not (self.gap_time == 0) else 0.1)

            else:
                while self.is_start_clicks == True:
                    print(self.key_click)
                    con = keyboard.Controller()
                    con.tap(self.key_click)
                    time.sleep(self.gap_time if not (self.gap_time == 0) else 0.1)

        else:
            print("Disabled")
    
def main(page: ft.Page):
    page.window.height = 350
    page.window.width = 350
    page.window.frameless = True
    page.padding = 20

    # Function'

    def format_mouse_key(key):
        return str(key)[7:]

    def start_clicks_thread():
        if page.autoclicker.is_start_clicks:
            threading.Thread(daemon=True, target=page.autoclicker.start_clicks, name="clicks").start()

    def validate_start_key(key):
        if page.is_listen:
            if key == page.start_key:
                page.autoclicker.is_start_clicks = True if page.autoclicker.is_start_clicks == False else False
                start_clicks_thread()
        else:
            pass

    def start_listener():
        listener = keyboard.Listener(on_release=validate_start_key)
        listener.start()
        listener.join()

    def initilization_listener(e):
        """ Запуск слушателя """

        page.is_listen = True
        page.thread_listener = threading.Thread(target=start_listener, daemon=True).start()

        getattr(e.control, "parent").controls[1].style.shadow_color = "#000000"
        getattr(e.control, "parent").controls[0].style.shadow_color = "#000000"
        e.control.style.shadow_color = ft.Colors.ON_SURFACE
        page.update()

    def stop_listener(e):
        try:
            page.is_listen = False

            getattr(e.control, "parent").controls[1].style.shadow_color = "#000000"
            getattr(e.control, "parent").controls[0].style.shadow_color = "#000000"
            e.control.style.shadow_color = ft.Colors.ON_SURFACE
            page.update()

            page.autoclicker.is_start_clicks = False

        except AttributeError:
            pass

    def change_screen(e):
        """ Изменение окна """

        if e.control.data == "Minimized":
            page.window.minimized = False if page.window.minimized else True
            page.update()

        else:
            if not page.window.full_screen:
                e.control.icon = ft.Icons.FULLSCREEN_EXIT
                page.window.full_screen = True

                page.update()

            else:
                e.control.icon = ft.Icons.FULLSCREEN
                page.window.full_screen = False

                page.window.width = 1000
                page.window.height = 650

                page.update()

    def listenin_mouse_start_key(e):
        if page.is_listener_start:
            page.mouse_listener = pynput.mouse.Listener(on_click=lambda posy, posx, key: put_start_key(key, e))
            page.mouse_listener.start()
            page.mouse_listener.join()
            
        else:
            page.mouse_listener.stop()

    def listenin_mouse_key(e):
        if page.is_listener_start:
            page.mouse_listener = pynput.mouse.Listener(on_click=lambda posy, posx, key: put_key(key, e))
            page.mouse_listener.start()
            page.mouse_listener.join()
            
        else:
            page.mouse_listener.stop()

    def put_key(fkey, e):
        if page.is_listener_start:
            page.listener.stop()
            page.mouse_listener.stop()
            

            if str(fkey)[:6] == "Button":
                key = format_mouse_key(fkey)
            else:
                key = fkey

            page.autoclicker.key_click = key
            e.control.text = f"{key}"
            page.is_listener_start = False
            page.update()
            page.listener.stop()
            page.mouse_listener.stop()
            

    def entrer_key(e):
        try:
            page.listener.stop()
        except AttributeError:
            pass

        page.is_listener_start = True

        threading.Thread(target=lambda: listenin_mouse_key(e), daemon=True).start()

        page.listener = keyboard.Listener(on_release=lambda key: put_key(key, e))
        print("Слушатель запущен. Нажмите клавиши. Нажмите Esc для выхода.")
        page.listener.start()
        page.listener.join()
            
    def put_start_key(key, e):
        if page.is_listener_start:
            page.start_key = key


            e.control.text = f"{key}"
            page.update()
            page.listener.stop()
            page.is_listener_start = False
            page.mouse_listener.stop()

    def entrer_start_key(e):
        try:
            page.listener.stop()
        except AttributeError:
            pass

        page.is_listener_start = True
        print("Слушатель запущен. ENTER ESC TO EXIT")
        
        threading.Thread(target=lambda: listenin_mouse_start_key(e), daemon=True).start()

        page.listener = keyboard.Listener(on_release=lambda key: put_start_key(key, e))
        page.listener.start()
        page.listener.join()
    
    def change_gap_time(e):
        if e.control.value:
            print(e.control.value)
            print(float(e.control.value))
            page.gap_time = float(e.control.value)
            page.autoclicker.gap_time = float(e.control.value)

    def start_enter_key(e):
        threading.Thread(target=lambda: entrer_key(e), daemon=True).start()

    def start_enter_start_key(e):
        threading.Thread(target=lambda: entrer_start_key(e), daemon=True).start()

    # // EHD

    # Variable's
    page.gap_time = 0.5

    page.autoclicker = Autoclicker(gap_time=page.gap_time)
    page.start_key = None
    page.is_listen = False

    # // END

    # Page's

    page.appbar = ft.AppBar(
        leading=ft.Container(
            ft.WindowDragArea(
            ft.Icon(ft.Icons.ADS_CLICK), 
            expand=True
        ),
        width=page.window.width * 0.1
        ),

        title=ft.Container(
            ft.WindowDragArea(
                ft.Text("krabb clicker", size=13),
                expand=True
            ),
            width=page.window.width * 0.9
        ),

        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST, 
        toolbar_height=30,
        actions=[
                    ft.Container(
                        ft.WindowDragArea(
                            ft.Row(
                                [
                                    ft.IconButton(icon=ft.Icons.MINIMIZE, icon_size=13,
                                                    on_click=change_screen, data="Minimized",
                                                    style=ft.ButtonStyle(overlay_color=ft.Colors.TRANSPARENT)),
                                    ft.IconButton(icon=ft.Icons.FULLSCREEN, icon_size=13,
                                        on_click=change_screen, data="Windowed mode",
                                        style=ft.ButtonStyle(overlay_color=ft.Colors.TRANSPARENT)),
                                    ft.IconButton(icon=ft.Icons.CLOSE, icon_size=13,
                                                on_click= lambda e: page.window.close(),
                                                style=ft.ButtonStyle(overlay_color=ft.Colors.TRANSPARENT))
                                ]),
                        expand=True),
                    )
                ]
            )


    main_page = ft.Container(
        ft.Column([
            ft.Row([
                ft.Container(ft.Divider(color=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                             width=page.window.width * 0.15, adaptive=True, expand=True),
                ft.Text("Keys", width=page.window.width * 0.1),
                ft.Container(ft.Divider(color=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                             width=page.window.width * 0.55, adaptive=True, expand=True),
            ]),
            ft.Row([
                ft.Text("key: "),
                ft.Button(on_click=start_enter_key, text="key", color=ft.Colors.ON_SURFACE_VARIANT,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=2),
                                                     bgcolor=ft.Colors.SURFACE,
                                                     color=ft.Colors.ON_SURFACE,
                                                     shadow_color=ft.Colors.ON_SURFACE
                                                     )),
                                            

                ft.Text(" ", width=page.window.width * 0.6, expand=True),
                ft.Text("start key: "),
                ft.Button(on_click=start_enter_start_key, text="start key", color=ft.Colors.ON_SURFACE_VARIANT,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=2),
                                                     bgcolor=ft.Colors.SURFACE,
                                                     color=ft.Colors.ON_SURFACE,
                                                     shadow_color=ft.Colors.ON_SURFACE
                                                     )),
            ]),

            ft.Text(),

            ft.Row([
                ft.Container(ft.Divider(color=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                             width=page.window.width * 0.125, adaptive=True, expand=True),
                ft.Text("Gap time", width=page.window.width * 0.18),
                ft.Container(ft.Divider(color=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                             width=page.window.width * 0.49, adaptive=True, expand=True),
            ]),

            ft.Row([ft.Text("gap time: "),
            ft.TextField(label="1.0", color=ft.Colors.ON_SURFACE_VARIANT,
            border_color=ft.Colors.SURFACE_CONTAINER_HIGHEST, expand=True, input_filter=ft.InputFilter(
            allow=True, regex_string=r'^\d*\.?\d{0,5}$', replacement_string=""
            ),
            on_change=change_gap_time
            )
            ]),
            
            ft.Text(),
            
            ft.Row([
                ft.Container(ft.Divider(color=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                             width=page.window.width * 0.15, adaptive=True, expand=True),
                ft.Text("Listener", width=page.window.width * 0.16),
                ft.Container(ft.Divider(color=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                             width=page.window.width * 0.49, adaptive=True, expand=True),
            ]),
            ft.Row([
                ft.Button(on_click=initilization_listener, text="Start listener", color=ft.Colors.ON_SURFACE_VARIANT,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=2),
                                                     bgcolor=ft.Colors.SURFACE,
                                                     color=ft.Colors.ON_SURFACE,
                                                     shadow_color="#000000"
                                                     )),

                ft.Button(on_click=stop_listener, text="Stop listener", color=ft.Colors.ON_SURFACE_VARIANT,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=2),
                                                     bgcolor=ft.Colors.SURFACE,
                                                     color=ft.Colors.ON_SURFACE,
                                                     shadow_color=ft.Colors.ON_SURFACE,
                                                     ))
            ])
        ]), adaptive=True, expand=True
    )

    # // END

    page.pages = {}

    page.add(main_page)
    page.update()


if __name__ == "__main__":
    ft.app(main)
