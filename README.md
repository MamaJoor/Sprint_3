reg_ren.py - генератор логинов и паролей, подключен только в тестах с регистрацией

test_registration.py - файл с набором тестов на регистрацию:
    def test_registration_with_correct_data_reg_success(self) - тест на регистрацию с корректными логином и паролем
    def test_registration_with_incorrect_password_password_error(self) - тест на регистрацию с проверкой некорректного пароля

test_log_in.py - файл с набором тестов на авторизацию (вход) с существующими данными:
    def test_log_in_from_main_page_enter_button_log_in_success(self) - тест входа с главной страницы через кнопку "Войти в аккаунт"
    def test_log_in_from_main_page_personal_account_button_log_in_success(self) - тест входа с главной страницы через кнопку "Личный Кабинет"
    def test_log_in_from_reg_page_enter_button_log_in_success(self) - тест входа со страницы регистрации через кнопку "Вход"
    def test_log_in_from_password_recovery_page_enter_button_log_in_success(self) - тест входа со страницы восстановления пароля

test_personal_account_transition.py - файл с набором тестов перехода с главной страницы в личный кабинет:
    def test_log_in_from_main_page_enter_button_log_in_success(self) - тест перехода из главной страницы в личный кабинет

test_from_account_to_constructor_transition.py - файл с набором тестов перехода из личного кабинет в конструктор 
    def test_transition_from_personal_account_to_main_by_construction_button_success(self) - тест перехода из личного кабинета в конструктор через нажатие на кнопку "Конструктор"
    def test_transition_from_personal_account_to_main_by_logo_button_success(self) - тест перехода из личного кабинета в конструктор через нажатие на лого 

test_log_out.py - файл с набором тестов на выход из аккаунта:
    def test_log_out_from_personal_account_logout_success(self) - тест на выход из аккаунта через кнопку "Выход" в личном кабинете

test_constructor_chapter.py - файл с набором тестов на переходы между разделами в конструкторе:
        def test_construction_chapter_transition_to_bulki_bulki_is_visible(self) - тест на переход на в раздел "Булки"
        def test_construction_chapter_transition_to_sousi_sousi_is_visible(self) - тест на переход на в раздел "Соусы"
        def test_construction_chapter_transition_to_nachinki_nachinki_is_visible(self) - тест на переход на в раздел "Начинки"
    

Комментарий: не получилось положить файл reg_ren.py в корневую директорию проекта, тесты его не видят, не понял как правильно использовать import в этом случае
