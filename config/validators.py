from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import re


@deconstructible
class PhoneValidator:

    def __call__(self, phone):

        value = re.match("^998(90|91|93|94|95|98|99|33|97|88|77)[0-9]{7}$", phone)
        if value and len(phone) == 12:
            return
        else:
            raise ValidationError(f"{phone} telefon raqam emas")
