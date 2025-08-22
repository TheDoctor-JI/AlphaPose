from easydict import EasyDict as edict

cfg = edict()
cfg.CONFIG = '/home/grace_team/HKUST_GRACE/SocialTaskImplementation/visual_perception_manager/AlphaPose/detector/tracker/cfg/yolov3.cfg'
cfg.WEIGHTS = '/home/grace_team/HKUST_GRACE/SocialTaskImplementation/visual_perception_manager/AlphaPose/detector/tracker/data/jde.1088x608.uncertainty.pt'
cfg.IMG_SIZE =  (1088, 608)
cfg.NMS_THRES =  0.6
cfg.CONFIDENCE = 0.4
cfg.BUFFER_SIZE = 30 # frame buffer