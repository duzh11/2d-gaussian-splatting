import os

# Mushroom dataset
TnTadvanced_root = '../../Data/TanksAndTemples_advanced-loftr'
TnTadvanced_exp = '../exps/full/TanksAndTemples_advanced-loftr-lambdadist-10'
TnTadvanced_scenes = ['Auditorium', 'Courtroom', 'Ballroom']
cuda_device = 0

# train
cmd_lis=[]
for scene in TnTadvanced_scenes:
    # cmd_lis.append(f'CUDA_VISIBLE_DEVICES={cuda_device} python train.py -s {TnTadvanced_root}/{scene} -m {TnTadvanced_exp}/{scene} -r 2 --eval --depth_ratio 1.0 --lambda_dist 1000 --port 6010')
    # cmd_lis.append(f'CUDA_VISIBLE_DEVICES={cuda_device} python render.py -s {TnTadvanced_root}/{scene} -m {TnTadvanced_exp}/{scene} -r 2 --eval --skip_train --skip_test --depth_ratio 1.0 --num_cluster 1 --depth_trunc 20.0 --voxel_size 0.01')
    cmd_lis.append(f'CUDA_VISIBLE_DEVICES={cuda_device} python render.py -s {TnTadvanced_root}/{scene} -m {TnTadvanced_exp}/{scene} -r 2 --eval --skip_train --skip_test --mesh_type poisson --depth_ratio 1.0 --num_cluster 1 --poisson_depth 12.0')

    # cmd_lis.append(f'CUDA_VISIBLE_DEVICES={cuda_device} python metrics.py -m {TnTadvanced_exp}/{scene} -f train')
    # cmd_lis.append(f'CUDA_VISIBLE_DEVICES={cuda_device} python metrics.py -m {TnTadvanced_exp}/{scene} -f test')
    # cmd_lis.append(f'CUDA_VISIBLE_DEVICES={cuda_device} python vis_outputs.py -m {TnTadvanced_exp}/{scene} -f train test')

# run cmd
for cmd in cmd_lis:
    print(cmd)
    os.system(cmd)
