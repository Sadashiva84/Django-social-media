from media_app.models import Post, LikePost

'''
argument => <user> 
return => <int?
This function computes the number of likes received by the user
'''

def find_no_of_likes_received_by_user(user):
    post_ids_of_user = user.post.all().values_list('id', flat=True)
    result = LikePost.objects.filter(post_id__in=post_ids_of_user).distinct().count()
    return result
    
    