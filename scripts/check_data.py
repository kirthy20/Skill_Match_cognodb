from recommendations.database import driver


def check_data():
    query = """
    MATCH (n)
    RETURN labels(n) AS labels, n
    ORDER BY labels(n)
    """

    with driver.session() as session:
        result = session.run(query)

        for record in result:
            print(record["labels"], record["n"])


if __name__ == "__main__":
    check_data()