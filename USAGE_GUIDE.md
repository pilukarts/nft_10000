# Guía Rápida de Uso / Quick Usage Guide

## 🇪🇸 Español

### Pasos para crear tu colección de NFTs:

#### 1. Preparar tus capas de arte
- Crea imágenes PNG con fondo transparente (recomendado 1000x1000 píxeles)
- Organiza tus archivos en carpetas por tipo de capa:
  - `layers/background/` - Fondos (pueden ser opacos)
  - `layers/body/` - Personaje o forma principal
  - `layers/clothes/` - Ropa o accesorios del cuerpo
  - `layers/eyes/` - Diferentes tipos de ojos
  - `layers/mouth/` - Expresiones de boca
  - `layers/accessories/` - Accesorios opcionales (sombreros, gafas, etc.)
  - `layers/special/` - Items raros o especiales

#### 2. Nombrar tus archivos
Usa este formato: `nombre_peso.png`

Ejemplos:
- `fondo_azul_100.png` - Común (aparece frecuentemente)
- `corona_dorada_5.png` - Muy raro (aparece raramente)

**Regla**: Números más altos = más común, números más bajos = más raro

#### 3. Calcular combinaciones posibles
Multiplica el número de variantes en cada capa:

Ejemplo: 
- 10 fondos × 8 cuerpos × 5 ropas × 4 ojos × 3 bocas × 3 accesorios = 14,400 combinaciones únicas

#### 4. Generar tu colección
```bash
# Instalar dependencias (solo la primera vez)
pip install -r requirements.txt

# Probar con pocos NFTs primero
python generate_nfts.py -n 100

# Generar colección completa
python generate_nfts.py -n 1000
```

#### 5. Verificar resultados
- Los NFTs se guardan en `output/images/`
- Los metadatos en `output/metadata/`
- Revisa algunos ejemplos para asegurarte que se vean bien

### Consejos importantes:
- **Siempre prueba con pocos NFTs primero** (10-100) antes de generar miles
- **Mantén el mismo tamaño** en todas las imágenes de capas
- **Usa transparencia (PNG)** en todas las capas excepto el fondo
- **Organiza bien tus archivos** desde el principio
- **Haz respaldos** de tus archivos originales

---

## 🇬🇧 English

### Steps to create your NFT collection:

#### 1. Prepare your art layers
- Create PNG images with transparent background (recommended 1000x1000 pixels)
- Organize your files in folders by layer type:
  - `layers/background/` - Backgrounds (can be opaque)
  - `layers/body/` - Main character or shape
  - `layers/clothes/` - Clothing or body accessories
  - `layers/eyes/` - Different eye types
  - `layers/mouth/` - Mouth expressions
  - `layers/accessories/` - Optional accessories (hats, glasses, etc.)
  - `layers/special/` - Rare or special items

#### 2. Name your files
Use this format: `name_weight.png`

Examples:
- `blue_background_100.png` - Common (appears frequently)
- `golden_crown_5.png` - Very rare (appears rarely)

**Rule**: Higher numbers = more common, lower numbers = more rare

#### 3. Calculate possible combinations
Multiply the number of variants in each layer:

Example:
- 10 backgrounds × 8 bodies × 5 clothes × 4 eyes × 3 mouths × 3 accessories = 14,400 unique combinations

#### 4. Generate your collection
```bash
# Install dependencies (first time only)
pip install -r requirements.txt

# Test with few NFTs first
python generate_nfts.py -n 100

# Generate full collection
python generate_nfts.py -n 1000
```

#### 5. Verify results
- NFTs are saved in `output/images/`
- Metadata in `output/metadata/`
- Check some examples to make sure they look good

### Important tips:
- **Always test with few NFTs first** (10-100) before generating thousands
- **Keep the same size** for all layer images
- **Use transparency (PNG)** in all layers except background
- **Organize your files well** from the start
- **Backup** your original files

---

## 🎯 Common Issues / Problemas Comunes

### Issue: "No layers found"
**Solution**: Make sure you created the layer folders and added PNG images to them.

**Solución**: Asegúrate de haber creado las carpetas de capas y agregado imágenes PNG.

### Issue: "Not enough unique combinations"
**Solution**: Add more variants to your layers or reduce the number of NFTs.

**Solución**: Agrega más variantes a tus capas o reduce el número de NFTs.

### Issue: Images overlapping incorrectly
**Solution**: Check the `layer_order` in `config.json`. First layer = bottom, last = top.

**Solución**: Verifica el `layer_order` en `config.json`. Primera capa = abajo, última = arriba.

---

## 📊 Rarity Examples / Ejemplos de Rareza

### Distribution suggestion / Sugerencia de distribución:

- **Common items (70%)**: Weight 80-100
- **Uncommon items (20%)**: Weight 40-60
- **Rare items (8%)**: Weight 15-25
- **Epic items (2%)**: Weight 5-10
- **Legendary items (0.1%)**: Weight 1-3

Example for backgrounds / Ejemplo para fondos:
- `blue_bg_100.png` (very common)
- `red_bg_100.png` (very common)
- `gradient_bg_50.png` (uncommon)
- `galaxy_bg_20.png` (rare)
- `animated_stars_bg_5.png` (epic)
- `golden_aura_bg_1.png` (legendary)

---

**¡Éxito con tu proyecto! / Good luck with your project! 🚀**
