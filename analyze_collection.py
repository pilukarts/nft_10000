#!/usr/bin/env python3
"""
Analyze generated NFT collection statistics
Shows trait distribution and rarity breakdown
"""

import json
import os
from pathlib import Path
from collections import defaultdict, Counter


def analyze_collection(metadata_dir="output/metadata"):
    """Analyze the generated NFT collection"""
    
    metadata_path = Path(metadata_dir)
    
    if not metadata_path.exists():
        print(f"Error: Metadata directory '{metadata_dir}' not found")
        return
    
    # Collect all metadata
    metadata_files = sorted(metadata_path.glob("*.json"))
    
    if not metadata_files:
        print("No metadata files found")
        return
    
    print(f"📊 NFT Collection Analysis")
    print(f"{'=' * 60}\n")
    print(f"Total NFTs: {len(metadata_files)}\n")
    
    # Collect trait statistics
    trait_stats = defaultdict(Counter)
    
    for metadata_file in metadata_files:
        with open(metadata_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            for attribute in data.get('attributes', []):
                trait_type = attribute['trait_type']
                trait_value = attribute['value']
                trait_stats[trait_type][trait_value] += 1
    
    # Display statistics for each trait type
    for trait_type in sorted(trait_stats.keys()):
        print(f"🎨 {trait_type}")
        print(f"{'-' * 60}")
        
        total_count = sum(trait_stats[trait_type].values())
        
        # Sort by count (most common first)
        sorted_traits = sorted(
            trait_stats[trait_type].items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        for trait_value, count in sorted_traits:
            percentage = (count / total_count) * 100
            bar_length = int(percentage / 2)  # Scale to 50 chars max
            bar = '█' * bar_length
            
            print(f"  {trait_value:30s} {count:4d} ({percentage:5.1f}%) {bar}")
        
        print()
    
    # Find rarest NFTs (those with rarest trait combinations)
    print("🌟 Rarity Analysis")
    print(f"{'-' * 60}")
    
    nft_rarity_scores = []
    
    for metadata_file in metadata_files:
        with open(metadata_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            # Calculate rarity score (sum of inverse frequencies)
            rarity_score = 0
            for attribute in data.get('attributes', []):
                trait_type = attribute['trait_type']
                trait_value = attribute['value']
                count = trait_stats[trait_type][trait_value]
                total = sum(trait_stats[trait_type].values())
                rarity_score += (1 / (count / total)) if count > 0 else 0
            
            nft_rarity_scores.append({
                'token_id': data['tokenId'],
                'name': data['name'],
                'rarity_score': rarity_score,
                'attributes': data['attributes']
            })
    
    # Sort by rarity score (highest = rarest)
    nft_rarity_scores.sort(key=lambda x: x['rarity_score'], reverse=True)
    
    print("\n🏆 Top 10 Rarest NFTs:")
    print(f"{'-' * 60}")
    for i, nft in enumerate(nft_rarity_scores[:10], 1):
        print(f"\n{i}. {nft['name']} (Score: {nft['rarity_score']:.2f})")
        for attr in nft['attributes']:
            trait_type = attr['trait_type']
            trait_value = attr['value']
            count = trait_stats[trait_type][trait_value]
            total = sum(trait_stats[trait_type].values())
            percentage = (count / total) * 100
            print(f"   - {trait_type}: {trait_value} ({percentage:.1f}%)")
    
    print("\n" + "=" * 60)
    print("✓ Analysis complete!")


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Analyze NFT collection statistics')
    parser.add_argument('-d', '--dir', type=str, default='output/metadata',
                      help='Path to metadata directory (default: output/metadata)')
    
    args = parser.parse_args()
    
    analyze_collection(metadata_dir=args.dir)


if __name__ == "__main__":
    main()
