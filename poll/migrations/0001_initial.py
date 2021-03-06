# Generated by Django 3.0.5 on 2020-04-24 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cases',
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'choices',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000, null=True)),
                ('image_url', models.URLField(max_length=2000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'questions',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True)),
                ('description', models.TextField(null=True)),
                ('image_url', models.URLField(max_length=2000, null=True)),
                ('audio_url', models.URLField(max_length=2000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poll.Case')),
            ],
            options={
                'db_table': 'results',
            },
        ),
        migrations.CreateModel(
            name='Stack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'stacks',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('browser', models.CharField(max_length=100, null=True)),
                ('ip_address', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('result', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poll.Result')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='result',
            name='stack',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poll.Stack'),
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('choice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poll.Choice')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poll.Question')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poll.User')),
            ],
            options={
                'db_table': 'responses',
            },
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poll.Question'),
        ),
        migrations.AddField(
            model_name='choice',
            name='stack',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poll.Stack'),
        ),
    ]
