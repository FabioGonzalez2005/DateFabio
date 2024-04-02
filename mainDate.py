from date import Date

def main():
    print("Días en febrero de 2020:", Date.days_in_month(5, 2021))

    date1 = Date(1, 1, 2021)
    print("Días transcurridos desde el 1-1-1900 hasta el date1:", date1.get_delta_days())
    print("Fecha corta de la date1:", date1.short_date)
    print("Día de la semana de la date1:", date1.weekday)
    print("¿Cae en fin de semana?", date1.is_weekend)

    date2 = date1 + 365
    print("date1 más 365 días:", date2)

main()