import random
from crud import (
    get_continent,
    create_continent,
    get_country,
    create_country,
    get_city,
    create_city,
    get_industry,
    create_industry,
    get_short_job_title,
    create_short_job_title,
    get_short_job_title_industry_link,
    create_short_job_title_industry_link,
    get_work_location_type,
    create_work_location_type,
    get_job_schedule_type,
    create_job_schedule_type,
    create_company,
    get_company,
    get_job_via,
    create_job_via,
    get_skill,
    create_skill,
    create_job,
    get_job_title_skill_link,
    create_job_title_skills_link,
)


from random_data import (
    countries_and_continents,
    continents,
    cities_and_countries,
    industries,
    job_titles_and_industries,
    work_location_types_data,
    job_schedule_types_data,
    job_via_names,
    companies,
    detailed_job_titles,
    skill_jobs,
)

async def pop_data():
    for data in continents:
        db_continent = await get_continent(data["continent_name"])
        if not db_continent:
            await create_continent(data["continent_name"])

    for data in countries_and_continents:
        db_country = await get_country(data["country_name"])
        if not db_country:
            await create_country(data=data)

    for data in cities_and_countries:
        db_city = await get_city(data["city_name"])
        if not db_city:
            await create_city(data=data)

    for data in industries:
        db_industry = await get_industry(data["industry_name"])
        if not db_industry:
            await create_industry(data["industry_name"])

    for data in job_titles_and_industries:
        db_short_title = await get_short_job_title(data["short_job_title"])
        if not db_short_title:
            await create_short_job_title(data["short_job_title"])

    for data in job_titles_and_industries:
        db_link = await get_short_job_title_industry_link(
            short_job_title_name=data["short_job_title"],
            industry_name=data["industry_name"],
        )
        if not db_link:
            await create_short_job_title_industry_link(
                short_job_title_name=data["short_job_title"],
                industry_name=data["industry_name"],
            )

    for data in work_location_types_data:
        db_work_location_type = await get_work_location_type(
            work_location_type=data["work_location_type"]
        )
        if not db_work_location_type:
            await create_work_location_type(
                work_location_type=data["work_location_type"]
            )

    for data in job_schedule_types_data:
        db_job_location_type = await get_job_schedule_type(
            job_schedule_type=data["job_schedule_type"]
        )
        if not db_job_location_type:
            await create_job_schedule_type(job_schedule_type=data["job_schedule_type"])

    for data in job_via_names:
        db_job_via = await get_job_via(job_via_name=data["job_via_name"])
        if not db_job_via:
            await create_job_via(job_via_name=data["job_via_name"])

    for data in companies:
        db_company = await get_company(company_name=data["company_name"])
        if not db_company:
            await create_company(data=data)

    for data in skill_jobs:
        db_skill = await get_skill(skill_name=data["skill_name"])
        if not db_skill:
            await create_skill(data=data)

    for data in detailed_job_titles:
        await create_job(
            data_jobs=data,
            job_city_location=random.choice(cities_and_countries)["city_name"],
            work_location_type=random.choice(work_location_types_data)[
                "work_location_type"
            ],
            job_via=random.choice(job_via_names)["job_via_name"],
            job_schedule_type=random.choice(job_schedule_types_data)[
                "job_schedule_type"
            ],
            company_name=random.choice(companies)["company_name"],
            salary=round(random.uniform(30000, 150000), 2),
        )
    for data in skill_jobs:
        db_skill_job_link = await get_job_title_skill_link(
            job_title=data["job_title"], skill_name=data["skill_name"]
        )
        if not db_skill_job_link:
            await create_job_title_skills_link(
                job_title=data["job_title"], skill_name=data["skill_name"]
            )
