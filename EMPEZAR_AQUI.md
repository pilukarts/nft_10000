# 🎨 Empieza Aquí - Guía Rápida en Español

## ¡Bienvenido a tu Generador de NFTs!

Este proyecto te ayuda a crear miles de NFTs únicos automáticamente, combinando diferentes capas de imágenes. Es perfecto para crear colecciones de 1,000, 5,000 o incluso 10,000+ NFTs sin cansarte.

---

## 🚀 Inicio Rápido (5 minutos)

### Paso 1: Instalar Python

Si no tienes Python instalado:
- **Windows**: Descarga de https://python.org
- **Mac**: Viene pre-instalado, o usa `brew install python3`
- **Linux**: `sudo apt install python3 python3-pip`

### Paso 2: Instalar Dependencias

Abre la terminal en esta carpeta y ejecuta:

```bash
pip install -r requirements.txt
```

### Paso 3: Probar el Sistema

Ejecuta el script de prueba para verificar que todo funciona:

```bash
python test_system.py
```

Deberías ver: `🎉 All tests passed! System is ready to use.`

### Paso 4: Crear Capas de Ejemplo

```bash
python create_example_layers.py
```

Esto crea imágenes de ejemplo en la carpeta `layers/` para que entiendas cómo funciona.

### Paso 5: Generar Tus Primeros NFTs

```bash
# Empieza con solo 10 para probar
python generate_nfts.py -n 10
```

Los NFTs se guardarán en `output/images/` y los metadatos en `output/metadata/`

---

## 📁 Estructura del Proyecto

```
nft_10000/
├── layers/                     ← Aquí pones tus imágenes
│   ├── background/            ← Fondos
│   ├── body/                  ← Cuerpos/personajes
│   ├── clothes/               ← Ropa
│   ├── eyes/                  ← Ojos
│   ├── mouth/                 ← Bocas
│   ├── accessories/           ← Accesorios (sombreros, gafas)
│   └── special/               ← Items especiales/raros
├── output/                     ← Los NFTs generados
│   ├── images/                ← Imágenes PNG
│   └── metadata/              ← Archivos JSON
├── generate_nfts.py           ← Script principal
├── config.json                ← Configuración
└── README.md                  ← Documentación completa
```

---

## 🎯 ¿Cómo Funciona?

El generador funciona como un "armador de personajes":

1. Toma una imagen de fondo
2. Le pone encima un cuerpo
3. Le añade ropa
4. Le pone ojos
5. Le añade una boca
6. Le pone accesorios opcionales
7. Le añade efectos especiales raros

**Resultado**: ¡Un NFT único!

### Ejemplo de Capas

Imagina que tienes:
- 8 fondos diferentes
- 5 tipos de cuerpo
- 4 opciones de ropa
- 3 estilos de ojos
- 2 tipos de boca
- 3 accesorios
- 3 items especiales

**Total**: 8 × 5 × 4 × 3 × 2 × 3 × 3 = **8,640 NFTs únicos posibles**

---

## 🎨 Crear Tus Propias Imágenes

### Requisitos

- **Formato**: PNG con fondo transparente
- **Tamaño**: Todos deben ser del mismo tamaño (recomendado 1000×1000px o 2000×2000px)
- **Software**: Puedes usar:
  - Photoshop
  - GIMP (gratis)
  - Procreate (iPad)
  - Illustrator
  - Inkscape (gratis)
  - Aseprite (para pixel art)

### Proceso

1. **Diseña tus variantes**
   - Haz varias versiones de cada tipo (diferentes fondos, diferentes cuerpos, etc.)
   
2. **Guarda como PNG**
   - Con fondo transparente (excepto los fondos)
   - Mismo tamaño todas las imágenes
   
3. **Nombra los archivos correctamente**
   - Formato: `nombre_rareza.png`
   - Ejemplo: `fondo_azul_100.png` (común)
   - Ejemplo: `corona_dorada_5.png` (muy raro)

4. **Organiza en carpetas**
   ```
   layers/
   ├── background/
   │   ├── cielo_100.png
   │   ├── espacio_100.png
   │   └── arcoiris_20.png
   ├── body/
   │   ├── robot_rojo_80.png
   │   └── robot_dorado_10.png
   ```

---

## 🔢 Sistema de Rareza

Los números en los nombres de archivo controlan qué tan frecuente aparece cada item:

### Distribución Sugerida

| Tipo | Rareza | Peso | Frecuencia Aproximada |
|------|--------|------|----------------------|
| Común | 80-100 | Alto | 70% de NFTs |
| Poco Común | 50-70 | Medio | 20% de NFTs |
| Raro | 20-40 | Bajo | 8% de NFTs |
| Épico | 5-15 | Muy Bajo | 2% de NFTs |
| Legendario | 1-3 | Mínimo | 0.1% de NFTs |

### Ejemplos

```
# Fondos comunes (aparecen mucho)
background/azul_100.png
background/rojo_100.png

# Accesorios poco comunes
accessories/gafas_50.png
accessories/sombrero_40.png

# Items raros
special/corona_10.png

# Items legendarios (muy raros)
special/aura_dorada_1.png
```

---

## 📊 Comandos Útiles

### Generar NFTs

```bash
# Prueba con pocos primero
python generate_nfts.py -n 10

# Generar 100
python generate_nfts.py -n 100

# Generar 1000
python generate_nfts.py -n 1000

# Generar cantidad personalizada
python generate_nfts.py -n 5000
```

### Analizar Colección

```bash
# Ver estadísticas de rareza
python analyze_collection.py
```

Esto te muestra:
- Cuántas veces aparece cada característica
- Cuáles son los NFTs más raros
- Distribución de rarezas

### Usar el Script Rápido

