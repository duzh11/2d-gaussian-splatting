import os

# Mushroom dataset
mushroom_root = '../../Data/MuSHRoom_iphone-loftr'
mushroom_exp = '../exps/full/MuSHRoom_iphone-loftr-lambdadist-10'
mushroom_scenes = ['koivu', 'honka', 'computer']
cuda_device = 0

# train
cmd_lis=[]
for scene in mushroom_scenes:
    # cmd_lis.append(f'CUDA_VISIBLE_DEVICES={cuda_device} python train.py -s {mushroom_root}/{scene} -m {mushroom_exp}/{scene} -r 2 --eval --depth_ratio 1.0 --lambda_dist 1000')
    # cmd_lis.append(f'CUDA_VISIBLE_DEVICES={cuda_device} python render.py -s {mushroom_root}/{scene} -m {mushroom_exp}/{scene} -r 2 --eval --skip_train --skip_test --depth_ratio 1.0 --num_cluster 1 --depth_trunc 5.0 --voxel_size 0.01')
    cmd_lis.append(f'CUDA_VISIBLE_DEVICES={cuda_device} python render.py -s {mushroom_root}/{scene} -m {mushroom_exp}/{scene} -r 2 --eval --skip_train --skip_test --mesh_type poisson --depth_ratio 1.0 --num_cluster 1 --poisson_depth 10.0')

    # cmd_lis.append(f'CUDA_VISIBLE_DEVICES={cuda_device} python metrics.py -m {mushroom_exp}/{scene} -f train')
    # cmd_lis.append(f'CUDA_VISIBLE_DEVICES={cuda_device} python metrics.py -m {mushroom_exp}/{scene} -f test')
    # cmd_lis.append(f'CUDA_VISIBLE_DEVICES={cuda_device} python vis_outputs.py -m {mushroom_exp}/{scene} -f train test')

# run cmd
for cmd in cmd_lis:
    print(cmd)
    os.system(cmd)
