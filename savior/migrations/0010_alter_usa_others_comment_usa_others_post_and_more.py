# Generated by Django 4.2.3 on 2023-08-12 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('savior', '0009_vietnam_others_comment_vietnam_clothes_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usa_others_comment',
            name='usa_others_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='savior.usa_others', verbose_name='미국 잡화 시세 댓글'),
        ),
        migrations.AlterField(
            model_name='vietnam_others_comment',
            name='vietnam_others_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='savior.vietnam_others', verbose_name='베트남 잡화 시세 댓글'),
        ),
    ]
