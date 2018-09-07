def make_car(manufactures, model, **car_infos):
    car = {}
    car['manufactures'] = manufactures
    car['model'] = model
    for key, value in car_infos.items():
        car[key] = value
    return car