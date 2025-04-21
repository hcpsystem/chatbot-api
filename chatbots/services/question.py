from chatbots.models import Question
from users.models import User
from core.services.app import AppService


class QuestionService(AppService):
    def __init__(self):
        self.department_data = {
            'item': 0,
            'name': None,
            'description': None,
            'is_active': True,
        }

    def register(self):
        self.reset()
        settings = {'is_input': True, 'questions': ['11']}
        Question.objects.create(
            **{'id': 1, 'flow_id': '10', 'name': 'Chatbot XXX', 'settings': settings})
        Question.objects.create(
            **{'id': 2, 'flow_id': '10.1', 'parent_id': '10', 'settings': {'is_group': True},
               'name': '¡Hola! Soy Victoria, tu asistente virtual. Estoy aquí para ayudarte a '
                       'conocer más sobre el régimen laboral de las personas trabajadoras del '
                       'hogar 🤖.\n'
                       '📍 En el Perú, este régimen se encuentra regulado en la Ley N° 31047, '
                       'publicada el 01 de octubre de 2020. Además, contamos con un reglamento '
                       'aprobado por Decreto Supremo N° 009-2021-TR.\n'}
        )
        Question.objects.create(
            **{'id': 3, 'flow_id': '10.2', 'parent_id': '10', 'settings': {'is_group': True},
               'name': 'Ahora que ya me conoces, dime ¿Cuál es tu nombre? 👩👨.'}
        )

        settings = {'is_input': True, 'is_answer': True, 'questions': ['12']}
        Question.objects.create(
            **{'id': 4, 'flow_id': '11', 'name': 'Chatbot XXX', 'settings': settings})
        Question.objects.create(
            **{'id': 5, 'flow_id': '11.0', 'parent_id': '11', 'is_read': True, 'settings': {'is_group': True},
               'name': '¡Bienvenido/a, XXXXXX! Cuéntame, ¿en qué región de Perú te encuentras? ✍️\n'}

        )
        Question.objects.create(
            **{'id': 6, 'flow_id': '11.1', 'parent_id': '11', 'name': '1. Lima', 'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 7, 'flow_id': '11.2', 'parent_id': '11', 'name': '2. Lima Provincia',
               'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 8, 'flow_id': '11.3', 'parent_id': '11', 'name': '3. Lambayeque', 'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 9, 'flow_id': '11.4', 'parent_id': '11', 'name': '4. Arequipa', 'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 10, 'flow_id': '11.5', 'parent_id': '11', 'name': '5. Tumbes', 'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 11, 'flow_id': '11.6', 'parent_id': '11', 'name': '6. Pasco', 'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 12, 'flow_id': '11.7', 'parent_id': '11', 'name': '7. Huánuco', 'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 13, 'flow_id': '11.8', 'parent_id': '11', 'name': '8. La Libertad', 'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 14, 'flow_id': '11.9', 'parent_id': '11', 'name': '9. Junín', 'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 15, 'flow_id': '11.10', 'parent_id': '11', 'name': '10. Áncash', 'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 16, 'flow_id': '11.11', 'parent_id': '11', 'name': '11. Cajamarca', 'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 17, 'flow_id': '11.12', 'parent_id': '11', 'name': '12. Callao', 'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 18, 'flow_id': '11.13', 'parent_id': '11', 'name': '13. Ica', 'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 19, 'flow_id': '11.14', 'parent_id': '11', 'name': '14. San Martin',
               'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 20, 'flow_id': '11.15', 'parent_id': '11', 'name': '15. Huancavelica',
               'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 21, 'flow_id': '11.16', 'parent_id': '11', 'name': '16. Piura', 'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 22, 'flow_id': '11.17', 'parent_id': '11', 'name': '17. Tacna', 'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 23, 'flow_id': '11.18', 'parent_id': '11', 'name': '18. Puno', 'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 24, 'flow_id': '11.19', 'parent_id': '11', 'name': '19. Madre de Dios',
               'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 25, 'flow_id': '11.20', 'parent_id': '11', 'name': '20. Ucayali', 'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 26, 'flow_id': '11.21', 'parent_id': '11', 'name': '21. Ayacucho', 'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 27, 'flow_id': '11.22', 'parent_id': '11', 'name': '22. Apurímac', 'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 28, 'flow_id': '11.23', 'parent_id': '11', 'name': '23. Cusco', 'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 29, 'flow_id': '11.24', 'parent_id': '11', 'name': '24. Amazonas', 'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 30, 'flow_id': '11.25', 'parent_id': '11', 'name': '25. Moquegua', 'settings': {'is_group': True}}
        )
        Question.objects.create(
            **{'id': 31, 'flow_id': '11.26', 'parent_id': '11', 'name': '26. Loreto', 'settings': {'is_group': True}}
        )

        settings = {'is_input': True, 'is_answer': True, 'questions': [13]}
        Question.objects.create(
            **{'id': 32, 'flow_id': '12', 'name': 'Chatbot XXX', 'settings': settings})
        Question.objects.create(
            **{'id': 33, 'flow_id': '12.0', 'parent_id': '12', 'settings': {'is_group': True},
               'name': '☝ Señala el número del perfil con el que te identificas\n'}
        )
        ##
        Question.objects.create(
            **{'id': 34, 'flow_id': '12.1', 'parent_id': '12',
               'settings': {'is_input': True, 'is_answer': True, 'is_group': True, 'questions': ['12.1']},
               'name': '1. Soy una persona trabajadora del hogar 👨‍🏭👩‍🔧'}
        )
        Question.objects.create(
            **{'id': 35, 'flow_id': '12.1.1', 'parent_id': '12.1',
               'settings': {'is_input': True, 'is_answer': True, 'is_group': True, 'questions': ['12.1.1']},
               'name': '¿Qué edad tienes?'}
        )

        ##
        Question.objects.create(
            **{'id': 36, 'flow_id': '12.2', 'parent_id': '12',
               'settings': {'is_input': True, 'is_answer': True, 'is_group': True, 'questions': ['13']},
               'name': '2. Soy una persona empleadora en trabajo del hogar 👩‍💼👨‍💼'}
        )

        ##
        Question.objects.create(
            **{'id': 37, 'flow_id': '12.3', 'parent_id': '12',
               'settings': {'is_input': True, 'is_answer': True, 'is_group': True, 'questions': ['13']},
               'name': '3. Soy una persona interesada en el tema  🕵️‍♀️👮‍'}
        )

        Question.objects.create(
            **{'id': 38, 'flow_id': '13', 'name': 'Chatbot XXX', 'settings': settings})
        Question.objects.create(
            **{'id': 39, 'flow_id': '13.0', 'parent_id': '13', 'settings': {'is_group': True},
               'name': '📌 Estoy aquí para ayudarte. A continuación, te mostraré una lista de temas que podrían ser de '
                       'tu interés. Por favor, elige el número correspondiente a la opción que deseas consultar.\n'}
        )

        # Option main 1
        Question.objects.create(
            **{'id': 40, 'flow_id': '13.1', 'parent_id': '13', 'settings': self.setting({'questions': ['13.1']}),
               'name': '1. ¿A quiénes se considera personas trabajadoras del hogar? 👨‍🏭👩‍🔧'
               }
        )
        Question.objects.create(
            **{'id': 41, 'flow_id': '13.1.0', 'parent_id': '13.1', 'settings': {'is_group': True},
               'name': 'Por favor, elige el número correspondiente a la opción que deseas consultar.\n'}
        )
        Question.objects.create(
            **{'id': 42, 'flow_id': '13.1.1', 'parent_id': '13.1',
               'settings': self.setting({'questions': ['13.1.1']}),
               'name': '1. Persona trabajadora del hogar  👨‍🏭👩‍🔧'}
        )
        Question.objects.create(
            **{'id': 43, 'flow_id': '13.1.1.1', 'parent_id': '13.1.1',
               'settings': {'is_group': True, 'is_answer': False, 'is_reload': True, 'questions': ['13.1.1.1', '14']},
               'name': 'Se considera persona trabajadora del hogar a aquella persona mayor de edad (18 años) que '
                       'realiza tareas domésticas dentro de un domicilio particular.\n'
                       'Las tareas domésticas incluyen la limpieza, cocina, asistencia de cocina, lavado, planchado;'
                       ' así como tareas de cuidado de otras personas.'}
        )
        Question.objects.create(
            **{'id': 44, 'flow_id': '13.1.2', 'parent_id': '13.1', 'settings': self.setting({'questions': ['13.1.2']}),
               'name': '2. Edad mínima 👨‍💻'}
        )
        Question.objects.create(
            **{'id': 45, 'flow_id': '13.1.2.1', 'parent_id': '13.1.2',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.1.2.1', '14']},
               'name': 'La persona trabajadora del hogar debe tener como mínimo 18 años. En ningún caso se puede '
                       'contratar a menores de edad, pues el trabajo del hogar y de cuidados son '
                       'considerados trabajos peligrosos para los adolescentes.'}
        )

        # Option main 2
        Question.objects.create(
            **{'id': 46, 'flow_id': '13.2', 'parent_id': '13', 'settings': self.setting({'questions': ['13.2']}),
               'name': '2. Pasos para formalizar a una persona trabajadora del hogar 📋'}
        )
        Question.objects.create(
            **{'id': 47, 'flow_id': '13.2.1', 'parent_id': '13.2', 'settings': self.setting({'questions': ['13.2.1']}),
               'name': '1. Firma y contenido del contrato de trabajo 📋'}
        )
        Question.objects.create(
            **{'id': 48, 'flow_id': '13.2.1.1', 'parent_id': '13.2.1',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.2.1.1', '14']},
               'name': 'Todas las personas trabajadoras del hogar deben tener un contrato escrito donde se '
                       'detallen sus condiciones laborales y derechos conforme a la normativa. Debe incluir: \n'
                       '1.	Datos personales: nombres, edad, sexo, estado civil, profesión u oficio de ambas partes. \n'
                       '2.	Especificaciones del tipo de labores a realizar \n'
                       '3.	Lugar de trabajo: Lugar o lugares de prestación del trabajo (dirección o direcciones) \n'
                       '4.	Tiempo que la persona trabajadora del hogar ha laborado previamente a la firma del contrato \n'
                       '5.	Fecha de inicio del contrato y duración (en caso sea tiempo determinado) \n'
                       '6.	Remuneración \n'
                       '7.	Jornada y horario, incluyendo días de descanso semanal \n'
                       '8.	Implementos que se le brindará a la persona trabajadora para resguardar su seguridad y salud en el trabajo \n'
                       '9.	Información sobre el Seguro Social de Salud y el sistema de pensiones de elección de la persona trabajadora del hogar \n'
                       '10.	Condiciones de alimentos, uniforme o alojamiento cuando corresponda \n'
                       '11.	Nombre de la entidad financiera elegida, número de cuenta bancaria personal y/o código de cuenta interbancaria \n'
                       '12.	Obligaciones del empleador (gratificaciones, CTS, vacaciones). \n'
                       '13.	Facilidades para educación, si estudia.'}
        )
        Question.objects.create(
            **{'id': 49, 'flow_id': '13.2.2', 'parent_id': '13.2', 'settings': self.setting({'questions': ['13.2.2']}),
               'name': '2. Registro del contrato ante el Ministerio de Trabajo y\n'
                       '   Promoción del Empleo -MTPE'}
        )
        Question.objects.create(
            **{'id': 50, 'flow_id': '13.2.2.1', 'parent_id': '13.2.2',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.2.2.1', '14']},
               'name': 'Todos los contratos de personas trabajadoras del hogar deben ser registrados en la plataforma '
                       'web “Registro del trabajo del hogar”, del Ministerio de Trabajo y Promoción del Empleo (MTPE).\n'
                       'Quien contrata tiene 3 días hábiles desde la firma del contrato para registrar el contrato de '
                       'trabajo ante el MTPE, luego tendrá 03 días hábiles más para entregar a la persona trabajadora '
                       'una constancia de dicho registro.\n'
                       'Una vez concluido el vínculo, el empleador debe dar de baja el registro en el aplicativo.\n'
                       'Para ingresar al registro visita el siguiente enlace: https://apps.trabajo.gob.pe/rcth/app/#/inicio'}
        )

        Question.objects.create(
            **{'id': 51, 'flow_id': '13.2.3', 'parent_id': '13.2', 'settings': self.setting({'questions': ['13.2.3']}),
               'name': '3. Necesito ayuda para formalizar a mi trabajadora/r del\n'
                       '   hogar 👩‍🔧'}
        )
        Question.objects.create(
            **{'id': 52, 'flow_id': '13.2.3.1', 'parent_id': '13.2.3',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.2.3.1', '14']},
               'name': 'El Centro Integrado Formaliza Perú (CIFP), brinda acompañamiento para facilitar los '
                       'trámites de la formalización laboral de tu trabajadora/r del hogar.\n'
                       'Puedes visitarlo  en cualquiera de sus sedes, a nivel nacional. Para ver los teléfonos y '
                       'direcciones de las oficinas del CIFP ingresa al siguiente enlace:\n'
                       'https://portal.trabajo.gob.pe/formalizaperu/nosotros'}
        )

        # Option main 3
        Question.objects.create(
            **{'id': 53, 'flow_id': '13.3', 'parent_id': '13', 'settings': self.setting({'questions': ['13.3']}),
               'name': '3. Principales derechos de la persona trabajadora del hogar 👨‍💻'}
        )
        # Option main 3 - 1
        Question.objects.create(
            **{'id': 54, 'flow_id': '13.3.1', 'parent_id': '13.3', 'settings': self.setting({'questions': ['13.3.1']}),
               'name': '1. Remuneración por el trabajo del hogar 💲'}
        )
        Question.objects.create(
            **{'id': 55, 'flow_id': '13.3.1.1', 'parent_id': '13.3.1',
               'settings': self.setting({'questions': ['13.3.1.1']}),
               'name': '1. Remuneración por el trabajo del hogar'}
        )
        Question.objects.create(
            **{'id': 56, 'flow_id': '13.3.1.1.1', 'parent_id': '13.3.1.1',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.1.1.1', '14']},
               'name': 'El monto de la remuneración de la persona trabajadora del hogar será establecido por acuerdo '
                       'libre entre empleador y la persona trabajadora del hogar, pero no podrá ser inferior a la '
                       'remuneración mínima vital (RMV), para las personas trabajadoras a tiempo completo, esto es '
                       'quienes laboran a partir de 24 horas semanales.\n'
                       'La remuneración de la persona trabajadora del hogar puede pagarse en forma semanal, quincenal '
                       'o mensual, según acuerdo.'}
        )
        Question.objects.create(
            **{'id': 57, 'flow_id': '13.3.1.2', 'parent_id': '13.3.1',
               'settings': self.setting({'questions': ['13.3.1.2']}),
               'name': '2. Remuneración por trabajo del hogar a tiempo parcial'}
        )
        Question.objects.create(
            **{'id': 58, 'flow_id': '13.3.1.2.1', 'parent_id': '13.3.1.2',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.1.2.1', '14']},
               'name': 'Si la persona trabajadora del hogar labora una jornada de trabajo inferior a 4 horas diarias '
                       'en promedio a la semana, la remuneración mensual podrá ser acordada en función de la cantidad '
                       'de horas trabajadas, usando como parámetro el valor de la RMV como mínimo.\n'
                       'La remuneración de la persona trabajadora del hogar puede pagarse en forma semanal, '
                       'quincenal o mensual, según acuerdo'}
        )
        Question.objects.create(
            **{'id': 59, 'flow_id': '13.3.1.3', 'parent_id': '13.3.1',
               'settings': self.setting({'questions': ['13.3.1.3']}),
               'name': '3. Conceptos que no forman parte de la remuneración'}
        )
        Question.objects.create(
            **{'id': 60, 'flow_id': '13.3.1.3.1', 'parent_id': '13.3.1.3',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.1.3.1', '14']},
               'name': 'Las condiciones de alojamiento, alimentación, entrega de uniformes, equipos de protección, '
                       'instrumentos o herramientas para la prestación del trabajo, así como los implementos de '
                       'bioseguridad y artículos de desinfección no son parte de la remuneración, por lo que bajo '
                       'ningún motivo se pueden descontar estos conceptos o contabilizarlos como '
                       'parte de la remuneración.'}
        )

        # Option main 3 - 2
        Question.objects.create(
            **{'id': 61, 'flow_id': '13.3.2', 'parent_id': '13.3',
               'settings': self.setting({'questions': ['13.3.2']}),
               'name': '2. Condiciones de trabajo en el trabajo del hogar 👨‍🚒'}
        )
        Question.objects.create(
            **{'id': 62, 'flow_id': '13.3.2.1', 'parent_id': '13.3.2',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.2.1', '14']},
               'name': 'En caso la modalidad de trabajo incluya residencia, la persona que emplea está obligada a '
                       'proporcionar alimentación'
                       'completa (desayuno, almuerzo y cena) y un alojamiento adecuado al nivel socioeconómico'
                       'de la persona trabajadora del hogar.\n'
                       'Asimismo, las condiciones laborales deben garantizar la dignidad de la persona trabajadora y '
                       'el cumplimiento de las normas de seguridad y salud en el trabajo. Esto incluye la entrega de '
                       'equipos de protección,'
                       'instrumentos y herramientas necesarios para la prestación del servicio.'}
        )
        # Option main 3 - 3
        Question.objects.create(
            **{'id': 63, 'flow_id': '13.3.3', 'parent_id': '13.3',
               'settings': self.setting({'questions': ['13.3.3']}),
               'name': '3. Jornada, descanso semanal y feriados  ⌛'}
        )
        Question.objects.create(
            **{'id': 64, 'flow_id': '13.3.3.1', 'parent_id': '13.3.3',
               'settings': self.setting({'questions': ['13.3.3.1']}),
               'name': '1. Jornada laboral del trabajo del hogar'}
        )
        Question.objects.create(
            **{'id': 65, 'flow_id': '13.3.3.1.1', 'parent_id': '13.3.3.1',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.3.1.1', '14']},
               'name': 'La persona trabajadora del hogar no debe trabajar más de 8 horas diarias, '
                       'ni más de 48 horas semanales. '}
        )
        Question.objects.create(
            **{'id': 66, 'flow_id': '13.3.3.2', 'parent_id': '13.3.3',
               'settings': self.setting({'questions': ['13.3.3.2']}),
               'name': '2. Descanso semanal de trabajo de la persona trabajadora del hogar'}
        )
        Question.objects.create(
            **{'id': 67, 'flow_id': '13.3.3.2.1', 'parent_id': '13.3.3.2',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.3.2.1', '14']},
               'name': 'La persona trabajadora del hogar debe contar con un periodo de descanso de 24 horas '
                       'continuas a la semana como mínimo.\n'
                       'En el caso de trabajo con residencia en el hogar (antes llamado “cama adentro”), la '
                       'persona trabajadora tiene derecho a contar con 12 horas continuas de descanso, entre el '
                       'término de una jornada y el inicio de la siguiente.'}
        )
        Question.objects.create(
            **{'id': 68, 'flow_id': '13.3.3.3', 'parent_id': '13.3.3',
               'settings': self.setting({'questions': ['13.3.3.3']}),
               'name': '3. Horas extras de trabajo de la persona trabajadora del hogar'}
        )
        Question.objects.create(
            **{'id': 69, 'flow_id': '13.3.3.3.1', 'parent_id': '13.3.3.3',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.3.3.1', '14']},
               'name': 'La persona trabajadora del hogar puede realizar horas extras a la jornada de trabajo de '
                       'manera voluntaria, previo acuerdo con quien la emplea y con un pago adicional.\n'
                       'Las horas extras se pagarán sobre el valor de una hora habitual más una sobretasa del '
                       '25 % por las dos primeras horas y posteriormente una sobretasa no menor al 35%.'}
        )

        Question.objects.create(
            **{'id': 70, 'flow_id': '13.3.3.4', 'parent_id': '13.3.3',
               'settings': self.setting({'questions': ['13.3.3.4']}),
               'name': '4. ¿Cuáles son los feriados que deben gozar las personas trabajadoras del hogar? '}
        )
        Question.objects.create(
            **{'id': 71, 'flow_id': '13.3.3.4.1', 'parent_id': '13.3.3.4',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.3.4.1', '14']},
               'name': 'La persona trabajadora del hogar tiene derecho a los mismos feriados que cualquier persona '
                       'trabajadora del sector privado. Estos son:\n'
                       '\n'
                       '●	Año Nuevo (1 de enero)\n'
                       '●	Jueves Santo y Viernes Santo (movibles)\n'
                       '●	Día del Trabajo (1 de mayo)\n'
                       '●	Batalla de Arica y Día de la Bandera (7 de junio)\n'
                       '●	San Pedro y San Pablo (29 de junio)\n'
                       '●	Conmemoración al heroico sacrificio del Capitán FAP José \n'
                       '    Abelardo Quiñones Gonzales (23 de julio)\n'
                       '●	Fiestas Patrias (28 y 29 de julio)\n'
                       '●	Batalla de Junín (6 de agosto)\n'
                       '●	Santa Rosa de Lima (30 de agosto)\n'
                       '●	Combate de Angamos (8 de octubre)\n'
                       '●	Todos los Santos (1 de noviembre)\n'
                       '●	Inmaculada Concepción (8 de diciembre)\n'
                       '●	Batalla de Ayacucho (9 de diciembre)\n'
                       '●	Navidad del Señor (25 de diciembre)\n'
                       '\n'
                       'Asimismo, cuentan con un feriado propio en el Día de las Trabajadoras y '
                       'Trabajadores del Hogar (30 de marzo).'}
        )
        Question.objects.create(
            **{'id': 72, 'flow_id': '13.3.3.5', 'parent_id': '13.3.3',
               'settings': self.setting({'questions': ['13.3.3.5']}),
               'name': '5. ¿Qué pasa si se trabaja en un feriado?'}
        )
        Question.objects.create(
            **{'id': 73, 'flow_id': '13.3.3.5.1', 'parent_id': '13.3.3.5',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.3.5.1', '14']},
               'name': 'Si la persona trabajadora accede, de manera voluntaria y por mutuo acuerdo, a trabajar '
                       'durante un feriado, se le debe pagar una sobretasa del 100 %; es decir, doble remuneración.\n'
                       'Ten en cuenta que para las personas trabajadoras del hogar que presten servicios con '
                       'residencia en el domicilio (cama adentro), los periodos durante los cuales no disponen '
                       'libremente de su tiempo y permanecen a disposición del hogar, son considerados  como '
                       'horas de trabajo y deben ser remuneradas.'}
        )
        # Option main 3 - 4
        Question.objects.create(
            **{'id': 74, 'flow_id': '13.3.4', 'parent_id': '13.3',
               'settings': self.setting({'questions': ['13.3.4']}),
               'name': '4. Vacaciones 🕓'}
        )
        Question.objects.create(
            **{'id': 75, 'flow_id': '13.3.4.1', 'parent_id': '13.3.4',
               'settings': self.setting({'questions': ['13.3.4.1']}),
               'name': '1. Vacaciones de la persona trabajadora del hogar a tiempo completo'}
        )
        Question.objects.create(
            **{'id': 76, 'flow_id': '13.3.4.1.1', 'parent_id': '13.3.4.1',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.4.1.1', '14']},
               'name': 'Si la persona trabajadora del hogar tiene una jornada de, al menos, 4 horas diarias en '
                       'promedio a la semana, y tiene más de un año laborando (desde que empezó a trabajar), '
                       'tiene derecho a 30 días de vacaciones remuneradas anuales que deben ser gozadas dentro del '
                       'periodo anual siguiente a aquel en que adquirió dicho derecho.\n'
                       'Dicho descanso no podrá ser otorgado cuando la trabajadora se encuentra incapacitada por '
                       'alguna enfermedad o accidente, pues en esos casos corresponde aplicar licencias o '
                       'contabilizar los días de inasistencia como faltas justificadas\n'
                       '\n'
                       'Ejemplo:\n'
                       'Ana empezó a trabajar el 14 de abril de 2022. Cumplió un año de servicios el '
                       '13 de abril de 2023 y, en ese momento, adquirió el derecho al descanso vacacional '
                       'correspondiente al primer año de trabajo, que podrá gozar a partir del 14 de abril de 2023.'}
        )
        Question.objects.create(
            **{'id': 77, 'flow_id': '13.3.4.2', 'parent_id': '13.3.4',
               'settings': self.setting({'questions': ['13.3.4.2']}),
               'name': '2. Fechas para tomar vacaciones'}
        )
        Question.objects.create(
            **{'id': 78, 'flow_id': '13.3.4.2.1', 'parent_id': '13.3.4.2',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.4.2.1', '14']},
               'name': 'Las fechas del descanso vacacional deben ser fijadas de común acuerdo entre la persona '
                       'empleadora y la persona trabajadora. En ausencia de un acuerdo claro, la persona empleadora '
                       'tiene la libertad de tomar decisiones según su propio juicio y dirección.\n'
                       '\n'
                       'Al término del vínculo laboral, en caso de que la persona trabajadora no haya gozado por '
                       'completo el descanso vacacional, o que solo se haya tomado una parte, el empleador deberá '
                       'pagar el equivalente a los días no gozados. En caso de no cumplir con el año completo de trabajo, '
                       'deberá recibir un pago proporcional a los meses y días que hubiera laborado.\n'
                       '\n'
                       'Las vacaciones se cuentan en días calendario, esto incluye sábados, domingos y feriados.'}
        )
        Question.objects.create(
            **{'id': 79, 'flow_id': '13.3.4.3', 'parent_id': '13.3.4',
               'settings': self.setting({'questions': ['13.3.4.3']}),
               'name': '3. Vacaciones de la persona trabajadora del hogar a tiempo parcial'}
        )
        Question.objects.create(
            **{'id': 80, 'flow_id': '13.3.4.3.1', 'parent_id': '13.3.4.3',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.4.3.1', '14']},
               'name': 'En caso de que la persona trabajadora del hogar labore menos de 4 horas diarias '
                       '(en promedio a la semana) y haya cumplido un año de trabajo, tiene derecho a, por lo menos, '
                       '6 días de vacaciones anuales (en aplicación del Convenio núm. 52 de la OIT).'}
        )
        # Option main 3 - 5
        Question.objects.create(
            **{'id': 81, 'flow_id': '13.3.5', 'parent_id': '13.3',
               'settings': self.setting({'questions': ['13.3.5']}),
               'name': '5. Gratificación de la persona trabajadora del hogar 🏡'}
        )
        Question.objects.create(
            **{'id': 82, 'flow_id': '13.3.5.1', 'parent_id': '13.3.5',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.5.1', '14']},
               'name': 'Independientemente de las horas que la persona trabajadora labore, le corresponde una '
                       'gratificación por Fiestas Patrias y una gratificación por Navidad. Cada una equivale a '
                       'una remuneración mensual en cada oportunidad (de acuerdo con la remuneración estipulada '
                       'en su contrato), y se calcula en función de los meses calendario completos laborados '
                       'dentro del semestre correspondiente.\n'
                       'Recuerda que la gratificación por Fiestas Patrias debe '
                       'pagarse en la primera quincena de julio y la gratificación por Navidad en la primera quincena '
                       'de diciembre.\n'
                       'En el siguiente enlace puede acceder a Calcula tu Grati, un aplicativo de SUNAFIL, '
                       'que te ayudará a realizar el cálculo:\n'
                       'https://aplicativosweb6.sunafil.gob.pe/si.calculadoraLaboral'}
        )
        # Option main 3 - 6
        Question.objects.create(
            **{'id': 83, 'flow_id': '13.3.6', 'parent_id': '13.3',
               'settings': self.setting({'questions': ['13.3.6']}),
               'name': '6. Compensación por Tiempo de Servicios - CTS 💰'}
        )
        Question.objects.create(
            **{'id': 84, 'flow_id': '13.3.6.1', 'parent_id': '13.3.6',
               'settings': self.setting({'questions': ['13.3.6.1']}),
               'name': '1. ¿Cuándo las personas trabajadoras del hogar reciben la CTS y cuál es la forma de entrega?'}
        )
        Question.objects.create(
            **{'id': 85, 'flow_id': '13.3.6.1.1', 'parent_id': '13.3.6.1',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.6.1.1', '14']},
               'name': 'Si la persona trabajadora del hogar labora al menos 4 horas diarias en promedio a la semana '
                       'y además ha acumulado, como mínimo, un mes de labores, tiene derecho a recibir la CTS, la '
                       'cual tiene como propósito la prevención de contingencias a consecuencia del término del '
                       'vínculo laboral, sin importar la causa.\n'
                       'La persona empleadora deposita la CTS de la persona trabajadora del hogar, en una cuenta '
                       'bancaria abierta para tal fin dentro de los primeros quince (15) días naturales de los '
                       'meses de mayo y noviembre de cada año. Si el último día es inhábil, el depósito puede '
                       'efectuarse el primer día hábil siguiente. Efectuado el depósito queda cumplida y pagada '
                       'la obligación de la persona empleadora del hogar.\n'
                       'Ten en cuenta que este monto no se descuenta de la remuneración que se le otorga a la '
                       'persona trabajadora.\n'
                       'Si la persona trabajadora del hogar cesa, pero hubiera laborado como mínimo un (01) mes '
                       'completo dentro del semestre correspondiente, la persona empleadora del hogar debe '
                       'pagar la CTS trunca directamente, dentro de las cuarenta y ocho (48) horas de '
                       'producido el cese.'}
        )
        Question.objects.create(
            **{'id': 86, 'flow_id': '13.3.6.2', 'parent_id': '13.3.6',
               'settings': self.setting({'questions': ['13.3.6.2']}),
               'name': '2. Información que debe entregar la persona trabajadora para recibir la CTS'}
        )
        Question.objects.create(
            **{'id': 87, 'flow_id': '13.3.6.2.1', 'parent_id': '13.3.6.2',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.6.2.1', '14']},
               'name': 'La persona trabajadora del hogar debe comunicar a su empleador el nombre de la entidad '
                       'financiera elegida para el depósito de la CTS, el número de cuenta, de CCI y el tipo '
                       'de moneda.\n'
                       'Si la persona trabajadora del hogar no brinda dicha información, quien la emplea deposita'
                       ' la CTS en cualquiera de las instituciones del sistema financiero, bajo la modalidad '
                       'de depósito a plazo fijo por el periodo más largo permitido.'}
        )
        Question.objects.create(
            **{'id': 88, 'flow_id': '13.3.6.3', 'parent_id': '13.3.6',
               'settings': self.setting({'questions': ['13.3.6.3']}),
               'name': '3. ¿Cómo se calcula la CTS?'}
        )
        Question.objects.create(
            **{'id': 89, 'flow_id': '13.3.6.3.1', 'parent_id': '13.3.6.3',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.6.3.1', '14']},
               'name': 'Como primer paso se debe calcular la remuneración computable, la cual comprende '
                       'la suma de los siguientes montos:\n'
                       '-	Remuneración básica\n'
                       '-	1/6 de la gratificación percibida en el semestre\n'
                       'Como segundo paso debes dividir la remuneración computable entre 12 y multiplicarlos '
                       'por los meses laborados completos en el semestre. En caso quieras calcularlo por días, '
                       'la remuneración computable la divides entre 360 y la multiplicas por los días laborados '
                       'en el semestre.\n'
                       'En el siguiente enlace puede acceder a Calcula tu CTS, un aplicativo de SUNAFIL, '
                       'que te ayudará a realizar el cálculo:\n'
                       'https://aplicativosweb6.sunafil.gob.pe/si.calculadoraLaboral/identificacionTrabajadorEmpresa'}
        )
        Question.objects.create(
            **{'id': 90, 'flow_id': '13.3.6.4', 'parent_id': '13.3.6',
               'settings': self.setting({'questions': ['13.3.6.4']}),
               'name': '4. ¿Cuáles son los periodos de trabajo computables y fecha de depósito?'}
        )
        Question.objects.create(
            **{'id': 91, 'flow_id': '13.3.6.4.1', 'parent_id': '13.3.6.4',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.6.4.1', '14']},
               'name': 'Periodos de trabajo computable:\n'
                       'Noviembre – abril. El depósito de este periodo se realiza la primera quincena de mayo.\n'
                       'Mayo - octubre. El depósito de este periodo se realiza la primera quincena de noviembre.'}
        )

        # Option main 3 - 7
        Question.objects.create(
            **{'id': 92, 'flow_id': '13.3.7', 'parent_id': '13.3',
               'settings': self.setting({'questions': ['13.3.7']}),
               'name': '7. Acceso a la seguridad social en salud- Essalud 🏥'}
        )
        Question.objects.create(
            **{'id': 93, 'flow_id': '13.3.7.1', 'parent_id': '13.3.7',
               'settings': self.setting({'questions': ['13.3.7.1']}),
               'name': '1. Afiliación y pago a EsSalud: ¿Cómo realizar el pago?'}
        )
        Question.objects.create(
            **{'id': 94, 'flow_id': '13.3.7.1.1', 'parent_id': '13.3.7.1',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.7.1.1', '14']},
               'name': 'Toda persona trabajadora del hogar tiene derecho a ser afiliada al Seguro Social de Salud (EsSalud). '
                       'Para ello, la persona empleadora debe realizar un pago equivalente '
                       'al 9% de la remuneración de la persona trabajadora del hogar. '
                       'Quien emplea asume el pago, en ningún caso deberá ser descontado de la remuneración de la persona '
                       'trabajadora del hogar.\n'
                       '\n'
                       '¿Cómo realizar el pago?\n'
                       'El primer paso para realizar el pago es registrar a la persona trabajadora del hogar en el '
                       'siguiente enlace:\n'
                       'Una vez que hayas registrado a la persona trabajadora del hogar en el Registro del MTPE, '
                       'puedes realizar los pagos a través de la página de SUNAT o a través de agencias bancarias '
                       'autorizadas a nivel nacional.\n'
                       'Para mayor información ingresa al siguiente enlace: '
                       'https://www.gob.pe/8076-declarar-y-pagar-aportes-de-trabajadores-del-hogar'
               }
        )
        Question.objects.create(
            **{'id': 95, 'flow_id': '13.3.7.2', 'parent_id': '13.3.7',
               'settings': self.setting({'questions': ['13.3.7.2']}),
               'name': '2. Beneficios de la afiliación a Essalud para la persona trabajadora del hogar'}
        )
        Question.objects.create(
            **{'id': 96, 'flow_id': '13.3.7.2.1', 'parent_id': '13.3.7.2',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.7.2.1', '14']},
               'name': 'La afiliación a EsSalud permite que la persona trabajadora del hogar y sus familiares '
                       'registrados como derechohabientes, accedan a diversos servicios de salud. '
                       'Incluso, según corresponda, a través de su afiliación el trabajador podrá percibir '
                       'un subsidio por maternidad, lactancia, sepelio e incapacidad temporal.\n'
                       'Las personas derechohabientes son: cónyuge o concubina(o), hija o hijo menor de edad '
                       'hasta que cumpla 18 años (salvo que vivan con una condición de incapacidad permanente), '
                       'y madre de hija o hijo concebido.'}
        )
        Question.objects.create(
            **{'id': 97, 'flow_id': '13.3.7.3', 'parent_id': '13.3.7',
               'settings': self.setting({'questions': ['13.3.7.3']}),
               'name': '3. Beneficios de la afiliación a Essalud para la persona empleadora del hogar'}
        )
        Question.objects.create(
            **{'id': 98, 'flow_id': '13.3.7.3.1', 'parent_id': '13.3.7.3',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.7.3.1', '14']},
               'name': 'Si eres persona empleadora y tus ingresos anuales superan las 7 UIT, puedes deducir de tu '
                       'Impuesto a la Renta, como gasto, las aportaciones al Seguro Social de Salud ESSALUD que '
                       'realices a favor de la persona trabajadora del hogar.'}
        )
        # Option main 3 - 8
        Question.objects.create(
            **{'id': 99, 'flow_id': '13.3.8', 'parent_id': '13.3',
               'settings': self.setting({'questions': ['13.3.8']}),
               'name': '8. Pensión para las personas trabajadoras del hogar ✍'}
        )
        Question.objects.create(
            **{'id': 100, 'flow_id': '13.3.8.1', 'parent_id': '13.3.8',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.8.1', '14']},
               'name': 'Toda persona trabajadora del hogar debe aportar a un sistema de pensiones público o privado '
                       '(ONP o AFP), para acceder a una pensión (jubilación).\n'
                       'Este aporte es retenido y descontado de la remuneración de la persona  trabajadora y el monto '
                       'puede variar entre 10 % y 13% de la remuneración, de acuerdo con el sistema de pensiones '
                       'que elija la persona trabajadora del hogar.\n'
                       '\n'
                       'Para realizar el pago de ONP, ingresa al siguiente enlace: https://www.gob.pe/8076-declarar-y-pagar-aportes-de-trabajadores-del-hogar'
               }
        )
        # Option main 3 - 9
        Question.objects.create(
            **{'id': 101, 'flow_id': '13.3.9', 'parent_id': '13.3',
               'settings': self.setting({'questions': ['13.3.9']}),
               'name': '9. Actos discriminatorios ⚠'}
        )
        Question.objects.create(
            **{'id': 102, 'flow_id': '13.3.9.1', 'parent_id': '13.3.9',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.9.1', '14']},
               'name': 'Se encuentra prohibida toda forma de discriminación contra la persona trabajadora del hogar '
                       'por motivo de origen, raza, sexo, idioma, religión, opinión, condición económica, u otros; '
                       'así como cualquier tratamiento o expresión que afecte tu dignidad como persona.\n'
                       'Ejemplo:\n'
                       '• Es discriminación obligar a usar uniformes, mandiles, delantales o cualquier otra '
                       'vestimenta o distintivo identificatorio en espacios o establecimientos públicos como '
                       'parques, plazas, playas, restaurantes, hoteles, locales comerciales, clubes sociales y '
                       'otros similares.\n'
                       '• Es discriminación obligar o establecer como condición que la persona trabajadora del '
                       'hogar realice actos contrarios a los valores y prácticas sociales, culturales, religiosos y '
                       'espirituales de su lugar de origen.'}
        )
        # Option main 3 - 10
        Question.objects.create(
            **{'id': 103, 'flow_id': '13.3.10', 'parent_id': '13.3',
               'settings': self.setting({'questions': ['13.3.10']}),
               'name': '10. Protección de la maternidad 📌'}
        )
        Question.objects.create(
            **{'id': 104, 'flow_id': '13.3.10.1', 'parent_id': '13.3.10',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.10.1', '14']},
               'name': 'Las trabajadoras del hogar tienen derecho a la protección durante su embarazo y periodo de '
                       'lactancia, por lo que no puede ser despedida por su embarazo, parto o lactancia.\n'
                       'Si se produce el despido en cualquier momento durante el embarazo o dentro de los 90 días '
                       'posteriores al nacimiento, ese despido es inválido y no tiene efecto legal.\n'
                       'Recuerda que el pago del subsidio por maternidad y lactancia es pagado directamente por EsSalud.'}
        )
        # Option main 3 - 11
        Question.objects.create(
            **{'id': 105, 'flow_id': '13.3.11', 'parent_id': '13.3',
               'settings': self.setting({'questions': ['13.3.11']}),
               'name': '11. Hostigamiento sexual 🚨'}
        )
        Question.objects.create(
            **{'id': 106, 'flow_id': '13.3.11.1', 'parent_id': '13.3.11',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.11.1', '14']},
               'name': 'La persona empleadora tiene la obligación de garantizar un espacio libre de hostigamiento '
                       'sexual y de todo tipo de violencia.\n'
                       'Para tal efecto, como parte de las medidas de prevención, quien emplea puede facilitar el acceso '
                       'a la “Guía de prevención ante el hostigamiento sexual laboral en el trabajo del hogar” a través del siguiente enlace:\n'
                       'https://cdn.www.gob.pe/uploads/document/file/3810604/Gu%C3%ADa%20prevenci%C3%B3n%20hostigamiento%20-%20Trabajadores%20del%20Hogar%20.pdf?v=1667574592 \n'
                       'Asimismo, puedes acceder a un curso sobre el tema en este enlace: '
                       'https://capacitacionlaboral.trabajo.gob.pe/cursos/prevencion-y-reporte-del-hostigamiento-sexual-laboral/  CAPACÍTA-T(trabajo.gob.pe)'
               })
        # Option main 3 - 12
        Question.objects.create(
            **{'id': 107, 'flow_id': '13.3.12', 'parent_id': '13.3',
               'settings': self.setting({'questions': ['13.3.12']}),
               'name': '12. Seguridad y Salud en el Trabajo 👨🏻‍⚕️'}
        )
        Question.objects.create(
            **{'id': 108, 'flow_id': '13.3.12.1', 'parent_id': '13.3.12',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.12.1', '14']},
               'name': 'Las personas trabajadoras del hogar tienen derecho a desarrollar su trabajo en condiciones '
                       'libres de cualquier tipo de riesgo.  Por ello, el empleador debe establecer medidas y '
                       'brindar medios para que las tareas o actividades se realicen en '
                       'condiciones seguras y saludables.\n'
                       'Asimismo, el empleador debe asumir las implicancias '
                       'económicas, legales y de cualquier otra índole a consecuencia de un accidente o enfermedad '
                       'que sufra la persona trabajadora del hogar en el desempeño de sus funciones o como '
                       'consecuencia de este.\n'
                       'El empleador debe garantizar como mínimo la asistencia a una capacitación en materia de riesgos '
                       'asociados al desarrollo de sus labores.\n'
                       'Puedes acceder cursos sobre este y otros temas en '
                       'el portal CAPACÍTA-T (trabajo.gob.pe) '
               }
        )

        # Option main 3 - 13
        Question.objects.create(
            **{'id': 109, 'flow_id': '13.3.13', 'parent_id': '13.3',
               'settings': self.setting({'questions': ['13.3.13']}),
               'name': '13. Calcular tus beneficios sociales'}
        )
        Question.objects.create(
            **{'id': 110, 'flow_id': '13.3.13.1', 'parent_id': '13.3.13',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.13.1', '14']},
               'name': ' Para calcular tus beneficios sociales accede a este '
                       ' link:\n https://portal.trabajo.gob.pe/calculadoraMTPE'}
        )

        # Option main 4
        Question.objects.create(
            **{'id': 111, 'flow_id': '13.4', 'parent_id': '13',
               'settings': self.setting({'questions': ['13.4']}),
               'name': '4. Agencias de empleo 🏠 '}
        )
        Question.objects.create(
            **{'id': 112, 'flow_id': '13.4.1', 'parent_id': '13.4',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.4.1', '14']},
               'name': 'Las agencias de empleo son empresas privadas cuyo objetivo radica en intermediar para la contratación de personas '
                       'trabajadoras del hogar, a cambio de un pago realizado por el empleador. '
                       'Estas tienen las siguientes prohibiciones:\n'
                       '● Cobrar o afectar la remuneración del trabajador/a para cobrar cualquier tipo '
                       'gasto realizado por la colocación del trabajador/a en un empleo.\n'
                       '● Retener el documento de identidad, objetos personales, de valor, '
                       'antecedentes penales, cartas de recomendación, o similares.'}
        )
        # Option main 5
        Question.objects.create(
            **{'id': 113, 'flow_id': '13.5', 'parent_id': '13',
               'settings': self.setting({'questions': ['13.5']}),
               'name': '5. Inspección del trabajo 👨‍🚒'}
        )
        # Option main 5 - 1
        Question.objects.create(
            **{'id': 114, 'flow_id': '13.5.1', 'parent_id': '13.5',
               'settings': self.setting({'questions': ['13.5.1']}),
               'name': '1. El rol de SUNAFIL'}
        )
        Question.objects.create(
            **{'id': 115, 'flow_id': '13.5.1.1', 'parent_id': '13.5.1',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.5.1.1', '14']},
               'name': 'La Superintendencia de Fiscalización Laboral - SUNAFIL, es la entidad encargada de '
                       'vigilar y exigir el cumplimiento de las obligaciones sociolaborales y de seguridad'
                       ' y salud en el trabajo.'}
        )
        # Option main 5 - 2
        Question.objects.create(
            **{'id': 116, 'flow_id': '13.5.2', 'parent_id': '13.5',
               'settings': self.setting({'questions': ['13.5.2']}),
               'name': '2. Soy trabajadora del hogar ¿Puedo recurrir a SUNAFIL si me despiden?'}
        )
        Question.objects.create(
            **{'id': 117, 'flow_id': '13.5.2.1', 'parent_id': '13.5.2',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.5.2.1', '14']},
               'name': 'Si te han despedido de tu trabajo y crees que ha sido injusto, puedes acudir a SUNAFIL para que revisen tu caso. \n '
                       'Luego de la verificación, te entregarán un “Acta de Verificación de Despido Arbitrario”, \n'
                       'que te servirá como prueba si decides presentar una demanda para solicitar una indemnización.\n'
                       '\n'
                       'Es importante que sepas que SUNAFIL no puede ordenar que te repongan en tu trabajo '
                       'ni exigir el pago de una indemnización por despido arbitrario. Sin embargo, '
                       'sí puede exigir que te paguen los beneficios laborales que te adeuden.\n'
                       '\n'
                       '📞 Si necesitas comunicarte con SUNAFIL, puedes llamar al (01) 3902800.'}
        )
        # Option main 5 - 3
        Question.objects.create(
            **{'id': 118, 'flow_id': '13.5.3', 'parent_id': '13.5',
               'settings': self.setting({'questions': ['13.5.3']}),
               'name': '3. Presentación de denuncia'}
        )
        Question.objects.create(
            **{'id': 119, 'flow_id': '13.5.3.1', 'parent_id': '13.5.3',
               'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.5.3.1', '14']},
               'name': 'La persona trabajadora del hogar cuenta con diversos canales para presentar una denuncia:\n'
                       '● La plataforma  “Denuncia Virtual” de SUNAFIL: https://aplicativosweb2.sunafil.gob.pe/si.denunciasVirtuales\n'
                       '● El aplicativo “SUNAFIL en tus manos”, disponible para celulares Android: https://play.google.com/store/apps/details?id=pe.gob.sunafil.sunafilentusmanos\n'
                       '● La Mesa de partes presencial en nuestras diversas Intendencias Regionales y Sede Central.\n'
                       'Para conocer nuestras sedes y teléfonos, ingresa al siguiente enlace: https://www.gob.pe/institucion/sunafil/sedes'}
        )

        # Option de salida
        Question.objects.create(
            **{'id': 120, 'flow_id': '14', 'name': 'Chatbot XXX',
               'settings': self.setting({'questions': ['14']})})
        Question.objects.create(
            **{'id': 121, 'flow_id': '14.0', 'parent_id': '14',
               'settings': self.setting({'questions': ['14.0']}),
               'name': '👋🏼 Sigo aquí para ayudarte 😊Digita el número de la opción que desees:'}
        )
        # Option main 14 - 1
        Question.objects.create(
            **{'id': 122, 'flow_id': '14.1', 'parent_id': '14',
               'settings': self.setting({'questions': ['13']}),
               'name': '1. Tengo otra consulta. ✍'}
        )
        # Option main 14 - 2
        Question.objects.create(
            **{'id': 123, 'flow_id': '14.2', 'parent_id': '14',
               'settings': self.setting({'is_answer': False, 'questions': ['14.2'], 'questions_next': ['14.2']}),
               'name': '2. Comunícame con un asesor.  👨‍💻 '}
        )
        Question.objects.create(
            **{'id': 124, 'flow_id': '14.2.1', 'parent_id': '14.2',
               'settings': self.setting({'is_answer': False, 'questions': ['14.2.2'], 'questions_next': ['14.2.2']}),
               'name': 'Los horarios de atencion son 8:30 am a 5:30 pm'}
        )
        Question.objects.create(
            **{'id': 125, 'flow_id': '14.2.2', 'parent_id': '14.2',
               'settings': self.setting({'is_answer': False, 'questions': ['14.2.2'], 'questions_next': ['14.2.2']}),
               'name': 'Dejanos tu numero de contacto y un asesor se comunicara contigo a la brevedad.'}
        )
        Question.objects.create(
            **{'id': 126, 'flow_id': '14.2.2.1', 'parent_id': '14.2.2',
               'name': '¡Gracias por proporcionar tu número! Un asesor se pondrá en contacto contigo pronto. '
                       'Asimismo, ponemos a tu disposición información sobre los siguientes servicios:\n'
                       '•	“Trabaja Sin Acoso” a través de la línea gratuita 1819.\n'
                       '•	Atención de consultas laborales a través de la línea gratuita 0800-1-6872, opción 3 ('
                       'trabajo del hogar)\n'
                       '•	Servicio de Patrocinio Judicial Gratuito del MTPE, accesible en Av. Gral. Salaverry 655, '
                       'Jesús María\n'
                       '¡Que tengas un excelente día!'}
        )

        # Option main 14 - 3
        Question.objects.create(
            **{'id': 127, 'flow_id': '14.3', 'parent_id': '14',
               'settings': self.setting({'is_answer': False, 'questions': ['14.3'], 'questions_next': ['14.3']}),
               'name': '3. No tengo más consultas. 🔚'}
        )
        Question.objects.create(
            **{'id': 128, 'flow_id': '14.3.1', 'parent_id': '14.3',
               'settings': self.setting({'is_answer': False, 'questions': ['14.3'], 'questions_next': ['13']}),
               'name': '¡Gracias por acudir a nuestro servicio! ponemos a tu disposición información '
                       'sobre los siguientes servicios:\n'
                       '• “Trabaja Sin Acoso” a través de la línea gratuita 1819.\n'
                       '• Atención de consultas laborales a través de la línea gratuita 0800-1-6872,'
                       ' opción 3 (trabajo del hogar)\n'
                       '• Servicio de Patrocinio Judicial Gratuito del MTPE, accesible en Av. '
                       'Gral. Salaverry 655, Jesús María\n'
                       '¡Que tengas un excelente día!'}
        )
        Question.objects.create(
            **{'id': 129, 'flow_id': '14.3.2', 'parent_id': '14.3.1',
               'settings': self.setting({'questions': ['14.3.1']}),
               'name': '😊Gracias por contactarte con nosotros, si me necesitas nuevamente, '
                       'estaré aquí para ayudarte. ¡Hasta pronto! 👋🏼'}
        )

    from chatbots.models import Question
    from users.models import User
    from core.services.app import AppService

    class QuestionService(AppService):
        def __init__(self):
            self.department_data = {
                'item': 0,
                'name': None,
                'description': None,
                'is_active': True,
            }

        def register(self):
            self.reset()
            settings = {'is_input': True, 'questions': ['11']}
            Question.objects.create(
                **{'id': 1, 'flow_id': '10', 'name': 'Chatbot XXX', 'settings': settings})
            Question.objects.create(
                **{'id': 2, 'flow_id': '10.1', 'parent_id': '10', 'settings': {'is_group': True},
                   'name': '¡Hola! Soy Victoria, tu asistente virtual. Estoy aquí para ayudarte a '
                           'conocer más sobre el régimen laboral de las personas trabajadoras del '
                           'hogar 🤖.\n'
                           '📍 En el Perú, este régimen se encuentra regulado en la Ley N° 31047, '
                           'publicada el 01 de octubre de 2020. Además, contamos con un reglamento '
                           'aprobado por Decreto Supremo N° 009-2021-TR.\n'}
            )
            Question.objects.create(
                **{'id': 3, 'flow_id': '10.2', 'parent_id': '10', 'settings': {'is_group': True},
                   'name': 'Ahora que ya me conoces, dime ¿Cuál es tu nombre? 👩👨.'}
            )

            settings = {'is_input': True, 'is_answer': True, 'questions': ['12']}
            Question.objects.create(
                **{'id': 4, 'flow_id': '11', 'name': 'Chatbot XXX', 'settings': settings})
            Question.objects.create(
                **{'id': 5, 'flow_id': '11.0', 'parent_id': '11', 'is_read': True, 'settings': {'is_group': True},
                   'name': '¡Bienvenido/a, XXXXXX! Cuéntame, ¿en qué región de Perú te encuentras? ✍️\n'}

            )
            Question.objects.create(
                **{'id': 6, 'flow_id': '11.1', 'parent_id': '11', 'name': '1. Lima', 'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 7, 'flow_id': '11.2', 'parent_id': '11', 'name': '2. Lima Provincia',
                   'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 8, 'flow_id': '11.3', 'parent_id': '11', 'name': '3. Lambayeque',
                   'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 9, 'flow_id': '11.4', 'parent_id': '11', 'name': '4. Arequipa', 'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 10, 'flow_id': '11.5', 'parent_id': '11', 'name': '5. Tumbes', 'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 11, 'flow_id': '11.6', 'parent_id': '11', 'name': '6. Pasco', 'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 12, 'flow_id': '11.7', 'parent_id': '11', 'name': '7. Huánuco', 'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 13, 'flow_id': '11.8', 'parent_id': '11', 'name': '8. La Libertad',
                   'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 14, 'flow_id': '11.9', 'parent_id': '11', 'name': '9. Junín', 'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 15, 'flow_id': '11.10', 'parent_id': '11', 'name': '10. Áncash',
                   'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 16, 'flow_id': '11.11', 'parent_id': '11', 'name': '11. Cajamarca',
                   'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 17, 'flow_id': '11.12', 'parent_id': '11', 'name': '12. Callao',
                   'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 18, 'flow_id': '11.13', 'parent_id': '11', 'name': '13. Ica', 'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 19, 'flow_id': '11.14', 'parent_id': '11', 'name': '14. San Martin',
                   'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 20, 'flow_id': '11.15', 'parent_id': '11', 'name': '15. Huancavelica',
                   'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 21, 'flow_id': '11.16', 'parent_id': '11', 'name': '16. Piura', 'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 22, 'flow_id': '11.17', 'parent_id': '11', 'name': '17. Tacna', 'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 23, 'flow_id': '11.18', 'parent_id': '11', 'name': '18. Puno', 'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 24, 'flow_id': '11.19', 'parent_id': '11', 'name': '19. Madre de Dios',
                   'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 25, 'flow_id': '11.20', 'parent_id': '11', 'name': '20. Ucayali',
                   'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 26, 'flow_id': '11.21', 'parent_id': '11', 'name': '21. Ayacucho',
                   'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 27, 'flow_id': '11.22', 'parent_id': '11', 'name': '22. Apurímac',
                   'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 28, 'flow_id': '11.23', 'parent_id': '11', 'name': '23. Cusco', 'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 29, 'flow_id': '11.24', 'parent_id': '11', 'name': '24. Amazonas',
                   'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 30, 'flow_id': '11.25', 'parent_id': '11', 'name': '25. Moquegua',
                   'settings': {'is_group': True}}
            )
            Question.objects.create(
                **{'id': 31, 'flow_id': '11.26', 'parent_id': '11', 'name': '26. Loreto',
                   'settings': {'is_group': True}}
            )

            settings = {'is_input': True, 'is_answer': True, 'questions': [13]}
            Question.objects.create(
                **{'id': 32, 'flow_id': '12', 'name': 'Chatbot XXX', 'settings': settings})
            Question.objects.create(
                **{'id': 33, 'flow_id': '12.0', 'parent_id': '12', 'settings': {'is_group': True},
                   'name': '☝ Señala el número del perfil con el que te identificas\n'}
            )
            ##
            Question.objects.create(
                **{'id': 34, 'flow_id': '12.1', 'parent_id': '12',
                   'settings': {'is_input': True, 'is_answer': True, 'is_group': True, 'questions': ['12.1']},
                   'name': '1. Soy una persona trabajadora del hogar 👨‍🏭👩‍🔧'}
            )
            Question.objects.create(
                **{'id': 35, 'flow_id': '12.1.1', 'parent_id': '12.1',
                   'settings': {'is_input': True, 'is_answer': True, 'is_group': True, 'questions': ['12.1.1']},
                   'name': '¿Qué edad tienes?'}
            )

            ##
            Question.objects.create(
                **{'id': 36, 'flow_id': '12.2', 'parent_id': '12',
                   'settings': {'is_input': True, 'is_answer': True, 'is_group': True, 'questions': ['13']},
                   'name': '2. Soy una persona empleadora en trabajo del hogar 👩‍💼👨‍💼'}
            )

            ##
            Question.objects.create(
                **{'id': 37, 'flow_id': '12.3', 'parent_id': '12',
                   'settings': {'is_input': True, 'is_answer': True, 'is_group': True, 'questions': ['13']},
                   'name': '3. Soy una persona interesada en el tema  🕵️‍♀️👮‍'}
            )

            Question.objects.create(
                **{'id': 38, 'flow_id': '13', 'name': 'Chatbot XXX', 'settings': settings})
            Question.objects.create(
                **{'id': 39, 'flow_id': '13.0', 'parent_id': '13', 'settings': {'is_group': True},
                   'name': '📌 Estoy aquí para ayudarte. A continuación, te mostraré una lista de temas que podrían ser de '
                           'tu interés. Por favor, elige el número correspondiente a la opción que deseas consultar.\n'}
            )

            # Option main 1
            Question.objects.create(
                **{'id': 40, 'flow_id': '13.1', 'parent_id': '13', 'settings': self.setting({'questions': ['13.1']}),
                   'name': '1. ¿A quiénes se considera personas trabajadoras del hogar? 👨‍🏭👩‍🔧'
                   }
            )
            Question.objects.create(
                **{'id': 41, 'flow_id': '13.1.0', 'parent_id': '13.1', 'settings': {'is_group': True},
                   'name': 'Por favor, elige el número correspondiente a la opción que deseas consultar.\n'}
            )
            Question.objects.create(
                **{'id': 42, 'flow_id': '13.1.1', 'parent_id': '13.1',
                   'settings': self.setting({'questions': ['13.1.1']}),
                   'name': '1. Persona trabajadora del hogar  👨‍🏭👩‍🔧'}
            )
            Question.objects.create(
                **{'id': 43, 'flow_id': '13.1.1.1', 'parent_id': '13.1.1',
                   'settings': {'is_group': True, 'is_answer': False, 'is_reload': True,
                                'questions': ['13.1.1.1', '14']},
                   'name': 'Se considera persona trabajadora del hogar a aquella persona mayor de edad (18 años) que '
                           'realiza tareas domésticas dentro de un domicilio particular.\n'
                           'Las tareas domésticas incluyen la limpieza, cocina, asistencia de cocina, lavado, planchado;'
                           ' así como tareas de cuidado de otras personas.'}
            )
            Question.objects.create(
                **{'id': 44, 'flow_id': '13.1.2', 'parent_id': '13.1',
                   'settings': self.setting({'questions': ['13.1.2']}),
                   'name': '2. Edad mínima 👨‍💻'}
            )
            Question.objects.create(
                **{'id': 45, 'flow_id': '13.1.2.1', 'parent_id': '13.1.2',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.1.2.1', '14']},
                   'name': 'La persona trabajadora del hogar debe tener como mínimo 18 años. En ningún caso se puede '
                           'contratar a menores de edad, pues el trabajo del hogar y de cuidados son '
                           'considerados trabajos peligrosos para los adolescentes.'}
            )

            # Option main 2
            Question.objects.create(
                **{'id': 46, 'flow_id': '13.2', 'parent_id': '13', 'settings': self.setting({'questions': ['13.2']}),
                   'name': '2. Pasos para formalizar a una persona trabajadora del hogar 📋'}
            )
            Question.objects.create(
                **{'id': 47, 'flow_id': '13.2.1', 'parent_id': '13.2',
                   'settings': self.setting({'questions': ['13.2.1']}),
                   'name': '1. Firma y contenido del contrato de trabajo 📋'}
            )
            Question.objects.create(
                **{'id': 48, 'flow_id': '13.2.1.1', 'parent_id': '13.2.1',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.2.1.1', '14']},
                   'name': 'Todas las personas trabajadoras del hogar deben tener un contrato escrito donde se '
                           'detallen sus condiciones laborales y derechos conforme a la normativa. Debe incluir: \n'
                           '1.	Datos personales: nombres, edad, sexo, estado civil, profesión u oficio de ambas partes. \n'
                           '2.	Especificaciones del tipo de labores a realizar \n'
                           '3.	Lugar de trabajo: Lugar o lugares de prestación del trabajo (dirección o direcciones) \n'
                           '4.	Tiempo que la persona trabajadora del hogar ha laborado previamente a la firma del contrato \n'
                           '5.	Fecha de inicio del contrato y duración (en caso sea tiempo determinado) \n'
                           '6.	Remuneración \n'
                           '7.	Jornada y horario, incluyendo días de descanso semanal \n'
                           '8.	Implementos que se le brindará a la persona trabajadora para resguardar su seguridad y salud en el trabajo \n'
                           '9.	Información sobre el Seguro Social de Salud y el sistema de pensiones de elección de la persona trabajadora del hogar \n'
                           '10.	Condiciones de alimentos, uniforme o alojamiento cuando corresponda \n'
                           '11.	Nombre de la entidad financiera elegida, número de cuenta bancaria personal y/o código de cuenta interbancaria \n'
                           '12.	Obligaciones del empleador (gratificaciones, CTS, vacaciones). \n'
                           '13.	Facilidades para educación, si estudia.'}
            )
            Question.objects.create(
                **{'id': 49, 'flow_id': '13.2.2', 'parent_id': '13.2',
                   'settings': self.setting({'questions': ['13.2.2']}),
                   'name': '2. Registro del contrato ante el Ministerio de Trabajo y\n'
                           '   Promoción del Empleo -MTPE'}
            )
            Question.objects.create(
                **{'id': 50, 'flow_id': '13.2.2.1', 'parent_id': '13.2.2',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.2.2.1', '14']},
                   'name': 'Todos los contratos de personas trabajadoras del hogar deben ser registrados en la plataforma '
                           'web “Registro del trabajo del hogar”, del Ministerio de Trabajo y Promoción del Empleo (MTPE).\n'
                           'Quien contrata tiene 3 días hábiles desde la firma del contrato para registrar el contrato de '
                           'trabajo ante el MTPE, luego tendrá 03 días hábiles más para entregar a la persona trabajadora '
                           'una constancia de dicho registro.\n'
                           'Una vez concluido el vínculo, el empleador debe dar de baja el registro en el aplicativo.\n'
                           'Para ingresar al registro visita el siguiente enlace: https://apps.trabajo.gob.pe/rcth/app/#/inicio'}
            )

            Question.objects.create(
                **{'id': 51, 'flow_id': '13.2.3', 'parent_id': '13.2',
                   'settings': self.setting({'questions': ['13.2.3']}),
                   'name': '3. Necesito ayuda para formalizar a mi trabajadora/r del\n'
                           '   hogar 👩‍🔧'}
            )
            Question.objects.create(
                **{'id': 52, 'flow_id': '13.2.3.1', 'parent_id': '13.2.3',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.2.3.1', '14']},
                   'name': 'El Centro Integrado Formaliza Perú (CIFP), brinda acompañamiento para facilitar los '
                           'trámites de la formalización laboral de tu trabajadora/r del hogar.\n'
                           'Puedes visitarlo  en cualquiera de sus sedes, a nivel nacional. Para ver los teléfonos y '
                           'direcciones de las oficinas del CIFP ingresa al siguiente enlace:\n'
                           'https://portal.trabajo.gob.pe/formalizaperu/nosotros'}
            )

            # Option main 3
            Question.objects.create(
                **{'id': 53, 'flow_id': '13.3', 'parent_id': '13', 'settings': self.setting({'questions': ['13.3']}),
                   'name': '3. Principales derechos de la persona trabajadora del hogar 👨‍💻'}
            )
            # Option main 3 - 1
            Question.objects.create(
                **{'id': 54, 'flow_id': '13.3.1', 'parent_id': '13.3',
                   'settings': self.setting({'questions': ['13.3.1']}),
                   'name': '1. Remuneración por el trabajo del hogar 💲'}
            )
            Question.objects.create(
                **{'id': 55, 'flow_id': '13.3.1.1', 'parent_id': '13.3.1',
                   'settings': self.setting({'questions': ['13.3.1.1']}),
                   'name': '1. Remuneración por el trabajo del hogar'}
            )
            Question.objects.create(
                **{'id': 56, 'flow_id': '13.3.1.1.1', 'parent_id': '13.3.1.1',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.1.1.1', '14']},
                   'name': 'El monto de la remuneración de la persona trabajadora del hogar será establecido por acuerdo '
                           'libre entre empleador y la persona trabajadora del hogar, pero no podrá ser inferior a la '
                           'remuneración mínima vital (RMV), para las personas trabajadoras a tiempo completo, esto es '
                           'quienes laboran a partir de 24 horas semanales.\n'
                           'La remuneración de la persona trabajadora del hogar puede pagarse en forma semanal, quincenal '
                           'o mensual, según acuerdo.'}
            )
            Question.objects.create(
                **{'id': 57, 'flow_id': '13.3.1.2', 'parent_id': '13.3.1',
                   'settings': self.setting({'questions': ['13.3.1.2']}),
                   'name': '2. Remuneración por trabajo del hogar a tiempo parcial'}
            )
            Question.objects.create(
                **{'id': 58, 'flow_id': '13.3.1.2.1', 'parent_id': '13.3.1.2',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.1.2.1', '14']},
                   'name': 'Si la persona trabajadora del hogar labora una jornada de trabajo inferior a 4 horas diarias '
                           'en promedio a la semana, la remuneración mensual podrá ser acordada en función de la cantidad '
                           'de horas trabajadas, usando como parámetro el valor de la RMV como mínimo.\n'
                           'La remuneración de la persona trabajadora del hogar puede pagarse en forma semanal, '
                           'quincenal o mensual, según acuerdo'}
            )
            Question.objects.create(
                **{'id': 59, 'flow_id': '13.3.1.3', 'parent_id': '13.3.1',
                   'settings': self.setting({'questions': ['13.3.1.3']}),
                   'name': '3. Conceptos que no forman parte de la remuneración'}
            )
            Question.objects.create(
                **{'id': 60, 'flow_id': '13.3.1.3.1', 'parent_id': '13.3.1.3',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.1.3.1', '14']},
                   'name': 'Las condiciones de alojamiento, alimentación, entrega de uniformes, equipos de protección, '
                           'instrumentos o herramientas para la prestación del trabajo, así como los implementos de '
                           'bioseguridad y artículos de desinfección no son parte de la remuneración, por lo que bajo '
                           'ningún motivo se pueden descontar estos conceptos o contabilizarlos como '
                           'parte de la remuneración.'}
            )

            # Option main 3 - 2
            Question.objects.create(
                **{'id': 61, 'flow_id': '13.3.2', 'parent_id': '13.3',
                   'settings': self.setting({'questions': ['13.3.2']}),
                   'name': '2. Condiciones de trabajo en el trabajo del hogar 👨‍🚒'}
            )
            Question.objects.create(
                **{'id': 62, 'flow_id': '13.3.2.1', 'parent_id': '13.3.2',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.2.1', '14']},
                   'name': 'En caso la modalidad de trabajo incluya residencia, la persona que emplea está obligada a '
                           'proporcionar alimentación'
                           'completa (desayuno, almuerzo y cena) y un alojamiento adecuado al nivel socioeconómico'
                           'de la persona trabajadora del hogar.\n'
                           'Asimismo, las condiciones laborales deben garantizar la dignidad de la persona trabajadora y '
                           'el cumplimiento de las normas de seguridad y salud en el trabajo. Esto incluye la entrega de '
                           'equipos de protección,'
                           'instrumentos y herramientas necesarios para la prestación del servicio.'}
            )
            # Option main 3 - 3
            Question.objects.create(
                **{'id': 63, 'flow_id': '13.3.3', 'parent_id': '13.3',
                   'settings': self.setting({'questions': ['13.3.3']}),
                   'name': '3. Jornada, descanso semanal y feriados  ⌛'}
            )
            Question.objects.create(
                **{'id': 64, 'flow_id': '13.3.3.1', 'parent_id': '13.3.3',
                   'settings': self.setting({'questions': ['13.3.3.1']}),
                   'name': '1. Jornada laboral del trabajo del hogar'}
            )
            Question.objects.create(
                **{'id': 65, 'flow_id': '13.3.3.1.1', 'parent_id': '13.3.3.1',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.3.1.1', '14']},
                   'name': 'La persona trabajadora del hogar no debe trabajar más de 8 horas diarias, '
                           'ni más de 48 horas semanales. '}
            )
            Question.objects.create(
                **{'id': 66, 'flow_id': '13.3.3.2', 'parent_id': '13.3.3',
                   'settings': self.setting({'questions': ['13.3.3.2']}),
                   'name': '2. Descanso semanal de trabajo de la persona trabajadora del hogar'}
            )
            Question.objects.create(
                **{'id': 67, 'flow_id': '13.3.3.2.1', 'parent_id': '13.3.3.2',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.3.2.1', '14']},
                   'name': 'La persona trabajadora del hogar debe contar con un periodo de descanso de 24 horas '
                           'continuas a la semana como mínimo.\n'
                           'En el caso de trabajo con residencia en el hogar (antes llamado “cama adentro”), la '
                           'persona trabajadora tiene derecho a contar con 12 horas continuas de descanso, entre el '
                           'término de una jornada y el inicio de la siguiente.'}
            )
            Question.objects.create(
                **{'id': 68, 'flow_id': '13.3.3.3', 'parent_id': '13.3.3',
                   'settings': self.setting({'questions': ['13.3.3.3']}),
                   'name': '3. Horas extras de trabajo de la persona trabajadora del hogar'}
            )
            Question.objects.create(
                **{'id': 69, 'flow_id': '13.3.3.3.1', 'parent_id': '13.3.3.3',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.3.3.1', '14']},
                   'name': 'La persona trabajadora del hogar puede realizar horas extras a la jornada de trabajo de '
                           'manera voluntaria, previo acuerdo con quien la emplea y con un pago adicional.\n'
                           'Las horas extras se pagarán sobre el valor de una hora habitual más una sobretasa del '
                           '25 % por las dos primeras horas y posteriormente una sobretasa no menor al 35%.'}
            )

            Question.objects.create(
                **{'id': 70, 'flow_id': '13.3.3.4', 'parent_id': '13.3.3',
                   'settings': self.setting({'questions': ['13.3.3.4']}),
                   'name': '4. ¿Cuáles son los feriados que deben gozar las personas trabajadoras del hogar? '}
            )
            Question.objects.create(
                **{'id': 71, 'flow_id': '13.3.3.4.1', 'parent_id': '13.3.3.4',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.3.4.1', '14']},
                   'name': 'La persona trabajadora del hogar tiene derecho a los mismos feriados que cualquier persona '
                           'trabajadora del sector privado. Estos son:\n'
                           '\n'
                           '●	Año Nuevo (1 de enero)\n'
                           '●	Jueves Santo y Viernes Santo (movibles)\n'
                           '●	Día del Trabajo (1 de mayo)\n'
                           '●	Batalla de Arica y Día de la Bandera (7 de junio)\n'
                           '●	San Pedro y San Pablo (29 de junio)\n'
                           '●	Conmemoración al heroico sacrificio del Capitán FAP José \n'
                           '    Abelardo Quiñones Gonzales (23 de julio)\n'
                           '●	Fiestas Patrias (28 y 29 de julio)\n'
                           '●	Batalla de Junín (6 de agosto)\n'
                           '●	Santa Rosa de Lima (30 de agosto)\n'
                           '●	Combate de Angamos (8 de octubre)\n'
                           '●	Todos los Santos (1 de noviembre)\n'
                           '●	Inmaculada Concepción (8 de diciembre)\n'
                           '●	Batalla de Ayacucho (9 de diciembre)\n'
                           '●	Navidad del Señor (25 de diciembre)\n'
                           '\n'
                           'Asimismo, cuentan con un feriado propio en el Día de las Trabajadoras y '
                           'Trabajadores del Hogar (30 de marzo).'}
            )
            Question.objects.create(
                **{'id': 72, 'flow_id': '13.3.3.5', 'parent_id': '13.3.3',
                   'settings': self.setting({'questions': ['13.3.3.5']}),
                   'name': '5. ¿Qué pasa si se trabaja en un feriado?'}
            )
            Question.objects.create(
                **{'id': 73, 'flow_id': '13.3.3.5.1', 'parent_id': '13.3.3.5',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.3.5.1', '14']},
                   'name': 'Si la persona trabajadora accede, de manera voluntaria y por mutuo acuerdo, a trabajar '
                           'durante un feriado, se le debe pagar una sobretasa del 100 %; es decir, doble remuneración.\n'
                           'Ten en cuenta que para las personas trabajadoras del hogar que presten servicios con '
                           'residencia en el domicilio (cama adentro), los periodos durante los cuales no disponen '
                           'libremente de su tiempo y permanecen a disposición del hogar, son considerados  como '
                           'horas de trabajo y deben ser remuneradas.'}
            )
            # Option main 3 - 4
            Question.objects.create(
                **{'id': 74, 'flow_id': '13.3.4', 'parent_id': '13.3',
                   'settings': self.setting({'questions': ['13.3.4']}),
                   'name': '4. Vacaciones 🕓'}
            )
            Question.objects.create(
                **{'id': 75, 'flow_id': '13.3.4.1', 'parent_id': '13.3.4',
                   'settings': self.setting({'questions': ['13.3.4.1']}),
                   'name': '1. Vacaciones de la persona trabajadora del hogar a tiempo completo'}
            )
            Question.objects.create(
                **{'id': 76, 'flow_id': '13.3.4.1.1', 'parent_id': '13.3.4.1',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.4.1.1', '14']},
                   'name': 'Si la persona trabajadora del hogar tiene una jornada de, al menos, 4 horas diarias en '
                           'promedio a la semana, y tiene más de un año laborando (desde que empezó a trabajar), '
                           'tiene derecho a 30 días de vacaciones remuneradas anuales que deben ser gozadas dentro del '
                           'periodo anual siguiente a aquel en que adquirió dicho derecho.\n'
                           'Dicho descanso no podrá ser otorgado cuando la trabajadora se encuentra incapacitada por '
                           'alguna enfermedad o accidente, pues en esos casos corresponde aplicar licencias o '
                           'contabilizar los días de inasistencia como faltas justificadas\n'
                           '\n'
                           'Ejemplo:\n'
                           'Ana empezó a trabajar el 14 de abril de 2022. Cumplió un año de servicios el '
                           '13 de abril de 2023 y, en ese momento, adquirió el derecho al descanso vacacional '
                           'correspondiente al primer año de trabajo, que podrá gozar a partir del 14 de abril de 2023.'}
            )
            Question.objects.create(
                **{'id': 77, 'flow_id': '13.3.4.2', 'parent_id': '13.3.4',
                   'settings': self.setting({'questions': ['13.3.4.2']}),
                   'name': '2. Fechas para tomar vacaciones'}
            )
            Question.objects.create(
                **{'id': 78, 'flow_id': '13.3.4.2.1', 'parent_id': '13.3.4.2',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.4.2.1', '14']},
                   'name': 'Las fechas del descanso vacacional deben ser fijadas de común acuerdo entre la persona '
                           'empleadora y la persona trabajadora. En ausencia de un acuerdo claro, la persona empleadora '
                           'tiene la libertad de tomar decisiones según su propio juicio y dirección.\n'
                           '\n'
                           'Al término del vínculo laboral, en caso de que la persona trabajadora no haya gozado por '
                           'completo el descanso vacacional, o que solo se haya tomado una parte, el empleador deberá '
                           'pagar el equivalente a los días no gozados. En caso de no cumplir con el año completo de trabajo, '
                           'deberá recibir un pago proporcional a los meses y días que hubiera laborado.\n'
                           '\n'
                           'Las vacaciones se cuentan en días calendario, esto incluye sábados, domingos y feriados.'}
            )
            Question.objects.create(
                **{'id': 79, 'flow_id': '13.3.4.3', 'parent_id': '13.3.4',
                   'settings': self.setting({'questions': ['13.3.4.3']}),
                   'name': '3. Vacaciones de la persona trabajadora del hogar a tiempo parcial'}
            )
            Question.objects.create(
                **{'id': 80, 'flow_id': '13.3.4.3.1', 'parent_id': '13.3.4.3',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.4.3.1', '14']},
                   'name': 'En caso de que la persona trabajadora del hogar labore menos de 4 horas diarias '
                           '(en promedio a la semana) y haya cumplido un año de trabajo, tiene derecho a, por lo menos, '
                           '6 días de vacaciones anuales (en aplicación del Convenio núm. 52 de la OIT).'}
            )
            # Option main 3 - 5
            Question.objects.create(
                **{'id': 81, 'flow_id': '13.3.5', 'parent_id': '13.3',
                   'settings': self.setting({'questions': ['13.3.5']}),
                   'name': '5. Gratificación de la persona trabajadora del hogar 🏡'}
            )
            Question.objects.create(
                **{'id': 82, 'flow_id': '13.3.5.1', 'parent_id': '13.3.5',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.5.1', '14']},
                   'name': 'Independientemente de las horas que la persona trabajadora labore, le corresponde una '
                           'gratificación por Fiestas Patrias y una gratificación por Navidad. Cada una equivale a '
                           'una remuneración mensual en cada oportunidad (de acuerdo con la remuneración estipulada '
                           'en su contrato), y se calcula en función de los meses calendario completos laborados '
                           'dentro del semestre correspondiente.\n'
                           'Recuerda que la gratificación por Fiestas Patrias debe '
                           'pagarse en la primera quincena de julio y la gratificación por Navidad en la primera quincena '
                           'de diciembre.\n'
                           'En el siguiente enlace puede acceder a Calcula tu Grati, un aplicativo de SUNAFIL, '
                           'que te ayudará a realizar el cálculo:\n'
                           'https://aplicativosweb6.sunafil.gob.pe/si.calculadoraLaboral'}
            )
            # Option main 3 - 6
            Question.objects.create(
                **{'id': 83, 'flow_id': '13.3.6', 'parent_id': '13.3',
                   'settings': self.setting({'questions': ['13.3.6']}),
                   'name': '6. Compensación por Tiempo de Servicios - CTS 💰'}
            )
            Question.objects.create(
                **{'id': 84, 'flow_id': '13.3.6.1', 'parent_id': '13.3.6',
                   'settings': self.setting({'questions': ['13.3.6.1']}),
                   'name': '1. ¿Cuándo las personas trabajadoras del hogar reciben la CTS y cuál es la forma de entrega?'}
            )
            Question.objects.create(
                **{'id': 85, 'flow_id': '13.3.6.1.1', 'parent_id': '13.3.6.1',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.6.1.1', '14']},
                   'name': 'Si la persona trabajadora del hogar labora al menos 4 horas diarias en promedio a la semana '
                           'y además ha acumulado, como mínimo, un mes de labores, tiene derecho a recibir la CTS, la '
                           'cual tiene como propósito la prevención de contingencias a consecuencia del término del '
                           'vínculo laboral, sin importar la causa.\n'
                           'La persona empleadora deposita la CTS de la persona trabajadora del hogar, en una cuenta '
                           'bancaria abierta para tal fin dentro de los primeros quince (15) días naturales de los '
                           'meses de mayo y noviembre de cada año. Si el último día es inhábil, el depósito puede '
                           'efectuarse el primer día hábil siguiente. Efectuado el depósito queda cumplida y pagada '
                           'la obligación de la persona empleadora del hogar.\n'
                           'Ten en cuenta que este monto no se descuenta de la remuneración que se le otorga a la '
                           'persona trabajadora.\n'
                           'Si la persona trabajadora del hogar cesa, pero hubiera laborado como mínimo un (01) mes '
                           'completo dentro del semestre correspondiente, la persona empleadora del hogar debe '
                           'pagar la CTS trunca directamente, dentro de las cuarenta y ocho (48) horas de '
                           'producido el cese.'}
            )
            Question.objects.create(
                **{'id': 86, 'flow_id': '13.3.6.2', 'parent_id': '13.3.6',
                   'settings': self.setting({'questions': ['13.3.6.2']}),
                   'name': '2. Información que debe entregar la persona trabajadora para recibir la CTS'}
            )
            Question.objects.create(
                **{'id': 87, 'flow_id': '13.3.6.2.1', 'parent_id': '13.3.6.2',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.6.2.1', '14']},
                   'name': 'La persona trabajadora del hogar debe comunicar a su empleador el nombre de la entidad '
                           'financiera elegida para el depósito de la CTS, el número de cuenta, de CCI y el tipo '
                           'de moneda.\n'
                           'Si la persona trabajadora del hogar no brinda dicha información, quien la emplea deposita'
                           ' la CTS en cualquiera de las instituciones del sistema financiero, bajo la modalidad '
                           'de depósito a plazo fijo por el periodo más largo permitido.'}
            )
            Question.objects.create(
                **{'id': 88, 'flow_id': '13.3.6.3', 'parent_id': '13.3.6',
                   'settings': self.setting({'questions': ['13.3.6.3']}),
                   'name': '3. ¿Cómo se calcula la CTS?'}
            )
            Question.objects.create(
                **{'id': 89, 'flow_id': '13.3.6.3.1', 'parent_id': '13.3.6.3',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.6.3.1', '14']},
                   'name': 'Como primer paso se debe calcular la remuneración computable, la cual comprende '
                           'la suma de los siguientes montos:\n'
                           '-	Remuneración básica\n'
                           '-	1/6 de la gratificación percibida en el semestre\n'
                           'Como segundo paso debes dividir la remuneración computable entre 12 y multiplicarlos '
                           'por los meses laborados completos en el semestre. En caso quieras calcularlo por días, '
                           'la remuneración computable la divides entre 360 y la multiplicas por los días laborados '
                           'en el semestre.\n'
                           'En el siguiente enlace puede acceder a Calcula tu CTS, un aplicativo de SUNAFIL, '
                           'que te ayudará a realizar el cálculo:\n'
                           'https://aplicativosweb6.sunafil.gob.pe/si.calculadoraLaboral/identificacionTrabajadorEmpresa'}
            )
            Question.objects.create(
                **{'id': 90, 'flow_id': '13.3.6.4', 'parent_id': '13.3.6',
                   'settings': self.setting({'questions': ['13.3.6.4']}),
                   'name': '4. ¿Cuáles son los periodos de trabajo computables y fecha de depósito?'}
            )
            Question.objects.create(
                **{'id': 91, 'flow_id': '13.3.6.4.1', 'parent_id': '13.3.6.4',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.6.4.1', '14']},
                   'name': 'Periodos de trabajo computable:\n'
                           'Noviembre – abril. El depósito de este periodo se realiza la primera quincena de mayo.\n'
                           'Mayo - octubre. El depósito de este periodo se realiza la primera quincena de noviembre.'}
            )

            # Option main 3 - 7
            Question.objects.create(
                **{'id': 92, 'flow_id': '13.3.7', 'parent_id': '13.3',
                   'settings': self.setting({'questions': ['13.3.7']}),
                   'name': '7. Acceso a la seguridad social en salud- Essalud 🏥'}
            )
            Question.objects.create(
                **{'id': 93, 'flow_id': '13.3.7.1', 'parent_id': '13.3.7',
                   'settings': self.setting({'questions': ['13.3.7.1']}),
                   'name': '1. Afiliación y pago a EsSalud: ¿Cómo realizar el pago?'}
            )
            Question.objects.create(
                **{'id': 94, 'flow_id': '13.3.7.1.1', 'parent_id': '13.3.7.1',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.7.1.1', '14']},
                   'name': 'Toda persona trabajadora del hogar tiene derecho a ser afiliada al Seguro Social de Salud (EsSalud). '
                           'Para ello, la persona empleadora debe realizar un pago equivalente '
                           'al 9% de la remuneración de la persona trabajadora del hogar. '
                           'Quien emplea asume el pago, en ningún caso deberá ser descontado de la remuneración de la persona '
                           'trabajadora del hogar.\n'
                           '\n'
                           '¿Cómo realizar el pago?\n'
                           'El primer paso para realizar el pago es registrar a la persona trabajadora del hogar en el '
                           'siguiente enlace:\n'
                           'Una vez que hayas registrado a la persona trabajadora del hogar en el Registro del MTPE, '
                           'puedes realizar los pagos a través de la página de SUNAT o a través de agencias bancarias '
                           'autorizadas a nivel nacional.\n'
                           'Para mayor información ingresa al siguiente enlace: '
                           'https://www.gob.pe/8076-declarar-y-pagar-aportes-de-trabajadores-del-hogar'
                   }
            )
            Question.objects.create(
                **{'id': 95, 'flow_id': '13.3.7.2', 'parent_id': '13.3.7',
                   'settings': self.setting({'questions': ['13.3.7.2']}),
                   'name': '2. Beneficios de la afiliación a Essalud para la persona trabajadora del hogar'}
            )
            Question.objects.create(
                **{'id': 96, 'flow_id': '13.3.7.2.1', 'parent_id': '13.3.7.2',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.7.2.1', '14']},
                   'name': 'La afiliación a EsSalud permite que la persona trabajadora del hogar y sus familiares '
                           'registrados como derechohabientes, accedan a diversos servicios de salud. '
                           'Incluso, según corresponda, a través de su afiliación el trabajador podrá percibir '
                           'un subsidio por maternidad, lactancia, sepelio e incapacidad temporal.\n'
                           'Las personas derechohabientes son: cónyuge o concubina(o), hija o hijo menor de edad '
                           'hasta que cumpla 18 años (salvo que vivan con una condición de incapacidad permanente), '
                           'y madre de hija o hijo concebido.'}
            )
            Question.objects.create(
                **{'id': 97, 'flow_id': '13.3.7.3', 'parent_id': '13.3.7',
                   'settings': self.setting({'questions': ['13.3.7.3']}),
                   'name': '3. Beneficios de la afiliación a Essalud para la persona empleadora del hogar'}
            )
            Question.objects.create(
                **{'id': 98, 'flow_id': '13.3.7.3.1', 'parent_id': '13.3.7.3',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.7.3.1', '14']},
                   'name': 'Si eres persona empleadora y tus ingresos anuales superan las 7 UIT, puedes deducir de tu '
                           'Impuesto a la Renta, como gasto, las aportaciones al Seguro Social de Salud ESSALUD que '
                           'realices a favor de la persona trabajadora del hogar.'}
            )
            # Option main 3 - 8
            Question.objects.create(
                **{'id': 99, 'flow_id': '13.3.8', 'parent_id': '13.3',
                   'settings': self.setting({'questions': ['13.3.8']}),
                   'name': '8. Pensión para las personas trabajadoras del hogar ✍'}
            )
            Question.objects.create(
                **{'id': 100, 'flow_id': '13.3.8.1', 'parent_id': '13.3.8',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.8.1', '14']},
                   'name': 'Toda persona trabajadora del hogar debe aportar a un sistema de pensiones público o privado '
                           '(ONP o AFP), para acceder a una pensión (jubilación).\n'
                           'Este aporte es retenido y descontado de la remuneración de la persona  trabajadora y el monto '
                           'puede variar entre 10 % y 13% de la remuneración, de acuerdo con el sistema de pensiones '
                           'que elija la persona trabajadora del hogar.\n'
                           '\n'
                           'Para realizar el pago de ONP, ingresa al siguiente enlace: https://www.gob.pe/8076-declarar-y-pagar-aportes-de-trabajadores-del-hogar'
                   }
            )
            # Option main 3 - 9
            Question.objects.create(
                **{'id': 101, 'flow_id': '13.3.9', 'parent_id': '13.3',
                   'settings': self.setting({'questions': ['13.3.9']}),
                   'name': '9. Actos discriminatorios ⚠'}
            )
            Question.objects.create(
                **{'id': 102, 'flow_id': '13.3.9.1', 'parent_id': '13.3.9',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.3.9.1', '14']},
                   'name': 'Se encuentra prohibida toda forma de discriminación contra la persona trabajadora del hogar '
                           'por motivo de origen, raza, sexo, idioma, religión, opinión, condición económica, u otros; '
                           'así como cualquier tratamiento o expresión que afecte tu dignidad como persona.\n'
                           'Ejemplo:\n'
                           '• Es discriminación obligar a usar uniformes, mandiles, delantales o cualquier otra '
                           'vestimenta o distintivo identificatorio en espacios o establecimientos públicos como '
                           'parques, plazas, playas, restaurantes, hoteles, locales comerciales, clubes sociales y '
                           'otros similares.\n'
                           '• Es discriminación obligar o establecer como condición que la persona trabajadora del '
                           'hogar realice actos contrarios a los valores y prácticas sociales, culturales, religiosos y '
                           'espirituales de su lugar de origen.'}
            )
            # Option main 3 - 10
            Question.objects.create(
                **{'id': 103, 'flow_id': '13.3.10', 'parent_id': '13.3',
                   'settings': self.setting({'questions': ['13.3.10']}),
                   'name': '10. Protección de la maternidad 📌'}
            )
            Question.objects.create(
                **{'id': 104, 'flow_id': '13.3.10.1', 'parent_id': '13.3.10',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.10.1', '14']},
                   'name': 'Las trabajadoras del hogar tienen derecho a la protección durante su embarazo y periodo de '
                           'lactancia, por lo que no puede ser despedida por su embarazo, parto o lactancia.\n'
                           'Si se produce el despido en cualquier momento durante el embarazo o dentro de los 90 días '
                           'posteriores al nacimiento, ese despido es inválido y no tiene efecto legal.\n'
                           'Recuerda que el pago del subsidio por maternidad y lactancia es pagado directamente por EsSalud.'}
            )
            # Option main 3 - 11
            Question.objects.create(
                **{'id': 105, 'flow_id': '13.3.11', 'parent_id': '13.3',
                   'settings': self.setting({'questions': ['13.3.11']}),
                   'name': '11. Hostigamiento sexual 🚨'}
            )
            Question.objects.create(
                **{'id': 106, 'flow_id': '13.3.11.1', 'parent_id': '13.3.11',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.11.1', '14']},
                   'name': 'La persona empleadora tiene la obligación de garantizar un espacio libre de hostigamiento '
                           'sexual y de todo tipo de violencia.\n'
                           'Para tal efecto, como parte de las medidas de prevención, quien emplea puede facilitar el acceso '
                           'a la “Guía de prevención ante el hostigamiento sexual laboral en el trabajo del hogar” a través del siguiente enlace:\n'
                           'https://cdn.www.gob.pe/uploads/document/file/3810604/Gu%C3%ADa%20prevenci%C3%B3n%20hostigamiento%20-%20Trabajadores%20del%20Hogar%20.pdf?v=1667574592 \n'
                           'Asimismo, puedes acceder a un curso sobre el tema en este enlace: '
                           'https://capacitacionlaboral.trabajo.gob.pe/cursos/prevencion-y-reporte-del-hostigamiento-sexual-laboral/  CAPACÍTA-T(trabajo.gob.pe)'
                   })
            # Option main 3 - 12
            Question.objects.create(
                **{'id': 107, 'flow_id': '13.3.12', 'parent_id': '13.3',
                   'settings': self.setting({'questions': ['13.3.12']}),
                   'name': '12. Seguridad y Salud en el Trabajo 👨🏻‍⚕️'}
            )
            Question.objects.create(
                **{'id': 108, 'flow_id': '13.3.12.1', 'parent_id': '13.3.12',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.12.1', '14']},
                   'name': 'Las personas trabajadoras del hogar tienen derecho a desarrollar su trabajo en condiciones '
                           'libres de cualquier tipo de riesgo.  Por ello, el empleador debe establecer medidas y '
                           'brindar medios para que las tareas o actividades se realicen en '
                           'condiciones seguras y saludables.\n'
                           'Asimismo, el empleador debe asumir las implicancias '
                           'económicas, legales y de cualquier otra índole a consecuencia de un accidente o enfermedad '
                           'que sufra la persona trabajadora del hogar en el desempeño de sus funciones o como '
                           'consecuencia de este.\n'
                           'El empleador debe garantizar como mínimo la asistencia a una capacitación en materia de riesgos '
                           'asociados al desarrollo de sus labores.\n'
                           'Puedes acceder cursos sobre este y otros temas en '
                           'el portal CAPACÍTA-T (trabajo.gob.pe) '
                   }
            )

            # Option main 3 - 13
            Question.objects.create(
                **{'id': 109, 'flow_id': '13.3.13', 'parent_id': '13.3',
                   'settings': self.setting({'questions': ['13.3.13']}),
                   'name': '13. Calcular tus beneficios sociales'}
            )
            Question.objects.create(
                **{'id': 110, 'flow_id': '13.3.13.1', 'parent_id': '13.3.13',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True,
                                'questions': ['13.3.13.1', '14']},
                   'name': ' Para calcular tus beneficios sociales accede a este '
                           ' link:\n https://portal.trabajo.gob.pe/calculadoraMTPE'}
            )

            # Option main 4
            Question.objects.create(
                **{'id': 111, 'flow_id': '13.4', 'parent_id': '13',
                   'settings': self.setting({'questions': ['13.4']}),
                   'name': '4. Agencias de empleo 🏠 '}
            )
            Question.objects.create(
                **{'id': 112, 'flow_id': '13.4.1', 'parent_id': '13.4',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.4.1', '14']},
                   'name': 'Las agencias de empleo son empresas privadas cuyo objetivo radica en intermediar para la contratación de personas '
                           'trabajadoras del hogar, a cambio de un pago realizado por el empleador. '
                           'Estas tienen las siguientes prohibiciones:\n'
                           '● Cobrar o afectar la remuneración del trabajador/a para cobrar cualquier tipo '
                           'gasto realizado por la colocación del trabajador/a en un empleo.\n'
                           '● Retener el documento de identidad, objetos personales, de valor, '
                           'antecedentes penales, cartas de recomendación, o similares.'}
            )
            # Option main 5
            Question.objects.create(
                **{'id': 113, 'flow_id': '13.5', 'parent_id': '13',
                   'settings': self.setting({'questions': ['13.5']}),
                   'name': '5. Inspección del trabajo 👨‍🚒'}
            )
            # Option main 5 - 1
            Question.objects.create(
                **{'id': 114, 'flow_id': '13.5.1', 'parent_id': '13.5',
                   'settings': self.setting({'questions': ['13.5.1']}),
                   'name': '1. El rol de SUNAFIL'}
            )
            Question.objects.create(
                **{'id': 115, 'flow_id': '13.5.1.1', 'parent_id': '13.5.1',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.5.1.1', '14']},
                   'name': 'La Superintendencia de Fiscalización Laboral - SUNAFIL, es la entidad encargada de '
                           'vigilar y exigir el cumplimiento de las obligaciones sociolaborales y de seguridad'
                           ' y salud en el trabajo.'}
            )
            # Option main 5 - 2
            Question.objects.create(
                **{'id': 116, 'flow_id': '13.5.2', 'parent_id': '13.5',
                   'settings': self.setting({'questions': ['13.5.2']}),
                   'name': '2. Soy trabajadora del hogar ¿Puedo recurrir a SUNAFIL si me despiden?'}
            )
            Question.objects.create(
                **{'id': 117, 'flow_id': '13.5.2.1', 'parent_id': '13.5.2',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.5.2.1', '14']},
                   'name': 'Si te han despedido de tu trabajo y crees que ha sido injusto, puedes acudir a SUNAFIL para que revisen tu caso. \n '
                           'Luego de la verificación, te entregarán un “Acta de Verificación de Despido Arbitrario”, \n'
                           'que te servirá como prueba si decides presentar una demanda para solicitar una indemnización.\n'
                           '\n'
                           'Es importante que sepas que SUNAFIL no puede ordenar que te repongan en tu trabajo '
                           'ni exigir el pago de una indemnización por despido arbitrario. Sin embargo, '
                           'sí puede exigir que te paguen los beneficios laborales que te adeuden.\n'
                           '\n'
                           '📞 Si necesitas comunicarte con SUNAFIL, puedes llamar al (01) 3902800.'}
            )
            # Option main 5 - 3
            Question.objects.create(
                **{'id': 118, 'flow_id': '13.5.3', 'parent_id': '13.5',
                   'settings': self.setting({'questions': ['13.5.3']}),
                   'name': '3. Presentación de denuncia'}
            )
            Question.objects.create(
                **{'id': 119, 'flow_id': '13.5.3.1', 'parent_id': '13.5.3',
                   'settings': {'is_input': True, 'is_group': True, 'is_reload': True, 'questions': ['13.5.3.1', '14']},
                   'name': 'La persona trabajadora del hogar cuenta con diversos canales para presentar una denuncia:\n'
                           '● La plataforma  “Denuncia Virtual” de SUNAFIL: https://aplicativosweb2.sunafil.gob.pe/si.denunciasVirtuales\n'
                           '● El aplicativo “SUNAFIL en tus manos”, disponible para celulares Android: https://play.google.com/store/apps/details?id=pe.gob.sunafil.sunafilentusmanos\n'
                           '● La Mesa de partes presencial en nuestras diversas Intendencias Regionales y Sede Central.\n'
                           'Para conocer nuestras sedes y teléfonos, ingresa al siguiente enlace: https://www.gob.pe/institucion/sunafil/sedes'}
            )

            # Option de salida
            Question.objects.create(
                **{'id': 120, 'flow_id': '14', 'name': 'Chatbot XXX',
                   'settings': self.setting({'questions': ['14']})})
            Question.objects.create(
                **{'id': 121, 'flow_id': '14.0', 'parent_id': '14',
                   'settings': self.setting({'questions': ['14.0']}),
                   'name': '👋🏼 Sigo aquí para ayudarte 😊Digita el número de la opción que desees:'}
            )
            # Option main 14 - 1
            Question.objects.create(
                **{'id': 122, 'flow_id': '14.1', 'parent_id': '14',
                   'settings': self.setting({'questions': ['13']}),
                   'name': '1. Tengo otra consulta. ✍'}
            )
            # Option main 14 - 2
            Question.objects.create(
                **{'id': 123, 'flow_id': '14.2', 'parent_id': '14',
                   'settings': self.setting({'is_answer': False, 'questions': ['14.2'], 'questions_next': ['14.2']}),
                   'name': '2. Comunícame con un asesor.  👨‍💻 '}
            )
            Question.objects.create(
                **{'id': 124, 'flow_id': '14.2.1', 'parent_id': '14.2',
                   'settings': self.setting(
                       {'is_answer': False, 'questions': ['14.2.2'], 'questions_next': ['14.2.2']}),
                   'name': 'Los horarios de atencion son 8:30 am a 5:30 pm'}
            )
            Question.objects.create(
                **{'id': 125, 'flow_id': '14.2.2', 'parent_id': '14.2',
                   'settings': self.setting(
                       {'is_answer': False, 'questions': ['14.2.2'], 'questions_next': ['14.2.2']}),
                   'name': 'Dejanos tu numero de contacto y un asesor se comunicara contigo a la brevedad.'}
            )
            Question.objects.create(
                **{'id': 126, 'flow_id': '14.2.2.1', 'parent_id': '14.2.2',
                   'name': '¡Gracias por proporcionar tu número! Un asesor se pondrá en contacto contigo pronto. '
                           'Asimismo, ponemos a tu disposición información sobre los siguientes servicios:\n'
                           '•	“Trabaja Sin Acoso” a través de la línea gratuita 1819.\n'
                           '•	Atención de consultas laborales a través de la línea gratuita 0800-1-6872, opción 3 ('
                           'trabajo del hogar)\n'
                           '•	Servicio de Patrocinio Judicial Gratuito del MTPE, accesible en Av. Gral. Salaverry 655, '
                           'Jesús María\n'
                           '¡Que tengas un excelente día!'}
            )

            # Option main 14 - 3
            Question.objects.create(
                **{'id': 127, 'flow_id': '14.3', 'parent_id': '14',
                   'settings': self.setting({'is_answer': False, 'questions': ['14.3'], 'questions_next': ['14.3']}),
                   'name': '3. No tengo más consultas. 🔚'}
            )
            Question.objects.create(
                **{'id': 128, 'flow_id': '14.3.1', 'parent_id': '14.3',
                   'settings': self.setting({'is_answer': False, 'questions': ['14.3'], 'questions_next': ['13']}),
                   'name': '¡Gracias por acudir a nuestro servicio! ponemos a tu disposición información '
                           'sobre los siguientes servicios:\n'
                           '• “Trabaja Sin Acoso” a través de la línea gratuita 1819.\n'
                           '• Atención de consultas laborales a través de la línea gratuita 0800-1-6872,'
                           ' opción 3 (trabajo del hogar)\n'
                           '• Servicio de Patrocinio Judicial Gratuito del MTPE, accesible en Av. '
                           'Gral. Salaverry 655, Jesús María\n'
                           '¡Que tengas un excelente día!'}
            )
            Question.objects.create(
                **{'id': 129, 'flow_id': '14.3.2', 'parent_id': '14.3.1',
                   'settings': self.setting({'questions': ['14.3.1']}),
                   'name': '😊Gracias por contactarte con nosotros, si me necesitas nuevamente, '
                           'estaré aquí para ayudarte. ¡Hasta pronto! 👋🏼'}
            )

        def reset(self):
            User.objects.all().delete()
            Question.objects.all().delete()

        def setting(self, obj):
            settings = {'is_input': True, 'is_answer': True, 'is_group': True, 'questions': ['13.1']}
            settings.update(obj)
            return settings

    def reset(self):
        User.objects.all().delete()
        Question.objects.all().delete()

    def setting(self, obj):
        settings = {'is_input': True, 'is_answer': True, 'is_group': True, 'questions': ['13.1']}
        settings.update(obj)
        return settings
