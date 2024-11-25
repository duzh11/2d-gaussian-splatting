import os

# TNT
# Barn, Caterpillar, Courthouse, Ignatius, Meetingroom, Truck

tnt_scenes = ['Barn', 'Caterpillar', 'Courthouse', 'Ignatius', 'Meetingroom', 'Truck']

# train
cmd_lis=[]
# for scene in dtu_scenes:
#     cmd_lis.append(f'python train.py -s ../../Data/DTU/{scene} -m ../exps/full/DTU/{scene} -r 2 --depth_ratio 1')

# render images,  extract and eval meshes
cmd_lis.append('python scripts/tnt_eval.py --TNT_data ../../Data/TNT --TNT_GT ../../Data/Official_TNT_dataset --output_path ../exps/wo_depthdist/TNT --skip_training --skip_rendering')

# eval nvs
# for scene in tnt_scenes:
#     cmd_lis.append(f'python metrics.py -m ../exps/full/TNT/{scene} -f train')
#     cmd_lis.append(f'python metrics.py -m ../exps/full/TNT/{scene} -f test')
#     cmd_lis.append(f'python vis_outputs.py -m ../exps/full/TNT/{scene} -f train test')

# run cmd
for cmd in cmd_lis:
    os.system(cmd)
