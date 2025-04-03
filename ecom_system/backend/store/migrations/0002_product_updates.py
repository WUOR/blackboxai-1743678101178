from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='main_image',
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
        ),
    ]