import datetime

from django.utils import timezone
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length = 300)
    pub_date = models.DateTimeField('date published')
    ans1_text = models.CharField(max_length = 80, default= "Yes")
    ans1_votes = models.IntegerField(default = 0)
    ans2_text = models.CharField(max_length = 80, default = "No")
    ans2_votes = models.IntegerField(default = 0)
    votes = models.IntegerField(default = 0)
    def __unicode__(self):
        return self.question_text
        
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
    def vote(self, ans_num):
        if(int(ans_num) == 0): 
            self.ans1_votes += 1    
        else: 
            self.ans2_votes += 1
        self.votes = self.ans1_votes + self.ans2_votes
