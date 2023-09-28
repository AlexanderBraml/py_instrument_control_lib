import os

from device_generation.generate_module import generate_module

source_dir = '../specifications'
gen_dir = '../devices'

specs = []

for file_path in os.listdir(source_dir):
    if os.path.isfile(os.path.join(source_dir, file_path)):
        specs.append(os.path.join(source_dir, file_path))

for spec in specs:
    generate_module(spec, gen_dir)
