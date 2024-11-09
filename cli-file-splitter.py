import os
import argparse
from pathlib import Path
from tqdm import tqdm

def split_file(input_file, chunk_size_gb=1, output_dir="split_files"):
    """
    Split a file into smaller chunks.
    
    Args:
        input_file (str): Path to the input file
        chunk_size_gb (int): Size of each chunk in gigabytes
        output_dir (str): Directory to store output files
    """
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Convert GB to bytes
    chunk_size = chunk_size_gb * 1024 * 1024 * 1024
    
    # Get file size and calculate number of chunks
    file_size = os.path.getsize(input_file)
    num_chunks = (file_size + chunk_size - 1) // chunk_size
    
    # Get base name of input file
    base_name = os.path.basename(input_file)
    name, ext = os.path.splitext(base_name)
    
    print(f"Splitting {input_file} into {num_chunks} chunks of {chunk_size_gb}GB each")
    
    # Open input file and create progress bar
    with open(input_file, 'rb') as f:
        with tqdm(total=file_size, unit='B', unit_scale=True) as pbar:
            for chunk_num in range(num_chunks):
                # Calculate chunk size (last chunk might be smaller)
                current_chunk_size = min(chunk_size, file_size - chunk_num * chunk_size)
                
                # Create output filename
                output_file = os.path.join(
                    output_dir,
                    f"{name}_part{chunk_num + 1:03d}{ext}"
                )
                
                # Read and write chunk
                chunk_data = f.read(current_chunk_size)
                with open(output_file, 'wb') as chunk_file:
                    chunk_file.write(chunk_data)
                
                # Update progress bar
                pbar.update(current_chunk_size)
    
    print(f"\nFile splitting completed! Files saved in: {output_dir}")

def main():
    parser = argparse.ArgumentParser(description='Split a large file into smaller chunks')
    parser.add_argument('input_file', help='Path to the input file')
    parser.add_argument('--size', type=int, default=1, help='Size of each chunk in GB (default: 1)')
    parser.add_argument('--output-dir', default='split_files', help='Output directory (default: split_files)')
    
    args = parser.parse_args()
    
    try:
        split_file(args.input_file, args.size, args.output_dir)
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
