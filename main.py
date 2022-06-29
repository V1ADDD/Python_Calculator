from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical", padding=3, spacing=3)
        self.solution = TextInput(multiline=False, readonly=False, halign="right", font_size=40)
        self.solution.focus = True
        self.solution.bind(text=self.on_key)
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(text="=", pos_hint={"center_x": 0.5, "center_y": 0.5})
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)
        Window.size = (500, 650)
        return main_layout

    def on_key(self, instance, value):
        if len(value) <= 1 and not value.isdigit() and value != "-":
            value = value[0:len(value) - 1]
        elif len(value) <= 1 and value.isdigit():
            self.solution.text = value
        elif len(value) <= 1 and value == "-":
            self.solution.text = value
        elif value[len(value) - 1].isdigit() or value[len(value) - 1] == "+" \
                or value[len(value) - 1] == "-" or value[len(value) - 1] == "/" \
                or value[len(value) - 1] == "*":
            if len(value) == 1:
                if not value.isdigit():
                    value = value[0:len(value) - 1]
            elif len(value) > 1 and not value[len(value) - 1].isdigit() \
                    and not value[len(value) - 2].isdigit() and (not value[len(value) - 3].isdigit() or
                                                                 value[len(value) - 1] != "-"):
                value = value[0:len(value) - 1]
        elif value[len(value) - 1] == "=":
            value = value[0:len(value) - 1]
            try:
                value = str(eval(value))
            except ArithmeticError:
                value = "Error"
        else:
            value = value[0:len(value) - 1]
        self.solution.text = value

    def on_button_press(self, instance):
        if instance.text == "C":
            self.solution.text = ""
        else:
            if len(self.solution.text) == 0:
                if instance.text.isdigit() or instance.text == "-":
                    self.solution.text += instance.text
            elif len(self.solution.text) > 0 and not self.solution.text[len(self.solution.text) - 1].isdigit() \
                    and not instance.text.isdigit() and instance.text != "-":
                self.solution.text += ""
            else:
                self.solution.text += instance.text

    def on_solution(self, instance):
        if self.solution.text:
            try:
                self.solution.text = str(eval(self.solution.text))
            except ArithmeticError:
                self.solution.text = "Error"


if __name__ == '__main__':
    MainApp().run()
