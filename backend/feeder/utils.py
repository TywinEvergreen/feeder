
def delete_related_files(obj):
    for field in obj._meta.get_fields():
        if field.__class__.__name__ in ['FileField', 'ImageField']:
            getattr(obj, field.name).delete()
