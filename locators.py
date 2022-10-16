urls = {'main_page': 'https://stellarburgers.nomoreparties.site',  # ссылка на главную страницу
        'registration_page': 'https://stellarburgers.nomoreparties.site/register',  # ссылка на страницу регистрации
        'log_in_page': 'https://stellarburgers.nomoreparties.site/login',  # сслыка на страницу входа
        'password_recovery_page': 'https://stellarburgers.nomoreparties.site/forgot-password'}  # ссылка на страницу
# восстановления пароля

locators = {'reg_name_field': './/fieldset/div/div/input',  # поле "имя" на странице регистрации
            'reg_email_field': './/fieldset[2]/div/div/input',  # поле "email" на странице регистрации
            'reg_password_field': './/fieldset[3]/div/div/input',  # поле "password" на странице регистрации
            'reg_reg_button': './/button[text() = "Зарегистрироваться"]',  # кнопка "зарегистрироватся" на странице регистрации
            'reg_log_in_button': '//*[@id="root"]/div/main/div/div/p/a',  # кнопка "войти" на странице регистрации
            'reg_password_error': './/p[text() = "Некорректный пароль"]',  # ошибка при некорректном вводе пароля на странице регистрации
            'log_in_email_field': './/fieldset/div/div/input',  # поле "email" на странице входа
            'log_in_password_field': './/fieldset[2]/div/div/input',  # поле "password" на странице входа
            'lod_in_login_button': './/button[text() = "Войти"]',  # кнопка "войти" на странице входа
            'main_page_log_in_button_': './/button[text() = "Войти в аккаунт"]',  # кнопка "Войти в аккаунт" на главной странице
            'transition_to_personal_account': './/p[text() = "Личный Кабинет"]',  # кнопка "Личный Кабинет" на главной странице
            'password_recovery_enter_button': '//a[text() = "Войти"]',  # кнопка "Восстановить пароль" на странице входа
            'personal_account_to_construction_button': '//*[@id="root"]/div/header/nav/ul/li[1]/a/p', # кнопка перехода из личного кабинета в конструктор
            'logo': './/svg[@xmlns="http://www.w3.org/2000/svg"]',  # "кнопка лого Stellar Burgers"
            'constructor_bulki_button': './/span[text() = "Булки"]',  # кнопка "Булки" в конструкторе
            'constructor_sousi_button': './/span[text() = "Соусы"]',  # кнопка "Соусы" в конструкторе
            'constructor_nachinki_button': './/span[text() = "Начинки"]',  # кнопка "Начинки" в конструкторе
            'flag_bulki_visible': './/span[text() = "Булки"]',  # флаг, что "Булки" видны
            'flag_sousi_visible': './/span[text() = "Соусы"]',  # флаг, что "Соусы" видны
            'flag_nachinki_visible': './/span[text() = "Начинки"]'  # флаг, что "Начинки" видны
            }
