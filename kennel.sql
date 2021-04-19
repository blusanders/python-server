SELECT
            e.id,
            e.name,
            e.address,
            e.location_id,
            l.name
        FROM employee e
        JOIN location l on l.id = e.location_id