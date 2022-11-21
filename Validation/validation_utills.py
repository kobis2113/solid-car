def validate_field(validation_callback, validation_value):

    if not (validation_callback(validation_value)):
        raise Exception(f'{validation_value} is invalid')
    return validation_value
