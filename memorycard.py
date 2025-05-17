# Importamos las clases necesarias de PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QRadioButton,
    QPushButton, QLabel)

# Importamos funciones útiles de la biblioteca random
from random import randint, shuffle

# Definimos una clase para representar una pregunta
class Question():
    #Contiene una pregunta, una respuesta correcta y tres incorrectas

    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        # Inicializamos los atributos con los valores pasados
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

# Creamos una lista que contendrá las preguntas
questions_list = []
# Agregamos algunas preguntas con su respuesta correcta e incorrectas
questions_list.append(Question('¿El idioma oficial de Brasil', 'Portugués', 'Inglés', 'Español', 'Brasilero'))
questions_list.append(Question('¿Qué color no aparece en la bandera americana', 'Verde', 'Rojo', 'Blanco', 'Azul'))
questions_list.append(Question('¿Casa tradicional del pueblo Yakut', 'Yurta', 'Urasa', 'Igloo', 'Khata'))

# Creamos la aplicación de PyQt
app = QApplication([])

# Creamos el botón que usaremos para responder o pasar a la siguiente pregunta
btn_OK = QPushButton('Reply')  # Botón Responder

# Creamos la etiqueta que mostrará la pregunta
lb_Question = QLabel('¡La pregunta más difícil del mundo!')

# Creamos un grupo visual (GroupBox) para las opciones de respuesta
RadioGroupBox = QGroupBox("Opciones de respuesta")

# Creamos 4 botones de opción (radio buttons)
rbtn_1 = QRadioButton('Opción 1')
rbtn_2 = QRadioButton('Opción 2')
rbtn_3 = QRadioButton('Opción 3')
rbtn_4 = QRadioButton('Opción 4')

# Agrupamos los radio buttons para que solo uno se pueda seleccionar a la vez
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# Creamos layouts (disposición visual) para colocar los botones en columnas
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

# Agregamos los botones a las columnas
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

# Añadimos las columnas al layout horizontal
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

# Asignamos el layout con los botones al GroupBox
RadioGroupBox.setLayout(layout_ans1)

# Creamos el panel para mostrar los resultados
AnsGroupBox = QGroupBox("Resultados de la prueba")
lb_Result = QLabel('¿Estás en lo cierto o no')  # Mostrará si es correcto o incorrecto
lb_Correct = QLabel('¡La respuesta estará aquí!')  # Mostrará la respuesta correcta

# Layout del panel de resultados
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

# Layouts generales de la interfaz
layout_line1 = QHBoxLayout()  # Línea para la pregunta
layout_line2 = QHBoxLayout()  # Línea para las opciones o resultados
layout_line3 = QHBoxLayout()  # Línea para el botón

# Añadimos la pregunta al layout
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

# Añadimos los paneles de respuesta y resultado al layout
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()  # Ocultamos el panel de resultados al inicio

# Colocamos el botón en el centro
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

# Creamos el layout principal de la tarjeta
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)  # Espaciado entre elementos

# Función para mostrar el panel de resultado
def show_result():
    RadioGroupBox.hide()  # Ocultamos las opciones
    AnsGroupBox.show()  # Mostramos la respuesta correcta
    btn_OK.setText('Próxima pregunta')

# Función para mostrar el panel de pregunta
def show_question():
    RadioGroupBox.show()  # Mostramos opciones
    AnsGroupBox.hide()  # Ocultamos resultado
    btn_OK.setText('Respuesta')  # Cambiamos el texto del botón
    RadioGroup.setExclusive(False)  # Permitimos desmarcar botones
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)  # Restauramos exclusividad

# Lista de los botones de respuesta
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

# Función que carga una pregunta en la interfaz
def ask(q: Question):
    shuffle(answers)  # Mezclamos el orden de los botones
    answers[0].setText(q.right_answer)  # Colocamos la respuesta correcta en una posición aleatoria
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)  # Mostramos la pregunta
    lb_Correct.setText(q.right_answer)  # Guardamos la respuesta correcta para mostrar después
    show_question()  # Mostramos el panel de pregunta

# Función para mostrar si la respuesta fue correcta o no
def show_correct(res):
    lb_Result.setText(res)  # Mostramos el texto recibido
    show_result()  # Cambiamos al panel de resultado

# Función para verificar si la respuesta es correcta
def check_answer():
    #si se elige cualquier opcion de respuesta, tenemos que comprobar y mostrar el panel de respuesta
    if answers[0].isChecked():
        show_correct('¡Correcto!')
        window.score += 1  # Aumentamos puntuación
        print('Estadísticasn-Preguntas totales ', window.total, 'n-Preguntas correctas ', window.score)
        print('Calificación ', (window.score / window.total * 100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('¡Respuesta incorrecta!')
            print('Calificación ', (window.score / window.total * 100), '%')

# Función para mostrar una nueva pregunta
def next_question():
    window.total += 1  # Contamos una nueva pregunta
    print('Estadísticasn-Preguntas totales ', window.total, 'n-Preguntas correctas ', window.score)
    cur_question = randint(0, len(questions_list) - 1)  # Seleccionamos una pregunta al azar
    q = questions_list[cur_question]
    ask(q)  # Mostramos la pregunta

# Función que se llama cuando se hace clic en el botón
def click_OK():
    if btn_OK.text() == 'Respuesta':
        check_answer()  # Verificamos la respuesta
    else:
        next_question()  # Mostramos otra pregunta

# Creamos la ventana principal y le asignamos el layout
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Tarjeta de memoria')  # Título de la ventana

# Conectamos el botón con la función que decide qué hacer
btn_OK.clicked.connect(click_OK)

# Variables de estadísticas
window.score = 0  # Preguntas correctas
window.total = 0  # Total de preguntas respondidas

# Mostramos la primera pregunta
next_question()

# Ajustamos tamaño y mostramos la ventana
window.resize(400, 300)
window.show()

# Ejecutamos la aplicación
app.exec()