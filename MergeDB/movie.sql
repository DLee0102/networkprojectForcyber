CREATE TABLE "actors" (
  "IMDb" text NOT NULL,
  "actor_name" text NOT NULL,
  PRIMARY KEY ("IMDb", "actor_name"),
  CONSTRAINT "fk_actors_basic_1" FOREIGN KEY ("IMDb") REFERENCES "basic" ("IMDb") ON DELETE CASCADE
);

CREATE TABLE "editors" (
  "IMDb" text NOT NULL,
  "editor_name" text NOT NULL,
  PRIMARY KEY ("IMDb", "editor_name"),
  CONSTRAINT "fk_editors_basic_1" FOREIGN KEY ("IMDb") REFERENCES "basic" ("IMDb") ON DELETE CASCADE
);

CREATE TABLE "Administrator" (
  "username" text NOT NULL,
  "password" text NOT NULL,
  PRIMARY KEY ("username")
);

CREATE TABLE "basic" (
  "IMDb" text NOT NULL,
  "cname" text NOT NULL,
  "fname" text,
  "pic_link" text NOT NULL,
  "director" text NOT NULL,
  "classes" text NOT NULL,
  "location" text NOT NULL,
  "language" text NOT NULL,
  "uptime" text NOT NULL,
  "length" integer NOT NULL,
  "other_name" text NOT NULL,
  "score" real NOT NULL,
  "rated" integer NOT NULL,
  "instruction" text NOT NULL,
  "comments_count" integer NOT NULL,
  "reviews_count" integer NOT NULL,
  PRIMARY KEY ("IMDb")
);

CREATE TABLE "comments" (
  "IMDb" text NOT NULL,
  "nickname" text NOT NULL,
  "commenttime" text NOT NULL,
  "content" text NOT NULL,
  "count_useful" text NOT NULL,
  PRIMARY KEY ("IMDb", "nickname", "commenttime", "content", "count_useful"),
  CONSTRAINT "fk_comments_basic_1" FOREIGN KEY ("IMDb") REFERENCES "basic" ("IMDb") ON DELETE CASCADE
);

CREATE TABLE "reviews" (
  "IMDb" text NOT NULL,
  "nickname" text NOT NULL,
  "commenttime" text NOT NULL,
  "content" text NOT NULL,
  "count_useful" text NOT NULL,
  "count_useless" text NOT NULL,
  "count_response" text NOT NULL,
  PRIMARY KEY ("IMDb", "nickname", "commenttime", "content", "count_useful", "count_useless", "count_response"),
  CONSTRAINT "fk_reviews_basic_1" FOREIGN KEY ("IMDb") REFERENCES "basic" ("IMDb") ON DELETE CASCADE
);



