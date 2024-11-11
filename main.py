import telebot
from telebot import types
from descriptive_variables import *             
import openai
import time
import os

openai.api_key = "OPENAI_TOKEN"

bot = telebot.TeleBot('BOT_TOKEN')#token code

print('Сервер запущен')
def detect_user_activity(message):
    user_info = dict()

    user_info['id'] = message.from_user.id
    user_info['username'] = message.from_user.username
    user_info['firstname'] = message.from_user.first_name
    user_info['lastname'] = message.from_user.last_name
    user_info['request'] = message.text.replace('◀️', '')
    user_info['time'] =  time.strftime('%d.%m.%Y г. %H:%M:%S')
    with open("doc.txt", "a", encoding='cp1251') as f:
        f.write(str(user_info))
        f.write('\n')
    
    print(user_info)


def main_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
    btn_school = types.KeyboardButton('О Школе')
    btn_exams = types.KeyboardButton('Экзамены')
    btn_universities = types.KeyboardButton('Поступление в вузы')
    btn_help = types.KeyboardButton('Помощь с профессией')
    btn_sources = types.KeyboardButton('Источники')
    btn_mektepomiri = types.KeyboardButton('Школьная жизнь')


    markup.add(btn_school, btn_mektepomiri)
    markup.row(btn_exams, btn_sources)
    markup.row(btn_universities, btn_help)
    
    
    return markup
    
    
@bot.message_handler(commands=['start'])
def start(message):
    mes = f'👋 Привет, <b>{message.from_user.first_name}</b>. Я твой NIS ассистент'
    markup = main_buttons(message)
    bot.send_message(message.chat.id, mes, parse_mode='html', reply_markup=markup)
    
    
    
