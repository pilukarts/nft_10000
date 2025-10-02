# Examples and Combinations / Ejemplos y Combinaciones

## 🎯 Understanding the System / Entendiendo el Sistema

This NFT generator uses a **layered approach** where each NFT is created by stacking multiple image layers on top of each other, similar to how you might create a character in a video game.

Este generador de NFT usa un **enfoque por capas** donde cada NFT se crea apilando múltiples capas de imágenes una encima de otra, similar a cómo podrías crear un personaje en un videojuego.

---

## 📊 Current Example Collection Statistics

With the included example layers, you can generate:

Con las capas de ejemplo incluidas, puedes generar:

- **8** Background variations / variaciones de fondo
- **5** Body variations / variaciones de cuerpo  
- **4** Clothes variations / variaciones de ropa
- **3** Eyes variations / variaciones de ojos
- **2** Mouth variations / variaciones de boca
- **3** Accessory variations / variaciones de accesorios
- **3** Special items / items especiales

**Total unique combinations:** 8 × 5 × 4 × 3 × 2 × 3 × 3 = **8,640 unique NFTs**

---

## 🎨 How Layers Work / Cómo Funcionan las Capas

### Layer Order (bottom to top) / Orden de Capas (de abajo hacia arriba):

1. **Background** - The base layer, usually opaque / La capa base, usualmente opaca
2. **Body** - Main character or shape / Personaje o forma principal
3. **Clothes** - Clothing on the body / Ropa en el cuerpo
4. **Eyes** - Eye style / Estilo de ojos
5. **Mouth** - Mouth expression / Expresión de boca
6. **Accessories** - Hats, glasses, etc. / Sombreros, gafas, etc.
7. **Special** - Rare overlays or effects / Superposiciones raras o efectos

---

## 🌟 Rarity System / Sistema de Rareza

Each file name includes a rarity weight number. The system uses weighted random selection:

Cada nombre de archivo incluye un número de peso de rareza. El sistema usa selección aleatoria ponderada:

### Example / Ejemplo:

```
background/
  ├── blue_100.png       (Common - appears ~100 out of 200 times)
  ├── red_100.png        (Common - appears ~100 out of 200 times)
  └── rainbow_5.png      (Rare - appears ~5 out of 205 times)
```

**Formula:** Weight / Total Weight = Probability

- Blue: 100 / 205 = 48.8% chance
- Red: 100 / 205 = 48.8% chance  
- Rainbow: 5 / 205 = 2.4% chance

---

## 💡 Scaling to 10,000+ NFTs / Escalando a 10,000+ NFTs

To generate 10,000 unique NFTs, you need enough combinations. Here's how:

Para generar 10,000 NFTs únicos, necesitas suficientes combinaciones. Así es cómo:

### Option 1: Add More Variants / Opción 1: Agregar Más Variantes

Add more images to existing layers:

Agrega más imágenes a las capas existentes:

- 10 backgrounds × 10 bodies × 10 clothes × 5 eyes × 5 mouths × 5 accessories × 3 special = **37,500 combinations**

### Option 2: Add New Layers / Opción 2: Agregar Nuevas Capas

Add new layer types:

Agrega nuevos tipos de capas:

- Add "hair" layer with 5 variants: 8,640 × 5 = **43,200 combinations**
- Add "background_effects" layer with 4 variants: 43,200 × 4 = **172,800 combinations**

### Option 3: Combine Both / Opción 3: Combinar Ambos

Best approach for large collections:

Mejor enfoque para colecciones grandes:

```
12 backgrounds
10 bodies
8 clothes
6 eyes
4 mouths
5 accessories
3 special
= 172,800 unique combinations
```

---

## 🎯 Real-World Example: Creating Your Own Collection

### English Instructions:

**Step 1: Plan Your Collection**

Decide on your theme. Examples:
- Animals (dogs, cats, birds)
- Characters (robots, aliens, humans)
- Objects (gems, planets, flowers)

**Step 2: Design Your Layers**

For a 10,000 NFT collection of robots:

```
layers/
├── background/        (10 variants: space, city, lab, etc.)
├── body/             (8 variants: different robot bodies)
├── head/             (8 variants: different head shapes)
├── eyes/             (6 variants: LED styles)
├── mouth/            (5 variants: grills, screens)
├── arms/             (6 variants: tool arms, weapon arms)
├── legs/             (5 variants: wheels, tracks, legs)
├── chest_emblem/     (8 variants: logos, symbols)
├── accessories/      (7 variants: antennas, badges)
└── special_effects/  (4 variants: glow, sparks + "none")
```

