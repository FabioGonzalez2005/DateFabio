from __future__ import annotations

class Date:
    def __init__(self, day: int, month: int, year: int):
        '''Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        El 1-1-1900 fue lunes.
        '''
        self.day = day
        self.month = month
        self.year = year
        if self.day <= 0 or self.day > 31:
            self.day = 1
        if self.month <= 0 or self.month > 12:
            self.month = 1
        if self.year < 1900 or self.year > 2050:
            self.year = 1900

    @staticmethod
    def is_leap_year(year: int) -> bool:
        resultado = False
        if year % 4 == 0 and year % 100 != 0 or year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            resultado = True
        return resultado

    @staticmethod
    def days_in_month(month: int, year: int) -> int:
        if month == 2:
            if Date.is_leap_year(year):
                return 29  
            else:
                return 28
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 31

    def get_delta_days(self) -> int:
        '''Número de días transcurridos desde el 1-1-1900 hasta la fecha'''
        days = 0
        for x in range(1900, self.year):
            if Date.is_leap_year(x):
                days += 366
            else:
                days += 365
        for y in range(1, self.month):
            days += Date.days_in_month(y, self.year)
        days += self.day - 1
        return days

    @property
    def weekday(self) -> int:
        '''Día de la semana de la fecha (0 para domingo, ..., 6 para sábado).'''
        dayInWeek = (self.get_delta_days() + 1) % 7
        return dayInWeek

    @property
    def is_weekend(self) -> bool:
        '''Saber si el día es entre lunes y viernes.'''
        if self.weekday == 0 or self.weekday > 5:
            return True
        else:
            return False
        
    @property
    def short_date(self) -> str:
        '''Poner la fecha corta (02/09/2003)'''
        day = self.day
        month = self.month

        if self.day < 10:
            day = '0' + str(self.day)

        if self.month < 10:
            month = '0' + str(self.month)
    
        return f"{day}/{month}/{self.year}"
        
    def __str__(self):
        '''Poner la fecha de forma larga'''
        dias_semana = ["DOMINGO", "LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SABADO",]
        meses = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
        return f"{dias_semana[self.weekday]} {self.day} DE {meses[self.month - 1]} DE {self.year}"

    def __add__(self, days: int) -> Date:
        '''Sumar un número de días a la fecha'''
        year = self.year
        month = self.month
        day = self.day
        while days > 0:
            daysInMonth = Date.days_in_month(month, year) - day + 1
            if days >= daysInMonth:
                days -= daysInMonth
                month += 1
                if month > 12:
                    month = 1
                    year += 1
                day = 1
            else:
                day += days
                days = 0
        return Date(day, month, year)

    def __sub__(self, other: Date | int) -> int | Date:
        '''Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días'''
        if isinstance(other, Date):
            return self.get_delta_days() - other.get_delta_days()
        
        '''2) Restar un número de días la fecha -> Nueva fecha'''
        year = self.year
        month = self.month
        day = self.day

        day -= other
        while day < 1:
            month -= 1
            if month < 1:
                month = 12
                year -= 1
            day += Date.days_in_month(month, year)

        return Date(day, month, year)

    def __lt__(self, other: Date) -> bool:
        return self.get_delta_days() < other.get_delta_days()

    def __gt__(self, other: Date) -> bool:
        return self.get_delta_days() > other.get_delta_days()

    def __eq__(self, other: Date) -> bool:
        return self.get_delta_days() == other.get_delta_days()