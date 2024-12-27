
# YamTimes

**YamTimes** is a modern, lightweight Python library for date and time manipulation, offering an intuitive API for common temporal operations. It provides a clean interface for working with dates, times, and timezones while maintaining simplicity and performance.

## 🚀 Key Features

### 📅 Comprehensive Date Handling

```python
# Easy date creation and formatting
time = YamTimes(2024, 3, 15)
print(time.to_string("%Y-%m-%d"))  # "2024-03-15"

# Check business days
time.is_weekday()  # True
time.next_business_day()  # Skip weekends
```

### ⏰ Time Manipulation

```python
# Time arithmetic
time.add_hours(24)
time.subtract_minutes(30)
time.next_week()
time.last_month()
```

### 🌟 Smart Date Features

```python
# Zodiac sign detection
time.is_aries_sign()  # Check if date falls in Aries
time.is_pisces_sign()  # Check if date falls in Pisces

# Date comparison
time.is_weekend()  # Check if it's weekend
time.is_holiday("US")  # Check if it's a holiday
```

### 🌍 Internationalization

```python
# Get localized names
time.month_name("pt_BR")  # "Março"
time.weekday_name("es_ES")  # "Viernes"
```

### 📊 Date Analysis

```python
# Period calculations
time.days_in_month()  # Get days in current month
time.is_leap_year()  # Check if current year is leap
time.weeks_in_year()  # Get number of weeks in year
```

### ⚡ Performance

- Lightweight wrapper around Python's datetime
- Fast execution for common operations

## 🛠️ Installation

```bash
pip install yamtimes
```

## 📚 Documentation

Full documentation available at [YamTimes Wiki](https://github.com/svidaniya/yamtimes/wiki)

## 📝 License

MIT License
