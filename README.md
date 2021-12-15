# REST API для парку машин з водіями

## endpoint для модели Driver:
    * + GET /drivers/driver/ - вивід списку водіїв
    * + GET /drivers/driver/?created_at__gte=D.M.Y - вивід списку водіїв, які створені після заданої дати
    * + GET /drivers/driver/?created_at__lte=D.M.Y - вивід списку водіїв, котрі створені до заданої дати
    * + GET /drivers/driver/<driver_id>/ - отримання інформації по певному водію
    * + POST /drivers/driver/ - створення нового водія
    * + UPDATE /drivers/driver/<driver_id>/ - редагування водія
    * + DELETE /drivers/driver/<driver_id>/ - видалення водія

## endpoint для модели Vehicle:
    * + GET /vehicles/vehicle/ - вивід списку машин
    * + GET /vehicles/vehicle/?with_drivers=false - вивід списку машин з водіями
    * + GET /vehicles/vehicle/?with_drivers=true - вивід списку машин без водіїв
    * + GET /vehicles/vehicle/<vehicle_id> - отримання інформації по певній машині
    * + POST /vehicles/vehicle/ - створення нової машини
    * + UPDATE /vehicles/vehicle/<vehicle_id>/ - редагування машини
    * + POST /vehicles/set_driver/<vehicle_id>/ - садимо водія в машину / висаджуємо водія з машини
    * + DELETE /vehicles/vehicle/<vehicle_id>/ - видалення машини