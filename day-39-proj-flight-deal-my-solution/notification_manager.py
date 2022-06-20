class NotificationManager:
    def __init__(self):
        # Insert twilio number, my number, twilio auth key here
        # Make header
        # decidedly NOT doing this part of the assignment.
        pass

    def notify_via_sms(self, trip):
        # Make message and send
        msg = f"Flight deal! {trip.price} {trip.currency} for {trip.orig_city} ({trip.orig_code}) " \
              f"to {trip.dest_city} ({trip.dest_code}), for {trip.duration} nights, " \
              f"{trip.depart_date} to {trip.return_date}"
        if trip.stop_overs > 0:
            add = f"Stop over in {trip.stopover_city}"
            msg = msg + add
        print(msg)

    # function to get emails from spreadsheet via sheety, fill in google fights urls, and send an email.
    