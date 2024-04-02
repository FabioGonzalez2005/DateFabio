from date import Date

def main():
    print("Días en febrero de 2020:", Date.days_in_month(5, 2021))

    date1 = Date(1, 1, 2020)
    print("Días transcurridos desde el 1-1-1900 hasta el 1-1-2020:", date1.get_delta_days())
    print("Fecha corta de la fecha 1:", date1.short_date)

main()