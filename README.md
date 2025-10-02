# NFT Collection Generator 🎨

**Generador de Colecciones NFT - Crea más de 1000 NFTs únicos automáticamente**

A powerful Python tool to generate thousands of unique NFTs by combining different layers (backgrounds, characters, accessories, etc.). Each NFT is guaranteed to be unique with its own metadata.

---

## 🌟 Features / Características

- ✅ Generate 1000+ unique NFTs automatically / Genera más de 1000 NFTs únicos automáticamente
- ✅ Layer-based system (backgrounds, body, clothes, eyes, etc.) / Sistema de capas (fondos, cuerpo, ropa, ojos, etc.)
- ✅ Rarity weights for traits / Pesos de rareza para características
- ✅ Automatic duplicate detection / Detección automática de duplicados
- ✅ JSON metadata generation for each NFT / Generación de metadatos JSON para cada NFT
- ✅ Configurable through JSON file / Configurable mediante archivo JSON
- ✅ PNG output with transparency support / Salida PNG con soporte de transparencia

---

## 📋 Requirements / Requisitos

- Python 3.7 or higher / Python 3.7 o superior
- Pillow (PIL) library / Biblioteca Pillow (PIL)

---

## 🚀 Quick Start / Inicio Rápido

### 1. Install Dependencies / Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 2. Create Example Layers / Crear Capas de Ejemplo

```bash
python create_example_layers.py
```

This will create example layer images in the `layers/` directory to help you get started.

Esto creará imágenes de capas de ejemplo en el directorio `layers/` para ayudarte a comenzar.

### 3. Generate NFT Collection / Generar Colección NFT

```bash
# Generate 100 NFTs (for testing)
python generate_nfts.py -n 100

# Generate 1000 NFTs
python generate_nfts.py -n 1000

# Generate 10000 NFTs
python generate_nfts.py -n 10000
```

Generated NFTs will be saved in:
- `output/images/` - PNG images
- `output/metadata/` - JSON metadata files

Los NFTs generados se guardarán en:
- `output/images/` - Imágenes PNG
- `output/metadata/` - Archivos de metadatos JSON

---

## 📁 Project Structure / Estructura del Proyecto

```
nft_10000/
├── generate_nfts.py           # Main generator script / Script principal
├── create_example_layers.py   # Create example layers / Crear capas de ejemplo
├── config.json                # Configuration file / Archivo de configuración
├── requirements.txt           # Python dependencies / Dependencias Python
├── layers/                    # Layer images directory / Directorio de capas
│   ├── background/           # Background layer / Capa de fondo
│   ├── body/                 # Body/character layer / Capa de cuerpo/personaje
│   ├── clothes/              # Clothes layer / Capa de ropa
│   ├── eyes/                 # Eyes layer / Capa de ojos
│   ├── mouth/                # Mouth layer / Capa de boca
│   ├── accessories/          # Accessories layer / Capa de accesorios
│   └── special/              # Special/rare items / Items especiales/raros
└── output/                    # Generated NFTs / NFTs generados
    ├── images/               # PNG images / Imágenes PNG
    ├── metadata/             # JSON metadata / Metadatos JSON
    └── collection.json       # Collection info / Info de colección
```

---

## 🎨 How to Add Your Own Layers / Cómo Agregar Tus Propias Capas

### English Instructions:

1. **Prepare your artwork**: Create PNG images with transparency (1000x1000px recommended)

2. **Organize by layers**: Place images in the appropriate layer folders:
   - `layers/background/` - Backgrounds (should be opaque)
   - `layers/body/` - Main character/body
   - `layers/clothes/` - Clothing items
   - `layers/eyes/` - Eye variations
   - `layers/mouth/` - Mouth expressions
   - `layers/accessories/` - Hats, glasses, etc.
   - `layers/special/` - Rare items (crowns, effects, etc.)

3. **Name your files with rarity**: 
   - Format: `name_rarity.png`
   - Example: `red_background_100.png` (common, weight 100)
   - Example: `golden_crown_5.png` (rare, weight 5)
   - Higher numbers = more common, lower numbers = more rare

4. **Run the generator**: `python generate_nfts.py -n 1000`

### Instrucciones en Español:

1. **Prepara tu arte**: Crea imágenes PNG con transparencia (1000x1000px recomendado)

2. **Organiza por capas**: Coloca las imágenes en las carpetas de capas apropiadas:
   - `layers/background/` - Fondos (deben ser opacos)
   - `layers/body/` - Personaje/cuerpo principal
   - `layers/clothes/` - Prendas de vestir
   - `layers/eyes/` - Variaciones de ojos
   - `layers/mouth/` - Expresiones de boca
   - `layers/accessories/` - Sombreros, gafas, etc.
   - `layers/special/` - Items raros (coronas, efectos, etc.)

