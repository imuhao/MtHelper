import base64
from io import BytesIO
import io
import random
import string
from PyQt6 import QtCore
from PyQt6.QtCore import QRunnable
import debugpy
import requests
from PIL import Image
from utils import cookie_util
#根据skuid 查询商品信息
class ImageWatermarkWorkSignals(QtCore.QObject):
    finished = QtCore.pyqtSignal(int,bool,str)

class ImageWatermarkWork(QRunnable):

    def __init__(self,cookie,skuid,index,watermarkPath):
        super().__init__()
        self.signals = ImageWatermarkWorkSignals()
        self.cookie = cookie
        self.skuid =skuid
        self.index = index
        self.watermarkPath = watermarkPath

    def run(self):
        # debugpy.debug_this_thread()
        # 模拟接口请求数据
        data = self.imageWatermark()
        if data == None:
            return
        self.signals.finished.emit(data)

    def imageWatermark(self):
        try:
            url = "https://yiyao.meituan.com/reuse/health/product/retail/r/searchListPageV2?yodaReady=h5"
            headers = {
                "Connection": "keep-alive",
                "Content-Type": "application/x-www-form-urlencoded; Charset=UTF-8",
                "Accept": "*/*",
                "Accept-Language": "zh-cn",
                "Referer": "https://yiyao.meituan.com/reuse/health/product/retail/r/searchListPageV2?yodaReady=h5",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36",
                "Content-Length": "341",
                "Host": "yiyao.meituan.com",
                'Cookie':self.cookie
                }
        
            data = {
                "wmPoiId": cookie_util.get_mt_cookie_wmPoiId(self.cookie),
                "pageNum": "1",
                "pageSize": "20",
                "needTag": "1",
                "name": "",
                "brandId": "0",
                "tagId": "0",
                "searchWord": self.skuid,
                "state": "0",
                "sortType": "",
                "sortKey": "",
                "saleStatus": "-1",
                "limitSale": "-1",
                "needCombinationSpu": "-1",
                "noStockAutoClear": "-1",
                "problemType": "1",
                "noSingleDeliveryType": "0",
                "keyword": self.skuid,
                "marketingPicture": "",
                "shippingTime": "",
                "stockClearedByZeroStock": "",
                "highlyRecommended": "",
                "searchWordType": "3"
            }

            response = requests.post(url, headers=headers, data=data)
            responseJson =response.json()
            data = responseJson["data"]
            productList = data["productList"]
            productData = productList[0]

            self.pictures = productData["pictures"]

            self.spuId = productData["id"]

            first_picture = self.pictures[0]

            base_image  = self.get_image_from_url(first_picture)
            # 添加水印
            watermarked_image = self.add_watermark_to_image(base_image, self.watermarkPath, position=(0, 0))  # 你可以调整水印的位置
            watermarked_image.save('watermarked_image.jpg')
            self.upload_image(watermarked_image)
        except Exception  as e:
            self.signals.finished.emit(self.index,False,str(e))


    def upload_image(self,image):
        try:
            url = 'https://yiyao.meituan.com/reuse/health/product/uploadTool/w/uploadImg?yodaReady=h5&csecplatform=4&csecversion=2.4.0&mtgsig=%7B%22a1%22%3A%221.1%22%2C%22a2%22%3A1720168115437%2C%22a3%22%3A%22z359yyu748xy5v7v0v19867z81x03z7881u768v22x297958091y48u2%22%2C%22a5%22%3A%22bZXNLmUNueR5kaO8ZbMbuiuYSQ60FNQQ5c%3D%3D%22%2C%22a6%22%3A%22hs1.4aOG4x69iuIGtADfqn9IKcQfrmrTOdjRUviuzUITmHHr9733NITpclGhHjJlKIfo%2B1VtST2HjRmUqOKRpkHvlXg%3D%3D%22%2C%22x0%22%3A4%2C%22d1%22%3A%2247afdd7cf4a5ea848816c033b30a37e3%22%7D'
            headers = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': self.cookie,
                'M-APPKEY': 'fe_com.sankuai.yiyao.eproduct.manager',
                'M-TRACEID': '-1666363599215271936',
                'Origin': 'https://yiyao.meituan.com',
                'Referer': 'https://yiyao.meituan.com/page/product/detail/product/15018166450/edit?spuId=15018166450&queryFrom=0&wmPoiId=21404632&region_id=1000370100&region_version=1715248801',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
                'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            data = {
                'multipart': self.image_to_base64(image),
                'picName':f"{self.generate_random_hex_string(40)}.png",
                'submissionKey':"8d57a8cd-f64f-4eb9-9b9e-bf95fbdc4856"
            }
            
            response = requests.post(url=url, data=data,headers=headers)
            responseJson = response.json()
            code = responseJson["code"]
            if code != 0:
                return
            image_url = responseJson["data"]["url"]

            self.setup_goddess_first_pic(image_url)

        except Exception  as e:
            self.signals.finished.emit(self.index,False,str(e))

    def setup_goddess_first_pic(self,image_url):
        try :
            url = "https://yiyao.meituan.com/reuse/health/product/retail/w/picture?yodaReady=h5"
            headers = {
                "Connection": "keep-alive",
                "Content-Type": "application/x-www-form-urlencoded; Charset=UTF-8",
                "Accept": "*/*",
                "Accept-Language": "zh-cn",
                "Referer": "https://yiyao.meituan.com/reuse/health/product/retail/w/picture?yodaReady=h5",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36",
                "Content-Length": "427",
                "Host": "yiyao.meituan.com",
                'Cookie':self.cookie
            }
            
            
            data = {
                "wmPoiId": cookie_util.get_mt_cookie_wmPoiId(self.cookie),
                "spuId": self.spuId,
                "pictures[0]": image_url,
            }

            for index, value in enumerate(self.pictures):
                if index == 0:
                    continue
                data[f"pictures[{index}]"] = value
            
            response = requests.post(url, headers=headers, data=data)
            responseJson = response.json()

            print(responseJson)

            if responseJson["code"] ==0:
                self.signals.finished.emit(self.index,True,str("修改成功"))
            else:
                self.signals.finished.emit(self.index,False,str(responseJson))
            
        except Exception  as e:
            self.signals.finished.emit(self.index,False,str(e))


    def generate_random_hex_string(self,length=40):
        hex_digits = string.hexdigits.lower()  # 包含'0123456789abcdef'
        random_string = ''.join(random.choice(hex_digits) for i in range(length))
        return random_string


    #将图片转换为Base64编码
    def image_to_base64(self,image):
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return img_str

    #从网络加载图片
    def get_image_from_url(self,url):
        response = requests.get(url)
        if response.status_code == 200:
            return Image.open(BytesIO(response.content))
        else:
            raise Exception('Image could not be downloaded.')

    #图片添加水印
    def add_watermark_to_image(self,base_image, watermark_image_path, position=(0, 0)):
        watermark = Image.open(watermark_image_path)
        # 调整水印大小
        base_image_width, base_image_height = base_image.size
        # watermark = watermark.resize((int(base_image_width * 0.3), int(base_image_height * 0.3)), Image.ANTIALIAS)
        # 添加水印
        base_image.paste(watermark, position, watermark)
        return base_image

#查看图片信息
#https://yiyao.meituan.com/reuse/health/product/retail/w/picture?yodaReady=h5

