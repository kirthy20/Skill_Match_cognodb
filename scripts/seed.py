from recommendations.database import driver


def seed_database():

    query = """
    // Create skills
    MERGE (python:Skill {name: 'Python'})
    MERGE (sql:Skill {name: 'SQL'})
    MERGE (powerbi:Skill {name: 'Power BI'})
    MERGE (excel:Skill {name: 'Excel'})
    MERGE (java:Skill {name: 'Java'})
    MERGE (javascript:Skill {name: 'JavaScript'})
    MERGE (html:Skill {name: 'HTML'})
    MERGE (css:Skill {name: 'CSS'})
    MERGE (react:Skill {name: 'React'})
    MERGE (django:Skill {name: 'Django'})
    MERGE (nodejs:Skill {name: 'Node.js'})
    MERGE (git:Skill {name: 'Git'})
    MERGE (aws:Skill {name: 'AWS'})
    MERGE (docker:Skill {name: 'Docker'})

    // Create candidate
    MERGE (candidate:Candidate {name: 'Keerthi'})

    // Candidate skills
    MERGE (candidate)-[:HAS_SKILL]->(python)
    MERGE (candidate)-[:HAS_SKILL]->(sql)
    MERGE (candidate)-[:HAS_SKILL]->(powerbi)
    MERGE (candidate)-[:HAS_SKILL]->(excel)
    MERGE (candidate)-[:HAS_SKILL]->(html)
    MERGE (candidate)-[:HAS_SKILL]->(css)
    MERGE (candidate)-[:HAS_SKILL]->(javascript)
    MERGE (candidate)-[:HAS_SKILL]->(git)

    // Create jobs
    MERGE (data_analyst:Job {title: 'Data Analyst'})
    MERGE (business_analyst:Job {title: 'Business Analyst'})
    MERGE (software_developer:Job {title: 'Software Developer'})
    MERGE (frontend_developer:Job {title: 'Frontend Developer'})
    MERGE (backend_developer:Job {title: 'Backend Developer'})
    MERGE (fullstack_developer:Job {title: 'Full Stack Developer'})
    MERGE (cloud_engineer:Job {title: 'Cloud Engineer'})
    MERGE (devops_engineer:Job {title: 'DevOps Engineer'})

    // Create companies
    MERGE (abc:Company {name: 'ABC Technologies'})
    MERGE (xyz:Company {name: 'XYZ Solutions'})
    MERGE (techcorp:Company {name: 'TechCorp'})
    MERGE (cloudtech:Company {name: 'CloudTech'})

    // Data Analyst skills
    MERGE (data_analyst)-[:REQUIRES]->(python)
    MERGE (data_analyst)-[:REQUIRES]->(sql)
    MERGE (data_analyst)-[:REQUIRES]->(powerbi)
    MERGE (data_analyst)-[:REQUIRES]->(excel)

    // Business Analyst skills
    MERGE (business_analyst)-[:REQUIRES]->(sql)
    MERGE (business_analyst)-[:REQUIRES]->(excel)
    MERGE (business_analyst)-[:REQUIRES]->(powerbi)

    // Software Developer skills
    MERGE (software_developer)-[:REQUIRES]->(python)
    MERGE (software_developer)-[:REQUIRES]->(java)
    MERGE (software_developer)-[:REQUIRES]->(sql)
    MERGE (software_developer)-[:REQUIRES]->(git)

    // Frontend Developer skills
    MERGE (frontend_developer)-[:REQUIRES]->(html)
    MERGE (frontend_developer)-[:REQUIRES]->(css)
    MERGE (frontend_developer)-[:REQUIRES]->(javascript)
    MERGE (frontend_developer)-[:REQUIRES]->(react)
    MERGE (frontend_developer)-[:REQUIRES]->(git)

    // Backend Developer skills
    MERGE (backend_developer)-[:REQUIRES]->(python)
    MERGE (backend_developer)-[:REQUIRES]->(django)
    MERGE (backend_developer)-[:REQUIRES]->(sql)
    MERGE (backend_developer)-[:git]->(git)

    // Full Stack Developer skills
    MERGE (fullstack_developer)-[:REQUIRES]->(javascript)
    MERGE (fullstack_developer)-[:REQUIRES]->(react)
    MERGE (fullstack_developer)-[:REQUIRES]->(nodejs)
    MERGE (fullstack_developer)-[:REQUIRES]->(html)
    MERGE (fullstack_developer)-[:REQUIRES]->(css)
    MERGE (fullstack_developer)-[:REQUIRES]->(git)

    // Cloud Engineer skills
    MERGE (cloud_engineer)-[:REQUIRES]->(aws)
    MERGE (cloud_engineer)-[:REQUIRES]->(docker)
    MERGE (cloud_engineer)-[:REQUIRES]->(git)
    MERGE (cloud_engineer)-[:REQUIRES]->(python)

    // DevOps Engineer skills
    MERGE (devops_engineer)-[:REQUIRES]->(docker)
    MERGE (devops_engineer)-[:REQUIRES]->(aws)
    MERGE (devops_engineer)-[:REQUIRES]->(git)
    MERGE (devops_engineer)-[:REQUIRES]->(python)

    // Companies
    MERGE (data_analyst)-[:OFFERED_BY]->(abc)
    MERGE (business_analyst)-[:OFFERED_BY]->(xyz)
    MERGE (software_developer)-[:OFFERED_BY]->(abc)
    MERGE (frontend_developer)-[:OFFERED_BY]->(techcorp)
    MERGE (backend_developer)-[:OFFERED_BY]->(techcorp)
    MERGE (fullstack_developer)-[:OFFERED_BY]->(xyz)
    MERGE (cloud_engineer)-[:OFFERED_BY]->(cloudtech)
    MERGE (devops_engineer)-[:OFFERED_BY]->(cloudtech)
    """

    with driver.session() as session:
        session.run(query)

    print("Database updated successfully!")


if __name__ == "__main__":
    seed_database()