from django.db import models

# Create your models here.


# 自定义objects
class TbBaseManager(models.Manager):
    def all(self):
        return super().all().filter(is_active=1)


class TbUiElementInfoManager(TbBaseManager):
    def get_elm_by_id(self, elm_id):
        return self.get(id=elm_id)

    def get_elms_by_page(self, page_name):
        return self.all().filter(page=page_name).order_by('id')

    def get_elms_by_component(self, component_name, page_name):
        return self.get_elms_by_page(page_name).filter(component=component_name).order_by('id')

    def delete_elms_by_id(self, id):
        return self.get_elm_by_id(id).delete()


class TbUiElementInfo(models.Model):
    """以上的类名代表了数据库表名，且继承了models.Model，类里面的字段代表数据表中的字段(name)，
    数据类型则由CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度。"""
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False, blank=False)
    page = models.CharField(max_length=128, null=False, blank=False)
    component = models.CharField(max_length=128, null=False, blank=False)
    find_by = models.CharField(max_length=128, null=False, blank=False)
    value = models.CharField(max_length=128, null=False, blank=False)
    parent_find_by = models.CharField(max_length=128, blank=True, null=True)
    parent_value = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=50)
    is_active = models.IntegerField(blank=True, null=True, db_column='isactive')
    insert_time = models.DateTimeField(auto_now_add=True, db_column='inserttime')
    update_time = models.DateTimeField(auto_now=True, db_column='updatetime')
    objects = TbUiElementInfoManager()

    """Meta 加入元信息 
    db_table 指定表名"""

    class Meta:
        managed = False
        db_table = 'tb_ui_element_info'





