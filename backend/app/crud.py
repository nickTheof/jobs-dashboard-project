from database import sessionLocal
import models
from sqlalchemy import select


async def get_db():
    async with sessionLocal() as session:
        yield session


async def get_continent(continent_name: str) -> models.Continents | None:
    async with sessionLocal() as session:
        async with session.begin():
            instance = (
                await session.scalars(
                    select(models.Continents).filter(
                        models.Continents.continent_name == continent_name
                    )
                )
            ).first()
            return instance


async def create_continent(continent_name: str) -> None:
    async with sessionLocal() as session:
        async with session.begin():
            new_continent = models.Continents(continent_name=continent_name)
            session.add(new_continent)
            await session.commit()


async def get_country(country_name: str) -> models.Countries | None:
    async with sessionLocal() as session:
        async with session.begin():
            instance = (
                await session.scalars(
                    select(models.Countries).filter(
                        models.Countries.country_name == country_name
                    )
                )
            ).first()
            return instance


async def create_country(data: dict[str, str]) -> None:
    async with sessionLocal() as session:
        async with session.begin():
            db_continent = await get_continent(data["continent_name"])
            if db_continent:
                new_country = models.Countries(
                    country_name=data["country_name"],
                    continent_id=db_continent.continent_id,
                )
                session.add(new_country)
                await session.commit()


async def get_city(city_name: str) -> models.Cities | None:
    async with sessionLocal() as session:
        async with session.begin():
            instance = (
                await session.scalars(
                    select(models.Cities).filter(models.Cities.city_name == city_name)
                )
            ).first()
            return instance


async def create_city(data: dict[str, str]) -> None:
    async with sessionLocal() as session:
        async with session.begin():
            db_country = await get_country(data["country_name"])
            if db_country:
                new_city = models.Cities(
                    city_name=data["city_name"], country_id=db_country.country_id
                )
                session.add(new_city)
                await session.commit()


async def get_industry(industry_name: str) -> models.Industries | None:
    async with sessionLocal() as session:
        async with session.begin():
            instance = (
                await session.scalars(
                    select(models.Industries).filter(
                        models.Industries.industry_name == industry_name
                    )
                )
            ).first()
            return instance


async def create_industry(industry_name: str) -> None:
    async with sessionLocal() as session:
        async with session.begin():
            new_industry = models.Industries(industry_name=industry_name)
            session.add(new_industry)
            await session.commit()


async def get_short_job_title(
    short_job_title_name: str,
) -> models.ShortJobTitles | None:
    async with sessionLocal() as session:
        async with session.begin():
            instance = (
                await session.scalars(
                    select(models.ShortJobTitles).filter(
                        models.ShortJobTitles.short_job_title_name
                        == short_job_title_name
                    )
                )
            ).first()
            return instance


async def create_short_job_title(short_job_title_name: str) -> None:
    async with sessionLocal() as session:
        async with session.begin():
            new_short_job_title = models.ShortJobTitles(
                short_job_title_name=short_job_title_name
            )
            session.add(new_short_job_title)
            await session.commit()


async def get_short_job_title_industry_link(
    short_job_title_name: str, industry_name: str
) -> models.ShortjobtitleIndustriesLink | None:
    async with sessionLocal() as session:
        async with session.begin():
            db_short_job_title = await get_short_job_title(
                short_job_title_name=short_job_title_name
            )
            db_industry = await get_industry(industry_name=industry_name)
            if db_short_job_title and db_industry:
                instance = (
                    await session.scalars(
                        select(models.ShortjobtitleIndustriesLink)
                        .filter(
                            models.ShortjobtitleIndustriesLink.short_job_title_id
                            == db_short_job_title.job_title_id
                        )
                        .filter(
                            models.ShortjobtitleIndustriesLink.industry_id
                            == db_industry.industry_id
                        )
                    )
                ).first()
            return instance


async def create_short_job_title_industry_link(
    short_job_title_name: str, industry_name: str
) -> None:
    async with sessionLocal() as session:
        async with session.begin():
            db_short_job_title = await get_short_job_title(
                short_job_title_name=short_job_title_name
            )
            db_industry = await get_industry(industry_name=industry_name)
            if db_short_job_title and db_industry:
                new_link = models.ShortjobtitleIndustriesLink(
                    short_job_title_id=db_short_job_title.job_title_id,
                    industry_id=db_industry.industry_id,
                )
                session.add(new_link)
                await session.commit()


async def get_work_location_type(
    work_location_type: str,
) -> models.WorkLocationType | None:
    async with sessionLocal() as session:
        async with session.begin():
            instance = (
                await session.scalars(
                    select(models.WorkLocationType).filter(
                        models.WorkLocationType.work_location_type == work_location_type
                    )
                )
            ).first()
            return instance


async def create_work_location_type(work_location_type: str) -> None:
    async with sessionLocal() as session:
        async with session.begin():
            new_work_location_type = models.WorkLocationType(
                work_location_type=work_location_type
            )
            session.add(new_work_location_type)
            await session.commit()


