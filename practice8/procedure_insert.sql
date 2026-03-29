CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_first_name TEXT[],
    p_last_name TEXT[],
    p_phone_number TEXT[],
    INOUT invalid_first_name TEXT[] DEFAULT '{}',
    INOUT invalid_last_name TEXT[] DEFAULT '{}',
    INOUT invalid_phone_number TEXT[] DEFAULT '{}'
)
LANGUAGE plpgsql
AS $$
DECLARE 
i INT;
BEGIN 
IF array_length(p_first_name, 1) IS DISTINCT FROM array_length(p_last_name, 1)
OR array_length(p_first_name, 1) IS DISTINCT FROM array_length(p_phone_number, 1) THEN 
RAISE EXCEPTION 'All arrays must have the same length';
END IF;

FOR i IN 1 .. array_length(p_first_name, 1) LOOP
IF p_phone_number[i] ~ '^\+7[0-9]{10}$' THEN
INSERT INTO phonebook(first_name, last_name, phone_number)
VALUES (p_first_name[i], p_last_name[i], p_phone_number[i]);
ELSE 
invalid_first_name := array_append(invalid_first_name, p_first_name[i]);
invalid_last_name := array_append(invalid_last_name, p_last_name[i]);
invalid_phone_number := array_append(invalid_phone_number, p_phone_number[i]);
END IF;
END LOOP;
END;
$$;