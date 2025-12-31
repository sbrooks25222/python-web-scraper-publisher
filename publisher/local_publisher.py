import os


def publish_locally(posts, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)

    for i, post in enumerate(posts, start=1):
        filename = f"post_{i}.html"
        path = os.path.join(output_dir, filename)

        html = f"""
<html>
<head>
    <title>{post['title']}</title>
</head>
<body>
    <h1>{post['title']}</h1>
    {post['content']}
</body>
</html>
"""

        with open(path, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"Created {filename}")
