from database import SessionLocal, engine
import models
from security import get_password_hash

models.Base.metadata.create_all(bind=engine)

# DATOS DE LA CARTA COFFEE BEANS
MENU_ITEMS = [
    # --- CAFETERÍA - BEBIDAS CALIENTES ---
    {
        "name": "ESPRESSO SIMPLE",
        "category": "Bebidas Calientes",
        "price": 2400,
        "description": "Espresso simple tradicional."
    },
    {
        "name": "FLAT WHITE",
        "category": "Bebidas Calientes",
        "price": 3200,
        "description": "Flat white cremoso."
    },
    {
        "name": "ESPRESSO DOBLE",
        "category": "Bebidas Calientes",
        "price": 2800,
        "description": "Espresso doble concentrado."
    },
    {
        "name": "LATTE",
        "category": "Bebidas Calientes",
        "price": 3500,
        "description": "Café latte con leche vaporizada."
    },
    {
        "name": "AMERICANO",
        "category": "Bebidas Calientes",
        "price": 2800,
        "description": "Café americano clásico."
    },
    {
        "name": "MACCHIATO",
        "category": "Bebidas Calientes",
        "price": 2700,
        "description": "Espresso con toque de leche vaporizada."
    },
    {
        "name": "CAPUCCINO",
        "category": "Bebidas Calientes",
        "price": 3200,
        "description": "Capuccino clásico con espuma de leche."
    },
    {
        "name": "CAFÉ FILTRADO",
        "category": "Bebidas Calientes",
        "price": 5000,
        "description": "Café de especialidad preparado por filtrado."
    },
    {
        "name": "CAPUCCINO DOBLE",
        "category": "Bebidas Calientes",
        "price": 3900,
        "description": "Capuccino con doble shot de espresso."
    },

    # --- CAFETERÍA - OTRAS BEBIDAS CALIENTES ---
    {
        "name": "MOCCA",
        "category": "Otras Bebidas Calientes",
        "price": 3600,
        "description": "Café con chocolate caliente."
    },
    {
        "name": "CHOCOLATE",
        "category": "Otras Bebidas Calientes",
        "price": 3200,
        "description": "Chocolate caliente cremoso."
    },
    {
        "name": "MATCHA LATTE",
        "category": "Otras Bebidas Calientes",
        "price": 3500,
        "description": "Latte de matcha con leche vaporizada."
    },
    {
        "name": "CHAI LATTE",
        "category": "Otras Bebidas Calientes",
        "price": 3000,
        "description": "Latte de chai especiado."
    },
    {
        "name": "DIRTY CHAI",
        "category": "Otras Bebidas Calientes",
        "price": 3600,
        "description": "Chai latte con shot de espresso."
    },
    {
        "name": "TAZA DE TÉ",
        "category": "Otras Bebidas Calientes",
        "price": 2800,
        "description": "Taza de té a elección."
    },

    # --- CAFETERÍA - BEBIDAS FRÍAS ---
    {
        "name": "EARLY RUSH (TÉ FRÍO)",
        "category": "Bebidas Frías",
        "price": 3000,
        "description": "Té frío refrescante."
    },
    {
        "name": "KOMBUCHA",
        "category": "Bebidas Frías",
        "price": 3200,
        "description": "Kombucha artesanal fermentada."
    },
    {
        "name": "MATCHA FRÍO",
        "category": "Bebidas Frías",
        "price": 3800,
        "description": "Matcha preparado en frío."
    },
    {
        "name": "ZUMO MANDARINA",
        "category": "Bebidas Frías",
        "price": 3200,
        "description": "Jugo de mandarina natural prensado."
    },
    {
        "name": "ESPRESSO TONIC",
        "category": "Bebidas Frías",
        "price": 3300,
        "description": "Espresso sobre agua tónica."
    },
    {
        "name": "ESPRESSO TANGERINE",
        "category": "Bebidas Frías",
        "price": 3500,
        "description": "Espresso con mandarina."
    },
    {
        "name": "AGUA EN BOTELLA",
        "category": "Bebidas Frías",
        "price": 2000,
        "description": "Agua mineral en botella."
    },

    # --- CAFETERÍA - EXTRAS ---
    {
        "name": "LECHE VEGETAL",
        "category": "Extras",
        "price": 500,
        "description": "Leche vegetal a elección."
    },
    {
        "name": "TOCINO O PALTA",
        "category": "Extras",
        "price": 1500,
        "description": "Porción de tocino o palta."
    },
    {
        "name": "HUEVOS",
        "category": "Extras",
        "price": 1000,
        "description": "Porción de huevos."
    },
    {
        "name": "SHOT DE CAFÉ",
        "category": "Extras",
        "price": 700,
        "description": "Shot extra de espresso."
    },
    {
        "name": "PORCIÓN DE PAN",
        "category": "Extras",
        "price": 1000,
        "description": "Porción de pan."
    },
    {
        "name": "PORCIÓN DE FRUTA",
        "category": "Extras",
        "price": 2500,
        "description": "Porción de fruta fresca de temporada."
    },

    # --- PASTELERÍA - TARTAS ---
    {
        "name": "TIRAMISÚ RECETA TRADICIONAL",
        "category": "Pastelería",
        "price": 3500,
        "description": "Tiramisú preparado con receta tradicional italiana."
    },
    {
        "name": "TORTA DE ZANAHORIA",
        "category": "Pastelería",
        "price": 3500,
        "description": "Torta de zanahoria con toque de manjar para endulzar el día."
    },
    {
        "name": "TARTA SUECA DE CHOCOLATE",
        "category": "Pastelería",
        "price": 2800,
        "description": "Tarta sueca de chocolate artesanal."
    },
    {
        "name": "CHEESECAKE DE ESPRESSO",
        "category": "Pastelería",
        "price": 3200,
        "description": "Cheesecake con base de espresso."
    },
    {
        "name": "TARTA DE FRUTOS ROJOS",
        "category": "Pastelería",
        "price": 2900,
        "description": "Tarta artesanal de frutos rojos."
    },

    # --- BOLLERÍA ---
    {
        "name": "WAFFLE AZUCARADO",
        "category": "Bollería",
        "price": 2300,
        "description": "Waffle clásico con azúcar."
    },
    {
        "name": "WAFFLE CREMA Y FRUTA",
        "category": "Bollería",
        "price": 3000,
        "description": "Waffle con crema y frutas frescas."
    },
    {
        "name": "PAN DE CHOCOLATE",
        "category": "Bollería",
        "price": 2200,
        "description": "Pan de chocolate artesanal."
    },
    {
        "name": "ROLLITO DE CANELA",
        "category": "Bollería",
        "price": 2300,
        "description": "Rollito de canela esponjoso."
    },
    {
        "name": "CROISSANT",
        "category": "Bollería",
        "price": 1800,
        "description": "Croissant clásico de mantequilla."
    },
    {
        "name": "CROISSANT DULCE RELLENO",
        "category": "Bollería",
        "price": 2950,
        "description": "Croissant relleno dulce."
    },
    {
        "name": "CROISSANT SALAME O JAMÓN/QUESO",
        "category": "Bollería",
        "price": 2950,
        "description": "Croissant salado relleno de salame o jamón con queso."
    },

    # --- BOLLERÍA - ESPECIAL ---
    {
        "name": "TOSTADA FRANCESA (Receta Coffee Beans)",
        "category": "Bollería",
        "price": 5100,
        "description": "Deliciosa tostada caramelizada, rellena de centro cremoso y almendras laminadas, coronada con pompón de crema batida y frutas de estación, acompañada con una porción de Miel de Maple para endulzar tu día."
    },

    # --- DESAYUNOS ---
    {
        "name": "DESAYUNO AMERICANO",
        "category": "Desayunos",
        "price": 8300,
        "description": "Deliciosos huevos cremosos, acompañados con tocino, tostadas frescas, café o té, jugo de mandarina, mermelada y un lingote de vainilla. Disponible hasta las 12am."
    },
    {
        "name": "COLOMBIANO",
        "category": "Desayunos",
        "price": 8500,
        "description": "Huevos coloridos (cebolla y tomate) acompañados con porción de arepitas de maíz, porción de queso fresco, pandebonos 2 unid (pan de queso), café o chocolate. Disponible hasta las 12am."
    },
    {
        "name": "BOWL DE GRANOLA",
        "category": "Desayunos",
        "price": 6700,
        "description": "Granola fresca preparada en casa, sobre una cama de yogurt natural, fruta fresca de temporada endulzada con miel, zumo prensado de mandarina o café. Disponible hasta las 12am."
    },

    # --- TOSTADAS SALADAS Y DULCES ---
    {
        "name": "RAYO DE SOL",
        "category": "Tostadas",
        "price": 8100,
        "description": "Pan blanco de masa madre. Mango en trozo grillado y caramelizado, sobre una base de pesto, acompañado con queso de cabra y aromatizado con dressing balsámico, una pizca de merquén que aporta profundidad al sabor."
    },
    {
        "name": "HUEVOS TURCOS",
        "category": "Tostadas",
        "price": 6800,
        "description": "Pan de masa madre. Dos huevos poché sobre una salsa de yogur natural con perejil y ajo, deliciosos triángulos de tostadas, bañado con aceite de paprica un poco picante."
    },
    {
        "name": "COFFEE BLOOM",
        "category": "Tostadas",
        "price": 5900,
        "description": "Pan blanco de masa madre. Carne mechada preparada al horno con finas hierbas a cocción lenta, acompañado con tomate cherry confitado en una cama de lechuga y bañado en una salsa de café fresco tostado por nosotros."
    },
    {
        "name": "BENEDICTA ITALIANA",
        "category": "Tostadas",
        "price": 5800,
        "description": "Pan blanco de masa madre. Salsa pomodoro fresca coronada con huevos poche, aromatizada con aceite de albahaca y delicioso queso cabra."
    },
    {
        "name": "HOLANDESA",
        "category": "Tostadas",
        "price": 5800,
        "description": "Pan semilla masa madre. También opción vegetariana. Deliciosos huevos pochados, bañados en cremosa salsa holandesa, acompañados con láminas de tocino o palta (opción vegetariana), ciboulette, toques de pimienta y coronado con hermosos brotes verdes."
    },
    {
        "name": "PURPLE BLISS",
        "category": "Tostadas",
        "price": 5100,
        "description": "Pan semilla de masa madre. Delicioso hummus de betarraga con un toque especial del chef, para hacerlo más cremoso. Acompañado de palta, aromatizado con aceite de cilantro y cilantro fresco finamente picado."
    },

    # --- SÁNDWICHES ---
    {
        "name": "TOSCANO",
        "category": "Sándwiches",
        "price": 8200,
        "description": "Pan blanco de masa madre. Delicioso queso boconccini sobre una base de pesto hecho en casa, acompañado con tomate cherry confitados, aromatizado con aceite de albahaca y una pizca de sal gruesa."
    },
    {
        "name": "FOCACCIA RUSTIC",
        "category": "Sándwiches",
        "price": 6800,
        "description": "Pan hecho en casa. Carne laminada, horneada en cocción lenta acompañada con un mix de hojas verdes, aderezado con una aromática mermelada de pimentón y acompañada de tomate confitado."
    },
    {
        "name": "MEDITERRANEO CRUNCH",
        "category": "Sándwiches",
        "price": 5400,
        "description": "Pan blanco. Vegetariano. Berenjena crispy, zapallos confitados acompañados con pasta de aceituna verde, albahaca y mizuna, tomate cherry fresco y salsa pomodoro."
    },
    {
        "name": "SMOKY CHICKEN GREENS",
        "category": "Sándwiches",
        "price": 5500,
        "description": "Pan blanco masa madre. Pollo perfectamente grillado acompañado de cebollas a la barbecue, y champiñones a la mantequilla, sobre una cama de mix de lechugas frescas."
    },

    # --- ENSALADAS ---
    {
        "name": "TROPICO",
        "category": "Ensaladas",
        "price": 6200,
        "description": "Ensalada con trozos de mango, queso de cabra y nueces, sobre un mix de hojas verdes, acompañado con un delicioso dressing hecho con compota de mango fresca, aromatizado con cardamomo y otros secretos del chef."
    },
    {
        "name": "DEL HUERTO",
        "category": "Ensaladas",
        "price": 5800,
        "description": "Pollo grillado, tomates frescos, trozos de pepino, aros de cebollas moradas, champiñones al ajillo, aceitunas negras, en una cama de lechugas y aderezado con una limoneta endulzada con miel de maple."
    },
    {
        "name": "FRUIT PUNCH",
        "category": "Ensaladas",
        "price": 3800,
        "description": "Mix de frutas de estación, hojas de menta fresca y rica salsa de frutos rojos al vino tinto, acompañado con mermelada de fruta."
    },
]


def seed_db():
    print("Cargando menú oficial Coffee Beans...")
    db = SessionLocal()

    count = 0
    for item in MENU_ITEMS:
        if "description" not in item:
            item["description"] = None

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