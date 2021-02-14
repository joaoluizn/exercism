import unittest

from hotel_book import HotelBook

class BookHotelTest(unittest.TestCase):
      
    def test_book_regular_week_success(self):
        book = HotelBook()
        self.assertEqual(book.find_best_hotel_options("Regular: 16Mar2020(mon), 17Mar2020(tues), 18Mar2020(wed)"), "Parque das flores")
      
    def test_book_regular_week_and_weekend_success(self):
        book = HotelBook()
        self.assertEqual(book.find_best_hotel_options("Regular: 20Mar2020(fri), 21Mar2020(sat), 22Mar2020(sun)"), "Jardim Botânico")

    def test_book_premium_week_and_weekend_success(self):
        book = HotelBook()
        self.assertEqual(book.find_best_hotel_options("Fidelidade: 26Mar2020(thur), 27Mar2020(fri), 28Mar2020(sat)"), "Mar Atlântico")

    def test_book_non_consecutive_dates_fail(self):
        book = HotelBook()
        with self.assertRaises(ValueError):
            book.find_best_hotel_options("Fidelidade: 26Mar2020(thur), 29Mar2020(fri), 28Mar2020(sat)")


if __name__ == '__main__':
    unittest.main()
