steps = [
    [
        """
        CREATE TABLE accounts (
            id              SERIAL PRIMARY KEY NOT NULL,
            first_name      VARCHAR(1000) NOT NULL,
            last_name       VARCHAR(100) NOT NULL,
            username        VARCHAR(100) NOT NULL,
            hashed_password VARCHAR(100) NOT NULL,
            email           VARCHAR(100) NOT NULL,
            phone_number    VARCHAR(100) NOT NULL
        );
        """,
        """
        DROP TABLE accounts;
        """,
    ],
    [
        """
        CREATE TABLE gardens (
            gardens_id SERIAL PRIMARY KEY,
            gardens_name VARCHAR(255) NOT NULL,
            description TEXT,
            accounts_id INTEGER REFERENCES accounts(id),
            zip_code INTEGER
        );
        """,
        """
        DROP TABLE garden;
        """,
    ],
    [
        """
        CREATE TABLE plants (
            plants_id SERIAL PRIMARY KEY,
            plants_name VARCHAR(255) NOT NULL,
            planted_date TIMESTAMP,
            description TEXT,
            gardens_id INTEGER REFERENCES gardens(gardens_id)
        );
        """,
        """
        DROP TABLE plants;
        """,
    ],
    [
        """
        CREATE TABLE groups (
            groups_id SERIAL PRIMARY KEY,
            groups_name VARCHAR(255) NOT NULL,
            description TEXT
        );
        """,
        """
        DROP TABLE groups;
        """,
    ],
    [
        """
        CREATE TABLE groups_members (
            groups_id INTEGER REFERENCES groups(groups_id),
            accounts_id INTEGER REFERENCES accounts(id),
            PRIMARY KEY (groups_id, accounts_id)
        );
        """,
        """
        DROP TABLE groups_members;
        """,
    ],
    [
        """
        CREATE TABLE groups_comments (
            comments_id SERIAL PRIMARY KEY,
            content TEXT NOT NULL,
            authors_id INTEGER REFERENCES accounts(id),
            groups_id INTEGER REFERENCES groups(groups_id),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """,
        """
        DROP TABLE groups_comments;
        """,
    ],
    [
        """
        CREATE TABLE blogs (
            blogs_id SERIAL PRIMARY KEY NOT NULL,
            accounts_id INTEGER NOT NULL REFERENCES accounts(id),
            title VARCHAR(255) NOT NULL
        );
        """,
        """
        DROP TABLE blog;
        """,
    ],
    [
        """
        CREATE TABLE blogs_post (
            blogs_post_id SERIAL PRIMARY KEY NOT NULL,
            blogs_id INTEGER NOT NULL REFERENCES blogs(blogs_id),
            title VARCHAR(255) NOT NULL,
            picture_url VARCHAR(1000) NOT NULL,
            text TEXT NOT NULL
        );
        """,
        """
        DROP TABLE blog_post;
        """,
    ],
    [
        """
        CREATE TABLE blogs_post_comment (
            blogs_post_comment_id SERIAL PRIMARY KEY NOT NULL,
            accounts_id INTEGER NOT NULL REFERENCES accounts(id),
            blogs_post_id INTEGER NOT NULL REFERENCES blogs_post(blogs_post_id),
            text TEXT NOT NULL
        );
        """,
        """
        DROP TABLE blog_post_comment;
        """,
    ],
]
