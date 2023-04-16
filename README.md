## Object Detection in Drone Dataset (Official Code in AI-Hub)

<p align="center">
  We released the dataset and utilization guide video on <a href='https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100'>AI-Hub</a>.
</p>

🎁 <a href='https://github.com/AICT-CVAI/Object-Detection-Drone'>Full Version(Yolov5, mmdetection)</a>

### My Environment
- OS : Ubuntu 18.04.5
- GPU : NVIDIA RTX 2070 super
- CUDA : 10.2

### Reference
- <a href='https://github.com/ultralytics/yolov5'>yolov5</a>

- <a href='https://github.com/open-mmlab/mmdetection'>mmdetection</a>



### weight file

- yolov5 : weights/drone_survivor.pt 🥇
- cascade rcnn : https://drive.google.com/file/d/1mXANwNMbQU7tmmmhZ81dFaIRvXU6rDQL/view?usp=sharing
- faster rcnn : https://drive.google.com/file/d/1mXANwNMbQU7tmmmhZ81dFaIRvXU6rDQL/view?usp=sharing
- retina net : https://drive.google.com/file/d/1mXANwNMbQU7tmmmhZ81dFaIRvXU6rDQL/view?usp=sharing


### How to do?

```
$ git clone https://github.com/winston1214/Object_Detection_Drone && cd Object_Detection_Drone
```
```
$ pip install -r requirements.txt
```
```
$ python3 ui2.py
```

### More Details

**Setting of input or output video location**

 Change <a href='https://github.com/winston1214/Object_Detection_Drone/blob/be4c2cf414967539286af7a284015500cf57946f/ui2.py#L63'>this part</a>
  - Input Video location : Change 'source' option :   ex. data/test.MP4 -> sample_dir/Sample.MP4
  - Output Video location : Change 'project' option :   ex. ui_test/ -> save_dir/

If you want to adjust the other options, you should refer <a href='https://github.com/winston1214/Object_Detection_Drone/blob/be4c2cf414967539286af7a284015500cf57946f/detect.py#L154'>here</a>

### Output

- **Detection Results**

<img src='https://user-images.githubusercontent.com/47775179/111962407-9a1c3700-8b35-11eb-9ed4-a3bdb1f0abb6.png'></src>


- **UI structure**

<img src='https://user-images.githubusercontent.com/47775179/111962311-82dd4980-8b35-11eb-9487-14093fe78982.png'></img>


