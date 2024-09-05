#########################
#--- train and eval ----#
#########################

python train.py -s <path to dataset>
# --lambda_normal  # hyperparameter for normal consistency
# --lambda_dist # hyperparameter for depth distortion
# --depth_ratio # 0 for mean depth and 1 for median depth, 0 works for most cases (unbounded scense), 1 works for bounded scenes

# render images and (un)bounded TSDF fusion
python render.py -m <path to pre-trained model> -s <path to COLMAP dataset> 
--depth_ratio # 0 for mean depth and 1 for median depth
--depth_trunc # depth truncation for bounded TSDF fusion
--voxel_size # voxel size for bounded TSDF fusion
--unbounded # flag for unbounded TSDF fusion
--mesh_res # mesh resolution for unbounded TSDF fusion, for bounded TSDF fusion, it is set to voxel_size (if exists)

# evaluation
python scripts/mipnerf_eval.py -m60 <path to the MipNeRF360 dataset>
python scripts/dtu_eval.py --dtu <path to the preprocessed DTU dataset> --DTU_Official <path to the official DTU dataset>
python scripts/tnt_eval.py --TNT_data <path to the preprocessed TNT dataset> --TNT_GT <path to the official TNT evaluation dataset>

# +++++++++ DTU +++++++++ # 
# scan24, scan37, scan40, scan55, scan63, scan65, scan69, scan83, 
# scan97, scan105, scan106, scan110, scan114, scan118, scan122

python train.py -s ../../Data/DTU/scan24 -m ../exps/full/DTU/scan24 -r 2 --depth_ratio 1
# python render.py -s ../../Data/DTU/scan24 -m ../exps/full/DTU/scan24 -r 2 --depth_ratio 1

python scripts/dtu_eval.py --dtu ../../Data/DTU --output_path ../exps/full/DTU --DTU_Official ../../Data/Offical_DTU_Dataset --skip_training
python metrics.py -m ../exps/full/DTU/scan24 -f train


# +++++++++ TNT +++++++++ # 
# Barn, Caterpillar, Courthouse, Ignatius, Meetingroom, Truck
python train.py -s ../../Data/TNT/Barn -m ../exps/full/TNT/Barn -r 2 --depth_ratio 1
# python render.py -s ../../Data/TNT/Barn -m ../exps/full/TNT/Barn -r 2 --depth_ratio 1

python scripts/tnt_eval.py --TNT_data ../../Data/TNT --TNT_GT ../../Data/Official_TNT_dataset --output_path ../exps/full/TNT --skip_training
python metrics.py -m ../exps/full/TNT/Barn -f train
python metrics.py -m ../exps/full/TNT/Barn -f test