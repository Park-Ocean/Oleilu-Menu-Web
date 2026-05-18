// API Configuration
export const API_BASE_URL = 'http://localhost:8000';

// Authentication
export const ADMIN_PASSWORD = 'ola2024';
export const LOGO_CLICKS_TO_LOGIN = 3;

// Categories
export const CATEGORIES = {
  ALL: "Todos",
  BRUNCH: "Brunch",
  ALMUERZO: "Almuerzo",
  DESAYUNO_BRUNCH: "Desayuno Brunch",
  ENSALADAS: "Ensaladas",
  SANDWICHES: "Sandwiches",
  PASTELERIA: "Pastelería",
  COOKIES: "Cookies",
  CAFETERIA: "Cafetería",
  CERVEZAS: "Cervezas",
  MOCKTAILS: "Mocktails",
  BEBIDAS: "Bebidas",
};

// Messages
export const MESSAGES = {
  LOGIN_SUCCESS: 'Acceso exitoso',
  LOGIN_ERROR: 'PIN Incorrecto',
  DELETE_CONFIRM: '¿Eliminar este producto?',
  DELETE_SUCCESS: 'Producto eliminado',
  SAVE_SUCCESS: 'Producto guardado',
  VALIDATION_ERROR: 'Por favor completa todos los campos',
};

// Timings (milliseconds)
export const TIMINGS = {
  NOTIFICATION_DURATION: 1000,
  DEBOUNCE_SEARCH: 300,
};
