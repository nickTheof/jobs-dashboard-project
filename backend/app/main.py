from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, status

from populate_data import pop_data
from crud import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, text
from models import Continents, Base
import schemas as _schemas
from database import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await pop_data()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def get_jobs(db: AsyncSession=Depends(get_db)):
    query = (await db.execute(text(f"""select j.job_id as job_id, j.job_title, sjt.short_job_title_name, cm.company_name, c.country_name, wlt.work_location_type, jst.job_schedule_type,jv.job_via_name, sal.expected_yearly_salary
                                        from jobs j
                                        join shortjobtitles sjt ON j.short_job_title_id = sjt.job_title_id
                                        join cities ct ON j.job_city_location_id = ct.city_id
                                        join jobsvia jv ON j.job_via_id = jv.job_via_id
                                        join worklocationtypes wlt ON j.work_location_type_id = wlt.work_location_type_id
                                        join jobscheduletypes jst ON j.job_schedule_type_id = jst.job_schedule_type_id
                                        join companies cm ON j.company_id = cm.company_id
                                        join countries c ON c.country_id = ct.country_id
                                        join salaries sal ON j.job_id = sal.salary_id
                                        ORDER BY sal.expected_yearly_salary DESC;""")))
    column_names = query.keys()
    rows = query.fetchall()
    data = []
    for values in rows:
        dat = {}
        for i, col_name in enumerate(column_names):
            dat.update({col_name: values[i]})
        data.append(dat)
    return data


@app.get("/continents", response_model=list[_schemas.Continent])
async def get_continents(db: AsyncSession=Depends(get_db)):
    query = (await db.scalars(select(Continents).order_by("continent_name"))).all()
    return query

@app.get("/continents/{continent_id}")
async def get_continent_by_id(continent_id: int, db: AsyncSession=Depends(get_db)):
    query = (await db.scalars(select(Continents).filter(Continents.continent_id == continent_id))).first()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Continent with id: {continent_id} doesn't exist.")
    dic = []
    for b1 in await query.awaitable_attrs.countries:
        dic.append({'country_id': b1.country_id, 'country_name': b1.country_name})
    return dic
        

@app.get("/continents/countries/jobs/{country_id}")
async def get_jobs_by_country_id(country_id: int, db: AsyncSession=Depends(get_db)):
    query = (await db.execute(text(f"""select j.job_id as job_id, j.job_title, sjt.short_job_title_name, cm.company_name, c.country_name, wlt.work_location_type, jst.job_schedule_type,jv.job_via_name, sal.expected_yearly_salary
                                        from jobs j
                                        join shortjobtitles sjt ON j.short_job_title_id = sjt.job_title_id
                                        join cities ct ON j.job_city_location_id = ct.city_id
                                        join jobsvia jv ON j.job_via_id = jv.job_via_id
                                        join worklocationtypes wlt ON j.work_location_type_id = wlt.work_location_type_id
                                        join jobscheduletypes jst ON j.job_schedule_type_id = jst.job_schedule_type_id
                                        join companies cm ON j.company_id = cm.company_id
                                        join countries c ON c.country_id = ct.country_id
                                        join salaries sal ON j.job_id = sal.salary_id
                                        WHERE c.country_id = {int(country_id)}
                                        ORDER BY sal.expected_yearly_salary DESC;""")))
    column_names = query.keys()
    rows = query.fetchall()
    data = []
    for values in rows:
        dat = {}
        for i, col_name in enumerate(column_names):
            dat.update({col_name: values[i]})
        data.append(dat)
    return data
