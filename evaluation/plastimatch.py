import subprocess

def convert(input_arg, input_path, output_arg, output_path):
    command = f"plastimatch convert --{input_arg} {input_path} --{output_arg} {output_path}"
    try:
        subprocess.run(command, check=True)
        print("Plastimatch convert completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Plastimatch convert failed with error: {e}")

def pw_linear_transform(input_path, output_path):
    pw_linear_transform_command = f"plastimatch adjust --input {input_path} --pw-linear \"-1024, -1024, -200, 80, -120, 40, 600, 1300\" --output {output_path}.nrrd"
    # Call the shell or batch script with input and output paths
    try:
        subprocess.run(pw_linear_transform_command, check=True)
        print("Plastimatch adjustment completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Plastimatch adjustment failed with error: {e}")

def dmap(input_path, output_path):
    command = f"plastimatch dmap --input {input_path} --absolute-distance --output {output_path}"
    try:
        subprocess.run(command, check=True)
        print("Plastimatch dmap calculation completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Plastimatch dmap calculation with error: {e}")

def register(params_filepath):
    command = f"plastimatch {params_filepath}"
    try:
        subprocess.run(command, check=True)
        print("Plastimatch register completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Plastimatch register failed with error: {e}")
        
def warp(input, output, vf):
    command = f"plastimatch warp --input {input} --output-img {output}.mha --xf {vf}"
    try:
        subprocess.run(command, check=True)
        print("Plastimatch warp completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Plastimatch warp failed with error: {e}")
        
def dice(segment, warp):
    result = None
    command = f"plastimatch dice --all {segment} {warp}"
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, text=True, check=True)
        print("Plastimatch dice completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Plastimatch dice failed with error: {e}")
    
    return result