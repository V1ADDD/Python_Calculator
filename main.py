from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


class MainApp(App):
    def build(self):  # constructor
        main_layout = BoxLayout(orientation="vertical", padding=3, spacing=3)  # window
        self.solution = TextInput(multiline=False, readonly=False, halign="right", font_size=40)  # obj for text input
        self.solution.focus = True  # focused on TextInput
        self.solution.bind(text=self.on_key)  # bind on text input for TextInput
        main_layout.add_widget(self.solution)  # add TextInput to main window
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]  # mass of button info's
        for row in buttons:
            h_layout = BoxLayout()  # window in window
            for label in row:
                button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5})  # obj for clicking (button)
                button.bind(on_press=self.on_button_press)  # bind on press for Button
                h_layout.add_widget(button)  # add Button on window in window
            main_layout.add_widget(h_layout)  # add window on window to window

        equals_button = Button(text="=", pos_hint={"center_x": 0.5, "center_y": 0.5})  # equal button
        equals_button.bind(on_press=self.on_solution)  # bind on press for Equal Button
        main_layout.add_widget(equals_button)  # add Equal Button to window
        Window.size = (500, 650)  # size for window
        return main_layout

    def on_key(self, instance, value):  # bind on text input
        if len(value) <= 1 and not value.isdigit() and value != "-":  # first entered symbol is not num or "-"
            value = value[0:len(value) - 1]
        elif len(value) <= 1 and (value.isdigit() or value == "-"):  # first entered symbol is num or "-"
            self.solution.text = value
        elif value[len(value) - 1].isdigit() or value[len(value) - 1] == "+" \
                or value[len(value) - 1] == "-" or value[len(value) - 1] == "/" or value[len(value) - 1] == "*" \
                or value[len(value) - 1] == ".":  # entered symbol is digit or some of math symbols
            if len(value) > 1 and not value[len(value) - 1].isdigit() \
                    and not value[len(value) - 2].isdigit() and (not value[len(value) - 3].isdigit() or
                                                                 value[len(value) - 1] != "-"):
                value = value[0:len(value) - 1]  # for kinda "2*-1" enters check
        elif value[len(value) - 1] == "=":  # equals
            value = value[0:len(value) - 1]
            try:
                value = str(eval(value))
            except:
                value = "Error"
        else:
            value = value[0:len(value) - 1]
        self.solution.text = value  # value to TextInput

    def on_button_press(self, instance):  # bind for buttons
        if instance.text == "C":  # C-button
            self.solution.text = ""  # clear all
        else:  # other buttons (exceptions bind in on_key())
            self.solution.text += instance.text

    def on_solution(self, instance):  # bind for equal button
        if self.solution.text:  # equals
            try:
                self.solution.text = str(eval(self.solution.text))
            except:
                self.solution.text = "Error"


if __name__ == '__main__':  # main window run
    MainApp().run()
