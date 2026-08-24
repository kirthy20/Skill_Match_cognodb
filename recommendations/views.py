from django.shortcuts import render

from .database import driver


def home(request):
    recommendations = []
    selected_skills = []

    # Get all skills from CognoDB
    skills_query = """
    MATCH (s:Skill)
    RETURN s.name AS name
    ORDER BY s.name
    """

    try:
        with driver.session() as session:
            result = session.run(skills_query)
            available_skills = [record["name"] for record in result]

    except Exception as e:
        print("Error loading skills:", e)
        available_skills = []

    # Handle form submission
    if request.method == "POST":

        selected_skills = request.POST.getlist("skills")

        if selected_skills:

            recommendation_query = """
            MATCH (job:Job)-[:REQUIRES]->(required:Skill)

            WITH job,
                 collect(required.name) AS required_skills

            OPTIONAL MATCH (job)-[:REQUIRES]->(matching:Skill)

            WHERE matching.name IN $skills

            WITH job,
                 required_skills,
                 collect(DISTINCT matching.name) AS matching_skills

            OPTIONAL MATCH (job)-[:OFFERED_BY]->(company:Company)

            RETURN
                job.title AS job,
                company.name AS company,
                required_skills,
                matching_skills

            ORDER BY size(matching_skills) DESC
            """

            try:

                with driver.session() as session:

                    result = session.run(
                        recommendation_query,
                        skills=selected_skills
                    )

                    for record in result:

                        required_skills = record["required_skills"]
                        matching_skills = record["matching_skills"]

                        # Calculate missing skills
                        missing_skills = [
                            skill
                            for skill in required_skills
                            if skill not in matching_skills
                        ]

                        # Calculate match percentage
                        if required_skills:

                            match_percentage = round(
                                (
                                    len(matching_skills)
                                    / len(required_skills)
                                ) * 100
                            )

                        else:

                            match_percentage = 0

                        recommendations.append({

                            "job": record["job"],

                            "company": record["company"],

                            "matching_skills": matching_skills,

                            "missing_skills": missing_skills,

                            "matching_count": len(matching_skills),

                            "total_required": len(required_skills),

                            "match_percentage": match_percentage,

                        })

            except Exception as e:

                print(
                    "Error getting recommendations:",
                    e
                )

    return render(
        request,
        "recommendations/index.html",
        {
            "available_skills": available_skills,

            "selected_skills": selected_skills,

            "recommendations": recommendations,
        }
    )