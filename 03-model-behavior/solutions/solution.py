from pydantic import BaseModel,model_validator,computed_field,field_validator,Field

# TODO: Create Booking model
# Fields:
# - user_id: int
# - room_id: int
# - nights: int (must be >=1)
# - rate_per_night: float
# Also, add computed field: total_amount = nights * rate_per_night

class Booking(BaseModel):
    user_id:int
    room_id:int
    nights:int=Field(...,ge=1)
    rate_per_night:float

    @computed_field
    @property
    def total_amount(self)->float:
        return self.nights * self.rate_per_night


INPUT_DATA={ "user_id":1, "room_id":1, "nights":2, "rate_per_night":100}
booking = Booking(**INPUT_DATA)

print(booking.total_amount)