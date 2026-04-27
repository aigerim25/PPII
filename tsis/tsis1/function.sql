    CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
    RETURNS TABLE (
        contact_name VARCHAR,
        email VARCHAR,
        phone VARCHAR,
        phone_type VARCHAR
    )
    LANGUAGE plpgsql
    AS $$
    BEGIN 
    RETURN QUERY 
    SELECT c.name, c.email, p.phone, p.type
    FROM contacts c
    LEFT JOIN phones p ON c.id = p.contacts_id
    WHERE c.name ILIKE '%' || p_query || '%'
    OR c.emial ILIKE '%' || p_query || '%'
    OR p.phone ILIKE '%' || p_query || '%';
    END;
    $$;