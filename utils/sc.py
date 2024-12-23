from init import *


def export_tweets(savePath):
    resource = []
    for file_dir in os.listdir(project_root_directory / 'query'):
        try:
            with open(project_root_directory / 'query/' / file_dir) as f:
                data = json.load(f)
                instructions = data["data"]["search_by_raw_query"]["search_timeline"]["timeline"]["instructions"]
                for instruction in instructions:
                    if instruction["type"] == "TimelineAddEntries":
                        entries = instruction["entries"]
                        for entry in entries:
                            try:
                                if entry["entryId"].startswith("tweet-"):
                                    media_list = []
                                    result = entry["content"]["itemContent"]["tweet_results"]["result"]
                                    core = result.get("core", None)
                                    if core == None:
                                        core = result.get("tweet").get("core", None)
                                    name = core.get("user_results").get("result").get("legacy").get("name")
                                    location = core.get("user_results").get("result").get("legacy").get("location")
                                    rest_id = core.get("user_results").get("result").get("rest_id")
                                    followers_count = core.get("user_results").get("result").get("legacy").get(
                                        "followers_count")
                                    friends_count = core.get("user_results").get("result").get("legacy").get(
                                        "friends_count")
                                    account_created_at = core.get("user_results").get("result").get("legacy").get(
                                        "created_at")
                                    description = core.get("user_results").get("result").get("legacy").get(
                                        "description")
                                    profile_url = core.get("user_results").get("result").get("legacy").get("url")

                                    legacy = result.get("legacy", None)
                                    if legacy == None:
                                        legacy = result.get("tweet").get("legacy", None)
                                    created_at = legacy["created_at"]
                                    content = legacy["full_text"]
                                    favorite_count = legacy["favorite_count"]
                                    retweet_count = legacy["retweet_count"]
                                    reply_count = legacy["reply_count"]
                                    screen_name = core["user_results"]["result"]["legacy"]["screen_name"]
                                    id_str = legacy["id_str"]
                                    is_quote_status = legacy["is_quote_status"]
                                    is_video = False
                                    is_photo = False
                                    medias = legacy.get("extended_entities", {}).get("media", [])

                                    for i, media in enumerate(medias):
                                        if media.get("type") == "video":
                                            variants = media.get("video_info", {}).get("variants", [])
                                            media_list.append(variants[-1]["url"])
                                            is_video = True
                                        elif media.get("type") == "photo":
                                            media_list.append(media["media_url_https"])
                                            is_photo = True
                                        elif media.get("type") == "animated_gif":
                                            media_list.append(media["media_url_https"])
                                    media_type = "video" if is_video else "photo" if is_photo else "text"
                                    resource.append({
                                        "name": name,
                                        # "rest_id": rest_id,
                                        # "followers_count": followers_count,
                                        # "friends_count": friends_count,
                                        # "account_created_at": account_created_at,
                                        # "description": description,
                                        # "profile_url": profile_url,
                                        "content": content,
                                        "media": media_list,
                                        "type":media_type,
                                        "resource_id":id_str,

                                        "favorite_count": favorite_count,
                                        "retweet_count": retweet_count,
                                        "reply_count": reply_count,
                                        # "url": f"https://twitter.com/{screen_name}/status/{id_str}",
                                        "created_at": created_at,
                                        # "location": location,
                                        # "is_quote_status": is_quote_status,
                                        # "is_video": is_video,
                                        # "is_photo": is_photo

                                    }
                                    )
                            except Exception as e:
                                logger.error(f"Error occurred while processing tweet: {e}")
        except Exception as e:
            logger.error(f"Error occurred while processing file {file_dir}: {e}")

    with open(project_root_directory / savePath, "w", encoding="utf-8") as t:
        json.dump(resource, t, ensure_ascii=False, indent=4)


def export_comments(savePath):
    resource = []
    for file_dir in os.listdir(project_root_directory / "query"):
        if file_dir.endswith(".json"):
            with open(project_root_directory / "query" / file_dir, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    for i in data["data"]["threaded_conversation_with_injections_v2"]["instructions"][0]["entries"]:
                        if i["entryId"].startswith("conversationthread-"):
                            item = i["content"]["items"][0]
                            screen_name = \
                            item["item"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"][
                                "legacy"]["screen_name"]
                            location = \
                            item["item"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"][
                                "legacy"]["location"]
                            rest_id = \
                            item["item"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"][
                                "rest_id"]
                            description = \
                            item["item"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"][
                                "legacy"]["description"]
                            favourites_count = \
                            item["item"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"][
                                "legacy"]["favourites_count"]
                            followers_count = \
                            item["item"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"][
                                "legacy"]["followers_count"]
                            friends_count = \
                            item["item"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"][
                                "legacy"]["friends_count"]
                            #                         /data/threaded_conversation_with_injections_v2/instructions/0/entries/0/content/items/0/item/itemContent/tweet_results/result/legacy/full_text
                            full_text = item["item"]["itemContent"]["tweet_results"]["result"]["legacy"]["full_text"]
                            quote_count = item["item"]["itemContent"]["tweet_results"]["result"]["legacy"][
                                "quote_count"]
                            reply_count = item["item"]["itemContent"]["tweet_results"]["result"]["legacy"][
                                "reply_count"]
                            retweet_count = item["item"]["itemContent"]["tweet_results"]["result"]["legacy"][
                                "retweet_count"]
                            created_at = item["item"]["itemContent"]["tweet_results"]["result"]["legacy"]["created_at"]
                            #
                            id_str = item["item"]["itemContent"]["tweet_results"]["result"]["legacy"]["id_str"]
                            resource.append({
                                "screen_name": screen_name,
                                "location": location,
                                "created_at": created_at,
                                "full_text": full_text,
                                "rest_id": rest_id,
                                "description": description,
                                "favourites_count": favourites_count,
                                "followers_count": followers_count,
                                "friends_count": friends_count,
                                "quote_count": quote_count,
                                "reply_count": reply_count,
                                "retweet_count": retweet_count,
                                "id_str": id_str

                            })
                except Exception as e:
                    print(e)

    with open(savePath, 'w', encoding='utf-8') as f:
        json.dump(resource, f, ensure_ascii=False, indent=4)

