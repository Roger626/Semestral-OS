# 🔌 Ejemplos de Integración Frontend - Backend

Este archivo contiene ejemplos prácticos de cómo conectar tu frontend con el backend.

---

## 🌐 Configuración base

### JavaScript/React/Vue/Angular

```javascript
// config.js - Configuración centralizada
const API_CONFIG = {
  // Para desarrollo local
  LOCAL: 'http://localhost:5000',
  
  // Para acceso remoto (reemplaza con la IP de tu servidor)
  REMOTE: 'http://192.168.1.100:5000',
  
  // Determinar automáticamente
  get BASE_URL() {
    return window.location.hostname === 'localhost' 
      ? this.LOCAL 
      : this.REMOTE;
  }
};

export default API_CONFIG;
```

---

## 📋 Ejemplos por operación

### 1. Obtener todos los platos

#### Vanilla JavaScript
```javascript
async function getAllDishes() {
  try {
    const response = await fetch('http://192.168.1.100:5000/menu');
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    
    if (data.code === 200) {
      console.log('Platos:', data.data);
      return data.data;
    } else {
      console.error('Error:', data.message);
      return [];
    }
  } catch (error) {
    console.error('Error al obtener platos:', error);
    return [];
  }
}

// Uso
getAllDishes().then(dishes => {
  dishes.forEach(dish => {
    console.log(`${dish.nombre} - $${dish.precio}`);
  });
});
```

#### React con Hooks
```jsx
import { useState, useEffect } from 'react';

function MenuList() {
  const [dishes, setDishes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchDishes() {
      try {
        const response = await fetch('http://192.168.1.100:5000/menu');
        const data = await response.json();
        
        if (data.code === 200) {
          setDishes(data.data);
        } else {
          setError(data.message);
        }
      } catch (err) {
        setError('Error al cargar el menú');
      } finally {
        setLoading(false);
      }
    }

    fetchDishes();
  }, []);

  if (loading) return <div>Cargando...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>Menú</h1>
      <ul>
        {dishes.map(dish => (
          <li key={dish.id}>
            <img src={dish.imagen_url} alt={dish.nombre} />
            <h3>{dish.nombre}</h3>
            <p>${dish.precio}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
```

#### Vue 3
```vue
<template>
  <div>
    <h1>Menú</h1>
    <div v-if="loading">Cargando...</div>
    <div v-else-if="error">Error: {{ error }}</div>
    <ul v-else>
      <li v-for="dish in dishes" :key="dish.id">
        <img :src="dish.imagen_url" :alt="dish.nombre" />
        <h3>{{ dish.nombre }}</h3>
        <p>${{ dish.precio }}</p>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const dishes = ref([]);
const loading = ref(true);
const error = ref(null);

const fetchDishes = async () => {
  try {
    const response = await fetch('http://192.168.1.100:5000/menu');
    const data = await response.json();
    
    if (data.code === 200) {
      dishes.value = data.data;
    } else {
      error.value = data.message;
    }
  } catch (err) {
    error.value = 'Error al cargar el menú';
  } finally {
    loading.value = false;
  }
};

onMounted(fetchDishes);
</script>
```

---

### 2. Crear un plato con JSON

#### Vanilla JavaScript
```javascript
async function createDish(dishData) {
  try {
    const response = await fetch('http://192.168.1.100:5000/menu', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dishData)
    });
    
    const data = await response.json();
    
    if (data.code === 201) {
      console.log('Plato creado exitosamente');
      return true;
    } else {
      console.error('Error:', data.message);
      return false;
    }
  } catch (error) {
    console.error('Error al crear plato:', error);
    return false;
  }
}

// Uso
const newDish = {
  nombre: 'Pizza Margherita',
  precio: 12.99,
  imagen_url: 'https://example.com/pizza.jpg'
};

createDish(newDish);
```

