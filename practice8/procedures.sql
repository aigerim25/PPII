CREATE OR REPLACE PROCEDURE upsert_contact(p_first_name VARCHAR, p_phone_number VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN 
IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_first_name)
THEN
UPDATE phonebook
SET phone_number = p_phone_number
WHERE first_name = p_first_name;
ELSE 
INSERT INTO phonebook(first_name, phone_number)
VALUES (p_first_name, p_phone_number);
END IF;
END;
$$;