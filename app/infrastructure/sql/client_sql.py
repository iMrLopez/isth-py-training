class clientSql:
    GET = "SELECT * FROM client WHERE CIF = {}"
    INSERT = "INSERT INTO client (CIF, Name, LastName, Link, age, isAdult) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')"
