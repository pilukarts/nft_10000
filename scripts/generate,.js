const fs = require("fs");
const path = require("path");
const { createCanvas, loadImage } = require("canvas");

const width = 1000;
const height = 1000;

const layers = [
  { name: "Background", path: path.join(__dirname, "../layers/Background") },
  { name: "Helmet", path: path.join(__dirname, "../layers/Helmet") },
  { name: "Body", path: path.join(__dirname, "../layers/Body") },
  // Añade más capas según tus necesidades
];

function getFilesInDir(dir) {
  return fs.readdirSync(dir)
    .filter(f => /\.(png|jpg|jpeg)$/i.test(f))
    .map(f => path.join(dir, f));
}

async function createNFT(id) {
  const canvas = createCanvas(width, height);
  const ctx = canvas.getContext("2d");

  const metadata = {
    name: `NFT #${id}`,
    description: "Una colección generada de forma automática",
    image: "",             // lo llenarás luego con la URL (IPFS, etc.)
    attributes: []
  };

  for (const layer of layers) {
    const choices = getFilesInDir(layer.path);
    if (choices.length === 0) {
      console.warn(`No hay archivos en la capa ${layer.name}`);
      continue;
    }
    const chosen = choices[Math.floor(Math.random() * choices.length)];
    const img = await loadImage(chosen);
    ctx.drawImage(img, 0, 0, width, height);

    // metadata trait
    const traitName = layer.name;
    const traitValue = path.basename(chosen, path.extname(chosen));
    metadata.attributes.push({
      trait_type: traitName,
      value: traitValue
    });
  }

  // guarda la imagen
  const imgBuffer = canvas.toBuffer("image/png");
  const imgPath = path.join(__dirname, "../output/images", `${id}.png`);
  fs.writeFileSync(imgPath, imgBuffer);

  // llena la URL de imagen en metadata (temporalmente solo ruta local)
  metadata.image = `images/${id}.png`;

  // guarda el JSON
  const metaPath = path.join(__dirname, "../output/metadata", `${id}.json`);
  fs.writeFileSync(metaPath, JSON.stringify(metadata, null, 2));

  console.log(`Generado NFT #${id}`);
}

async function main() {
  const total = 1000;  // puedes cambiar a 10000
  // asegúrate de que existan las carpetas de salida
  const outImgDir = path.join(__dirname, "../output/images");
  const outMetaDir = path.join(__dirname, "../output/metadata");
  if (!fs.existsSync(outImgDir)) fs.mkdirSync(outImgDir, { recursive: true });
  if (!fs.existsSync(outMetaDir)) fs.mkdirSync(outMetaDir, { recursive: true });

  for (let i = 1; i <= total; i++) {
    await createNFT(i);
  }
  console.log("Hecho!");
}

main();
