CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p text)
RETURNS TABLE (first_name VARCHAR, phone_number VARCHAR) AS $$
BEGIN 
RETURN QUERY
SELECT c.first_name, c.phone_number
FROM phonebook c 
WHERE c.phone_number LIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;