@bot.message_handler(func=lambda _:True)
def get_user_text(message):
    detect_user_activity(message)
    os.system('C:\school_bot\doc.txt')
    user_message = message.text.lower()
    
    if user_message == 'о школе':
        markup = types.InlineKeyboardMarkup()
        btn_mission = types.InlineKeyboardButton('🎯 Миссия школы', callback_data='mission')
        btn_values = types.InlineKeyboardButton('🧩 Ценности школы', callback_data="values")
        btn_all =types.InlineKeyboardButton('📄 Получить весь документ', callback_data='all_print')   
        btn_tarbie =types.InlineKeyboardButton('📔 Воспитательная часть', callback_data='tarbie')    
                                                                                                                                                                     
        
        
        markup.row(btn_mission, btn_values)
        markup.add(btn_tarbie)
        markup.add(btn_all)
        bot.send_message(message.chat.id, "Выберите раздел", reply_markup=markup)
    
    elif user_message == 'школьная жизнь':
        markup = types.InlineKeyboardMarkup()
        btn_shanyrak = types.InlineKeyboardButton('Шаныраки', callback_data='shanyrak')
        btn_tutor =types.InlineKeyboardButton('Кураторы', callback_data='tutor')    
                                                                                                                                                                     
        
        
        markup.row(btn_shanyrak)
        markup.add(btn_tutor)
  
        bot.send_message(message.chat.id, "Выберите раздел", reply_markup=markup)

    elif user_message == 'ielts':
        markup = types.InlineKeyboardMarkup()
        btn_structer = types.InlineKeyboardButton('Структура экзамена', callback_data='ielts_structure')
        btn_tips = types.InlineKeyboardButton('Советы по подготовке', callback_data="ielts_tips")                                                                                                                                                                  
        
        
        markup.add(btn_structer)
        markup.add(btn_tips)
        markup.add(types.InlineKeyboardButton('Материалы по подготовке', url = 'https://drive.google.com/drive/u/0/folders/1wX7YGbWc3wAqxEsZtKwjQ9xujiwzrDoI?direction=a'))
        markup.add(types.InlineKeyboardButton('Забронировать место', url = 'https://kazakhstan.britishcouncil.org/ru/exam/ielts/book-test?gclid=CjwKCAjwvdajBhBEEiwAeMh1U94w6-QRxKrJS90jrWzboqDANCuZ210LlzMhuwOemjodPv95aZgAzxoCsQwQAvD_BwE'))
        bot.send_message(message.chat.id,  IELTS_ABOUT_STR, parse_mode='html', reply_markup=markup)
    
    

    elif user_message == 'экзамены':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn0 = types.KeyboardButton('◀️Главное меню')
        btn1 = types.KeyboardButton('SAT')
        btn2 = types.KeyboardButton('IELTS')
        btn3 = types.KeyboardButton('МЭСК')
        
        markup.add(btn0, btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup)
    elif user_message == 'sat':
        markup = types.InlineKeyboardMarkup()
        btn_structer1 = types.InlineKeyboardButton('Структура экзамена', callback_data='sat_structure')
        btn_tips1 = types.InlineKeyboardButton('Советы по подготовке', callback_data="sat_tips")                                                                                                                                                                  
        btn_sources1 = types.InlineKeyboardButton('Материалы по подготовке', callback_data='sat_sources')

        markup.add(btn_structer1)
        markup.add(btn_tips1)
        markup.add(btn_sources1)
        markup.add(types.InlineKeyboardButton('Забронировать место', url = 'https://satsuite.collegeboard.org/sat/registration'))
        bot.send_message(message.chat.id, SAT_ABOUT_STR, parse_mode='html', reply_markup=markup)

    elif user_message == 'мэск':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn4 = types.KeyboardButton('◀️Главное меню')
        btn5 = types.KeyboardButton('10 класс')
        btn6 = types.KeyboardButton('11 класс')
        btn7 = types.KeyboardButton('12 класс')
        
        markup.add(btn5, btn6, btn7, btn4)
        bot.send_message(message.from_user.id, "Выберите класс", reply_markup=markup)
    
    elif user_message == '10 класс':
        markup = types.InlineKeyboardMarkup()
        btn_subjects = types.InlineKeyboardButton('Предметы', callback_data='mesk_grade_10_subjects')                                                                                                                                                                
        btn_sources2 = types.InlineKeyboardButton('Материалы по подготовке', callback_data='mesk_grade_10_sources')

        markup.row(btn_subjects,btn_sources2)
        bot.send_message(message.chat.id, MESK_GRADE_10_ABOUT_STR, parse_mode='html', reply_markup=markup)
    
    elif user_message == '11 класс':
        markup = types.InlineKeyboardMarkup()
        btn_subjects11 = types.InlineKeyboardButton('Предметы', callback_data='mesk_grade_11_subjects')                                                                                                                                                                
        btn_sources11 = types.InlineKeyboardButton('Материалы по подготовке', callback_data='mesk_grade_11_sources')

        markup.row(btn_subjects11,btn_sources11)
        bot.send_message(message.chat.id, MESK_GRADE_11_ABOUT_STR, parse_mode='html', reply_markup=markup)
    
    elif user_message == '12 класс':
        markup = types.InlineKeyboardMarkup()
        btn_subjects12 = types.InlineKeyboardButton('Предметы', callback_data='mesk_grade_12_subjects')                                                                                                                                                                
        btn_sources12 = types.InlineKeyboardButton('Материалы по подготовке', callback_data='mesk_grade_12_sources')

        markup.row(btn_subjects12,btn_sources12)
        bot.send_message(message.chat.id, MESK_GRADE_12_ABOUT_STR, parse_mode='html', reply_markup=markup)
    
    elif user_message == 'документы':
        markup = types.InlineKeyboardMarkup()
        btn_subjects5 = types.InlineKeyboardButton('Страна и программа', callback_data='strana_programma')                                                                                                                                                                
        btn_sources5 = types.InlineKeyboardButton('Финансирование', callback_data='finances')
                                                                                                                                                                   
        btn_sources55 = types.InlineKeyboardButton('Стратегии', callback_data='strategies')
        btn_subjects555 = types.InlineKeyboardButton('Ожидание ответов', callback_data='expect')                                                                                                                                                                
        btn_sources555 = types.InlineKeyboardButton('Важно', callback_data='important')

        markup.row(btn_subjects5)
        markup.row(btn_sources5)
        markup.row(btn_sources55)
        markup.row(btn_subjects555)
        markup.row(btn_sources555)

        bot.send_message(message.chat.id, DOCUM_TEXT, parse_mode='html', reply_markup=markup)

    elif user_message == 'типы документов':
        markup = types.InlineKeyboardMarkup()
        btn_motiv = types.InlineKeyboardButton('Мотивационное эссе', callback_data='motivational_letter')
        btn_recom = types.InlineKeyboardButton('Рекомендательно письмо', callback_data="recomendational_letter")                                                                                                                                                                  
        btn_trans = types.InlineKeyboardButton('Перевод диплома', callback_data="diploma_translation")
        btn_resum = types.InlineKeyboardButton('Академическое резюме', callback_data="academic_resume")
        btn_common = types.InlineKeyboardButton('СommonApp', callback_data="common_app")
        btn_cssprof = types.InlineKeyboardButton('CSS Profile', callback_data="css_profile")

        markup.add(btn_motiv)
        markup.add(btn_recom)
        markup.add(btn_trans)
        markup.add(btn_resum)
        markup.add(btn_common)
        markup.add(btn_cssprof)
      
        markup.add(types.InlineKeyboardButton('Заполнение CommonApp', url = 'https://www.commonapp.org/'))
        markup.add(types.InlineKeyboardButton('Заполнение CSS Profile', url = 'https://cssprofile.collegeboard.org/'))
        bot.send_message(message.chat.id,  DOCUMENTS, parse_mode='html', reply_markup=markup)

    elif user_message == '◀️главное меню':   
        markup = main_buttons(message)
        bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup)
    elif user_message == '/site':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Посетить веб сайт', url = 'https://fmsh.nis.edu.kz/'))
        bot.send_message(message.chat.id, '🌐 Перейдите на сайт', reply_markup=markup)
    elif user_message == '/connectwithprof':   
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Нажмите для перехода', url = 'https://wa.me/+77072700077'))
        bot.send_message(message.chat.id, 'Свяжитесь с нашим профориентатором(Марат Алибекович)', reply_markup=markup)

    elif user_message == '/connectwithadmin':   
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Нажмите для перехода', url = 'https://wa.me/+77479394705'))
        bot.send_message(message.chat.id, 'Свяжитесь с Гаухар Сапаргалиевной!', reply_markup=markup)
    elif user_message == 'поступление в вузы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn_back = types.KeyboardButton('◀️Главное меню')
        btn_sat = types.KeyboardButton('SAT')
        btn_gpa = types.KeyboardButton('GPA')
        btn_ielts = types.KeyboardButton('IELTS')
        btn_mesk = types.KeyboardButton('МЭСК(12 класс)')
        btn_docs = types.KeyboardButton('Документы')
        btn_types = types.KeyboardButton('Типы документов')
        
        markup.add(btn_sat, btn_ielts)
        markup.add(btn_mesk, btn_gpa)
        markup.add(btn_docs, btn_types)
        markup.add(btn_back)
        bot.send_message(message.from_user.id, UNI_ADMISSION_STR, reply_markup=markup)
    else:
        markup = main_buttons(message)
        response = "Используй ключевые слова!"

        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # prompt=message.text,
        temperature=0.9,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        messages=[
        
        {"role": "user", "content": f"{message.text}"}]
        )
        bot.send_message(chat_id=message.from_user.id, text = response)
   

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'all_print':
        img = open('sources/image.jpg', 'rb')
        bot.send_document(callback.message.chat.id, img)
    elif callback.data == 'shanyrak':
        doc_1 = open('sources/shanyrak.docx', 'rb')
        bot.send_document(callback.message.chat.id, doc_1)
    elif callback.data == 'tutor':
        doc_2 = open('sources/tutor.docx', 'rb')
        bot.send_document(callback.message.chat.id, doc_2)
   
    else:
        bot.send_message(callback.message.chat.id, callback_functions_dict[callback.data], parse_mode='html')


   
        
bot.polling() #обязательная для работы бота часть
