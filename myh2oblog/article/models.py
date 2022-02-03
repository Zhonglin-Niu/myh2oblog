from django.db import models


class Tags(models.Model):
    title = models.CharField(max_length=16, verbose_name='标签名字')
    created = models.DateTimeField(verbose_name='创建日期', auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '文章标签'


class Categories(models.Model):
    title = models.CharField(max_length=16, verbose_name='分类名字')
    created = models.DateTimeField(verbose_name='创建日期', auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '文章分类'


def set_default_category():
    return '1'


class Articles(models.Model):
    title = models.CharField(verbose_name='文章标题', max_length=32)
    description = models.CharField(verbose_name='文章简介', max_length=128, null=True, blank=True)
    content = models.TextField(verbose_name='文章内容')
    created = models.DateTimeField(verbose_name='文章发布日期', auto_now_add=True, null=True)
    cover = models.URLField(max_length=300, verbose_name='封面图链接', default="https://pic.myh2o.top/defaultCover")
    category = models.ForeignKey(to='Categories', verbose_name="文章分类", blank=True, on_delete=models.SET_DEFAULT,
                                 default=set_default_category)
    tag = models.ManyToManyField(to='Tags', verbose_name='文章标签', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '文章'