#### React
```jsx
function CreateDishForm() {
  const [formData, setFormData] = useState({
    nombre: '',
    precio: '',
    imagen_url: ''
  });
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      const response = await fetch('http://192.168.1.100:5000/menu', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
      });
      
      const data = await response.json();
      
      if (data.code === 201) {
        setMessage('Plato creado exitosamente');
        setFormData({ nombre: '', precio: '', imagen_url: '' });
      } else {
        setMessage(`Error: ${data.message}`);
      }
    } catch (error) {
      setMessage('Error al crear plato');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Nombre"
        value={formData.nombre}
        onChange={(e) => setFormData({...formData, nombre: e.target.value})}
        required
      />
      <input
        type="number"
        step="0.01"
        placeholder="Precio"
        value={formData.precio}
        onChange={(e) => setFormData({...formData, precio: e.target.value})}
        required
      />
      <input
        type="url"
        placeholder="URL de imagen"
        value={formData.imagen_url}
        onChange={(e) => setFormData({...formData, imagen_url: e.target.value})}
        required
      />
      <button type="submit">Crear Plato</button>
      {message && <p>{message}</p>}
    </form>
  );
}
```

---

### 3. Crear un plato con archivo de imagen

#### Vanilla JavaScript
```javascript
async function createDishWithFile(nombre, precio, imageFile) {
  try {
    const formData = new FormData();
    formData.append('nombre', nombre);
    formData.append('precio', precio);
    formData.append('imagen', imageFile);
    
    const response = await fetch('http://192.168.1.100:5000/menu', {
      method: 'POST',
      body: formData  // NO incluir Content-Type, el navegador lo configura automáticamente
    });
    
    const data = await response.json();
    
    if (data.code === 201) {
      console.log('Plato creado exitosamente');
      return true;
    } else {
      console.error('Error:', data.message);
      return false;
    }
  } catch (error) {
    console.error('Error al crear plato:', error);
    return false;
  }
}

// Uso con input file
document.getElementById('dishForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const nombre = document.getElementById('nombre').value;
  const precio = document.getElementById('precio').value;
  const imageFile = document.getElementById('imagen').files[0];
  
  await createDishWithFile(nombre, precio, imageFile);
});
```

#### React
```jsx
function CreateDishWithImageForm() {
  const [nombre, setNombre] = useState('');
  const [precio, setPrecio] = useState('');
  const [imageFile, setImageFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [message, setMessage] = useState('');
  const [uploading, setUploading] = useState(false);

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setImageFile(file);
      setPreview(URL.createObjectURL(file));
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setUploading(true);
    
    try {
      const formData = new FormData();
      formData.append('nombre', nombre);
      formData.append('precio', precio);
      formData.append('imagen', imageFile);
      
      const response = await fetch('http://192.168.1.100:5000/menu', {
        method: 'POST',
        body: formData
      });
      
      const data = await response.json();
      
      if (data.code === 201) {
        setMessage('Plato creado exitosamente');
        setNombre('');
        setPrecio('');
        setImageFile(null);
        setPreview(null);
      } else {
        setMessage(`Error: ${data.message}`);
      }
    } catch (error) {
      setMessage('Error al crear plato');
    } finally {
      setUploading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Nombre del plato"
        value={nombre}
        onChange={(e) => setNombre(e.target.value)}
        required
      />
      <input
        type="number"
        step="0.01"
        placeholder="Precio"
        value={precio}
        onChange={(e) => setPrecio(e.target.value)}
        required
      />
      <input
        type="file"
        accept="image/*"
        onChange={handleImageChange}
        required
      />
      {preview && <img src={preview} alt="Preview" style={{maxWidth: '200px'}} />}
      <button type="submit" disabled={uploading}>
        {uploading ? 'Subiendo...' : 'Crear Plato'}
      </button>
      {message && <p>{message}</p>}
    </form>
  );
}
```

---

### 4. Actualizar un plato

```javascript
async function updateDish(dishId, dishData) {
  try {
    const response = await fetch(`http://192.168.1.100:5000/menu/${dishId}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dishData)
    });
    
    const data = await response.json();
    
    if (data.code === 200) {
      console.log('Plato actualizado exitosamente');
      return true;
    } else {
      console.error('Error:', data.message);
      return false;
    }
  } catch (error) {
    console.error('Error al actualizar plato:', error);
    return false;
  }
}

