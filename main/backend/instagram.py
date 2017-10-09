'''
Module contains class and methods to interact with instagram's API
Each of the classes has quick access attributes such as number of followers, user/media id
'''
import datetime
from pprint import pprint as pp
from datacollection.request_handler import request_handler
import itertools
from collections import Counter
time_fmt = "%c"  # because time is very important define it here.

# create class User
class User(object):
    """ base class to store urls, user_id, user_search_data etc """

    
    def __init__(self, username=None, media_id=None):
        self.username = username
        self.media_id = media_id
        self.media_id_url = "https://api.instagram.com/v1/media/{}?access_token={}".format(self.media_id, access_token) if media_id is not None else None
        if username is not None:
            search_url = "https://api.instagram.com/v1/users/search?q={}&access_token={}".format(username, self.access_token)
            self.user_search_data = request_handler(search_url, "data")[0]  # requests.get(search_url)
            self.user_id = self.user_search_data['id']

            self.user_info_url = "https://api.instagram.com/v1/users/{}/?access_token={}".format(self.user_id, access_token)
            self.recent_media_url = "https://api.instagram.com/v1/users/{}/media/recent/?access_token={}".format(self.user_id, access_token)
            self.followed_by_url = "https://api.instagram.com/v1/users/{}/followed-by/?access_token={}".format(self.user_id, access_token)
            self.user_info_data = request_handler(self.user_info_url, 'data')


# create class Profile
class Profile(User):
    """
    gets profile infomation such as total following and followers
    profile_item= Profile("bryoh_15")
    print(profile_item.followers)
    print(profile_item.following)
    """
    def __init__(self, username):
        User.__init__(self, username)
        self.name = self.user_search_data["full_name"]
        self.bio = self.user_search_data["bio"]
        self.id = self.user_id
        self.profile_picture_link = self.user_search_data["profile_picture"]
        self.website = self.user_search_data["website"]
        self.counts = self.user_info_data["counts"]
        self.followers = self.counts["followed_by"]
        self.follows = self.counts["follows"]
        self.media_total = self.counts['media']
        self.media_recent_data = request_handler(self.recent_media_url, 'data')
        self.media_recent_obj_list = [Media(media_data=obj) for obj in self.media_recent_data]
        self.common_tags = list(itertools.chain(*[Media(media_data=obj).tags for obj in self.media_recent_data]))
        self.common_tags_dict = {tag: int(Counter(self.common_tags)[tag]) for
                                 tag in self.common_tags}
    def created_times_fmt(self, time_labels):
        """
        :return a reversed  list of formatted created time, useful for label
        """
        return [datetime.datetime.strptime(obj.created_time, '%c').strftime(time_labels)for obj in self.media_recent_obj_list[::-1]]

    def each_media_obj(self):
        for obj in self.media_recent_obj_list[::-1]:
            yield Media(media_data=obj)

    def reversed_common_tags(self): return list(itertools.chain(*[obj.tags for obj in self.each_media_obj()]))

    def recent_likes_reversed(self): return [obj.likes for obj in self.media_recent_obj_list[::-1]]

    def recent_comment_count(self): return [obj.comments for obj in self.media_recent_obj_list[::-1]]

    def reversed_media_id_urls(self): return [obj.link for obj in self.media_recent_obj_list[::-1]]

    def reversed_tags_s_likes(self):
        ret = {}
        for tag in self.common_tags:
            for media in self.media_recent_obj_list[::-1]:
                if tag in media.tags:
                    old_val = ret.setdefault(tag, 0)
                    ret[tag] = old_val + media.likes
        return ret




# create class Media
class Media(User):
    """
    Gets media info such as date/time, tags, caption,filter, comments count, etc
    Requires the media-id
    """
    def __init__(self, media_id=None, media_data=None):
        if media_id is not None:
            User.__init__(self, media_id=media_id)
            self.media_data = request_handler(self.media_id_url, 'data')
        if media_data is not None:
            self.media_data = media_data
        self.likes = self.media_data["likes"]['count']
        self.attribution = self.media_data["attribution"]
        self.tags = self.media_data["tags"]
        self.images = self.media_data["images"]
        self.comments = self.media_data["comments"]['count']
        self.media_filter = self.media_data["filter"]
        timestamp = self.media_data["created_time"]
        self.created_time = datetime.datetime.fromtimestamp(float(timestamp)).strftime(time_fmt)
        self.link = self.media_data["link"]
        self.location = self.media_data["location"]
        self.user_has_liked = self.media_data["user_has_liked"]
        self.users_in_photo = self.media_data["users_in_photo"]
        self.caption = self.media_data["caption"]  # ['text']
        self.media_type = self.media_data["type"]
        self.media_id = self.media_data["id"]
        self.media_user = self.media_data["user"]



if __name__ == "__main__":
    bryoh = Profile('bryoh_15')
    pp( bryoh.__dict__ )

