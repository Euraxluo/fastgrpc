from fastgrpc import protoBuild
import sys
import os

os.chdir(sys.path[0])

if __name__ == '__main__':
    protos_dir = './protos'
    output_dir = '.'
    protoBuild(protos_dir, output_dir)
