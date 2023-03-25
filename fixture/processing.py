
def propagate(data_source, obj):
    for key, value in data_source.__dict__.items():
        if getattr(obj, key) is None:
            setattr(obj, key, value)
    return obj