// Uso
const updatedDish = {
  nombre: 'Pizza Margherita Premium',
  precio: 15.99,
  imagen_url: 'https://example.com/pizza-premium.jpg'
};

updateDish(1, updatedDish);
```

---

### 5. Eliminar un plato

```javascript
async function deleteDish(dishId) {
  try {
    // Confirmar antes de eliminar
    if (!confirm('¿Estás seguro de eliminar este plato?')) {
      return false;
    }
    
    const response = await fetch(`http://192.168.1.100:5000/menu/${dishId}`, {
      method: 'DELETE'
    });
    
    const data = await response.json();
    
    if (data.code === 200) {
      console.log('Plato eliminado exitosamente');
      return true;
    } else {
      console.error('Error:', data.message);
      return false;
    }
  } catch (error) {
    console.error('Error al eliminar plato:', error);
    return false;
  }
}

// Uso
deleteDish(1);
```

---

## 🔧 Servicio completo reutilizable

### JavaScript/TypeScript

```javascript
// menuService.js
class MenuService {
  constructor(baseURL = 'http://192.168.1.100:5000') {
    this.baseURL = baseURL;
  }

  async getAllDishes() {
    try {
      const response = await fetch(`${this.baseURL}/menu`);
      const data = await response.json();
      return data.code === 200 ? data.data : [];
    } catch (error) {
      console.error('Error al obtener platos:', error);
      throw error;
    }
  }

  async getDishById(id) {
    try {
      const response = await fetch(`${this.baseURL}/menu/${id}`);
      const data = await response.json();
      return data.code === 200 ? data.data : null;
    } catch (error) {
      console.error('Error al obtener plato:', error);
      throw error;
    }
  }

