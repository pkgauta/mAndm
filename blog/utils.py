from .models import BLOG_POST_STATUS, BLOG_IMAGE_STATUS, BLOG_POST_CATEGORY

model_referential_dict = {
    "add-post": {"blog_status": BLOG_POST_STATUS, "blog_image": BLOG_IMAGE_STATUS,
    "blog_category": BLOG_POST_CATEGORY}
}

def get_choices_for_pages(page=None):
    return model_referential_dict[page]
