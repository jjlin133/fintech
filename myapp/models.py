from django.db import models

class users(models.Model):
    uid = models.CharField(max_length=50, null=False)
    question = models.CharField(max_length=250, null=False)
    
    def __str__(self):
        return self.uid

# 連結至 db.sqlite3 之資料表 myapp_ntuhqna
class ntuhqna(models.Model):
    title = models.CharField(max_length=50,null=False)
    que = models.CharField(max_length=180,null=False)
    ans = models.CharField(max_length=250,null=False)
    
    def _str_(self):
        return self.qid