Total: 10 × 8 × 8 × 6 × 5 × 6 × 5 × 8 × 7 × 4 = **12,902,400 combinations**

Far more than enough for 10,000 unique NFTs!

**Step 3: Create the Art**

- Use vector graphics software (Illustrator, Inkscape)
- Or pixel art software (Aseprite, Photoshop)
- Keep consistent size (e.g., 1000x1000px or 2000x2000px)
- Export as PNG with transparency

**Step 4: Name Files with Rarity**

```
body/
├── standard_body_80.png       (Common)
├── heavy_body_60.png          (Uncommon)
├── sleek_body_40.png          (Rare)
└── golden_body_10.png         (Very Rare)
```

**Step 5: Generate and Test**

```bash
# Test with small batch first
python generate_nfts.py -n 100

# Check results, adjust if needed
python analyze_collection.py

# Generate full collection
python generate_nfts.py -n 10000
```

---

### Instrucciones en Español:

**Paso 1: Planea Tu Colección**

Decide tu tema. Ejemplos:
- Animales (perros, gatos, pájaros)
- Personajes (robots, aliens, humanos)
- Objetos (gemas, planetas, flores)

**Paso 2: Diseña Tus Capas**

Para una colección de 10,000 NFTs de robots:

```
layers/
├── background/        (10 variantes: espacio, ciudad, laboratorio, etc.)
├── body/             (8 variantes: diferentes cuerpos de robot)
├── head/             (8 variantes: diferentes formas de cabeza)
├── eyes/             (6 variantes: estilos de LED)
├── mouth/            (5 variantes: rejillas, pantallas)
├── arms/             (6 variantes: brazos de herramientas, armas)
├── legs/             (5 variantes: ruedas, orugas, piernas)
├── chest_emblem/     (8 variantes: logos, símbolos)
├── accessories/      (7 variantes: antenas, insignias)
└── special_effects/  (4 variantes: brillo, chispas + "ninguno")
```

Total: 10 × 8 × 8 × 6 × 5 × 6 × 5 × 8 × 7 × 4 = **12,902,400 combinaciones**

¡Mucho más que suficiente para 10,000 NFTs únicos!

**Paso 3: Crea el Arte**

- Usa software de gráficos vectoriales (Illustrator, Inkscape)
- O software de pixel art (Aseprite, Photoshop)
- Mantén tamaño consistente (ej., 1000x1000px o 2000x2000px)
- Exporta como PNG con transparencia

**Paso 4: Nombra Archivos con Rareza**

```
body/
├── cuerpo_estandar_80.png     (Común)
├── cuerpo_pesado_60.png       (Poco común)
├── cuerpo_elegante_40.png     (Raro)
└── cuerpo_dorado_10.png       (Muy Raro)
```

**Paso 5: Genera y Prueba**

```bash
# Prueba con un lote pequeño primero
python generate_nfts.py -n 100

# Verifica resultados, ajusta si es necesario
python analyze_collection.py

# Genera la colección completa
python generate_nfts.py -n 10000
```

---

## 🔥 Advanced Tips / Consejos Avanzados

### Trait Dependencies / Dependencias de Características

For more complex logic (e.g., "aliens can't wear human clothes"), you'll need to modify the generator script or create separate layer sets.

Para lógica más compleja (ej., "los aliens no pueden usar ropa humana"), necesitarás modificar el script generador o crear conjuntos de capas separados.

### Metadata Enrichment / Enriquecimiento de Metadatos

Edit the metadata files after generation to add:
- External URLs
- Animation URLs (if you create animated versions)
- Background colors
- Creator royalties

Edita los archivos de metadatos después de la generación para agregar:
- URLs externas
- URLs de animación (si creas versiones animadas)
- Colores de fondo
- Regalías del creador

### Batch Processing / Procesamiento por Lotes

For very large collections (50,000+), generate in batches:

Para colecciones muy grandes (50,000+), genera en lotes:

```bash
python generate_nfts.py -n 10000  # Batch 1
python generate_nfts.py -n 10000  # Batch 2
# etc.
```

---

## 📚 Resources / Recursos

- **OpenSea Metadata Standards**: https://docs.opensea.io/docs/metadata-standards
- **NFT Best Practices**: Research successful collections for inspiration
- **Design Tools**: GIMP (free), Photoshop, Illustrator, Procreate

---

**Remember / Recuerda:** Quality over quantity! It's better to have 1,000 well-designed, unique NFTs than 10,000 poorly made ones.

**¡La calidad sobre la cantidad!** Es mejor tener 1,000 NFTs bien diseñados y únicos que 10,000 mal hechos.
