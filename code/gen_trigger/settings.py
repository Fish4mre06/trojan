caffe_root = "/usr/local/bin/caffe" #/usr/local/bin/caffe
model_path = "/Users/jamesmccoy/Documents/Github/TrojanNN/models/face/vgg_face_caffe/VGG_FACE.caffemodel"    #"/path/to/VGG_FACE.caffemodel"
# add  'force_backward: true' in the prototxt file otherwise the caffe does not do backward computation and gradient is 0
model_definition   = "/Users/jamesmccoy/Documents/Github/TrojanNN/models/face/vgg_face_caffe/VGG_FACE_deploy.prototxt" #'/path/to/VGG_FACE_deploy.prototxt'
gpu = False
