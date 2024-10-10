import os
import subprocess
from const import VUL4J_IDX

if __name__ == "__main__":
    for idx in VUL4J_IDX:
        #cmd = ['vul4j','checkout','--id',f'VUL4J-{idx}','-d',f'/mnt/workspace/dataset/VUL4J-{idx}']
        cmd = f'vul4j checkout --id VUL4J-{idx} -d /mnt/workspace/dataset/VUL4J-{idx}'
        try:
            result = subprocess.run(cmd, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Successfully checked out VUL4J-{idx}. Output:\n {result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while checking out VUL4J-{idx}. Error:\n {e.stderr}")

        