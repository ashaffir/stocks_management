# Generated by Django 3.0.2 on 2021-09-14 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kadima', '0018_auto_20200127_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HistoryStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_index', models.IntegerField()),
                ('ticker', models.CharField(max_length=100)),
                ('stock_price', models.FloatField(default=0, null=True)),
                ('week_1', models.FloatField(blank=True, null=True)),
                ('week_1_color', models.CharField(blank=True, max_length=100)),
                ('week_2', models.FloatField(blank=True, null=True)),
                ('week_2_color', models.CharField(blank=True, max_length=100)),
                ('week_3', models.FloatField(blank=True, null=True)),
                ('week_3_color', models.CharField(blank=True, max_length=100)),
                ('week_5', models.FloatField(blank=True, null=True)),
                ('week_5_color', models.CharField(blank=True, max_length=100)),
                ('gap_1', models.FloatField(blank=True, null=True)),
                ('gap_1_color', models.CharField(blank=True, max_length=100)),
                ('earnings_call_displayed', models.CharField(blank=True, max_length=100, null=True)),
                ('sold_date', models.DateTimeField(blank=True, null=True)),
                ('time_added', models.DateTimeField(auto_now=True)),
                ('stocks_bought', models.FloatField(default=0, null=True)),
                ('purchase_price', models.FloatField(default=0.0, null=True)),
                ('stocks_sold', models.FloatField(default=0, null=True)),
                ('selling_price', models.FloatField(default=0.0, null=True)),
                ('profit', models.FloatField(default=0.0, null=True)),
                ('dividends', models.FloatField(default=0.0, null=True)),
                ('total_profit', models.FloatField(default=0.0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndicesData',
            fields=[
                ('index_symbol', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('sample_date', models.DateTimeField(auto_now=True)),
                ('index_prev_close', models.FloatField(blank=True, null=True)),
                ('index_current_value', models.FloatField(blank=True, null=True)),
                ('index_api_id', models.IntegerField(null=True)),
                ('index_change', models.FloatField(blank=True, null=True)),
                ('index_week1', models.FloatField(blank=True, null=True)),
                ('index_week1_min', models.FloatField(blank=True, null=True)),
                ('index_week1_max', models.FloatField(blank=True, null=True)),
                ('index_week2', models.FloatField(blank=True, null=True)),
                ('index_week2_min', models.FloatField(blank=True, null=True)),
                ('index_week2_max', models.FloatField(blank=True, null=True)),
                ('index_week3', models.FloatField(blank=True, null=True)),
                ('index_week3_min', models.FloatField(blank=True, null=True)),
                ('index_week3_max', models.FloatField(blank=True, null=True)),
                ('index_week_1_color', models.CharField(blank=True, max_length=100)),
                ('index_week_2_color', models.CharField(blank=True, max_length=100)),
                ('index_week_3_color', models.CharField(blank=True, max_length=100)),
                ('index_trend', models.FloatField(blank=True, null=True)),
                ('index_macd', models.FloatField(blank=True, null=True)),
                ('index_macd_clash', models.BooleanField(blank=True, default=False, null=True)),
                ('index_macd_color', models.CharField(blank=True, max_length=50, null=True)),
                ('index_mfi', models.FloatField(blank=True, null=True)),
                ('index_mfi_clash', models.BooleanField(blank=True, default=False, null=True)),
                ('index_mfi_color', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='stockdata',
            name='dividend',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='dividend_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='dividend_warning',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='macd_14_clash',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='macd_14_color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='macd_30_clash',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='macd_30_color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='macd_trend_14',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='macd_trend_30',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='mfi_14_clash',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='mfi_14_color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='mfi_30_clash',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='mfi_30_color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='money_flow_trend_14',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='money_flow_trend_30',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='prev_close',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='rsi',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockdata',
            name='rsi_color',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='sample_period_14',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='sold_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_10',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_10_color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_1_color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_2_color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_3_color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_4_color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_5_color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_6',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_6_color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_7',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_7_color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_8',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_8_color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_9',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_9_color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_delta',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_sound_on_off',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_alarm_trigger_set',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_current_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_email_alert',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_initial_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_load_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_price_down_alarm',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_price_up_alarm',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_trend_14',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock_trend_30',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='todays_open',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='updading_gap_1_flag',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='week_1_max',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='week_1_min',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='week_2_max',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='week_2_min',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='week_3_max',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='week_3_min',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='week_5_max',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='week_5_min',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='dividends',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='earnings_call',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='earnings_call_displayed',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='earnings_warning',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='gap_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='gap_1_color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='gap_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='gap_2_color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='gap_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='gap_3_color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='profit',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='purchase_price',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='selling_price',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='stock_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='stock_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='stocks_bought',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='stocks_sold',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='total_profit',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='week_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='week_1_color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='week_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='week_2_color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='week_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='week_3_color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='week_5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='week_5_color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='stockdata',
            unique_together={('ticker', 'table_index')},
        ),
        migrations.RemoveField(
            model_name='stockdata',
            name='macd_clash',
        ),
        migrations.RemoveField(
            model_name='stockdata',
            name='macd_color',
        ),
        migrations.RemoveField(
            model_name='stockdata',
            name='macd_trend',
        ),
        migrations.RemoveField(
            model_name='stockdata',
            name='mfi_clash',
        ),
        migrations.RemoveField(
            model_name='stockdata',
            name='mfi_color',
        ),
        migrations.RemoveField(
            model_name='stockdata',
            name='money_flow_trend',
        ),
        migrations.RemoveField(
            model_name='stockdata',
            name='stock_trend',
        ),
    ]
