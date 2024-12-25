import os

scannetpp_root = '../../Data/ScanNetpp'
scannetpp_exp = '../exps/full/scannetpp'
scannetpp_scenes = ['8b5caf3398', '116456116b', '13c3e046d7', '0a184cf634', '578511c8a9', '21d970d8de']
cuda_device = 0

cmd_lis = []
for scene in scannetpp_scenes:
    source = scannetpp_root + "/" + scene

    # training
    # common_args = " --test_iterations -1 --depth_ratio 1.0 -r 2 --eval --lambda_dist 100"
    # cmd_lis.append(f"CUDA_VISIBLE_DEVICES={cuda_device} python train.py -s " + source + " -m " + scannetpp_exp + "/" + scene + common_args)

    # rendering image, depth, normal, and mesh
    common_args = " --quiet --depth_ratio 1.0 -r 2 --eval --num_cluster 1 --depth_trunc 5.0 --voxel_size 0.01 --skip_mesh"
    cmd_lis.append(f"CUDA_VISIBLE_DEVICES={cuda_device} python render.py --iteration 30000 -s " + source + " -m " + scannetpp_exp + "/" + scene + common_args)
    
    # NVS metrics and visualization 
    # cmd_lis.append(f'CUDA_VISIBLE_DEVICES={cuda_device} python metrics.py -m {scannetpp_exp}/{scene} -f train')
    # cmd_lis.append(f'CUDA_VISIBLE_DEVICES={cuda_device} python metrics.py -m {scannetpp_exp}/{scene} -f test')
    # cmd_lis.append(f'CUDA_VISIBLE_DEVICES={cuda_device} python vis_outputs.py -m {scannetpp_exp}/{scene} -f train test')

    # evaluate mesh, depth & normal
    common_args = " -f train test -p tsdf poisson"
    cmd_lis.append(f"CUDA_VISIBLE_DEVICES={cuda_device} python scripts/eval_geometry.py -s " + source + " -m " + scannetpp_exp + "/" + scene + common_args)

# run cmd
for cmd in cmd_lis:
    print(cmd)
    os.system(cmd)