from easydict import EasyDict as edict

cfg = edict()
cfg.CONFIG = '/home/grace_team/HKUST_GRACE/SocialTaskImplementation/visual_perception_manager/AlphaPose/detector/yolo/cfg/yolov3-spp.cfg'
cfg.WEIGHTS = '/home/grace_team/HKUST_GRACE/SocialTaskImplementation/visual_perception_manager/AlphaPose/detector/yolo/data/yolov3-spp.weights'
cfg.INP_DIM =  608
cfg.NMS_THRES =  0.6
cfg.CONFIDENCE = 0.1
cfg.NUM_CLASSES = 80
