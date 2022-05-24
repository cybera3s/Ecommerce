def user_avatar_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'customers/images/avatars/user_{0}/{1}'.format(instance.user.id, filename)