from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from deep_translator import GoogleTranslator

class TranslatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=20, **kwargs)

        self.add_widget(Label(
            text='Переводчик 3-в-1: Русский, Английский, Узбекский',
            size_hint=(1, 0.1),
            font_size='18sp',
            bold=True,
            color=[0, 0, 1, 1]
        ))

        self.input_field = TextInput(
            hint_text='Бирор нима ёзинг(рус ва лотин алифбосида)...',
            size_hint=(1, 0.15),
            font_size='16sp',
            multiline=False,
            write_tab=False,  # Важно для Android
            on_text_validate=lambda x: self.translate(None)  # Перевод по Enter
        )
        self.add_widget(self.input_field)

        button_layout = BoxLayout(size_hint=(1, 0.15), spacing=10)
        self.translate_button = Button(
            text='Таржима',
            background_color=(0, 0.5, 0.8, 1),
            font_size='14sp'
        )
        self.clear_button = Button(
            text='Тозалаш',
            background_color=(1, 0.4, 0.4, 1),
            font_size='14sp'
        )
        self.translate_button.bind(on_press=self.translate)
        self.clear_button.bind(on_press=self.clear)
        button_layout.add_widget(self.translate_button)
        button_layout.add_widget(self.clear_button)
        self.add_widget(button_layout)

        self.output_scroll = ScrollView(size_hint=(1, 0.6))
        self.output_label = Label(
            text='',
            font_size='16sp',
            halign='left',
            valign='top',
            markup=True,
            size_hint_y=None
        )
        self.output_label.bind(texture_size=self._update_label_height)
        self.output_scroll.add_widget(self.output_label)
        self.add_widget(self.output_scroll)

    def _update_label_height(self, *args):
        self.output_label.height = self.output_label.texture_size[1]
        self.output_label.text_size = (self.output_scroll.width - 20, None)

    def translate(self, instance):
        word = self.input_field.text.strip()
        if not word:
            self.output_label.text = "[color=ff0000]❗ Введите слово![/color]"
            return

        try:
            ru = GoogleTranslator(source='auto', target='ru').translate(word)
            en = GoogleTranslator(source='auto', target='en').translate(word)
            uz = GoogleTranslator(source='auto', target='uz').translate(word)
            result = (
                f"[b]Русский:[/b] {ru}\n\n"
                f"[b]Английский:[/b] {en}\n\n"
                f"[b]Узбекский:[/b] {uz}"
            )
            self.output_label.text = result
        except Exception as e:
            self.output_label.text = f"[color=ff0000]Ошибка перевода:[/color] {str(e)}"

    def clear(self, instance):
        self.input_field.text = ''
        self.output_label.text = ''


class TranslatorApp(App):
    def build(self):
        return TranslatorLayout()


if __name__ == '__main__':
    TranslatorApp().run()