async def get_job_schedule_type(
    job_schedule_type: str,
) -> models.JobScheduleType | None:
    async with sessionLocal() as session:
        async with session.begin():
            instance = (
                await session.scalars(
                    select(models.JobScheduleType).filter(
                        models.JobScheduleType.job_schedule_type == job_schedule_type
                    )
                )
            ).first()
            return instance


async def create_job_schedule_type(job_schedule_type: str) -> None:
    async with sessionLocal() as session:
        async with session.begin():
            new_job_schedule_type = models.JobScheduleType(
                job_schedule_type=job_schedule_type
            )
            session.add(new_job_schedule_type)
            await session.commit()


async def get_job_via(job_via_name: str) -> models.JobsVia | None:
    async with sessionLocal() as session:
        async with session.begin():
            instance = (
                await session.scalars(
                    select(models.JobsVia).filter(
                        models.JobsVia.job_via_name == job_via_name
                    )
                )
            ).first()
            return instance


async def create_job_via(job_via_name: str) -> None:
    async with sessionLocal() as session:
        async with session.begin():
            new_job_via = models.JobsVia(job_via_name=job_via_name)
            session.add(new_job_via)
            await session.commit()


async def get_company(company_name: str) -> models.Companies | None:
    async with sessionLocal() as session:
        async with session.begin():
            instance = (
                await session.scalars(
                    select(models.Companies).filter(
                        models.Companies.company_name == company_name
                    )
                )
            ).first()
            return instance


async def create_company(data: dict[str, str]) -> None:
    async with sessionLocal() as session:
        async with session.begin():
            db_country = await get_country(data["country_name"])
            if db_country:
                new_company = models.Companies(
                    company_name=data["company_name"], country_id=db_country.country_id
                )
                session.add(new_company)
                await session.commit()


async def get_skill(skill_name: str) -> models.Skills | None:
    async with sessionLocal() as session:
        async with session.begin():
            instance = (
                await session.scalars(
                    select(models.Skills).filter(models.Skills.skill_name == skill_name)
                )
            ).first()
            return instance


async def create_skill(data: dict[str, str]) -> None:
    async with sessionLocal() as session:
        async with session.begin():
            new_skill = models.Skills(skill_name=data["skill_name"])
            session.add(new_skill)
            await session.commit()


async def get_job(job_title: str) -> models.Jobs | None:
    async with sessionLocal() as session:
        async with session.begin():
            instance = (
                await session.scalars(
                    select(models.Jobs).filter(models.Jobs.job_title == job_title)
                )
            ).first()
            return instance


async def get_job_title_skill_link(
    job_title: str, skill_name: str
) -> models.JobSkillsLink | None:
    async with sessionLocal() as session:
        async with session.begin():
            db_job = await get_job(job_title=job_title)
            db_skill = await get_skill(skill_name=skill_name)
            if db_job and db_skill:
                instance = (
                    await session.scalars(
                        select(models.JobSkillsLink)
                        .filter(models.JobSkillsLink.job_id == db_job.job_id)
                        .filter(models.JobSkillsLink.skill_id == db_skill.skill_id)
                    )
                ).first()
            return instance


async def create_job_title_skills_link(job_title: str, skill_name: str) -> None:
    async with sessionLocal() as session:
        async with session.begin():
            db_job = await get_job(job_title=job_title)
            db_skill = await get_skill(skill_name=skill_name)
            if db_job and db_skill:
                new_link = models.JobSkillsLink(
                    job_id=db_job.job_id,
                    skill_id=db_skill.skill_id,
                )
                session.add(new_link)
                await session.commit()


async def create_job(
    data_jobs: dict[str, str],
    job_city_location: str,
    job_via: str,
    work_location_type: str,
    job_schedule_type: str,
    company_name: str,
    salary: float,
) -> None:
    async with sessionLocal() as session:
        async with session.begin():
            db_short_job = await get_short_job_title(
                short_job_title_name=data_jobs["short_job_title"]
            )
            db_job_city_location = await get_city(city_name=job_city_location)
            db_job_via = await get_job_via(job_via_name=job_via)
            db_work_location_type = await get_work_location_type(
                work_location_type=work_location_type
            )
            db_job_schedule_type = await get_job_schedule_type(
                job_schedule_type=job_schedule_type
            )
            db_company = await get_company(company_name=company_name)
            if (
                db_short_job
                and db_job_city_location
                and db_job_via
                and db_work_location_type
                and db_job_schedule_type
                and db_company
            ):
                new_job = models.Jobs(
                    job_title=data_jobs["job_title"],
                    short_job_title_id=db_short_job.job_title_id,
                    job_city_location_id=db_job_city_location.city_id,
                    job_via_id=db_job_via.job_via_id,
                    work_location_type_id=db_work_location_type.work_location_type_id,
                    job_schedule_type_id=db_job_schedule_type.job_schedule_type_id,
                    company_id=db_company.company_id,
                )
                session.add(new_job)
                await session.flush()
                new_salary = models.Salaries(
                    salary_id=new_job.job_id, expected_yearly_salary=salary
                )
                session.add(new_salary)

                await session.commit()
