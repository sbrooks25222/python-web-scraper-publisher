import pandas as pd

def format_posts(df):
    posts = []

    for _, row in df.iterrows():
        title = f"Quote by {row['author']}"
        body = f"""
<blockquote>
{row['quote']}
</blockquote>

<p><strong>Author:</strong> {row['author']}</p>
<p><strong>Tags:</strong> {row['tags']}</p>
"""
        posts.append({
            "title": title,
            "content": body,
            "tags": row["tags"]
        })

    return posts
