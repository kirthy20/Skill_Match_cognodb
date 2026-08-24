import os

from dotenv import load_dotenv
from neo4j import GraphDatabase


load_dotenv()

COGNODB_URI = os.getenv("COGNODB_URI")
COGNODB_USERNAME = os.getenv("COGNODB_USERNAME")
COGNODB_PASSWORD = os.getenv("COGNODB_PASSWORD")


driver = GraphDatabase.driver(
    COGNODB_URI,
    auth=(COGNODB_USERNAME, COGNODB_PASSWORD)
)


def test_connection():
    with driver.session() as session:
        result = session.run(
            "RETURN 'CognoDB connection successful!' AS message"
        )

        return result.single()["message"]