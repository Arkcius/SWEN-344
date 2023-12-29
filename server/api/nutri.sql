DROP table if EXISTS food CASCADE;

CREATE TABLE food (
    id          SERIAL PRIMARY KEY NOT NULL,
    name        VARCHAR(30),
    category    VARCHAR(30),
    calories    VARCHAR(10),
    totalFat   VARCHAR(10),
    saturatedFat     VARCHAR(10),
    transFat   VARCHAR(10),
    protein     VARCHAR(10),
    carbohydrate VARCHAR(10)
);