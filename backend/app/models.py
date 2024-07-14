from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from sqlalchemy import Integer, VARCHAR, ForeignKey, DECIMAL
from sqlalchemy.ext.asyncio import AsyncAttrs



class Base(AsyncAttrs, DeclarativeBase):
    pass


class Continents(Base):
    __tablename__ = "continents"

    continent_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    continent_name: Mapped[str] = mapped_column(VARCHAR(30), unique=True, index=True)
    countries: Mapped[list["Countries"]] = relationship(back_populates="continent")


class Countries(Base):
    __tablename__ = "countries"

    country_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    country_name: Mapped[str] = mapped_column(VARCHAR(30), unique=True, index=True)
    continent_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("continents.continent_id")
    )
    continent: Mapped[Continents] = relationship(back_populates="countries")
    companies: Mapped[list["Companies"]] = relationship(back_populates="country")
    cities: Mapped[list["Cities"]] = relationship(back_populates="country")


class Companies(Base):
    __tablename__ = "companies"

    company_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    company_name: Mapped[str] = mapped_column(VARCHAR(100), unique=True, index=True)
    country_id: Mapped[int] = mapped_column(Integer, ForeignKey("countries.country_id"))
    country: Mapped[Countries] = relationship(back_populates="companies")
    jobs: Mapped[list["Jobs"]] = relationship(back_populates="company")


class Cities(Base):
    __tablename__ = "cities"

    city_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    city_name: Mapped[str] = mapped_column(VARCHAR(100), unique=True, index=True)
    country_id: Mapped[int] = mapped_column(Integer, ForeignKey("countries.country_id"))
    country: Mapped[Countries] = relationship(back_populates="cities")
    jobs: Mapped[list["Jobs"]] = relationship(back_populates="job_city_location")


class ShortjobtitleIndustriesLink(Base):
    __tablename__ = "shortjobtitleindustrieslinktable"

    short_job_title_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("shortjobtitles.job_title_id"), primary_key=True
    )
    industry_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("industries.industry_id"), primary_key=True
    )


class ShortJobTitles(Base):
    __tablename__ = "shortjobtitles"

    job_title_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    short_job_title_name: Mapped[str] = mapped_column(
        VARCHAR(100), unique=True, index=True
    )
    industries: Mapped[list["Industries"]] = relationship(
        secondary="shortjobtitleindustrieslinktable",
        back_populates="short_job_titles",
    )
    jobs: Mapped[list["Jobs"]] = relationship(back_populates="short_job_title")


class Industries(Base):
    __tablename__ = "industries"

    industry_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    industry_name: Mapped[str] = mapped_column(VARCHAR(100), unique=True, index=True)
    short_job_titles: Mapped[list[ShortJobTitles]] = relationship(
        secondary="shortjobtitleindustrieslinktable",
        back_populates="industries",
    )


class WorkLocationType(Base):
    __tablename__ = "worklocationtypes"

    work_location_type_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    work_location_type: Mapped[str] = mapped_column(
        VARCHAR(30), unique=True, index=True
    )
    jobs: Mapped[list["Jobs"]] = relationship(back_populates="work_location_type")


class JobScheduleType(Base):
    __tablename__ = "jobscheduletypes"

    job_schedule_type_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    job_schedule_type: Mapped[str] = mapped_column(VARCHAR(30), unique=True, index=True)
    jobs: Mapped[list["Jobs"]] = relationship(back_populates="job_schedule_type")


class JobsVia(Base):
    __tablename__ = "jobsvia"

    job_via_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    job_via_name: Mapped[str] = mapped_column(VARCHAR(30), unique=True, index=True)
    jobs: Mapped[list["Jobs"]] = relationship(back_populates="job_via")


class Skills(Base):
    __tablename__ = "skills"

    skill_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    skill_name: Mapped[str] = mapped_column(VARCHAR(100), unique=True, index=True)
    jobs: Mapped[list["Jobs"]] = relationship(
        secondary="jobSkillsLinkTable", back_populates="skills"
    )


class Salaries(Base):
    __tablename__ = "salaries"

    salary_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("jobs.job_id"), primary_key=True, autoincrement=True
    )
    expected_yearly_salary: Mapped[float] = mapped_column(DECIMAL(10, 2), index=True)
    job: Mapped["Jobs"] = relationship(back_populates="salary")


class JobSkillsLink(Base):
    __tablename__ = "jobSkillsLinkTable"

    job_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("jobs.job_id"), primary_key=True
    )
    skill_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("skills.skill_id"), primary_key=True
    )


class Jobs(Base):
    __tablename__ = "jobs"
    job_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    job_title: Mapped[str] = mapped_column(VARCHAR(100))
    short_job_title_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("shortjobtitles.job_title_id")
    )
    job_city_location_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("cities.city_id")
    )
    job_via_id: Mapped[int] = mapped_column(Integer, ForeignKey("jobsvia.job_via_id"))
    work_location_type_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("worklocationtypes.work_location_type_id")
    )
    job_schedule_type_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("jobscheduletypes.job_schedule_type_id")
    )
    company_id: Mapped[int] = mapped_column(Integer, ForeignKey("companies.company_id"))
    skills: Mapped[list[Skills]] = relationship(
        secondary="jobSkillsLinkTable", back_populates="jobs"
    )
    salary: Mapped[Salaries] = relationship(back_populates="job")
    short_job_title: Mapped[ShortJobTitles] = relationship(back_populates="jobs")
    job_city_location: Mapped[Cities] = relationship(back_populates="jobs")
    job_via: Mapped[JobsVia] = relationship(back_populates="jobs")
    work_location_type: Mapped[WorkLocationType] = relationship(back_populates="jobs")
    job_schedule_type: Mapped[JobScheduleType] = relationship(back_populates="jobs")
    company: Mapped[Companies] = relationship(back_populates="jobs")
