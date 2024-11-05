# Design a Python-based experiment to analyze the performance of MD5, SHA-1, and SHA-256 hashing techniques 
# in terms of computation time and collision resistance. Generate a dataset of random strings ranging from 50 to 100 
# strings, compute the hash values using each hashing technique, and measure the time taken for hash computation. 
# Implement collision detection algorithms to identify any collisions within the hashed dataset.

import hashlib
import time
import random
import string
from collections import defaultdict

def generate_random_strings(num_strings=100, length_range=(50, 100)):
    return [''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(*length_range))) 
            for _ in range(num_strings)]

def compute_hash(hash_func, data):
    return hash_func(data.encode('utf-8')).hexdigest()

def time_hashing(hash_func, data):
    start_time = time.time()
    hashed_value = compute_hash(hash_func, data)
    end_time = time.time()
    return hashed_value, end_time - start_time

def analyze_hash_performance(data_list):
    results = {
        'md5': {'times': [], 'hashes': []},
        'sha1': {'times': [], 'hashes': []},
        'sha256': {'times': [], 'hashes': []}
    }

    # Compute hashes and times for each hashing function
    for data in data_list:
        md5_hash, md5_time = time_hashing(hashlib.md5, data)
        results['md5']['hashes'].append(md5_hash)
        results['md5']['times'].append(md5_time)

        sha1_hash, sha1_time = time_hashing(hashlib.sha1, data)
        results['sha1']['hashes'].append(sha1_hash)
        results['sha1']['times'].append(sha1_time)

        sha256_hash, sha256_time = time_hashing(hashlib.sha256, data)
        results['sha256']['hashes'].append(sha256_hash)
        results['sha256']['times'].append(sha256_time)
    return results

def detect_collisions(hashes):
    hash_counts = defaultdict(int)
    for hash_value in hashes:
        hash_counts[hash_value] += 1
    collisions = {hash_value: count for hash_value, count in hash_counts.items() if count > 1}
    return collisions

random_strings = generate_random_strings(num_strings=100, length_range=(50, 100))
results = analyze_hash_performance(random_strings)

md5_collisions = detect_collisions(results['md5']['hashes'])
sha1_collisions = detect_collisions(results['sha1']['hashes'])
sha256_collisions = detect_collisions(results['sha256']['hashes'])

print("Hashing Performance Analysis:")
print("MD5:")
print(f"  Average time: {sum(results['md5']['times']) / len(results['md5']['times']):.6f} seconds")
print(f"  Collisions detected: {len(md5_collisions)}")

print("SHA-1:")
print(f"  Average time: {sum(results['sha1']['times']) / len(results['sha1']['times']):.6f} seconds")
print(f"  Collisions detected: {len(sha1_collisions)}")

print("SHA-256:")
print(f"  Average time: {sum(results['sha256']['times']) / len(results['sha256']['times']):.6f} seconds")
print(f"  Collisions detected: {len(sha256_collisions)}")