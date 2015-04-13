# coding: utf-8
from faker.providers.person.ru_RU import Provider as BaseProvider
from third_names import MALE as THIRD_MALE_NAMES, FEMALE as THIRD_FEMALE_NAMES
from nations import NATIONS, MALE as MALE_NATIONS, FEMALE as FEMALE_NATIONS
from marriage import STATUSES as MARRIAGE_STATUSES
from education import TYPES as EDUCATION_TYPES, DOCS as EDUCATION_DOCS
from language import LANGUAGES


class Provider(BaseProvider):
    """
    Провайдер для персональных данных человека
    """
    # формат Фамилия Имя Отчество
    fullname_format = ['{{last_name}} {{first_name}} {{third_name}}']
    # формат Имя Отчество Фамилия
    fullname_reverse_format = ['{{first_name}} {{third_name}} {{last_name}}']
    # формат Фамилия И.О.
    initials_format = [
        '{{last_name}} {{first_name_initial}}.{{third_name_initial}}.']
    # формат И.О. Фамилия
    initials_reverse_format = [
        '{{first_name_initial}}.{{third_name_initial}}. {{last_name}}']
    # мужские отчества
    third_male_names = THIRD_MALE_NAMES
    # женские отчества
    third_female_names = THIRD_FEMALE_NAMES
    # отчества
    third_names = THIRD_MALE_NAMES + THIRD_FEMALE_NAMES
    # национальности во множественном числе
    multi_nations = NATIONS
    # национальности мужского рода
    male_nations = MALE_NATIONS
    # нациоанльности женского рода
    female_nations = FEMALE_NATIONS
    # семейные положения
    marriage_statuses = MARRIAGE_STATUSES
    # виды образования
    education_types = EDUCATION_TYPES
    # документы об образовании
    education_docs = EDUCATION_DOCS
    # языки
    languages = LANGUAGES

    @classmethod
    def first_name_initial(cls):
        """
        Возвращает инициал имени человека
        :return: Инициал имени человека
        :rtype: unicode
        """
        return cls.first_name()[0]

    @classmethod
    def third_name_initial(cls):
        """
        Возвращает инициал отчества человека
        :return: Инициал отчества человека
        :rtype: unicode
        """
        return cls.third_name()[0]

    @classmethod
    def third_name(cls):
        """
        Возвращает отчество человека
        :return: Отчество
        :rtype: unicode
        """
        return cls.random_element(cls.third_names)

    @classmethod
    def third_male_name(cls):
        """
        Возвращает мужское отчество
        :return: Отчество
        :rtype: unicode
        """
        return cls.random_element(cls.third_male_names)

    @classmethod
    def third_female_name(cls):
        """
        Возвращает женское отчество
        :return: Отчество
        :rtype: unicode
        """
        return cls.random_element(cls.third_female_names)

    def fullname(self, reverse=False):
        """
        Возвращает полное ФИО (ИОФ) человека
        :param reverse: ФИО, если reverse == False, иначе ИОФ
        :type reverse: bool
        :return: ФИО (ИОФ)
        :rtype: unicode
        """
        format_ = (
            self.fullname_reverse_format if reverse else self.fullname_format)
        pattern = self.random_element(format_)

        return self.generator.parse(pattern)

    def initials(self, reverse=False):
        """
        Возвращает фамилию и инициалы человека
        :param reverse: Фамилия И.О., если reverse == False, иначе И.О. Фамилия
        :type reverse: bool
        :return: Фамилия И.О. (И.О. Фамилия)
        :rtype: unicode
        """
        format_ = (
            self.initials_reverse_format if reverse else self.initials_format)
        pattern = self.random_element(format_)

        return self.generator.parse(pattern)

    # FIXME: Работает некорректно
    def person_inn(self):
        """
        Возвращает ИНН физического лица
        :return: ИНН физического лица
        :rtype: unicode
        """
        def get_element(indexes):
            _sum = sum(map(lambda x: int(x[0]) * x[1], zip(inn, indexes)))

            return str(_sum % 11 % 10)

        base_indexes = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
        extended_indexes = [3] + base_indexes
        inn = self.numerify('##########')
        element_11 = get_element(base_indexes)
        element_12 = get_element(extended_indexes)
        inn += element_11 + element_12

        return inn

    @classmethod
    def nations(cls):
        """
        Возвращает национальность во множественном числе
        :return: Национальность
        :rtype: unicode
        """
        return cls.random_element(cls.multi_nations)

    @classmethod
    def male_nation(cls):
        """
        Возвращает национальность мужского рода
        :return: Национальность
        :rtype: unicode
        """
        return cls.random_element(cls.male_nations)

    @classmethod
    def female_nation(cls):
        """
        Возвращает национальность женского рода
        :return: Национальность
        :rtype: unicode
        """
        return cls.random_element(cls.female_nations)

    @classmethod
    def marriage_status(cls):
        """
        Возвращает семейной положение человека
        :return: Семейное положение
        :rtype: unicode
        """
        return cls.random_element(cls.marriage_statuses)

    @classmethod
    def education_type(cls):
        """
        Возвращает вид образования человека
        :return: Вид образования
        :rtype: unicode
        """
        return cls.random_element(cls.education_types)

    @classmethod
    def education_doc(cls):
        """
        Возвращает документ об образовании человека
        :return: Документ об образовании
        :rtype: unicode
        """
        return cls.random_element(cls.education_docs)

    @classmethod
    def language(cls):
        """
        Возвращает язык человека
        :return: Язык
        :rtype: unicode
        """
        return cls.random_element(cls.languages)