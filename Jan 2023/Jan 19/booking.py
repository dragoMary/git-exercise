from datetime import datetime, timedelta


booking_info = {
    'name': 'dragomir M',
    'email': 'dragomir@email.com',
    'room_type': 'Deluxe Suite',
    'check_in_date': '01/01/2023',
    'check_out_date': '01/05/2023',
    'guest_count': 'nr.of guests: 2',
}

file_name = booking_info['name']




check_in_date = datetime.strptime(booking_info['check_in_date'], '%m/%d/%Y')
check_out_date = datetime.strptime(booking_info['check_out_date'], '%m/%d/%Y')


booking_duration = check_out_date - check_in_date

print('Booking information saved to ' + file_name)
print('Number of days booked:', booking_duration.days)
print(booking_info['room_type'])
print(booking_info['guest_count'])

