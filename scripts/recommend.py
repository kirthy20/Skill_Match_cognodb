from recommendations.database import driver


def get_recommendations():

    query = """
    MATCH (candidate:Candidate {name: 'Keerthi'})
          -[:HAS_SKILL]->(skill:Skill)
          <-[:REQUIRES]-(job:Job)

    RETURN
        job.title AS job,
        count(skill) AS matching_skills

    ORDER BY matching_skills DESC
    """

    with driver.session() as session:
        result = session.run(query)

        for record in result:
            print(
                f"{record['job']} -> "
                f"{record['matching_skills']} matching skills"
            )


if __name__ == "__main__":
    get_recommendations()
    