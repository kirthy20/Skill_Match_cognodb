from recommendations.database import driver


def check_relationships():
    query = """
    MATCH (a)-[r]->(b)
    RETURN
        labels(a) AS from_labels,
        a.name AS from_name,
        a.title AS from_title,
        type(r) AS relationship,
        labels(b) AS to_labels,
        b.name AS to_name,
        b.title AS to_title
    """

    with driver.session() as session:
        result = session.run(query)

        for record in result:
            print(
                record["from_labels"],
                record["from_name"] or record["from_title"],
                "--",
                record["relationship"],
                "-->",
                record["to_labels"],
                record["to_name"] or record["to_title"]
            )


if __name__ == "__main__":
    check_relationships()