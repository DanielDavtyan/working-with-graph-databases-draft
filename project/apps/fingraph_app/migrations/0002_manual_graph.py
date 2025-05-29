from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('fingraph_app', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE OR REPLACE PROPERTY GRAPH IF NOT EXISTS Follow
            NODE TABLES (Person)
            EDGE TABLES (
               Follows
                    SOURCE KEY (follower_person_id) REFERENCES Person(id),
                    DESTINATION KEY (followed_person_id) REFERENCES Person(id),
                    EDGE LABEL IsFollowing
            )
            """, reverse_sql='DROP PROPERTY GRAPH IF EXISTS Follow'
        ),
    ]
