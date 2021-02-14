""" A simple solution for best option hotel booking """

import datetime
from typing import List


class HotelBook:
    """ find best option between hotels to a given user and date interval """

    HOTELS = {
        'Parque das flores': {'Regular': {'week': 110, 'weekend': 90},
        'Fidelidade': {'week': 80, 'weekend': 80},
        'rate': 3},
        'Jardim Botânico': {'Regular': {'week': 160, 'weekend': 60},
        'Fidelidade': {'week': 110, 'weekend': 50},
        'rate': 4},
        'Mar Atlântico': {'Regular': {'week': 220, 'weekend': 150},
        'Fidelidade': {'week': 100, 'weekend': 40},
        'rate': 5}
    }

    def find_best_hotel_options(self, information: str) -> str:
        """
        Finds best hotel option given user information

        :param str information: given user information
        :return str: the best option hotel name
        """
        user_type, interval = information.split(': ')
        date_interval = interval.replace(' ', '').split(',')
        date_interval = self.__convert_datestr_to_datetime(date_interval)

        if self.__validate_date_interval(date_interval):
            number_of_week_days_types = self.count_week_and_weekend_days(
                date_interval)

            week_days = number_of_week_days_types.get('week_days')
            weekend_days = number_of_week_days_types.get('weekend_days')

            return self.__find_best_hotel_for_user(user_type, week_days, weekend_days)
        else:
            raise ValueError("Dates should be formed of consecutive dates.")

    @staticmethod
    def count_week_and_weekend_days(date_list: List[str]) -> dict:
        week = 0
        weekend = 0
        for date in date_list:
            if date.weekday() > 4:
                weekend += 1
            else:
                week += 1

        return dict(week_days=week, weekend_days=weekend)

    def __find_best_hotel_for_user(self, user_type: str, week_days: int, weekend_days: int) -> str:
        first = True
        best_option = {}

        for hotel_name, hotel_info in self.HOTELS.items():
            hotel_prices_for_user = hotel_info.get(user_type)
            total_value = self.get_total_value_for_hotel_book(
                hotel_prices_for_user, week_days, weekend_days)
            new_option = {'name': hotel_name,
                          'price': total_value, 'rate': hotel_info.get('rate')}

            if first:
                best_option = new_option
                first = False
            else:
                best_option = self.compare_best_option(
                    best_option, new_option)
        return best_option.get('name')

    @staticmethod
    def get_total_value_for_hotel_book(hotel_prices: dict, week_days: int, weekend_days: int) -> int:
        return hotel_prices.get('week') * week_days + hotel_prices.get('weekend') * weekend_days

    @staticmethod
    def compare_best_option(best_option: dict, new_option: dict) -> dict:
        is_new_option_cheaper = best_option.get(
            'price', 0) > new_option.get('price')
        are_options_same_price = best_option.get(
            'price', 0) == new_option.get('price')
        is_new_option_hig_rate = best_option.get(
            'rate', 0) < new_option.get('rate')
        is_new_option_same_price_with_high_rate = are_options_same_price and is_new_option_hig_rate

        return new_option if is_new_option_cheaper or is_new_option_same_price_with_high_rate else best_option
    
    def __convert_datestr_to_datetime(self, dates):
        clear_date_strings = [date.split('(')[0] for date in dates]
        return [datetime.datetime.strptime(date, '%d%b%Y') for date in clear_date_strings]

    def __validate_date_interval(self, dates) -> bool:
        def consecutive(a, b, step=datetime.timedelta(days=1)):
            return (a + step) == b
        return all(consecutive(dates[i], dates[i+1]) for i in range(len(dates) - 1))
