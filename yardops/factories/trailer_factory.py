from yardops.models.trailer import Trailer

class TrailerFactory:
    @staticmethod
    def create(trailer_type, trailer_number,carrier_name, **kwargs):
        trailer_type = trailer_type.upper()
        if trailer_type == "REEFER":
            temp = kwargs.get("temp_setting", -10)
            return Trailer(
                trailer_type=trailer_type,
                trailer_number=trailer_number,
                carrier_name=carrier_name,
                temp_setting=temp
            )

        elif trailer_type == "FLATBED":
            if kwargs.get("temp_setting") is not None:
                raise ValueError("flatbed should not have temp_setting")
            return Trailer(
                trailer_type=trailer_type,
                trailer_number=trailer_number,
                carrier_name=carrier_name
                )
        elif trailer_type == "DRY":
            return Trailer(
                trailer_type=trailer_type,
                trailer_number=trailer_number,
                carrier_name = carrier_name
            )
        else:
            raise ValueError("Invalid")
    