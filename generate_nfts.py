#!/usr/bin/env python3
"""
NFT Collection Generator
Generates unique NFTs by combining different layers (traits)
"""

import os
import json
import random
import hashlib
from PIL import Image
from pathlib import Path
from typing import List, Dict, Tuple
from collections import defaultdict


class NFTGenerator:
    """Generate unique NFT collections with layered images and metadata"""
    
    def __init__(self, config_path: str = "config.json"):
        """
        Initialize the NFT generator
        
        Args:
            config_path: Path to configuration file
        """
        self.config = self._load_config(config_path)
        self.output_dir = Path(self.config.get("output_dir", "output"))
        self.layers_dir = Path(self.config.get("layers_dir", "layers"))
        self.image_size = tuple(self.config.get("image_size", [1000, 1000]))
        self.generated_hashes = set()
        self.generated_combinations = set()
        
        # Create output directories
        self.images_dir = self.output_dir / "images"
        self.metadata_dir = self.output_dir / "metadata"
        self.images_dir.mkdir(parents=True, exist_ok=True)
        self.metadata_dir.mkdir(parents=True, exist_ok=True)
    
    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from JSON file"""
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def _get_layers(self) -> Dict[str, List[Dict]]:
        """
        Scan layers directory and build layers dictionary
        
        Returns:
            Dictionary mapping layer names to list of available files with rarity
        """
        layers = defaultdict(list)
        
        if not self.layers_dir.exists():
            print(f"Warning: Layers directory '{self.layers_dir}' not found")
            return layers
        
        # Get layer order from config
        layer_order = self.config.get("layer_order", [])
        
        for layer_name in layer_order:
            layer_path = self.layers_dir / layer_name
            if not layer_path.exists():
                print(f"Warning: Layer '{layer_name}' directory not found")
                continue
            
            # Get all image files in this layer
            for img_file in sorted(layer_path.glob("*.png")):
                # Extract rarity from filename if present (e.g., background_common_50.png)
                parts = img_file.stem.split('_')
                rarity = 100  # Default rarity weight
                
                if len(parts) > 1 and parts[-1].isdigit():
                    rarity = int(parts[-1])
                
                layers[layer_name].append({
                    "path": img_file,
                    "name": img_file.stem,
                    "rarity": rarity
                })
        
        return layers
    
    def _select_trait(self, traits: List[Dict]) -> Dict:
        """
        Select a trait based on rarity weights
        
        Args:
            traits: List of trait dictionaries with rarity weights
            
        Returns:
            Selected trait dictionary
        """
        if not traits:
            return None
        
        # Calculate total weight
        total_weight = sum(trait["rarity"] for trait in traits)
        
        # Random selection based on weights
        rand = random.randint(1, total_weight)
        current = 0
        
        for trait in traits:
            current += trait["rarity"]
            if rand <= current:
                return trait
        
        return traits[-1]
    
    def _create_combination_key(self, selected_traits: Dict) -> str:
        """Create a unique key for this combination of traits"""
        trait_names = []
        for layer in sorted(selected_traits.keys()):
            if selected_traits[layer]:
                trait_names.append(f"{layer}:{selected_traits[layer]['name']}")
        return "|".join(trait_names)
    
    def _generate_unique_nft(self, layers: Dict[str, List[Dict]], max_attempts: int = 100) -> Tuple[Image.Image, Dict]:
        """
        Generate a unique NFT by combining layers
        
        Args:
            layers: Dictionary of available layers
            max_attempts: Maximum attempts to generate unique combination
            
        Returns:
            Tuple of (PIL Image, metadata dict) or (None, None) if failed
        """
        for attempt in range(max_attempts):
            # Select one trait from each layer
            selected_traits = {}
            for layer_name, traits in layers.items():
                if traits:  # Only if layer has traits
                    selected_traits[layer_name] = self._select_trait(traits)
            
            # Check if this combination is unique
            combination_key = self._create_combination_key(selected_traits)
            if combination_key not in self.generated_combinations:
                self.generated_combinations.add(combination_key)
                
                # Create the image
                image = Image.new('RGBA', self.image_size, (0, 0, 0, 0))
                
                metadata = {
                    "attributes": []
                }
                
                # Layer the images in order
                for layer_name in self.config.get("layer_order", []):
                    if layer_name in selected_traits and selected_traits[layer_name]:
                        trait = selected_traits[layer_name]
                        layer_img = Image.open(trait["path"]).convert('RGBA')
                        
                        # Resize if needed
                        if layer_img.size != self.image_size:
                            layer_img = layer_img.resize(self.image_size, Image.LANCZOS)
                        
                        # Composite the layer
                        image = Image.alpha_composite(image, layer_img)
                        
                        # Add to metadata
                        metadata["attributes"].append({
                            "trait_type": layer_name.replace('_', ' ').title(),
                            "value": trait["name"].replace('_', ' ').title()
                        })
                
                # Generate hash to ensure uniqueness
                img_hash = hashlib.md5(image.tobytes()).hexdigest()
                if img_hash not in self.generated_hashes:
                    self.generated_hashes.add(img_hash)
                    return image, metadata
        
        return None, None
    
    def generate_collection(self, num_nfts: int = 1000) -> None:
        """
        Generate a collection of unique NFTs
        
        Args:
            num_nfts: Number of NFTs to generate
        """
        print(f"Generating {num_nfts} unique NFTs...")
        
        layers = self._get_layers()
        
        if not layers:
            print("Error: No layers found. Please add image layers to the 'layers' directory.")
            return
        
        print(f"Found {len(layers)} layers:")
        for layer_name, traits in layers.items():
            print(f"  - {layer_name}: {len(traits)} variants")
        
        # Calculate theoretical maximum unique combinations
        max_combinations = 1
        for traits in layers.values():
            max_combinations *= len(traits) if traits else 1
        
        print(f"Maximum possible unique combinations: {max_combinations}")
        
        if num_nfts > max_combinations:
            print(f"Warning: Requested {num_nfts} NFTs but only {max_combinations} unique combinations possible")
            num_nfts = max_combinations
        
        # Generate NFTs
        generated = 0
        failed = 0
        
        for i in range(num_nfts * 2):  # Try up to 2x to account for duplicates
            if generated >= num_nfts:
                break
            
            image, metadata = self._generate_unique_nft(layers)
            
            if image is None:
                failed += 1
                if failed > 100:
                    print(f"Warning: Failed to generate unique NFT after many attempts. Stopping.")
                    break
                continue
            
            # Save image
            token_id = generated + 1
            image_filename = f"{token_id}.png"
            image_path = self.images_dir / image_filename
            image.save(image_path, 'PNG')
            
            # Add metadata fields
            metadata["name"] = f"{self.config.get('collection_name', 'NFT')} #{token_id}"
            metadata["description"] = self.config.get('collection_description', 'Unique NFT from collection')
            metadata["image"] = image_filename
            metadata["tokenId"] = token_id
            
            # Save metadata
            metadata_path = self.metadata_dir / f"{token_id}.json"
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)
            
            generated += 1
            
            if generated % 100 == 0:
                print(f"Generated {generated}/{num_nfts} NFTs...")
        
        print(f"\n✓ Successfully generated {generated} unique NFTs!")
        print(f"  Images saved to: {self.images_dir}")
        print(f"  Metadata saved to: {self.metadata_dir}")
        
        # Generate collection metadata
        self._generate_collection_metadata(generated)
    
    def _generate_collection_metadata(self, total_supply: int) -> None:
        """Generate overall collection metadata file"""
        collection_metadata = {
            "name": self.config.get('collection_name', 'NFT Collection'),
            "description": self.config.get('collection_description', 'Unique NFT collection'),
            "total_supply": total_supply,
            "image_size": self.image_size,
            "layers": list(self._get_layers().keys())
        }
        
        metadata_path = self.output_dir / "collection.json"
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(collection_metadata, f, indent=2, ensure_ascii=False)
        
        print(f"  Collection metadata saved to: {metadata_path}")


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate unique NFT collection')
    parser.add_argument('-n', '--number', type=int, default=1000,
                      help='Number of NFTs to generate (default: 1000)')
    parser.add_argument('-c', '--config', type=str, default='config.json',
                      help='Path to configuration file (default: config.json)')
    
    args = parser.parse_args()
    
    generator = NFTGenerator(config_path=args.config)
    generator.generate_collection(num_nfts=args.number)


if __name__ == "__main__":
    main()
