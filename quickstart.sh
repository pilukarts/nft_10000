#!/bin/bash
# Quick start script for NFT generation
# Este script te ayuda a empezar rápidamente / This script helps you get started quickly

echo "🎨 NFT Collection Generator - Quick Start"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "   Please install Python 3.7 or higher"
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Check if Pillow is installed
if ! python3 -c "import PIL" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
    echo ""
fi

echo "✓ Dependencies installed"
echo ""

# Check if layers exist
if [ ! -d "layers/background" ] || [ -z "$(ls -A layers/background)" ]; then
    echo "📁 Creating example layers..."
    python3 create_example_layers.py
    echo ""
fi

echo "✓ Layers ready"
echo ""

# Ask user what to do
echo "What would you like to do? / ¿Qué te gustaría hacer?"
echo ""
echo "1) Test with 10 NFTs (recommended for first time)"
echo "   Probar con 10 NFTs (recomendado la primera vez)"
echo ""
echo "2) Generate 100 NFTs"
echo "   Generar 100 NFTs"
echo ""
echo "3) Generate 1000 NFTs"
echo "   Generar 1000 NFTs"
echo ""
echo "4) Generate custom amount"
echo "   Generar cantidad personalizada"
echo ""
echo "5) Analyze existing collection"
echo "   Analizar colección existente"
echo ""
echo "6) Exit / Salir"
echo ""

read -p "Enter your choice (1-6): " choice

case $choice in
    1)
        echo ""
        echo "🚀 Generating 10 test NFTs..."
        python3 generate_nfts.py -n 10
        ;;
    2)
        echo ""
        echo "🚀 Generating 100 NFTs..."
        python3 generate_nfts.py -n 100
        ;;
    3)
        echo ""
        echo "🚀 Generating 1000 NFTs..."
        python3 generate_nfts.py -n 1000
        ;;
    4)
        echo ""
        read -p "Enter number of NFTs to generate: " num
        echo "🚀 Generating $num NFTs..."
        python3 generate_nfts.py -n "$num"
        ;;
    5)
        echo ""
        if [ -d "output/metadata" ] && [ "$(ls -A output/metadata)" ]; then
            echo "📊 Analyzing collection..."
            python3 analyze_collection.py
        else
            echo "❌ No collection found. Generate NFTs first."
        fi
        ;;
    6)
        echo "Goodbye! / ¡Hasta luego!"
        exit 0
        ;;
    *)
        echo "❌ Invalid choice / Opción inválida"
        exit 1
        ;;
esac

echo ""
echo "=========================================="
echo "✅ Done! / ¡Listo!"
echo ""

if [ -d "output/images" ] && [ "$(ls -A output/images)" ]; then
    echo "📁 Your NFTs are in: output/images/"
    echo "   Tus NFTs están en: output/images/"
    echo ""
    echo "📝 Metadata is in: output/metadata/"
    echo "   Los metadatos están en: output/metadata/"
    echo ""
    
    # Offer to analyze
    if [ "$choice" != "5" ]; then
        read -p "Would you like to analyze the collection? (y/n): " analyze
        if [ "$analyze" = "y" ] || [ "$analyze" = "Y" ]; then
            echo ""
            python3 analyze_collection.py
        fi
    fi
fi

echo ""
echo "📖 For more information, see README.md or USAGE_GUIDE.md"
echo "   Para más información, ver README.md o USAGE_GUIDE.md"
