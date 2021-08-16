# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class PicturescrapyPipeline:
    def process_item(self, item, spider):
        return item

class ImagespiderPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        # 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
        name='_'.join(request.url.split('/')[-3:])
        name=name.replace(':','')
        image_guid = name  # 提取url前面名称作为图片名。
        return image_guid