  async createDish(dishData) {
    try {
      const response = await fetch(`${this.baseURL}/menu`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(dishData)
      });
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error al crear plato:', error);
      throw error;
    }
  }

  async createDishWithImage(nombre, precio, imageFile) {
    try {
      const formData = new FormData();
      formData.append('nombre', nombre);
      formData.append('precio', precio);
      formData.append('imagen', imageFile);
      
      const response = await fetch(`${this.baseURL}/menu`, {
        method: 'POST',
        body: formData
      });
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error al crear plato con imagen:', error);
      throw error;
    }
  }

  async updateDish(id, dishData) {
    try {
      const response = await fetch(`${this.baseURL}/menu/${id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(dishData)
      });
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error al actualizar plato:', error);
      throw error;
    }
  }

  async updateDishWithImage(id, nombre, precio, imageFile) {
    try {
      const formData = new FormData();
      formData.append('nombre', nombre);
      formData.append('precio', precio);
      if (imageFile) {
        formData.append('imagen', imageFile);
      }
      
      const response = await fetch(`${this.baseURL}/menu/${id}`, {
        method: 'PUT',
        body: formData
      });
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error al actualizar plato con imagen:', error);
      throw error;
    }
  }

  async deleteDish(id) {
    try {
      const response = await fetch(`${this.baseURL}/menu/${id}`, {
        method: 'DELETE'
      });
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error al eliminar plato:', error);
      throw error;
    }
  }

  async healthCheck() {
    try {
      const response = await fetch(`${this.baseURL}/health`);
      const data = await response.json();
      return data.status === 'online';
    } catch (error) {
      console.error('Error en health check:', error);
      return false;
    }
  }
}

// Exportar instancia
export default new MenuService('http://192.168.1.100:5000');

// Uso
// import menuService from './menuService.js';
// const dishes = await menuService.getAllDishes();
```

---

## ⚠️ Manejo de errores robusto

```javascript
async function fetchWithErrorHandling(url, options = {}) {
  try {
    const response = await fetch(url, options);
    const data = await response.json();
    
    // Verificar código de respuesta del backend
    if (data.code >= 200 && data.code < 300) {
      return { success: true, data: data.data || data };
    } else {
      return { 
        success: false, 
        error: data.message || 'Error desconocido',
        code: data.code 
      };
    }
  } catch (error) {
    // Error de red o JSON inválido
    if (error.name === 'TypeError' && error.message.includes('fetch')) {
      return { 
        success: false, 
        error: 'No se pudo conectar con el servidor. Verifica que esté corriendo.',
        code: 0
      };
    }
    
    return { 
      success: false, 
      error: error.message || 'Error inesperado',
      code: 0
    };
  }
}

// Uso
const result = await fetchWithErrorHandling('http://192.168.1.100:5000/menu');

if (result.success) {
  console.log('Datos:', result.data);
} else {
  console.error('Error:', result.error);
  
  // Mostrar mensaje al usuario
  alert(`Error: ${result.error}`);
}
```

---

## 🎨 Componente completo de ejemplo (React)

```jsx
import { useState, useEffect } from 'react';
import menuService from './menuService';

function MenuManager() {
  const [dishes, setDishes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [editingId, setEditingId] = useState(null);

  // Cargar platos al montar componente
  useEffect(() => {
    loadDishes();
  }, []);

  const loadDishes = async () => {
    try {
      setLoading(true);
      const data = await menuService.getAllDishes();
      setDishes(data);
      setError(null);
    } catch (err) {
      setError('Error al cargar el menú');
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id) => {
    if (!window.confirm('¿Eliminar este plato?')) return;
    
    try {
      const result = await menuService.deleteDish(id);
      if (result.code === 200) {
        await loadDishes();
      } else {
        alert(`Error: ${result.message}`);
      }
    } catch (err) {
      alert('Error al eliminar plato');
    }
  };

  if (loading) return <div>Cargando...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>Gestión de Menú</h1>
      
      {/* Formulario de creación/edición */}
      <DishForm 
        onSubmit={loadDishes} 
        editingId={editingId}
        onCancel={() => setEditingId(null)}
      />
      
      {/* Lista de platos */}
      <div className="dishes-grid">
        {dishes.map(dish => (
          <div key={dish.id} className="dish-card">
            <img src={dish.imagen_url} alt={dish.nombre} />
            <h3>{dish.nombre}</h3>
            <p className="price">${dish.precio}</p>
            <div className="actions">
              <button onClick={() => setEditingId(dish.id)}>Editar</button>
              <button onClick={() => handleDelete(dish.id)}>Eliminar</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default MenuManager;
```

---

## 📱 Ejemplo con Python (para scripts o backend adicional)

```python
import requests

BASE_URL = "http://192.168.1.100:5000"

class MenuClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url
    
    def get_all_dishes(self):
        response = requests.get(f"{self.base_url}/menu")
        data = response.json()
        return data['data'] if data['code'] == 200 else []
    
    def create_dish(self, nombre, precio, imagen_url):
        dish_data = {
            "nombre": nombre,
            "precio": precio,
            "imagen_url": imagen_url
        }
        response = requests.post(f"{self.base_url}/menu", json=dish_data)
        return response.json()
    
    def create_dish_with_file(self, nombre, precio, image_path):
        with open(image_path, 'rb') as f:
            files = {'imagen': f}
            data = {
                'nombre': nombre,
                'precio': precio
            }
            response = requests.post(
                f"{self.base_url}/menu",
                files=files,
                data=data
            )
            return response.json()
    
    def update_dish(self, dish_id, nombre, precio, imagen_url):
        dish_data = {
            "nombre": nombre,
            "precio": precio,
            "imagen_url": imagen_url
        }
        response = requests.put(
            f"{self.base_url}/menu/{dish_id}",
            json=dish_data
        )
        return response.json()
    
    def delete_dish(self, dish_id):
        response = requests.delete(f"{self.base_url}/menu/{dish_id}")
        return response.json()

# Uso
client = MenuClient()
dishes = client.get_all_dishes()
for dish in dishes:
    print(f"{dish['nombre']}: ${dish['precio']}")
```

---

¡Estos ejemplos te ayudarán a integrar tu frontend con el backend! 🚀