3. **Nombra tus archivos con rareza**: 
   - Formato: `nombre_rareza.png`
   - Ejemplo: `fondo_rojo_100.png` (común, peso 100)
   - Ejemplo: `corona_dorada_5.png` (raro, peso 5)
   - Números más altos = más común, números más bajos = más raro

4. **Ejecuta el generador**: `python generate_nfts.py -n 1000`

---

## ⚙️ Configuration / Configuración

Edit `config.json` to customize your collection:

Edita `config.json` para personalizar tu colección:

```json
{
  "collection_name": "My NFT Collection",
  "collection_description": "Description of your collection",
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

**Important**: The `layer_order` determines how layers are stacked (first = bottom, last = top).

**Importante**: El `layer_order` determina cómo se apilan las capas (primero = abajo, último = arriba).

---

## 💡 Tips for Creating 10,000+ Unique NFTs / Consejos para Crear 10,000+ NFTs Únicos

### English:
- **Calculate combinations**: If you have 10 backgrounds × 10 bodies × 10 clothes × 5 eyes × 5 mouths × 5 accessories = 12,500 possible combinations
- **Use rarity wisely**: Make rare items really rare (weight 5-10) and common items common (weight 80-100)
- **Add variety**: More layers and variants = more unique combinations
- **Test first**: Generate 100 NFTs first to verify everything looks good
- **Name consistently**: Use descriptive names like `blue_background_100.png` not just `1.png`

### Español:
- **Calcula las combinaciones**: Si tienes 10 fondos × 10 cuerpos × 10 ropas × 5 ojos × 5 bocas × 5 accesorios = 12,500 combinaciones posibles
- **Usa la rareza sabiamente**: Haz que los items raros sean realmente raros (peso 5-10) y los comunes sean comunes (peso 80-100)
- **Agrega variedad**: Más capas y variantes = más combinaciones únicas
- **Prueba primero**: Genera 100 NFTs primero para verificar que todo se vea bien
- **Nombra consistentemente**: Usa nombres descriptivos como `fondo_azul_100.png` no solo `1.png`

---

## 📊 Understanding Metadata / Entendiendo los Metadatos

Each NFT generates a JSON metadata file compatible with OpenSea and other marketplaces:

Cada NFT genera un archivo de metadatos JSON compatible con OpenSea y otros mercados:

```json
{
  "name": "My NFT Collection #1",
  "description": "Unique NFT from collection",
  "image": "1.png",
  "tokenId": 1,
  "attributes": [
    {
      "trait_type": "Background",
      "value": "Blue"
    },
    {
      "trait_type": "Body",
      "value": "Circle Red"
    }
  ]
}
```

---

## 🔧 Advanced Usage / Uso Avanzado

### Custom Configuration File / Archivo de Configuración Personalizado

```bash
python generate_nfts.py -n 5000 -c my_custom_config.json
```

### Command Line Options / Opciones de Línea de Comandos

```bash
python generate_nfts.py --help

Options:
  -n, --number NUM    Number of NFTs to generate (default: 1000)
  -c, --config PATH   Path to configuration file (default: config.json)
```

---

## 🐛 Troubleshooting / Solución de Problemas

### "No layers found" Error
**English**: Make sure you have created layer directories and added PNG images to them.

**Español**: Asegúrate de haber creado los directorios de capas y agregado imágenes PNG a ellos.

### "Not enough unique combinations"
**English**: You need more layer variants. Add more images to your layer folders or reduce the number of NFTs to generate.

**Español**: Necesitas más variantes de capas. Agrega más imágenes a tus carpetas de capas o reduce el número de NFTs a generar.

### Images don't look right
**English**: Check the `layer_order` in config.json. Backgrounds should be first, overlays should be last.

**Español**: Verifica el `layer_order` en config.json. Los fondos deben estar primero, las superposiciones deben estar al final.

---

## 📝 License / Licencia

This project is provided as-is for creating NFT collections. Feel free to use and modify for your projects.

Este proyecto se proporciona tal cual para crear colecciones NFT. Siéntete libre de usar y modificar para tus proyectos.

---

## 🤝 Contributing / Contribuir

Contributions are welcome! Feel free to submit issues or pull requests.

¡Las contribuciones son bienvenidas! Siéntete libre de enviar issues o pull requests.

---

## 📧 Support / Soporte

If you have questions or need help, please open an issue on GitHub.

Si tienes preguntas o necesitas ayuda, por favor abre un issue en GitHub.

---

**¡Buena suerte creando tu colección NFT! / Good luck creating your NFT collection! 🚀**
