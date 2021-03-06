## Cloud Vision 電腦視覺實戰
##
* [Google Cloud Vision AI](https://cloud.google.com/vision/?hl=zh_TW#header_3)
* [Cloud AutoML Vision: AutoML Vision API Tutorial](https://cloud.google.com/vision/automl/docs/tutorial)
* [AutoML vision AI Tutorial 指令整理](https://github.com/jumbokh/gcp_class/blob/master/VISION/AutoML-Vision-API-Tutorial.md)
* [視覺辨識課程講義](https://github.com/jumbokh/gcp_class/blob/master/VISION/%E8%A6%96%E8%A6%BA%E8%BE%A8%E8%AD%98%E8%AA%B2%E7%A8%8B.pptx)
* [維基百科: 萊娜圖（Lenna）](https://zh.wikipedia.org/wiki/%E8%90%8A%E5%A8%9C%E5%9C%96)
* [自動下載影像圖、標示及辨識](https://github.com/jumbokh/cv_face/tree/master/opencv/day3)
* [深度學習-什麼是one stage，什麼是two stage 物件偵測](https://medium.com/@chih.sheng.huang821/%E6%B7%B1%E5%BA%A6%E5%AD%B8%E7%BF%92-%E4%BB%80%E9%BA%BC%E6%98%AFone-stage-%E4%BB%80%E9%BA%BC%E6%98%AFtwo-stage-%E7%89%A9%E4%BB%B6%E5%81%B5%E6%B8%AC-fc3ce505390f)
* [GITHUB: google-images-download](https://github.com/hardikvasa/google-images-download)

##
### [LAB1: 試用 Cloud vision API](https://cloud.google.com/vision/docs/drag-and-drop?hl=zh-tw)
### [LAB2: Cloud AutoML vision quick start](https://blog.gcp.expert/cloud-automl-vision-quick-start/)
### [LAB3: 一秒辨識屈中恆、宋少卿、鈕承澤：就用 Cloud AutoML Vision！](https://blog.gcp.expert/cloud-automl-vision-application-1/)
* [resources](https://drive.google.com/open?id=1VPpYnA1PKA3jtUEZ3dKF0GOtB2eeHpXa)
#### 抓圖說明:
### 安裝
* [說明](https://openingsource.org/2010/zh-tw/)
<pre>
pip install google_images_download
git clone https://github.com/hardikvasa/google-images-download.git
cd google-images-download 
python setup.py install
</pre>
* googleimagesdownload -k "鈕承澤" -f png -l 20 -o New
* googleimagesdownload -k "屈中恆" -f png -l 20 -o Chu
* googleimagesdownload -k "宋紹卿" -f png -l 20 -o Song
