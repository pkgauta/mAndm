from blog.models import BlogImages


def create_blog_images_object(files):
    obj_id = list(map(lambda s: BlogImages.objects.create(post_image=s), files.getlist("post_image")))
    return obj_id
