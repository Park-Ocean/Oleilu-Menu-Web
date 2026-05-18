from database import SessionLocal, engine
import models
from security import get_password_hash

models.Base.metadata.create_all(bind=engine)

# DATOS DE LA CARTA OLEILU
MENU_ITEMS = [

    # --- BRUNCH (todos los días hasta las 12:30) ---
    {
        "name": "BRUNCH BENEDICTINO",
        "category": "Brunch",
        "price": 13500,
        "description": "Elige tu tostón benedictino tocino o salmón, un café a elección y jugo o limonada."
    },
    {
        "name": "DESAYUNO COMPLETO",
        "category": "Brunch",
        "price": 15000,
        "description": "Huevos revueltos, tocino y palta. Camote o tostadas de masa madre. Café a elección, medialuna o queque y jugo o limonada a elección."
    },
    {
        "name": "BRUNCH CLÁSICO",
        "category": "Brunch",
        "price": 14000,
        "description": "Sandwich El Fundido, elige tu bollería preferida, café a elección y jugo o limonada."
    },

    # --- ALMUERZO OLEILU (12:30 a 15:30) ---
    {
        "name": "SÁNDWICH, PAPITAS Y BEBIDA",
        "category": "Almuerzo",
        "price": 13000,
        "description": "Elige cualquiera de nuestros sándwiches con agregado de mix de papas y camote frito. Además una bebida o limonada. Cambia tu bebida por una cerveza hasta pronto por $2000 adicionales."
    },

    # --- DESAYUNO / BRUNCH (carta individual) ---
    {
        "name": "BENEDICTINOS TOCINO",
        "category": "Desayuno Brunch",
        "price": 10500,
        "description": "Tostón de pan brioche, huevos pochados, tocino y salsa holandesa. Alternativa vegetariana con palta."
    },
    {
        "name": "BENEDICTINOS SALMÓN",
        "category": "Desayuno Brunch",
        "price": 11500,
        "description": "Tostón de pan brioche, huevos pochados, salmón ahumado, salsa holandesa y furikake."
    },
    {
        "name": "SANDWICH OLEILÚ",
        "category": "Desayuno Brunch",
        "price": 9900,
        "description": "Omelette, straciattela, pesto de albahaca y tocino. En pan brioche."
    },
    {
        "name": "DESAYUNO CLÁSICO",
        "category": "Desayuno Brunch",
        "price": 9900,
        "description": "Huevos revueltos, tocino y palta. Alternativa de camote o tostadas de masa madre."
    },
    {
        "name": "TOSTÓN VEGANO",
        "category": "Desayuno Brunch",
        "price": 8900,
        "description": "Tostón de masa madre, humus, salteado de verduras, tomates cherry y semillas de zapallo.",
        "tags": ["vegano"]
    },

    # --- ENSALADAS ---
    {
        "name": "CAESAR CLÁSICA",
        "category": "Ensaladas",
        "price": 12500,
        "description": "Mix de hojas verdes, milanesa de pollo, cubos de palta, tomate cherry, crutones caseros, cebolla morada, topping de parmesano y dressing caesar de la casa."
    },
    {
        "name": "LENTEJAS VEGAN",
        "category": "Ensaladas",
        "price": 12500,
        "description": "Mix de hojas verdes, lentejas con vinagreta de comino, cubos de palta, tomates cherry, camote asado, crutones caseros y topping de semillas.",
        "tags": ["vegano"]
    },
    {
        "name": "AGREGADO PAPITAS",
        "category": "Ensaladas",
        "price": 2500,
        "description": "Mix de papas y camote frito."
    },

    # --- SANDWICHES ---
    {
        "name": "CUBANITO",
        "category": "Sandwiches",
        "price": 10900,
        "description": "Jamón artesanal, lomo de cerdo asado, pepinillos, mostaza, queso cheddar y queso gouda. En pan de masa madre."
    },
    {
        "name": "BERENJENA SPICY",
        "category": "Sandwiches",
        "price": 8900,
        "description": "Milanesa de berenjena, salsa de ají fermentado, hojas verdes. En focaccia."
    },
    {
        "name": "EL FUNDIDO",
        "category": "Sandwiches",
        "price": 7900,
        "description": "Jamón artesanal, queso gouda y queso cheddar. En pan brioche."
    },
    {
        "name": "CRUNCHY CAESAR",
        "category": "Sandwiches",
        "price": 11300,
        "description": "Pollo apanado, cebolla morada, pesto de la casa, hojas verdes y dressing caesar de la casa. En focaccia. Alternativa vegetariana con berenjena apanada."
    },
    {
        "name": "SIERRA MELT",
        "category": "Sandwiches",
        "price": 8900,
        "description": "Sierra ahumada artesanal, en salsa tártara, queso gauda y queso cheddar fundido. En pan de masa madre."
    },
    {
        "name": "SEA CROISSANT",
        "category": "Sandwiches",
        "price": 12500,
        "description": "Slice de salmón ahumado, con palta laminada, ricota y rúcula con una reducción de aceto balsámico en croissant."
    },

    # --- PASTELERÍA ---
    {
        "name": "ROLLO DE CANELA",
        "category": "Pastelería",
        "price": 3200,
        "description": "Rollo de canela artesanal."
    },
    {
        "name": "MEDIALUNA",
        "category": "Pastelería",
        "price": 2500,
        "description": "Medialuna artesanal."
    },
    {
        "name": "CROISSANT",
        "category": "Pastelería",
        "price": 2800,
        "description": "Croissant artesanal."
    },
    {
        "name": "CARROT CAKE",
        "category": "Pastelería",
        "price": 3000,
        "description": "Carrot cake artesanal."
    },
    {
        "name": "CHOCO BANANA BREAD",
        "category": "Pastelería",
        "price": 2800,
        "description": "Choco banana bread artesanal."
    },
    {
        "name": "BROWNIE",
        "category": "Pastelería",
        "price": 4000,
        "description": "Con nueces y ganache de chocolate Neucober 72%."
    },
    {
        "name": "CROISSANT OLEILÚ",
        "category": "Pastelería",
        "price": 5500,
        "description": "Crema pastelera de Earl Grey y naranja confitada."
    },
    {
        "name": "CROISSANT GIANDUJA",
        "category": "Pastelería",
        "price": 6000,
        "description": "Nutella y frutos rojos."
    },
    {
        "name": "CROISSANT MANJAR",
        "category": "Pastelería",
        "price": 5500,
        "description": "Manjar, topping de almendras y azúcar flor."
    },
    {
        "name": "TOSTÓN FRANCÉS",
        "category": "Pastelería",
        "price": 7000,
        "description": "Tostón de pan brioche rebozado, fruta de estacionalidad y yogur montado."
    },
    {
        "name": "PANCAKES",
        "category": "Pastelería",
        "price": 7000,
        "description": "Topping de yogur montado, miel de palma y fruta de estación."
    },

    # --- COOKIES ---
    {
        "name": "COOKIE CHIP DE CHOCOLATE",
        "category": "Cookies",
        "price": 3500,
        "description": "Clásica galleta de vainilla con trozos de chocolate semi amargo."
    },
    {
        "name": "COOKIE MATCHA & FRAMBUESA",
        "category": "Cookies",
        "price": 3500,
        "description": "Galleta de matcha y chocolate blanco con insert de mermelada de frambuesa."
    },
    {
        "name": "COOKIE LEMON PIE",
        "category": "Cookies",
        "price": 3500,
        "description": "Relleno de crema de limón y topping de merengue."
    },
    {
        "name": "COOKIE CHEESECAKE ARÁNDANO",
        "category": "Cookies",
        "price": 3200,
        "description": "Relleno de queso crema y arándanos."
    },
    {
        "name": "COOKIE MANÍ & SALTED CARAMEL",
        "category": "Cookies",
        "price": 3200,
        "description": "Relleno de pasta de maní y salsa de caramelo salado."
    },
    {
        "name": "COOKIE APPLE TOFFEE",
        "category": "Cookies",
        "price": 3200,
        "description": "Con nueces, manzana caramelizada y salsa toffee."
    },

    # --- CAFETERÍA ---
    {
        "name": "ESPRESSO SIMPLE",
        "category": "Cafetería",
        "price": 2400,
        "description": "Espresso simple. Café italiano premium marca Vergnano."
    },
    {
        "name": "ESPRESSO DOBLE",
        "category": "Cafetería",
        "price": 2800,
        "description": "Espresso doble. Café italiano premium marca Vergnano."
    },
    {
        "name": "AMERICANO SIMPLE",
        "category": "Cafetería",
        "price": 2800,
        "description": "Americano simple. Café italiano premium marca Vergnano."
    },
    {
        "name": "AMERICANO DOBLE",
        "category": "Cafetería",
        "price": 3200,
        "description": "Americano doble. Café italiano premium marca Vergnano."
    },
    {
        "name": "CAPUCCINO SIMPLE",
        "category": "Cafetería",
        "price": 3290,
        "description": "Capuccino simple. Café italiano premium marca Vergnano."
    },
    {
        "name": "CAPUCCINO DOBLE",
        "category": "Cafetería",
        "price": 3590,
        "description": "Capuccino doble. Café italiano premium marca Vergnano."
    },
    {
        "name": "MOCACCINO",
        "category": "Cafetería",
        "price": 4000,
        "description": "Mocaccino. Café italiano premium marca Vergnano."
    },
    {
        "name": "LATTE",
        "category": "Cafetería",
        "price": 3590,
        "description": "Latte. Café italiano premium marca Vergnano."
    },
    {
        "name": "FLAT WHITE",
        "category": "Cafetería",
        "price": 3800,
        "description": "Flat white. Café italiano premium marca Vergnano."
    },
    {
        "name": "CHAI LATTE",
        "category": "Cafetería",
        "price": 3500,
        "description": "Chai latte."
    },
    {
        "name": "DIRTY CHAI LATTE",
        "category": "Cafetería",
        "price": 4000,
        "description": "Dirty chai latte."
    },
    {
        "name": "MATCHA LATTE",
        "category": "Cafetería",
        "price": 3500,
        "description": "Matcha latte."
    },
    {
        "name": "TÉ",
        "category": "Cafetería",
        "price": 2000,
        "description": "Té."
    },
    {
        "name": "AGREGADO LECHE VEGETAL",
        "category": "Cafetería",
        "price": 500,
        "description": "Not milk o soya."
    },
    {
        "name": "SHOT DE SYRUP",
        "category": "Cafetería",
        "price": 500,
        "description": "Vainilla o caramelo."
    },
    {
        "name": "DESCAFEINADO",
        "category": "Cafetería",
        "price": 300,
        "description": "Agregado descafeinado."
    },
    {
        "name": "ICED",
        "category": "Cafetería",
        "price": 300,
        "description": "Agregado para bebida helada."
    },

    # --- CERVEZAS ---
    {
        "name": "CERVEZA HASTA PRONTO",
        "category": "Cervezas",
        "price": 5000,
        "description": "Mientras Tanto Amber Ale o Tiempo Libre Lager."
    },
    {
        "name": "MICHELADA",
        "category": "Cervezas",
        "price": 4500,
        "description": "Cerveza lager, borde de sal y merquén, jugo de limón y salsa inglesa."
    },
    {
        "name": "CHELADA",
        "category": "Cervezas",
        "price": 4000,
        "description": "Cerveza lager, borde de sal y jugo de limón."
    },

    # --- MOCKTAILS ---
    {
        "name": "GOLDEN GINGER",
        "category": "Mocktails",
        "price": 5000,
        "description": "Mezcla de jugo de piña y limón, jengibre y agua tónica."
    },
    {
        "name": "ESPRESSO TONIC",
        "category": "Mocktails",
        "price": 5500,
        "description": "Shot de espresso con agua tónica."
    },
    {
        "name": "LIMONADA",
        "category": "Mocktails",
        "price": 4000,
        "description": "Simple, Menta o Menta Jengibre."
    },
    {
        "name": "JUGO VARIEDADES",
        "category": "Mocktails",
        "price": 4000,
        "description": "Jugo de frutas variadas."
    },

    # --- BEBIDAS ---
    {
        "name": "COCA COLA",
        "category": "Bebidas",
        "price": 2500,
        "description": "Coca Cola."
    },
    {
        "name": "COCA COLA ZERO",
        "category": "Bebidas",
        "price": 2500,
        "description": "Coca Cola Zero."
    },
    {
        "name": "SPRITE",
        "category": "Bebidas",
        "price": 2500,
        "description": "Sprite."
    },
    {
        "name": "SPRITE ZERO",
        "category": "Bebidas",
        "price": 2500,
        "description": "Sprite Zero."
    },
    {
        "name": "FANTA",
        "category": "Bebidas",
        "price": 2500,
        "description": "Fanta."
    },
]


def seed_db():
    print("Cargando menú oficial Oleilu...")
    db = SessionLocal()

    count = 0
    for item in MENU_ITEMS:
        if "description" not in item:
            item["description"] = None
            
        if "tags" in item:
            tags_str = ", ".join(item.pop("tags"))
            if item["description"]:
                item["description"] += f" [{tags_str}]"
            else:
                item["description"] = f"[{tags_str}]"

        producto = models.Product(**item)
        db.add(producto)
        count += 1
        
    # Crear configuración inicial si no existe
    config = db.query(models.AppConfig).first()
    if not config:
        print("Creando configuración inicial de la aplicación...")
        hashed_pw = get_password_hash("ola2024")
        new_config = models.AppConfig(admin_password=hashed_pw, recovery_email=None)
        db.add(new_config)

    db.commit()
    print(f"Se cargaron {count} productos oficiales en la base de datos.")
    db.close()


if __name__ == "__main__":
    seed_db()