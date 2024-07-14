import streamlit as st
import requests as re
import pandas as pd
from streamlit_option_menu import option_menu
from utils import plot_barplot, plot_boxplot
from requests.exceptions import ConnectionError
import os

BACKEND_HOST = os.getenv("BACKEND_SERVICE_NAME")
BACKEND_PORT = os.getenv("BACKEND_PORT")


@st.cache_data(show_spinner=False)
def get_continents():
    result = re.get(f"http://{BACKEND_HOST}:{BACKEND_PORT}/continents")
    return result.json()


@st.cache_data(show_spinner=False)
def get_countries_by_continent_id(continent_id: int):
    result = re.get(f"http://{BACKEND_HOST}:{BACKEND_PORT}/continents/{continent_id}")
    data = result.json()
    return data


@st.cache_data(show_spinner=False)
def get_all_jobs():
    result = re.get(f"http://{BACKEND_HOST}:{BACKEND_PORT}/")
    data = result.json()
    return data


st.set_page_config(layout="wide")
st.markdown(
    """
    <h1 style='text-align: center;'>🚀Global Available Jobs - Interactive Dashboard🚀</h1>
    """,
    unsafe_allow_html=True,
)

# ---------------NAVIGATION MENU-----------------------------------
main_menu = option_menu(
    menu_title=None,
    options=["Globally Analysis", "Country Analysis"],
    icons=["compass", "pin-map"],
    orientation="horizontal",
)

# -------------------------------------------------------------------
try:
    df_all = pd.DataFrame(get_all_jobs())
    if main_menu == "Globally Analysis":
        st.dataframe(df_all)
        col1, col2 = st.columns(2)
        with col1:
            df_all_1 = (
                df_all["short_job_title_name"]
                .value_counts()
                .head(10)
                .to_frame(name="count")
            )
            fig, ax = plot_barplot(
                data=df_all_1,
                x="count",
                y="short_job_title_name",
                hue="count",
                xlabel="Number of posted Jobs",
                suptitle="Number of posted jobs by Top 10 Short Job Titles",
            )
            st.pyplot(fig=fig)
        with col2:
            df_all_2 = (
                df_all[["short_job_title_name", "expected_yearly_salary"]]
                .groupby("short_job_title_name")
                .agg("median")
                .sort_values(by="expected_yearly_salary", ascending=False)
                .head(10)
            )
            fig, ax = plot_barplot(
                data=df_all_2,
                x="expected_yearly_salary",
                y="short_job_title_name",
                hue="expected_yearly_salary",
                xlabel="Median Salary",
                suptitle="Top 10 Median Salaries by Short Job title Name",
            )
            st.pyplot(fig=fig)
        col1, col2 = st.columns(2)
        with col1:
            df_all_3 = df_all["work_location_type"].value_counts().to_frame(name="count")
            fig, ax = plot_barplot(
                data=df_all_3,
                x="count",
                y="work_location_type",
                hue="count",
                xlabel="Number of posted Jobs",
                suptitle="Number of posted jobs by Work Location Type",
            )
            st.pyplot(fig=fig)
        with col2:
            df_all_4 = (
                df_all[["work_location_type", "expected_yearly_salary"]]
                .groupby("work_location_type")
                .agg("median")
                .sort_values(by="expected_yearly_salary", ascending=False)
            )
            fig, ax = plot_barplot(
                data=df_all_4,
                x="expected_yearly_salary",
                y="work_location_type",
                hue="expected_yearly_salary",
                xlabel="Median Salary",
                suptitle="Median Salaries by Work Location Type",
            )
            st.pyplot(fig=fig)
        col1, col2 = st.columns(2)
        with col1:
            fig, ax = plot_boxplot(
                data=df_all,
                x="expected_yearly_salary",
                hue="work_location_type",
                gap=0.3,
                leg_loc="upper right",
                suptitle="Boxplot of Expected Yearly Salary by Work Location Type",
            )
            st.pyplot(fig=fig)
        with col2:
            fig, ax = plot_boxplot(
                data=df_all,
                x="expected_yearly_salary",
                hue="job_schedule_type",
                gap=0.3,
                leg_loc="upper right",
                suptitle="Boxplot of Expected Yearly Salary by Job Schedule Type",
            )
            st.pyplot(fig=fig)
    else:
        df = pd.DataFrame(get_continents())
        continent_option = st.selectbox(
            "Choose the desired continent:", list(df["continent_name"].values)
        )
        df2 = pd.DataFrame(
            get_countries_by_continent_id(
                int(df[df["continent_name"] == continent_option]["continent_id"].iloc[0])
            )
        ).sort_values(by="country_name")
        country_option = st.selectbox(
            "Choose the desired country", list(df2["country_name"].values)
        )
        df3 = df_all[df_all["country_name"] == country_option]

        st.dataframe(df3)
        col1, col2 = st.columns(2)
        with col1:
            df4 = df3["short_job_title_name"].value_counts().head(10).to_frame(name="count")
            fig, ax = plot_barplot(
                data=df4,
                x="count",
                y="short_job_title_name",
                hue="count",
                xlabel="Number of posted Jobs",
                suptitle=f"Number of posted jobs by Top 10 Short Job Titles in {country_option}",
            )
            st.pyplot(fig=fig)
        with col2:
            df5 = (
                df3[["short_job_title_name", "expected_yearly_salary"]]
                .groupby("short_job_title_name")
                .agg("median")
                .sort_values(by="expected_yearly_salary", ascending=False)
                .head(10)
            )
            fig, ax = plot_barplot(
                data=df5,
                x="expected_yearly_salary",
                y="short_job_title_name",
                hue="expected_yearly_salary",
                xlabel="Median Salary",
                suptitle=f"Top 10 Median Salaries by Short Job title Name in {country_option}",
            )
            st.pyplot(fig=fig)
        col1, col2 = st.columns(2)
        with col1:
            df6 = df3["work_location_type"].value_counts().to_frame(name="count")
            fig, ax = plot_barplot(
                data=df6,
                x="count",
                y="work_location_type",
                hue="count",
                xlabel="Number of posted Jobs",
                suptitle=f"Number of posted jobs by Work Location Type in {country_option}",
            )
            st.pyplot(fig=fig)
        with col2:
            df7 = (
                df3[["work_location_type", "expected_yearly_salary"]]
                .groupby("work_location_type")
                .agg("median")
                .sort_values(by="expected_yearly_salary", ascending=False)
            )
            fig, ax = plot_barplot(
                data=df7,
                x="expected_yearly_salary",
                y="work_location_type",
                hue="expected_yearly_salary",
                xlabel="Median Salary",
                suptitle=f"Median Salaries by Work Location Type in {country_option}",
            )
            st.pyplot(fig=fig)

        col1, col2 = st.columns(2)
        with col1:
            fig, ax = plot_boxplot(
                data=df3,
                x="expected_yearly_salary",
                hue="work_location_type",
                gap=0.3,
                leg_loc="upper right",
                suptitle=f"Boxplot of Expected Yearly Salary by Work Location Type in {country_option}",
            )
            st.pyplot(fig=fig)
        with col2:
            fig, ax = plot_boxplot(
                data=df3,
                x="expected_yearly_salary",
                hue="job_schedule_type",
                gap=0.3,
                leg_loc="upper right",
                suptitle=f"Boxplot of Expected Yearly Salary by Job Schedule Type in {country_option}",
            )
            st.pyplot(fig=fig)
except ConnectionError:
    st.error(body="Failed to fetch data from the server.", icon="🚨")
