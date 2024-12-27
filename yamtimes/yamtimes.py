import locale
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta  
import calendar


class YamTimes:
    def __init__(self,year = None, month = None, day = None, hour = None, minute = None, dt=None):
        """
        Initializes the YamTimes object, setting the date and time based on the given parameters or the current datetime.

        Parameters:
        - year (int, optional): The year to set. Defaults to the current year if not provided.
        - month (int, optional): The month to set. Defaults to the current month if not provided.
        - day (int, optional): The day to set. Defaults to the current day if not provided.
        - hour (int, optional): The hour to set. Defaults to the current hour if not provided.
        - minute (int, optional): The minute to set. Defaults to the current minute if not provided.
        - dt (datetime, optional): A specific datetime object to set. If not provided, the current datetime is used.
        """
        self.__datetime = datetime
        if dt is None:
            self.__datetime : datetime = datetime.now()
            if(year is not None or month is not None or day is not None or hour is not None or minute is not None):
                self.__datetime = datetime(year if year is not None else self.__datetime.year,month if month is not None else self.__datetime.month,day if day is not None else self.__datetime.day,hour if hour is not None else self.__datetime.hour,minute if minute is not None else self.__datetime.minute)
        else:
            self.__datetime : datetime = dt

    def to_datetime(self) -> datetime:
        """
        Returns the datetime object stored in the YamTimes instance.

        Returns:
        - datetime: The datetime object representing the stored date and time.
        """

        return self.__datetime

    def is_aries_sign(self) -> bool:
        """
        Checks if the current date corresponds to the Aries zodiac sign.

        Returns:
        - bool: True if the current date is within the Aries range (March 21 - April 19), False otherwise.
        """

        return self.__is_between_dates(3, 21, 4, 19)

    def is_taurus_sign(self) -> bool:
        """
        Checks if the current date corresponds to the Taurus zodiac sign.

        Returns:
        - bool: True if the current date is within the Taurus range (April 20 - May 20), False otherwise.
        """

        return self.__is_between_dates(4, 20, 5, 20)

    def is_gemini_sign(self) -> bool:
        """
        Checks if the current date corresponds to the Gemini zodiac sign.

        Returns:
        - bool: True if the current date is within the Gemini range (May 21 - June 20), False otherwise.
        """
        return self.__is_between_dates(5, 21, 6, 20)

    def is_cancer_sign(self) -> bool:
        """
        Checks if the current date corresponds to the Cancer zodiac sign.

        Returns:
        - bool: True if the current date is within the Cancer range (June 21 - July 22), False otherwise.
        """
        return self.__is_between_dates(6, 21, 7, 22)

    def is_leo_sign(self) -> bool:
        """
        Checks if the current date corresponds to the Leo zodiac sign.

        Returns:
        - bool: True if the current date is within the Leo range (July 23 - August 22), False otherwise.
        """
        return self.__is_between_dates(7, 23, 8, 22)

    def is_virgo_sign(self) -> bool:
        """
        Checks if the current date corresponds to the Virgo zodiac sign.

        Returns:
        - bool: True if the current date is within the Virgo range (August 23 - September 22), False otherwise.
        """
       
        return self.__is_between_dates(8, 23, 9, 22)

    def is_libra_sign(self) -> bool:
        """
        Checks if the current date corresponds to the Libra zodiac sign.

        Returns:
        - bool: True if the current date is within the Libra range (September 23 - October 22), False otherwise.
        """
        
        return self.__is_between_dates(9, 23, 10, 22)

    def is_scorpio_sign(self) -> bool:
        """
        Checks if the current date corresponds to the Scorpio zodiac sign.

        Returns:
        - bool: True if the current date is within the Scorpio range (October 23 - November 21), False otherwise.
        """
        
        return self.__is_between_dates(10, 23, 11, 21)

    def is_sagittarius_sign(self) -> bool:
        """
        Checks if the current date corresponds to the Sagittarius zodiac sign.

        Returns:
        - bool: True if the current date is within the Sagittarius range (November 22 - December 21), False otherwise.
        """
        return self.__is_between_dates(11, 22, 12, 21)

    def is_capricorn_sign(self) -> bool:
        """
        Checks if the current date corresponds to the Capricorn zodiac sign.

        Returns:
        - bool: True if the current date is within the Capricorn range (December 22 - January 19), False otherwise.
        """
        return self.__is_between_dates(12, 22, 1, 19)

    def is_aquarius_sign(self) -> bool:
        """
        Checks if the current date corresponds to the Aquarius zodiac sign.

        Returns:
        - bool: True if the current date is within the Aquarius range (January 20 - February 18), False otherwise.
        """
        
        return self.__is_between_dates(1, 20, 2, 18)

    def is_pisces_sign(self) -> bool:
        """
        Checks if the current date corresponds to the Pisces zodiac sign.

        Returns:
        - bool: True if the current date is within the Pisces range (February 19 - March 20), False otherwise.
        """
        
        return self.__is_between_dates(2, 19, 3, 20)

    def __is_between_dates(self, start_month: int, start_day: int, end_month: int, end_day: int) -> bool:
        date = self.__datetime
        if start_month < end_month or (start_month == end_month and start_day <= end_day):
            return (start_month == date.month and start_day <= date.day) or \
                   (end_month == date.month and date.day <= end_day) or \
                   (start_month < date.month < end_month)
        else:
            # Handles Capricorn, which wraps around the year
            return (start_month == date.month and start_day <= date.day) or \
                   (end_month == date.month and date.day <= end_day) or \
                   (date.month > start_month or date.month < end_month)

    def to_datetime(self) -> datetime:
        """
        Returns the internal datetime object of the YamTimes instance.
        
        """
        return self.__datetime
    def to_string(self,format: str = "%Y-%m-%d %H:%M:%S") -> str:
        """
        Converts the internal datetime object of the YamTimes instance into a string
        based on the given format.

        Parameters:
        - format (str): The format to use for the conversion. Defaults to "%Y-%m-%d %H:%M:%S" if not provided.

        Returns:
        - str: The string representation of the internal datetime object according to the given format.
        """
        return self.__datetime.strftime(format)
    
    
    def _set_locale(self, language_code: str):
        try:
            locale.setlocale(locale.LC_TIME, language_code)
        except locale.Error:
            print(f"Idioma {language_code} não é suportado.")

    def month_name(self, language_code: str = 'en_US') -> str:
        """
        Returns the name of the month of the internal datetime object based on the given language_code.

        Parameters:
        - language_code (str): The language code to use for the month name. Defaults to "en_US" if not provided.

        Returns:
        - str: The name of the month of the internal datetime object according to the given language_code.
        """
        self._set_locale(language_code)
        return self.__datetime.strftime("%B")

    def weekday_name(self, language_code: str = 'en_US') -> str:
        """
        Returns the name of the weekday of the internal datetime object based on the given language_code.

        Parameters:
        - language_code (str): The language code to use for the weekday name. Defaults to "en_US" if not provided.

        Returns:
        - str: The name of the weekday of the internal datetime object according to the given language_code.
        """
        self._set_locale(language_code)
        return self.__datetime.strftime("%A")

    def day_of_month(self) -> int:
        """
        Returns the day of the month of the internal datetime object as an integer.
        """
        
        return self.__datetime.day

    def week_number(self) -> int:
        """
        Returns the week number of the internal datetime object as an integer.

        """
        
        return self.__datetime.isocalendar()[1]

    def is_weekend(self) -> bool:
        """
        Returns True if the internal datetime object is a weekend (saturday or sunday) and False otherwise.

        Returns:
        - bool: True if the internal datetime object is a weekend, False otherwise.
        """
        return self.__datetime.weekday() >= 5

    def days_in_month(self) -> int:
        """
        Returns the number of days in the month of the internal datetime object.

        Returns:
        - int: The number of days in the current month.
        """

        return calendar.monthrange(self.__datetime.year, self.__datetime.month)[1]

    def is_leap_year(self) -> bool:
        """
        Determines if the year of the internal datetime object is a leap year.

        Returns:
        - bool: True if the year is a leap year, False otherwise.
        """

        return (self.__datetime.year % 4 == 0 and (self.__datetime.year % 100 != 0 or self.__datetime.year % 400 == 0))

    def month(self) -> int:
        """
        Returns the month of the internal datetime object as an integer.

        Returns:
        - int: The month of the current date.
        """
 
        return self.__datetime.month

    def year(self) -> int:
        """
        Returns the year of the internal datetime object as an integer.

        Returns:
        - int: The year of the current date.
        """
        return self.__datetime.year

    def weekday_number(self) -> int:
        """
        Returns the day of the week of the internal datetime object as an integer.

        Where Monday is 0 and Sunday is 6.

        Returns:
        - int: The day of the week of the internal datetime object as an integer.
        """
        return self.__datetime.weekday()

    def hour(self) -> int:
        """
        Returns the hour of the internal datetime object as an integer.

        Returns:
        - int: The hour of the current time.
        """

        return self.__datetime.hour

    def minute(self) -> int:
        """
        Returns the minute of the internal datetime object as an integer.

        Returns:
        - int: The minute of the current time.
        """
        return self.__datetime.minute

    def second(self) -> int:
        """
        Returns the second of the internal datetime object as an integer.

        Returns:
        - int: The second of the current time.
        """
        return self.__datetime.second

    def timestamp(self) -> float:
        """
        Returns the timestamp of the internal datetime object as a float.

        Returns:
        - float: The timestamp of the internal datetime object.
        """
        return self.__datetime.timestamp()

    def next_month(self) -> "YamTimes":
        """
        Advances the internal datetime object to the first day of the next month.

        Returns:
        - YamTimes: A new YamTimes instance representing the first day of the following month.
        """

        next_month = self.__datetime.replace(day=28) + timedelta(days=4)
        return YamTimes(dt=next_month.replace(day=1))

    def next_year(self) -> "YamTimes":
        """
        Advances the internal datetime object to the same date in the next year.

        Returns:
        - YamTimes: A new YamTimes instance representing the same date in the following year.
        """
        return YamTimes(dt = self.__datetime.replace(year=self.__datetime.year + 1))

    def last_week(self) -> "YamTimes":
        """
        Goes back one week from the current date.

        Returns:
        - YamTimes: A new YamTimes instance representing the same day one week ago.
        """
        return YamTimes(dt = self.__datetime - timedelta(weeks=1))

    def last_month(self) -> "YamTimes":
        """
        Goes back one month from the current date.

        Returns:
        - YamTimes: A new YamTimes instance representing the same day one month ago.
        """
        return YamTimes(dt = self.__datetime - timedelta(days=30))

    def is_dst(self) -> bool:
        """
        Determines if the internal datetime object is observing daylight saving time.

        Returns:
        - bool: True if the datetime is in daylight saving time, False otherwise.
        """

        return bool(self.__datetime.dst())

    def weeks_in_year(self) -> int:
        """
        Determines the number of weeks in the year of the internal datetime object.

        Returns:
        - int: 52 if it's a common year, 53 if it's a leap year.
        """
        return 52 if not self.is_leap_year() else 53

    def start_of_month(self) -> "YamTimes":
        """
        Goes to the first day of the month of the internal datetime object.

        Returns:
        - YamTimes: A new YamTimes instance representing the first day of the month.
        """
        return YamTimes(dt = self.__datetime.replace(day=1, hour=0, minute=0, second=0, microsecond=0))

    def end_of_month(self) -> "YamTimes":
        """
        Goes to the last day of the month of the internal datetime object.

        Returns:
        - YamTimes: A new YamTimes instance representing the last day of the month.
        """

        last_day = calendar.monthrange(self.__datetime.year, self.__datetime.month)[1]
        return YamTimes(dt = self.__datetime.replace(day=last_day, hour=23, minute=59, second=59, microsecond=999999))

    def start_of_year(self) -> "YamTimes":
        """
        Goes to the first day of the year of the internal datetime object.

        Returns:
        - YamTimes: A new YamTimes instance representing the first day of the year.
        """

        return YamTimes(dt = self.__datetime.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0))

    def end_of_year(self) -> "YamTimes":
        """
        Goes to the last day of the year of the internal datetime object.

        Returns:
        - YamTimes: A new YamTimes instance representing the last day of the year.
        """
        return YamTimes(dt = self.__datetime.replace(month=12, day=31, hour=23, minute=59, second=59, microsecond=999999))

    def quarter(self) -> str:
        """
        Returns the quarter of the internal datetime object as a string.

        Returns:
        - str: The quarter of the internal datetime object as a string ("Q1", "Q2", "Q3", or "Q4").
        """
        month = self.__datetime.month
        if month <= 3:
            return "Q1"
        elif month <= 6:
            return "Q2"
        elif month <= 9:
            return "Q3"
        return "Q4"

    def previous_day(self) -> "YamTimes":
        """
        Returns a new YamTimes instance representing the previous day.

        Returns:
        - YamTimes: A new YamTimes instance set to one day before the current internal datetime.
        """

        return YamTimes(dt = self.__datetime - timedelta(days=1))

    def next_day(self) -> "YamTimes":
        """
        Returns a new YamTimes instance representing the next day.

        Returns:
        - YamTimes: A new YamTimes instance set to one day after the current internal datetime.
        """
        return YamTimes(dt = self.__datetime + timedelta(days=1))

    def start_of_week(self) -> "YamTimes":
        """
        Returns a new YamTimes instance representing the start of the week.

        This method calculates the start of the week (Monday) for the internal datetime
        object and returns a new YamTimes instance set to that date with the time set to 00:00:00.

        Returns:
        - YamTimes: A new YamTimes instance representing the start of the week.
        """

        start = self.__datetime - timedelta(days=self.__datetime.weekday())
        return YamTimes(dt = start.replace(hour=0, minute=0, second=0, microsecond=0))

    def end_of_week(self) -> "YamTimes":
        """
        Returns a new YamTimes instance representing the end of the week.

        This method calculates the end of the week (Sunday) for the internal datetime
        object and returns a new YamTimes instance set to that date with the time set to 23:59:59.999999.

        Returns:
        - YamTimes: A new YamTimes instance representing the end of the week.
        """

        end = self.__datetime + timedelta(days=(6 - self.__datetime.weekday()))
        return YamTimes(dt = end.replace(hour=23, minute=59, second=59, microsecond=999999))

    def add_days(self, days: int) -> "YamTimes":
        """
        Adds a specified number of days to the internal datetime object.

        Parameters:
        - days (int): The number of days to add. Can be positive or negative.

        Returns:
        - YamTimes: A new YamTimes instance representing the datetime after adding the specified number of days.
        """

        return YamTimes(dt = self.__datetime + timedelta(days=days))

    def subtract_days(self, days: int) -> "YamTimes":
        """
        Subtracts a specified number of days from the internal datetime object.

        Parameters:
        - days (int): The number of days to subtract. Can be positive or negative.

        Returns:
        - YamTimes: A new YamTimes instance representing the datetime after subtracting the specified number of days.
        """

        return YamTimes(dt = self.__datetime - timedelta(days=days))

    def add_months(self, months: int) -> "YamTimes":
        """
        Adds a specified number of months to the internal datetime object.

        Parameters:
        - months (int): The number of months to add. Can be positive or negative.

        Returns:
        - YamTimes: A new YamTimes instance representing the datetime after adding the specified number of months.
        """
        new_month = self.__datetime.month + months
        year_adjustment = (new_month - 1) // 12
        new_month = new_month % 12 + 1
        return YamTimes(dt = self.__datetime.replace(year=self.__datetime.year + year_adjustment, month=new_month))

    def subtract_months(self, months: int) -> "YamTimes":
        """
        Subtracts a specified number of months from the internal datetime object.

        Parameters:
        - months (int): The number of months to subtract.

        Returns:
        - YamTimes: A new YamTimes instance representing the datetime after subtracting the specified number of months.
        """

        return self.add_months(-months)

    def add_years(self, years: int) -> "YamTimes":
        """
        Adds a specified number of years to the internal datetime object.

        Parameters:
        - years (int): The number of years to add. Can be positive or negative.

        Returns:
        - YamTimes: A new YamTimes instance representing the datetime after adding the specified number of years.
        """
        return YamTimes(dt = self.__datetime.replace(year=self.__datetime.year + years))

    def subtract_years(self, years: int) -> "YamTimes":
        """
        Subtracts a specified number of years from the internal datetime object.

        Parameters:
        - years (int): The number of years to subtract.

        Returns:
        - YamTimes: A new YamTimes instance representing the datetime after subtracting the specified number of years.
        """
        
        return self.add_years(-years)

    def seconds_until(self, other: "YamTimes") -> int:
        """
        Calculates the number of seconds until another YamTimes instance.

        Parameters:
        - other (YamTimes): The YamTimes instance to compare against.

        Returns:
        - int: The number of seconds from the current instance to the `other` instance.
        """

        return int((other.datetime - self.__datetime).total_seconds())

    def days_until(self, other: "YamTimes") -> int:
        """
        Calculates the number of days until another YamTimes instance.

        Parameters:
        - other (YamTimes): The YamTimes instance to compare against.

        Returns:
        - int: The number of days from the current instance to the `other` instance.
        """
        
        return (other.datetime - self.__datetime).days

    def hours_until(self, other: "YamTimes") -> int:
        """
        Calculates the number of whole hours until another YamTimes instance.

        Parameters:
        - other (YamTimes): The YamTimes instance to compare against.

        Returns:
        - int: The number of whole hours from the current instance to the `other` instance.
        """

        return (other.datetime - self.__datetime).seconds // 3600

    def day_of_year(self) -> int:
        """
        Returns the day of the year of the internal datetime object as an integer.

        Returns:
        - int: The day of the year of the current date.
        """
        return self.__datetime.timetuple().tm_yday

    def short_month_name(self, language_code: str = 'en_US') -> str:
        """
        Returns the short name of the month of the internal datetime object based on the given language_code.

        Parameters:
        - language_code (str): The language code to use for the month name. Defaults to "en_US" if not provided.

        Returns:
        - str: The short name of the month of the internal datetime object according to the given language_code.
        """
        self._set_locale(language_code)
        return self.__datetime.strftime("%b")

    def short_weekday_name(self, language_code: str = 'en_US') -> str:
        """
        Returns the short name of the weekday of the internal datetime object based on the given language_code.

        Parameters:
        - language_code (str): The language code to use for the weekday name. Defaults to "en_US" if not provided.

        Returns:
        - str: The short name of the weekday of the internal datetime object according to the given language_code.
        """
        self._set_locale(language_code)
        return self.__datetime.strftime("%a")

    def week_day_number(self) -> int:
        """
        Returns the day of the week of the internal datetime object as an integer.

        Where Monday is 1 and Sunday is 7.

        Returns:
        - int: The day of the week of the internal datetime object as an integer.
        """
        return self.__datetime.weekday() + 1

    def time_12hr_format(self) -> str:
        """
        Returns the time of the internal datetime object in 12-hour format.

        Returns:
        - str: The time of the internal datetime object in 12-hour format.
        """
        return self.__datetime.strftime("%I:%M:%S %p")

    def readable_format(self, language_code: str = 'en_US') -> str:
        """
        Returns a human-readable string representation of the internal datetime object based on the specified language code.

        Parameters:
        - language_code (str): The language code to use for the formatting. Defaults to "en_US" if not provided.

        Returns:
        - str: A formatted string representing the date and time in the format "Day, DD Month YYYY HH:MM:SS AM/PM".
        """

        self._set_locale(language_code)
        return self.__datetime.strftime("%A, %d %B %Y %I:%M:%S %p")

    def is_holiday(self) -> bool:
        """
        Checks if the internal datetime object is a holiday in the given country.

        Parameters:
        - country_code (str): The ISO 3166-1 alpha-2 country code. Defaults to "US" if not provided.

        Returns:
        - bool: True if the internal datetime object is a holiday, False otherwise.
        """
        return False  

    def years_difference(self, other: "YamTimes") -> int:
        """
        Calculates the absolute difference in years between the internal datetime and another YamTimes instance.

        Parameters:
        - other (YamTimes): The YamTimes instance to compare against.

        Returns:
        - int: The absolute difference in years.
        """

        return abs(self.__datetime.year - other.datetime.year)

    def current_quarter(self) -> int:
        """
        Returns the current quarter of the year of the internal datetime object.

        Returns:
        - int: The current quarter of the year as an integer (1-4).
        """
        return (self.__datetime.month - 1) // 3 + 1

    def day_of_year_number(self) -> int:
        """
        Returns the day of the year of the internal datetime object as an integer.

        Returns:
        - int: The day of the year of the current date.
        """

        return self.__datetime.timetuple().tm_yday

    def time_24hr_format(self) -> str:
        """
        Returns the time of the internal datetime object in 24-hour format.

        Returns:
        - str: The time of the internal datetime object in 24-hour format.
        """
        return self.__datetime.strftime("%H:%M:%S")

    def iso_with_microseconds(self) -> str:
        """
        Returns the internal datetime object as an ISO 8601 formatted string with microsecond precision.

        Returns:
        - str: The internal datetime object as an ISO 8601 formatted string with microsecond precision.
        """
        return self.__datetime.isoformat()

    @property
    def datetime(self) -> datetime:
        """
        Returns the internal datetime object.

        Returns:
        - datetime: The internal datetime object.
        """

        return self.__datetime


    def now(self) -> "YamTimes":
        """
        Returns a new YamTimes instance set to the current date and time.

        Returns:
        - YamTimes: A new YamTimes instance set to the current date and time.
        """
        return YamTimes(dt = datetime.now())

    def tomorrow(self) -> "YamTimes":
        """
        Returns a new YamTimes instance set to the next day from the internal datetime object.

        Returns:
        - YamTimes: A new YamTimes instance set to the next day from the internal datetime object.
        """
        return YamTimes(dt = self.__datetime + timedelta(days=1))

    def yesterday(self) -> "YamTimes":
        """
        Returns a new YamTimes instance set to the previous day from the internal datetime object.

        Returns:
        - YamTimes: A new YamTimes instance set to the previous day from the internal datetime object.
        """

        return YamTimes(dt = self.__datetime - timedelta(days=1))

    def today(self) -> "YamTimes":
        """
        Class method to create a YamTimes instance set to the current date at midnight.

        Returns:
        - YamTimes: A new YamTimes instance set to the current date at midnight.
        """
        return YamTimes(dt = self.__datetime.replace(hour=0, minute=0, second=0, microsecond=0))


    def from_string(self, date_string: str, format: str = "%Y-%m-%d %H:%M:%S") -> "YamTimes":
        """
        Class method to create a YamTimes instance from a string representation of a date and time.

        Parameters:
        - date_string (str): The string representation of the date and time.
        - format (str): The format that the date_string is in. Defaults to "%Y-%m-%d %H:%M:%S".

        Returns:
        - YamTimes: A new YamTimes instance initialized with the parsed date and time.
        """

        return YamTimes(dt = datetime.strptime(date_string, format))

    def from_iso_format(self, iso_string: str) -> "YamTimes":
        """
        Class method to create a YamTimes instance from an ISO 8601 format string.

        Parameters:
        - iso_string (str): The ISO 8601 format string representation of the date and time.

        Returns:
        - YamTimes: A new YamTimes instance initialized with the parsed date and time.
        """
        return YamTimes(dt = datetime.fromisoformat(iso_string))


    def from_timestamp(self, ts: float) -> "YamTimes":
        """
        Class method to create a YamTimes instance from a given timestamp.

        Parameters:
        - ts (float): The timestamp to use for the internal datetime object.

        Returns:
        - YamTimes: A new YamTimes instance initialized with the given timestamp.
        """
        return YamTimes(dt = datetime.fromtimestamp(ts))

    def after(self, years=0, months=0, days=0, hours=0, minutes=0, seconds=0) -> "YamTimes":
        """
        Returns a new YamTimes instance that is ahead of the current datetime object by the given
        time period.

        Parameters:
        - years (int): The number of years to add to the current datetime object.
        - months (int): The number of months to add to the current datetime object.
        - days (int): The number of days to add to the current datetime object.
        - hours (int): The number of hours to add to the current datetime object.
        - minutes (int): The number of minutes to add to the current datetime object.
        - seconds (int): The number of seconds to add to the current datetime object.

        Returns:
        - YamTimes: A new YamTimes instance ahead of the current datetime object by the given time period.
        """
        return YamTimes(
            dy = self.__datetime + relativedelta(
                years=years, months=months, days=days, hours=hours, minutes=minutes, seconds=seconds
            )
        )

    def before(self, years=0, months=0, days=0, hours=0, minutes=0, seconds=0) -> "YamTimes":
        """
        Returns a new YamTimes instance that is before the current datetime object by the given
        time period.

        Parameters:
        - years (int): The number of years to subtract from the current datetime object.
        - months (int): The number of months to subtract from the current datetime object.
        - days (int): The number of days to subtract from the current datetime object.
        - hours (int): The number of hours to subtract from the current datetime object.
        - minutes (int): The number of minutes to subtract from the current datetime object.
        - seconds (int): The number of seconds to subtract from the current datetime object.

        Returns:
        - YamTimes: A new YamTimes instance before the current datetime object by the given time period.
        """

        return YamTimes(
            dt = self.__datetime - relativedelta(
                years=years, months=months, days=days, hours=hours, minutes=minutes, seconds=seconds
            )
        )

    def set_time(self, hour: int = 0, minute: int = 0, second: int = 0) -> "YamTimes":
        """
        Sets the time of the internal datetime object to the specified hour, minute, and second.

        Parameters:
        - hour (int, optional): The hour to set. Defaults to 0 if not provided.
        - minute (int, optional): The minute to set. Defaults to 0 if not provided.
        - second (int, optional): The second to set. Defaults to 0 if not provided.

        Returns:
        - YamTimes: A new YamTimes instance with the updated time.
        """

        return YamTimes(dt = self.__datetime.replace(hour=hour, minute=minute, second=second, microsecond=0))

    def set_date(self, year: int, month: int, day: int) -> "YamTimes":
        """
        Sets the date of the internal datetime object to the specified year, month, and day.

        Parameters:
        - year (int): The year to set.
        - month (int): The month to set.
        - day (int): The day to set.

        Returns:
        - YamTimes: A new YamTimes instance with the updated date.
        """
        return YamTimes(dt = self.__datetime.replace(year=year, month=month, day=day))

    def start_of_week(self) -> "YamTimes":
        """
        Returns a new YamTimes instance that is at the start of the week.

        Returns:
        - YamTimes: A new YamTimes instance at the start of the week.
        """
        start = self.__datetime - timedelta(days=self.__datetime.weekday())
        return YamTimes(dt = start.replace(hour=0, minute=0, second=0, microsecond=0))

    def end_of_week(self) -> "YamTimes":
        """
        Returns a new YamTimes instance that is at the end of the week.

        The end of the week is considered to be Sunday at 23:59:59.999999.

        Returns:
        - YamTimes: A new YamTimes instance at the end of the week.
        """

        end = self.__datetime + timedelta(days=(6 - self.__datetime.weekday()))
        return YamTimes(dt = end.replace(hour=23, minute=59, second=59, microsecond=999999))

    def start_of_month(self) -> "YamTimes":
        """
        Returns a new YamTimes instance that is at the start of the month.

        The start of the month is considered to be the first day of the month at 00:00:00.000000.

        Returns:
        - YamTimes: A new YamTimes instance at the start of the month.
        """
        return YamTimes(dt = self.__datetime.replace(day=1, hour=0, minute=0, second=0, microsecond=0))

    def end_of_month(self) -> "YamTimes":
        """
        Returns a new YamTimes instance that is at the end of the month.

        The end of the month is considered to be the last day of the month
        at 23:59:59.999999.

        Returns:
        - YamTimes: A new YamTimes instance at the end of the month.
        """

        last_day = calendar.monthrange(self.__datetime.year, self.__datetime.month)[1]
        return YamTimes(dt = self.__datetime.replace(day=last_day, hour=23, minute=59, second=59, microsecond=999999))

    def start_of_year(self) -> "YamTimes":
        """
        Returns a new YamTimes instance that is at the start of the year.

        The start of the year is considered to be January 1st at 00:00:00.000000.

        Returns:
        - YamTimes: A new YamTimes instance at the start of the year.
        """
        return YamTimes(dt = self.__datetime.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0))

    def end_of_year(self) -> "YamTimes":
        """
        Returns a new YamTimes instance that is at the end of the year.

        The end of the year is considered to be December 31st at 23:59:59.999999.

        Returns:
        - YamTimes: A new YamTimes instance at the end of the year.
        """
        return YamTimes(dt = self.__datetime.replace(month=12, day=31, hour=23, minute=59, second=59, microsecond=999999))

    def is_same_day(self, other: "YamTimes") -> bool:
        """
        Checks if two YamTimes instances are on the same day.

        Returns True if the two instances are on the same day, False otherwise.

        Parameters:
        - other (YamTimes): The other YamTimes instance to compare against.

        Returns:
        - bool: Whether the two instances are on the same day.
        """
        return self.__datetime.date() == other.datetime.date()

    def is_past(self) -> bool:
        """
        Determines if the internal datetime object is in the past relative to the current datetime.

        Returns:
        - bool: True if the internal datetime object is earlier than the current datetime, False otherwise.
        """

        return self.__datetime < datetime.now()

    def is_future(self) -> bool:
        """
        Determines if the internal datetime object is in the future relative to the current datetime.

        Returns:
        - bool: True if the internal datetime object is later than the current datetime, False otherwise.
        """
        return self.__datetime > datetime.now()

    def days_in_month(self) -> int:
        """
        Returns the number of days in the month of the internal datetime object.

        Returns:
        - int: The number of days in the current month.
        """
        return calendar.monthrange(self.__datetime.year, self.__datetime.month)[1]

    def to_iso_format(self) -> str:
        """
        Returns the internal datetime object as an ISO 8601 formatted string.

        Returns:
        - str: The internal datetime object as an ISO 8601 formatted string.
        """
        return self.__datetime.isoformat()

    def string(self, format: str = "%Y-%m-%d %H:%M:%S") -> str:
        """
        Returns a string representation of the internal datetime object based on the given format.

        Parameters:
        - format (str): The format to use for the conversion. Defaults to "%Y-%m-%d %H:%M:%S" if not provided.

        Returns:
        - str: The string representation of the internal datetime object according to the given format.
        """

        return self.__datetime.strftime(format)

    def timestamp(self) -> float:
        """
        Returns the timestamp of the internal datetime object as a float.

        Returns:
        - float: The timestamp of the internal datetime object.
        """
        return self.__datetime.timestamp()

    def difference(self, other: "YamTimes") -> timedelta:
        """
        Calculates the difference between the internal datetime object and another YamTimes instance.

        Parameters:
        - other (YamTimes): The YamTimes instance to compare against.

        Returns:
        - timedelta: The difference between the internal datetime object and the other YamTimes instance.
        """

        if not isinstance(other, YamTimes):
            raise TypeError("O argumento deve ser uma instância de YamTimes")
        return self.__datetime - other.datetime

    def time_until(self, other: "YamTimes") -> timedelta:
        """
        Calculates the time difference between the internal datetime object and another YamTimes instance.

        Parameters:
        - other (YamTimes): The YamTimes instance to compare against.

        Returns:
        - timedelta: The time difference between the internal datetime object and the other YamTimes instance.

        Raises:
        - TypeError: If the argument is not a YamTimes instance.
        """
        
        if not isinstance(other, YamTimes):
            raise TypeError("The argument must be an instance of YamTimes")
        return other.datetime - self.__datetime

    def is_before(self, other: "YamTimes") -> bool:
        """
        Checks if the internal datetime object is before another YamTimes instance.

        Parameters:
        - other (YamTimes): The YamTimes instance to compare against.

        Returns:
        - bool: Whether the internal datetime object is before the other instance.

        Raises:
        - TypeError: If the argument is not a YamTimes instance.
        """
        if not isinstance(other, YamTimes):
            raise TypeError("The argument must be an instance of YamTimes")
        return self.__datetime < other.datetime

    def is_after(self, other: "YamTimes") -> bool:
        """
        Determines if the internal datetime object is after another YamTimes instance.

        Parameters:
        - other (YamTimes): The YamTimes instance to compare against.

        Returns:
        - bool: True if the internal datetime object is later than the other YamTimes instance, False otherwise.

        Raises:
        - TypeError: If the argument is not a YamTimes instance.
        """
        if not isinstance(other, YamTimes):
            raise TypeError("The argument must be an instance of YamTimes")
        return self.__datetime > other.datetime
    def is_monday(self) -> bool:
        """
        Checks if the internal datetime object is a Monday.

        Returns:
        - bool: True if the internal datetime object is a Monday, False otherwise.
        """
        return self.__datetime.weekday() == 0

    def is_tuesday(self) -> bool:
        """
        Checks if the internal datetime object is a Tuesday.

        Returns:
        - bool: True if the internal datetime object is a Tuesday, False otherwise.
        """

        return self.__datetime.weekday() == 1

    def is_wednesday(self) -> bool:
        """
        Checks if the internal datetime object is a Wednesday.

        Returns:
        - bool: True if the internal datetime object is a Wednesday, False otherwise.
        """
        return self.__datetime.weekday() == 2

    def is_thursday(self) -> bool:
        """
        Checks if the internal datetime object is a Thursday.

        Returns:
        - bool: True if the internal datetime object is a Thursday, False otherwise.
        """
        return self.__datetime.weekday() == 3

    def is_friday(self) -> bool:
        """
        Checks if the internal datetime object is a Friday.

        Returns:
        - bool: True if the internal datetime object is a Friday, False otherwise.
        """

        return self.__datetime.weekday() == 4

    def is_saturday(self) -> bool:
        """
        Checks if the internal datetime object is a Saturday.

        Returns:
        - bool: True if the internal datetime object is a Saturday, False otherwise.
        """
        return self.__datetime.weekday() == 5

    def is_sunday(self) -> bool:
        """
        Checks if the internal datetime object is a Sunday.

        Returns:
        - bool: True if the internal datetime object is a Sunday, False otherwise.
        """
        return self.__datetime.weekday() == 6

    def next_week(self) -> "YamTimes":
        """
        Returns a new YamTimes instance that is one week ahead of the current instance.

        Returns:
        - YamTimes: A new YamTimes instance that is one week ahead of the current instance.
        """
        return YamTimes(dt=self.__datetime + timedelta(weeks=1))

    def last_week(self) -> "YamTimes":
        """
        Returns a new YamTimes instance that is one week behind the current instance.

        Returns:
        - YamTimes: A new YamTimes instance that is one week behind the current instance.
        """
        return YamTimes(dt=self.__datetime - timedelta(weeks=1))

    def weeks_between(self, other: "YamTimes") -> int:
        """
        Calculates the number of whole weeks between the internal datetime object and another YamTimes instance.

        Parameters:
        - other (YamTimes): The YamTimes instance to compare against.

        Returns:
        - int: The number of whole weeks from the current instance to the `other` instance.
        """
        delta = self.__datetime - other.datetime
        return delta.days // 7

    def is_same_month(self, other: "YamTimes") -> bool:
        """
        Checks if the internal datetime object is in the same month as another YamTimes instance.

        Parameters:
        - other (YamTimes): The YamTimes instance to compare against.

        Returns:
        - bool: True if the internal datetime object is in the same month as the `other` instance, False otherwise.
        """
        return self.__datetime.month == other.datetime.month and self.__datetime.year == other.datetime.year

    def is_same_year(self, other: "YamTimes") -> bool:
        """
        Checks if the internal datetime object is in the same year as another YamTimes instance.

        Parameters:
        - other (YamTimes): The YamTimes instance to compare against.

        Returns:
        - bool: True if the internal datetime object is in the same year as the `other` instance, False otherwise.
        """

        return self.__datetime.year == other.datetime.year

    def add_seconds(self, seconds: int) -> "YamTimes":
        """
        Adds a specified number of seconds to the internal datetime object.

        Parameters:
        - seconds (int): The number of seconds to add. Can be positive or negative.

        Returns:
        - YamTimes: A new YamTimes instance representing the datetime after adding the specified number of seconds.
        """

        return YamTimes(dt=self.__datetime + timedelta(seconds=seconds))

    def subtract_seconds(self, seconds: int) -> "YamTimes":
        """
        Subtracts a specified number of seconds from the internal datetime object.

        Parameters:
        - seconds (int): The number of seconds to subtract. Can be positive or negative.

        Returns:
        - YamTimes: A new YamTimes instance representing the datetime after subtracting the specified number of seconds.
        """
        return YamTimes(dt=self.__datetime - timedelta(seconds=seconds))

    def start_of_quarter(self) -> "YamTimes":
        """
        Returns a new YamTimes instance that is at the start of the quarter.

        The start of the quarter is considered to be the first day of the quarter at 00:00:00.000000.

        Returns:
        - YamTimes: A new YamTimes instance at the start of the quarter.
        """
        month = self.__datetime.month
        if month <= 3:
            start_month = 1
        elif month <= 6:
            start_month = 4
        elif month <= 9:
            start_month = 7
        else:
            start_month = 10
        return YamTimes(dt=self.__datetime.replace(month=start_month, day=1, hour=0, minute=0, second=0))

    def end_of_quarter(self) -> "YamTimes":
        """
        Returns a new YamTimes instance that is at the end of the quarter.

        The end of the quarter is considered to be the last day of the quarter at 23:59:59.999999.

        Returns:
        - YamTimes: A new YamTimes instance at the end of the quarter.
        """
        month = self.__datetime.month
        if month <= 3:
            end_month = 3
        elif month <= 6:
            end_month = 6
        elif month <= 9:
            end_month = 9
        else:
            end_month = 12
        last_day = calendar.monthrange(self.__datetime.year, end_month)[1]
        return YamTimes(dt=self.__datetime.replace(month=end_month, day=last_day, hour=23, minute=59, second=59))

    def is_weekday(self) -> bool:
        """
        Checks if the internal datetime object is a weekday (Monday to Friday).

        Returns:
        - bool: True if the internal datetime object is a weekday, False otherwise.
        """

        return 0 <= self.__datetime.weekday() <= 4

    def is_within_range(self, start: "YamTimes", end: "YamTimes") -> bool:
        """
        Determines if the internal datetime object is within a specified range.

        Parameters:
        - start (YamTimes): The start of the range.
        - end (YamTimes): The end of the range.

        Returns:
        - bool: True if the internal datetime object is within the range [start, end], inclusive, False otherwise.
        """

        return start.datetime <= self.__datetime <= end.datetime

    def next_business_day(self) -> "YamTimes":
        """
        Returns a new YamTimes instance representing the next business day.

        The next business day is defined as the next day that is not a weekend (Saturday or Sunday).

        Returns:
        - YamTimes: A new YamTimes instance representing the next business day.
        """
        next_day = self.__datetime + timedelta(days=1)
        while next_day.weekday() >= 5:  # Skip weekends
            next_day += timedelta(days=1)
        return YamTimes(dt=next_day)

    def last_business_day(self) -> "YamTimes":
        """
        Returns a new YamTimes instance representing the last business day.

        The last business day is defined as the last day that is not a weekend (Saturday or Sunday).

        Returns:
        - YamTimes: A new YamTimes instance representing the last business day.
        """
        last_day = self.__datetime - timedelta(days=1)
        while last_day.weekday() >= 5:  # Skip weekends
            last_day -= timedelta(days=1)
        return YamTimes(dt=last_day)

    def to_unix_timestamp(self) -> int:
        """
        Converts the internal datetime object of the YamTimes instance into a Unix timestamp.

        Returns:
        - int: The Unix timestamp of the internal datetime object.
        """
        return int(self.__datetime.timestamp())
    
    def is_weekday(self) -> bool:
        """
        Checks if the internal datetime object is a weekday (Monday to Friday).
        The internal datetime object is considered a weekday if it is not a weekend (Saturday or Sunday).

        Returns:
        - bool: True if the internal datetime object is a weekday, False otherwise.
        """
        return not self.is_weekend_day()

    def is_am(self) -> bool:
        """
        Checks if the internal datetime object is in the morning (AM) portion of the day.

        The internal datetime object is considered to be in the morning if its hour is less than 12.

        Returns:
        - bool: True if the internal datetime object is in the morning, False otherwise.
        """
        return self.__datetime.hour < 12

    def is_pm(self) -> bool:
        """
        Checks if the internal datetime object is in the afternoon (PM) portion of the day.

        The internal datetime object is considered to be in the afternoon if its hour is greater than 11.

        Returns:
        - bool: True if the internal datetime object is in the afternoon, False otherwise.
        """
        return not self.is_am()

    def set_to_midnight(self) -> "YamTimes":
        """
        Returns a new YamTimes instance with the internal datetime object set to midnight.

        The resulting YamTimes instance will have the same date as the current instance, but the time will
        be set to 00:00:00.

        Returns:
        - YamTimes: A new YamTimes instance with the time set to midnight.
        """
        return YamTimes(dt=self.__datetime.replace(hour=0, minute=0, second=0, microsecond=0))

    def set_to_noon(self) -> "YamTimes":
        """
        Returns a new YamTimes instance with the internal datetime object set to noon.

        The resulting YamTimes instance will have the same date as the current instance, but the time will
        be set to 12:00:00.

        Returns:
        - YamTimes: A new YamTimes instance with the time set to noon.
        """

        return YamTimes(dt=self.__datetime.replace(hour=12, minute=0, second=0, microsecond=0))

    def add_minutes(self, minutes: int) -> "YamTimes":
        """
        Adds a specified number of minutes to the internal datetime object.

        Parameters:
        - minutes (int): The number of minutes to add. Can be positive or negative.

        Returns:
        - YamTimes: A new YamTimes instance representing the datetime after adding the specified number of minutes.
        """
        return YamTimes(dt=self.__datetime + timedelta(minutes=minutes))

    def subtract_minutes(self, minutes: int) -> "YamTimes":
        """
        Subtracts a specified number of minutes from the internal datetime object.

        Parameters:
        - minutes (int): The number of minutes to subtract. Can be positive or negative.

        Returns:
        - YamTimes: A new YamTimes instance representing the datetime after subtracting the specified number of minutes.
        """
        return YamTimes(dt=self.__datetime - timedelta(minutes=minutes))

    def add_seconds(self, seconds: int) -> "YamTimes":
        """
        Adds a specified number of seconds to the internal datetime object.

        Parameters:
        - seconds (int): The number of seconds to add. Can be positive or negative.

        Returns:
        - YamTimes: A new YamTimes instance representing the datetime after adding the specified number of seconds.
        """
        return YamTimes(dt=self.__datetime + timedelta(seconds=seconds))

    def subtract_seconds(self, seconds: int) -> "YamTimes":
        """
        Subtracts a specified number of seconds from the internal datetime object.

        Parameters:
        - seconds (int): The number of seconds to subtract. Can be positive or negative.

        Returns:
        - YamTimes: A new YamTimes instance representing the datetime after subtracting the specified number of seconds.
        """

        return YamTimes(dt=self.__datetime - timedelta(seconds=seconds))

    def is_same_month(self, other: "YamTimes") -> bool:
        """
        Checks if the internal datetime object is in the same month as another YamTimes instance.

        Parameters:
        - other (YamTimes): The YamTimes instance to compare against.

        Returns:
        - bool: True if the internal datetime object is in the same month as the other YamTimes instance, False otherwise.
        """
        return self.__datetime.year == other.datetime.year and self.__datetime.month == other.datetime.month

    def is_same_year(self, other: "YamTimes") -> bool:
        """
        Checks if the internal datetime object is in the same year as another YamTimes instance.

        Parameters:
        - other (YamTimes): The YamTimes instance to compare against.

        Returns:
        - bool: True if the internal datetime object is in the same year as the other YamTimes instance, False otherwise.
        """
        return self.__datetime.year == other.datetime.year

    def is_same_week(self, other: "YamTimes") -> bool:
        """
        Checks if the internal datetime object is in the same week as another YamTimes instance.

        A week is defined as a period of 7 days, starting on Monday. The first day of the week is
        considered to be Monday, and the last day of the week is considered to be Sunday.

        Parameters:
        - other (YamTimes): The YamTimes instance to compare against.

        Returns:
        - bool: True if the internal datetime object is in the same week as the other YamTimes instance, False otherwise.
        """
        start_of_week_self = self.start_of_week().datetime.date()
        start_of_week_other = other.start_of_week().datetime.date()
        return start_of_week_self == start_of_week_other

    def time_difference_in_seconds(self, other: "YamTimes") -> int:
        """
        Calculates the absolute difference in seconds between the internal datetime object and another YamTimes instance.

        Parameters:
        - other (YamTimes): The YamTimes instance to compare against.

        Returns:
        - int: The absolute difference in seconds.
        """
        return int(abs((self.__datetime - other.datetime).total_seconds()))

    def time_difference_in_minutes(self, other: "YamTimes") -> int:
        """
        Calculates the absolute difference in minutes between the internal datetime object and another YamTimes instance.

        Parameters:
        - other (YamTimes): The YamTimes instance to compare against.

        Returns:
        - int: The absolute difference in minutes.
        """
        return self.time_difference_in_seconds(other) // 60

    def time_difference_in_hours(self, other: "YamTimes") -> int:
        """

        Parameters:
        - other (YamTimes): The YamTimes instance to compare against.

        Returns:
        - int: The absolute difference in hours.
        """
        return self.time_difference_in_minutes(other) // 60

    def time_difference_in_days(self, other: "YamTimes") -> int:
        """
        Calculates the absolute difference in days between the internal datetime object and another YamTimes instance.

        Parameters:
        - other (YamTimes): The YamTimes instance to compare against.

        Returns:
        - int: The absolute difference in days.
        """
        return abs((self.__datetime - other.datetime).days)

    def is_before_today(self) -> bool:
        """
        Checks if the internal datetime object is before the current date.

        Returns:
        - bool: True if the internal datetime object is before the current date, False otherwise.
        """
        return self.__datetime.date() < datetime.today().date()

    def is_after_today(self) -> bool:
        """
        Checks if the internal datetime object is after the current date.

        Returns:
        - bool: True if the internal datetime object is after the current date, False otherwise.
        """
        return self.__datetime.date() > datetime.today().date()

    def is_in_current_month(self) -> bool:
        """
        Checks if the internal datetime object is in the current month.

        Returns:
        - bool: True if the internal datetime object is in the current month, False otherwise.
        """
        return self.__datetime.month == datetime.now().month

    def is_in_current_year(self) -> bool:
        """
        Checks if the internal datetime object is in the current year.

        Returns:
        - bool: True if the internal datetime object is in the current year, False otherwise.
        """
        return self.__datetime.year == datetime.now().year

    def is_in_current_week(self) -> bool:
        """
        Checks if the internal datetime object is in the current week.

        Returns:
        - bool: True if the internal datetime object is in the current week, False otherwise.
        """
        return self.is_same_week(YamTimes.now())

    def get_month_name(self, language_code: str = 'en_US') -> str:
        """
        Returns the full name of the month of the internal datetime object based on the given language_code.

        Parameters:
        - language_code (str): The language code to use for the month name. Defaults to "en_US" if not provided.

        Returns:
        - str: The full name of the month of the internal datetime object according to the given language_code.
        """
        self._set_locale(language_code)
        return self.__datetime.strftime('%B')

    def get_short_month_name(self, language_code: str = 'en_US') -> str:
        """
        Returns the abbreviated name of the month of the internal datetime object based on the given language_code.

        Parameters:
        - language_code (str): The language code to use for the month name. Defaults to "en_US" if not provided.

        Returns:
        - str: The abbreviated name of the month of the internal datetime object according to the given language_code.
        """

        self._set_locale(language_code)
        return self.__datetime.strftime('%b')

    def get_weekday_name(self, language_code: str = 'en_US') -> str:
        """
        Returns the full name of the weekday of the internal datetime object based on the given language_code.

        Parameters:
        - language_code (str): The language code to use for the weekday name. Defaults to "en_US" if not provided.

        Returns:
        - str: The full name of the weekday of the internal datetime object according to the given language_code.
        """

        self._set_locale(language_code)
        return self.__datetime.strftime('%A')

    def get_short_weekday_name(self, language_code: str = 'en_US') -> str:
        """
        Returns the abbreviated name of the weekday of the internal datetime object based on the given language_code.

        Parameters:
        - language_code (str): The language code to use for the weekday name. Defaults to "en_US" if not provided.

        Returns:
        - str: The abbreviated name of the weekday of the internal datetime object according to the given language_code.
        """

        self._set_locale(language_code)
        return self.__datetime.strftime('%a')

    def is_birthday(self, birthday: "YamTimes") -> bool:
        """
        Checks if the internal datetime object is on the same day as a given birthday.

        Parameters:
        - birthday (YamTimes): The birthday to check against.

        Returns:
        - bool: True if the internal datetime object is on the same day as the given birthday, False otherwise.
        """
        return self.__datetime.month == birthday.datetime.month and self.__datetime.day == birthday.datetime.day

    def set_to_last_day_of_month(self) -> "YamTimes":
        """
        Returns a new YamTimes instance set to the last day of the month of the internal datetime object.

        Returns:
        - YamTimes: A new YamTimes instance set to the last day of the month of the internal datetime object.
        """
        last_day = calendar.monthrange(self.__datetime.year, self.__datetime.month)[1]
        return YamTimes(dt=self.__datetime.replace(day=last_day))

    def add_weeks_from_now(self, weeks: int) -> "YamTimes":
        """
        Returns a new YamTimes instance that is ahead of the current datetime object by the given
        number of weeks.

        Parameters:
        - weeks (int): The number of weeks to add to the current datetime object.

        Returns:
        - YamTimes: A new YamTimes instance ahead of the current datetime object by the given number of weeks.
        """        
        return YamTimes(dt=datetime.now() + timedelta(weeks=weeks))

    def subtract_weeks_from_now(self, weeks: int) -> "YamTimes":
        """
        Returns a new YamTimes instance that is behind the current datetime object by the given
        number of weeks.

        Parameters:
        - weeks (int): The number of weeks to subtract from the current datetime object.

        Returns:
        - YamTimes: A new YamTimes instance behind the current datetime object by the given number of weeks.
        """

        return YamTimes(dt=datetime.now() - timedelta(weeks=weeks))

    def add_months_from_now(self, months: int) -> "YamTimes":
        """
        Returns a new YamTimes instance that is ahead of the current datetime object by the given
        number of months.

        Parameters:
        - months (int): The number of months to add to the current datetime object.

        Returns:
        - YamTimes: A new YamTimes instance ahead of the current datetime object by the given number of months.
        """
        return YamTimes(dt=self.add_months(months).datetime)

    def subtract_months_from_now(self, months: int) -> "YamTimes":
        """
        Returns a new YamTimes instance that is behind the current datetime object by the given
        number of months.

        Parameters:
        - months (int): The number of months to subtract from the current datetime object.

        Returns:
        - YamTimes: A new YamTimes instance behind the current datetime object by the given number of months.
        """

        return YamTimes(dt=self.subtract_months(months).datetime)

    def last_day_of_week(self) -> "YamTimes":
        """
        Returns a new YamTimes instance that is set to the last day of the week of the internal datetime object.

        The last day of the week is considered to be Sunday at 23:59:59.999999.

        Returns:
        - YamTimes: A new YamTimes instance set to the last day of the week of the internal datetime object.
        """

        end_of_week = self.end_of_week().datetime
        return YamTimes(dt=end_of_week.replace(hour=23, minute=59, second=59, microsecond=999999))

    def first_day_of_week(self) -> "YamTimes":
        """
        Returns a new YamTimes instance that is set to the first day of the week of the internal datetime object.

        The first day of the week is considered to be Monday at 00:00:00.

        Returns:
        - YamTimes: A new YamTimes instance set to the first day of the week of the internal datetime object.
        """
        start_of_week = self.start_of_week().datetime
        return YamTimes(dt=start_of_week.replace(hour=0, minute=0, second=0, microsecond=0))

    def first_day_of_year(self) -> "YamTimes":
        """
        Returns a new YamTimes instance that is set to the first day of the year of the internal datetime object.

        The first day of the year is considered to be January 1st at 00:00:00.

        Returns:
        - YamTimes: A new YamTimes instance set to the first day of the year of the internal datetime object.
        """
        return YamTimes(dt=self.start_of_year().datetime.replace(hour=0, minute=0, second=0, microsecond=0))

    def last_day_of_year(self) -> "YamTimes":
        """
        Returns a new YamTimes instance that is set to the last day of the year of the internal datetime object.

        The last day of the year is considered to be December 31st at 23:59:59.999999.

        Returns:
        - YamTimes: A new YamTimes instance set to the last day of the year of the internal datetime object.
        """
        return YamTimes(dt=self.end_of_year().datetime.replace(hour=23, minute=59, second=59, microsecond=999999))

    def time_until_next_month(self) -> "YamTimes":
        """
        Returns a new YamTimes instance that is set to the first day of the next month of the internal datetime object.

        Returns:
        - YamTimes: A new YamTimes instance set to the first day of the next month of the internal datetime object.
        """
        next_month = self.next_month().datetime
        return YamTimes(dt=next_month)

    def is_same_day_of_week(self, other: "YamTimes") -> bool:
        """
        Checks if two YamTimes instances are on the same day of the week.

        This method does not check if the two instances are on the same date, but
        rather if they are on the same day of the week (e.g. Monday, Tuesday, etc.).

        Parameters:
        - other (YamTimes): The other YamTimes instance to compare against.

        Returns:
        - bool: Whether the two instances are on the same day of the week.
        """
        return self.__datetime.weekday() == other.datetime.weekday()

    def is_same_time(self, other: "YamTimes") -> bool:
        """
        Checks if two YamTimes instances are at the same time of day.

        This method does not check if the two instances are on the same date, but
        rather if they are at the same time of day (e.g. 10:00:00 AM, 12:00:00 PM, etc.).

        Parameters:
        - other (YamTimes): The other YamTimes instance to compare against.

        Returns:
        - bool: Whether the two instances are at the same time of day.
        """

        return self.__datetime.time() == other.datetime.time()

    def day_of_week(self) -> str:
        """
        Returns the full name of the day of the week for the internal datetime object.

        Returns:
        - str: The full name of the day of the week (e.g., "Monday", "Tuesday").
        """

        return self.__datetime.strftime('%A')

    def month_of_year(self) -> str:
        """
        Returns the full name of the month for the internal datetime object.

        Returns:
        - str: The full name of the month (e.g., "January", "February", etc.).
        """
        return self.__datetime.strftime('%B')

    def time_of_day(self) -> str:
        """
        Returns the time of day as a string in 12-hour format with AM/PM.

        Returns:
        - str: The time of day in 12-hour format (e.g., "12:00:00 PM", "09:45:10 AM", etc.).
        """
        return self.__datetime.strftime('%I:%M:%S %p')

    def get_time_zone(self) -> str:
        """
        Returns the time zone as a string for the internal datetime object.

        Returns:
        - str: The time zone as a string (e.g., "UTC", "EST", "PDT", etc.).
        """
        return self.__datetime.strftime('%Z')

    def add_hours(self, hours: int) -> "YamTimes":
        """
        Adds a specified number of hours to the internal datetime object.

        Parameters:
        - hours (int): The number of hours to add. Can be positive or negative.

        Returns:
        - YamTimes: A new YamTimes instance representing the datetime after adding the specified number of hours.
        """
        return YamTimes(dt=self.__datetime + timedelta(hours=hours))

    def subtract_hours(self, hours: int) -> "YamTimes":
        """
        Subtracts a specified number of hours from the internal datetime object.

        Parameters:
        - hours (int): The number of hours to subtract. Can be positive or negative.

        Returns:
        - YamTimes: A new YamTimes instance representing the datetime after subtracting the specified number of hours.
        """
        return YamTimes(dt=self.__datetime - timedelta(hours=hours))

    def is_same_hour(self, other: "YamTimes") -> bool:
        """
        Checks if the internal datetime object is in the same hour as another YamTimes instance.

        Parameters:
        - other (YamTimes): The YamTimes instance to compare against.

        Returns:
        - bool: True if the internal datetime object is in the same hour as the other YamTimes instance, False otherwise.
        """

        return self.__datetime.hour == other.datetime.hour

    def start_of_next_month(self) -> "YamTimes":
        """
        Advances the internal datetime object to the start of the next month.

        This method calculates the first day of the following month
        from the internal datetime object and returns a new YamTimes instance 
        set to that date with the time set to 00:00:00.

        Returns:
        - YamTimes: A new YamTimes instance representing the start of the next month.
        """
        return self.next_month().start_of_month()

    def end_of_next_month(self) -> "YamTimes":
        """
        Advances the internal datetime object to the end of the next month.

        This method calculates the last day of the following month
        from the internal datetime object and returns a new YamTimes instance
        set to that date with the time set to 23:59:59.999999.

        Returns:
        - YamTimes: A new YamTimes instance representing the end of the next month.
        """
        return self.next_month().end_of_month()


    def time_until_next_year(self) -> "YamTimes":
        """
        Calculates the time difference between the internal datetime object and the start of the next year.

        Returns:
        - YamTimes: The time difference between the internal datetime object and the start of the next year.
        """

        
        return YamTimes(dt=datetime(self.__datetime.year + 1, 1, 1))

    def get_iso_date(self) -> str:
        """
        Returns the internal datetime object as an ISO 8601 formatted date string.

        Returns:
        - str: The internal datetime object as an ISO 8601 formatted date string (YYYY-MM-DD).
        """
        return self.__datetime.strftime('%Y-%m-%d')

    def get_iso_time(self) -> str:
        """
        Returns the internal datetime object as an ISO 8601 formatted time string.

        Returns:
        - str: The internal datetime object as an ISO 8601 formatted time string (HH:MM:SS).
        """        
        return self.__datetime.strftime('%H:%M:%S')

    def is_working_day(self) -> bool:
        """
        Determines if the internal datetime object represents a working day.

        A working day is considered to be any weekday (Monday to Friday).

        Returns:
        - bool: True if the internal datetime object is a working day, False otherwise.
        """
        return self.__datetime.weekday() < 5

    def get_current_timestamp(self) -> float:
        """
        Returns the current timestamp as a float.

        Returns:
        - float: The current timestamp in seconds since the Epoch (January 1, 1970).
        """
        
        return datetime.now().timestamp()

    def get_current_datetime(self) -> "YamTimes":
        """
        Returns a new YamTimes instance set to the current date and time.

        Returns:
        - YamTimes: A new YamTimes instance set to the current date and time.
        """
        return YamTimes(dt=datetime.now())
    
    def __call__(self):
        return self.string()

    def __str__(self):
        return self.string()

    def __repr__(self):
        return f"YamTimes({self.__datetime!r})"

    def __format__(self, format_spec):
        return self.__datetime.strftime(format_spec or "%Y-%m-%d %H:%M:%S")

    def __eq__(self, other):
        return isinstance(other, YamTimes) and self.__datetime == other.datetime

    def __lt__(self, other):
        return isinstance(other, YamTimes) and self.__datetime < other.datetime

    def __le__(self, other):
        return isinstance(other, YamTimes) and self.__datetime <= other.datetime

    def __gt__(self, other):
        return isinstance(other, YamTimes) and self.__datetime > other.datetime

    def __ge__(self, other):
        return isinstance(other, YamTimes) and self.__datetime >= other.datetime
