import os

# DTU
# scan24, scan37, scan40, scan55, scan63, scan65, scan69, scan83, 
# scan97, scan105, scan106, scan110, scan114, scan118, scan122

dtu_scenes = ['scan24', 'scan37', 'scan40', 'scan55', 'scan63', 'scan65', 'scan69', 'scan83', \
              'scan97', 'scan105', 'scan106', 'scan110', 'scan114', 'scan118', 'scan122']

# train
cmd_lis=[]
# for scene in dtu_scenes:
#     cmd_lis.append(f'python train.py -s ../../Data/DTU/{scene} -m ../exps/full/DTU/{scene} -r 2 --depth_ratio 1')

# render images,  extract and eval meshes
cmd_lis.append('python scripts/dtu_eval.py --dtu ../../Data/DTU --output_path ../exps/full/DTU --DTU_Official ../../Data/Offical_DTU_Dataset --skip_training')

# eval nvs
for scene in dtu_scenes:
    # cmd_lis.append(f'python metrics.py -m ../exps/full/DTU/{scene} -f train')
    cmd_lis.append(f'python vis_outputs.py -m ../exps/full/DTU/{scene} -f train')

# run cmd
for cmd in cmd_lis:
    os.system(cmd)
