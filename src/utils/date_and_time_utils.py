import datetime


def to_iso_zulu(input_date):
    if input_date is None:
        return None
    return input_date.replace(microsecond=0).replace(tzinfo=datetime.timezone.utc).isoformat().replace("+00:00", "Z")