```bash
# Menú interactivo
bash quickstart.sh
```

---

## 🎯 Planificar Tu Colección

### Para 1,000 NFTs

Necesitas al menos 1,000 combinaciones únicas. Ejemplo:

```
10 fondos × 8 cuerpos × 5 ropas × 5 accesorios = 2,000 combinaciones ✓
```

### Para 10,000 NFTs

Necesitas al menos 10,000 combinaciones. Ejemplo:

```
12 fondos × 10 cuerpos × 8 ropas × 6 ojos × 4 bocas × 5 accesorios × 3 especiales
= 172,800 combinaciones ✓
```

### Calculadora Rápida

El número total de combinaciones es:
```
(fondos) × (cuerpos) × (ropas) × (ojos) × (bocas) × (accesorios) × (especiales)
```

**Tip**: Usa el script de prueba para calcular automáticamente:
```bash
python test_system.py
```

---

## ⚙️ Configuración Avanzada

### Editar config.json

```json
{
  "collection_name": "Mi Colección NFT",
  "collection_description": "Descripción de tu colección",
  "output_dir": "output",
  "layers_dir": "layers",
  "image_size": [1000, 1000],
  "layer_order": [
    "background",
    "body",
    "clothes",
    "eyes",
    "mouth",
    "accessories",
    "special"
  ]
}
```

### Cambiar el Orden de Capas

El orden importa! Las primeras capas van abajo, las últimas arriba.

**Correcto** para personajes:
1. background (fondo, abajo)
2. body (cuerpo)
3. clothes (ropa encima del cuerpo)
4. accessories (accesorios encima de todo)

### Cambiar Tamaño de Imagen

Para NFTs de mayor calidad:
```json
"image_size": [2000, 2000]
```

Asegúrate que todas tus capas tengan este tamaño!

---

## 🐛 Solución de Problemas

### "No layers found"
**Problema**: No hay carpetas de capas o están vacías.
**Solución**: Crea las carpetas y añade archivos PNG.

### "Not enough unique combinations"
**Problema**: Pides más NFTs de los que puedes generar.
**Solución**: Añade más variantes a tus capas o genera menos NFTs.

### Las imágenes se ven mal
**Problema**: El orden de capas no es correcto.
**Solución**: Verifica `layer_order` en `config.json`. Los fondos deben estar primero.

### Los archivos son muy grandes
**Problema**: Las imágenes PNG son muy pesadas.
**Solución**: 
- Reduce el tamaño de imagen en config.json
- Optimiza las imágenes con herramientas como TinyPNG
- Usa menos colores en las imágenes originales

---

## 💰 Publicar Tu Colección

Una vez generados tus NFTs:

### 1. Revisa la Calidad
Mira varios ejemplos para asegurarte que se ven bien:
```bash
python analyze_collection.py
```

### 2. Sube a IPFS (Recomendado)
- Usa Pinata, NFT.Storage, o similar
- Sube las imágenes y metadatos
- Obtendrás URLs permanentes

### 3. Publica en un Marketplace
- OpenSea
- Rarible
- Foundation
- Otros marketplaces NFT

### 4. Actualiza los Metadatos
Edita los archivos JSON en `output/metadata/` para añadir:
- URL de la imagen en IPFS
- URL de tu sitio web
- Información de regalías

---

## 📚 Recursos Adicionales

### Documentación
- `README.md` - Guía completa en inglés y español
- `USAGE_GUIDE.md` - Guía de uso detallada
- `EXAMPLES.md` - Ejemplos y casos de uso

### Scripts Útiles
- `generate_nfts.py` - Generador principal
- `analyze_collection.py` - Analizar estadísticas
- `test_system.py` - Verificar que todo funciona
- `create_example_layers.py` - Crear capas de ejemplo
- `quickstart.sh` - Menú interactivo

---

## 🎓 Consejos de Experto

1. **Empieza pequeño**: Prueba con 10-100 NFTs antes de generar miles
2. **Calidad sobre cantidad**: Mejor 1,000 NFTs excelentes que 10,000 mediocres
3. **Sé consistente**: Mantén el mismo estilo en todas las capas
4. **Piensa en rareza**: Los items raros hacen tu colección más interesante
5. **Prueba diferentes combinaciones**: Genera varias veces para ver variedad
6. **Documenta tu proceso**: Guarda los archivos originales y versiones

---

## 🤝 Comunidad y Ayuda

Si tienes preguntas o problemas:
1. Revisa la documentación completa en README.md
2. Ejecuta `python test_system.py` para diagnosticar problemas
3. Abre un issue en GitHub
4. Comparte tus creaciones!

---

## ✅ Lista de Verificación

Antes de generar tu colección final:

- [ ] Todas las imágenes son del mismo tamaño
- [ ] Todas las capas tienen formato PNG
- [ ] Los nombres de archivo incluyen pesos de rareza
- [ ] Probaste con una muestra pequeña (10-100 NFTs)
- [ ] Revisaste que las combinaciones se ven bien
- [ ] Calculaste que tienes suficientes combinaciones
- [ ] Configuraste `config.json` correctamente
- [ ] Hiciste respaldo de tus archivos originales

---

## 🎉 ¡Éxito!

¡Felicitaciones por crear tu generador de NFTs! Ahora puedes:
- Generar miles de NFTs únicos en minutos
- Controlar la rareza de cada característica
- Analizar estadísticas de tu colección
- Crear una colección profesional

**Recuerda**: La creatividad y el diseño son lo más importante. Esta herramienta solo te ayuda a automatizar el proceso técnico.

---

**¡Mucha suerte con tu proyecto NFT! 🚀**

Si este generador te ayudó, considera compartirlo con otros creadores.
