CREATE OR REPLACE PROCEDURE delete_contact(
    p_first_name VARCHAR,
    p_last_name VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN 
DELETE FROM phonebook
WHERE first_name = p_first_name
AND last_name = p_last_name;
END;
$$;