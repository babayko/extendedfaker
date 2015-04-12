# coding: utf-8
from faker.providers.person.ru_RU import Provider as BaseProvider
from third_male_names import THIRD_MALE_NAMES
from third_female_names import THIRD_FEMALE_NAMES


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
            return str(
                sum(
                    map(lambda x: int(x[0]) * x[1], zip(inn, indexes))
                ) / 11 / 10)

        base_indexes = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
        extended_indexes = [3] + base_indexes
        inn = self.numerify('##########')
        element_11 = get_element(base_indexes)
        element_12 = get_element(extended_indexes)
        inn += element_11 + element_12

        return inn










