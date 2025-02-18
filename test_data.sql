INSERT INTO users (username) VALUES ('john.doe');
INSERT INTO users (username) VALUES ('jane.doe');
INSERT INTO users (username) VALUES ('tommy.doe');

INSERT INTO profiles (biography, users_id) VALUES ('', 1);
INSERT INTO profiles (biography, users_id) VALUES ('', 2);
INSERT INTO profiles (biography, users_id) VALUES ('', 3);

INSERT INTO followers (follower_id, followed_id) VALUES (1, 2); 
INSERT INTO followers (follower_id, followed_id) VALUES (1, 3);
INSERT INTO followers (follower_id, followed_id) VALUES (2, 3);
INSERT INTO followers (follower_id, followed_id) VALUES (3, 1); 


INSERT INTO tasks (label, users_id) VALUES ('Aprender Python y Flask', 1);