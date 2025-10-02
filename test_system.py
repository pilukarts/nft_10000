#!/usr/bin/env python3
"""
Test script to verify NFT generation system
Runs various tests to ensure everything works correctly
"""

import os
import sys
import json
import subprocess
from pathlib import Path


def print_header(text):
    """Print a formatted header"""
    print(f"\n{'=' * 60}")
    print(f"  {text}")
    print(f"{'=' * 60}\n")


def print_status(emoji, text):
    """Print a status message"""
    print(f"{emoji} {text}")


def test_dependencies():
    """Test if required dependencies are installed"""
    print_header("Testing Dependencies")
    
    try:
        import PIL
        print_status("✓", f"Pillow installed (version {PIL.__version__})")
        return True
    except ImportError:
        print_status("✗", "Pillow not installed")
        print("  Install with: pip install -r requirements.txt")
        return False


def test_layers_exist():
    """Test if layer directories and files exist"""
    print_header("Testing Layer Structure")
    
    layers_dir = Path("layers")
    if not layers_dir.exists():
        print_status("✗", "Layers directory not found")
        return False
    
    layer_names = ["background", "body", "clothes", "eyes", "mouth", "accessories", "special"]
    all_good = True
    
    for layer_name in layer_names:
        layer_path = layers_dir / layer_name
        if not layer_path.exists():
            print_status("✗", f"Layer directory missing: {layer_name}")
            all_good = False
        else:
            png_files = list(layer_path.glob("*.png"))
            if len(png_files) == 0:
                print_status("⚠", f"Layer '{layer_name}' has no PNG files")
                all_good = False
            else:
                print_status("✓", f"Layer '{layer_name}' has {len(png_files)} variants")
    
    return all_good


def test_config_valid():
    """Test if config.json is valid"""
    print_header("Testing Configuration")
    
    if not os.path.exists("config.json"):
        print_status("✗", "config.json not found")
        return False
    
    try:
        with open("config.json", 'r') as f:
            config = json.load(f)
        
        required_keys = ["collection_name", "layer_order", "image_size"]
        for key in required_keys:
            if key not in config:
                print_status("✗", f"Missing required config key: {key}")
                return False
        
        print_status("✓", f"Collection name: {config['collection_name']}")
        print_status("✓", f"Image size: {config['image_size']}")
        print_status("✓", f"Layer order: {len(config['layer_order'])} layers")
        return True
        
    except json.JSONDecodeError:
        print_status("✗", "config.json is not valid JSON")
        return False


def test_generation():
    """Test NFT generation with small batch"""
    print_header("Testing NFT Generation")
    
    # Clean up any existing test output
    test_output = Path("test_output")
    if test_output.exists():
        import shutil
        shutil.rmtree(test_output)
    
    # Modify config temporarily
    try:
        with open("config.json", 'r') as f:
            config = json.load(f)
        
        original_output = config.get("output_dir", "output")
        config["output_dir"] = "test_output"
        
        with open("config_test.json", 'w') as f:
            json.dump(config, f, indent=2)
        
        # Run generation
        print("Generating 5 test NFTs...")
        result = subprocess.run(
            ["python3", "generate_nfts.py", "-n", "5", "-c", "config_test.json"],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print_status("✗", "Generation failed")
            print(result.stderr)
            return False
        
        # Check output
        images_dir = test_output / "images"
        metadata_dir = test_output / "metadata"
        
        if not images_dir.exists() or not metadata_dir.exists():
            print_status("✗", "Output directories not created")
            return False
        
        images = list(images_dir.glob("*.png"))
        metadata_files = list(metadata_dir.glob("*.json"))
        
        if len(images) != 5 or len(metadata_files) != 5:
            print_status("✗", f"Expected 5 files, got {len(images)} images and {len(metadata_files)} metadata")
            return False
        
        print_status("✓", "Generated 5 test NFTs successfully")
        
        # Test metadata structure
        with open(metadata_dir / "1.json", 'r') as f:
            metadata = json.load(f)
        
        required_fields = ["name", "description", "image", "tokenId", "attributes"]
        for field in required_fields:
            if field not in metadata:
                print_status("✗", f"Metadata missing field: {field}")
                return False
        
        print_status("✓", "Metadata structure is correct")
        
        # Cleanup
        import shutil
        shutil.rmtree(test_output)
        os.remove("config_test.json")
        
        return True
        
    except Exception as e:
        print_status("✗", f"Error during generation test: {str(e)}")
        return False


def calculate_max_combinations():
    """Calculate maximum possible unique combinations"""
    print_header("Calculating Maximum Combinations")
    
    layers_dir = Path("layers")
    layer_order = ["background", "body", "clothes", "eyes", "mouth", "accessories", "special"]
    
    total = 1
    details = []
    
    for layer_name in layer_order:
        layer_path = layers_dir / layer_name
        if layer_path.exists():
            variants = len(list(layer_path.glob("*.png")))
            if variants > 0:
                total *= variants
                details.append(f"{layer_name}: {variants}")
    
    print("Layer breakdown:")
    for detail in details:
        print(f"  • {detail}")
    
    print(f"\n{total:,} unique combinations possible")
    
    if total < 1000:
        print_status("⚠", "Warning: Less than 1,000 unique combinations possible")
        print("  Consider adding more layer variants")
    elif total < 10000:
        print_status("✓", "Sufficient for generating 1,000+ unique NFTs")
    else:
        print_status("✓", "Sufficient for generating 10,000+ unique NFTs")
    
    return True


def main():
    """Run all tests"""
    print_header("NFT Generator Test Suite")
    
    tests = [
        ("Dependencies", test_dependencies),
        ("Layer Structure", test_layers_exist),
        ("Configuration", test_config_valid),
        ("Max Combinations", calculate_max_combinations),
        ("Generation", test_generation),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print_status("✗", f"Test '{test_name}' raised exception: {str(e)}")
            results.append((test_name, False))
    
    # Summary
    print_header("Test Summary")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        emoji = "✓" if result else "✗"
        print_status(emoji, test_name)
    
    print(f"\n{passed}/{total} tests passed")
    
    if passed == total:
        print_status("🎉", "All tests passed! System is ready to use.")
        return 0
    else:
        print_status("⚠", "Some tests failed. Please fix issues before generating NFTs.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
