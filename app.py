import streamlit as st
import pandas as pd
import os

# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="Farmer Assistance & Resource Platform",
    page_icon="🌾",
    layout="wide"
)

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------

crops = pd.read_csv("crops.csv")
fertilizers = pd.read_csv("fertilizer.csv")
pests = pd.read_csv("pests.csv")
markets = pd.read_csv("markets.csv")
helplines = pd.read_csv("helplines.csv")


# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.title("🌾 Farmer Assistance & Resource Platform")

st.write(
    "A simple digital platform providing agricultural information, "
    "crop guidance, pest management, irrigation support and farmer assistance."
)

st.divider()


# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("🌾 Farmer Platform")

menu = st.sidebar.radio(
    "Select Service",
    [
        "🏠 Dashboard",
        "🌱 Crop Information",
        "🧪 Fertilizer Guidance",
        "🐛 Pest & Disease",
        "💧 Irrigation Guidance",
        "🏪 Market Information",
        "📞 Agricultural Helplines",
        "📝 Farmer Query",
        "🌾 Crop Recommendation",
        "🔎 Search Resources"
    ]
)


# -------------------------------------------------
# DASHBOARD
# -------------------------------------------------

if menu == "🏠 Dashboard":

    st.header("🏠 Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🌱 Crops", len(crops))

    with col2:
        st.metric("🧪 Guidance Records", len(fertilizers))

    with col3:
        st.metric("🐛 Pest Records", len(pests))

    with col4:
        st.metric("🏪 Markets", len(markets))

    st.subheader("🌾 Welcome")

    st.write(
        """
        This platform provides farmers with easy access to useful
        agricultural resources.

        **Available Services:**

        - 🌱 Crop Information
        - 🧪 Fertilizer Guidance
        - 🐛 Pest & Disease Assistance
        - 💧 Irrigation Guidance
        - 🏪 Market Information
        - 📞 Agricultural Helplines
        - 📝 Farmer Query Registration
        - 🌾 Crop Recommendation
        """
    )

    st.info(
        "Information provided by this educational project is for general guidance. "
        "Farmers should consult qualified agricultural experts and official sources "
        "for crop-specific decisions."
    )


# -------------------------------------------------
# CROP INFORMATION
# -------------------------------------------------

elif menu == "🌱 Crop Information":

    st.header("🌱 Crop Information")

    crop_name = st.selectbox(
        "Select Crop",
        sorted(crops["crop"].unique())
    )

    selected = crops[crops["crop"] == crop_name]

    st.dataframe(
        selected,
        use_container_width=True,
        hide_index=True
    )


# -------------------------------------------------
# FERTILIZER GUIDANCE
# -------------------------------------------------

elif menu == "🧪 Fertilizer Guidance":

    st.header("🧪 Fertilizer Guidance")

    crop_name = st.selectbox(
        "Select Crop",
        sorted(fertilizers["crop"].unique())
    )

    result = fertilizers[
        fertilizers["crop"] == crop_name
    ]

    st.dataframe(
        result,
        use_container_width=True,
        hide_index=True
    )

    st.warning(
        "Fertilizer decisions should preferably be based on soil testing "
        "and recommendations from qualified agricultural professionals."
    )


# -------------------------------------------------
# PEST & DISEASE
# -------------------------------------------------

elif menu == "🐛 Pest & Disease":

    st.header("🐛 Pest & Disease Assistance")

    crop_name = st.selectbox(
        "Select Crop",
        sorted(pests["crop"].unique())
    )

    result = pests[
        pests["crop"] == crop_name
    ]

    for _, row in result.iterrows():

        with st.expander(f"🐛 {row['problem']}"):

            st.write(
                f"**Possible Cause:** {row['possible_cause']}"
            )

            st.write(
                f"**Management:** {row['management']}"
            )


# -------------------------------------------------
# IRRIGATION
# -------------------------------------------------

elif menu == "💧 Irrigation Guidance":

    st.header("💧 Irrigation Guidance")

    crop = st.selectbox(
        "Select Crop",
        sorted(crops["crop"].unique())
    )

    soil = st.selectbox(
        "Select Soil Type",
        [
            "Clay Soil",
            "Loamy Soil",
            "Sandy Soil",
            "Black Soil",
            "Red Soil"
        ]
    )

    weather = st.selectbox(
        "Current Weather",
        [
            "Sunny",
            "Cloudy",
            "Rainy",
            "Hot"
        ]
    )

    if weather == "Rainy":

        st.info(
            "🌧️ Avoid unnecessary irrigation during rainfall. "
            "Check soil moisture before watering."
        )

    elif weather == "Hot":

        st.warning(
            "☀️ Hot conditions may increase water requirement. "
            "Monitor soil moisture regularly."
        )

    else:

        st.success(
            "💧 Check soil moisture before irrigation and avoid overwatering."
        )

    st.write(f"**Selected Crop:** {crop}")
    st.write(f"**Selected Soil:** {soil}")


# -------------------------------------------------
# MARKET INFORMATION
# -------------------------------------------------

elif menu == "🏪 Market Information":

    st.header("🏪 Market Information")

    st.info(
        "The values shown below are sample project data and are not live market prices."
    )

    st.dataframe(
        markets,
        use_container_width=True,
        hide_index=True
    )


# -------------------------------------------------
# HELPLINES
# -------------------------------------------------

elif menu == "📞 Agricultural Helplines":

    st.header("📞 Agricultural Helplines")

    for _, row in helplines.iterrows():

        st.subheader(f"📞 {row['service']}")

        st.write(row["description"])

        st.write(
            f"**Contact:** {row['contact']}"
        )

        st.divider()


# -------------------------------------------------
# FARMER QUERY
# -------------------------------------------------

elif menu == "📝 Farmer Query":

    st.header("📝 Farmer Query Registration")

    name = st.text_input("Farmer Name")

    village = st.text_input("Village")

    district = st.text_input("District")

    mobile = st.text_input("Mobile Number")

    crop = st.selectbox(
        "Select Crop",
        sorted(crops["crop"].unique())
    )

    problem = st.selectbox(
        "Problem",
        [
            "Pest Attack",
            "Disease",
            "Water Problem",
            "Fertilizer Guidance",
            "Crop Selection",
            "Market Information",
            "Other"
        ]
    )

    description = st.text_area(
        "Describe Your Problem"
    )

    if st.button("Submit Query"):

        if name and village and district and mobile and description:

            new_query = pd.DataFrame({
                "name": [name],
                "village": [village],
                "district": [district],
                "mobile": [mobile],
                "crop": [crop],
                "problem": [problem],
                "description": [description]
            })

            file_name = "farmer_queries.csv"

            if os.path.exists(file_name):

                new_query.to_csv(
                    file_name,
                    mode="a",
                    header=False,
                    index=False
                )

            else:

                new_query.to_csv(
                    file_name,
                    index=False
                )

            st.success(
                "✅ Farmer query submitted successfully!"
            )

        else:

            st.error(
                "Please fill all required fields."
            )


# -------------------------------------------------
# CROP RECOMMENDATION
# -------------------------------------------------

elif menu == "🌾 Crop Recommendation":

    st.header("🌾 Crop Recommendation")

    soil = st.selectbox(
        "Select Soil Type",
        [
            "Black Soil",
            "Clay/Loamy",
            "Sandy Loamy",
            "Loamy",
            "Black/Loamy"
        ]
    )

    water = st.selectbox(
        "Water Availability",
        [
            "Low",
            "Medium",
            "High"
        ]
    )

    season = st.selectbox(
        "Select Season",
        [
            "Kharif",
            "Rabi",
            "Kharif/Rabi",
            "Multiple"
        ]
    )

    if st.button("Recommend Crops"):

        result = crops[
            (
                crops["soil"].str.contains(
                    soil.split("/")[0],
                    case=False,
                    na=False
                )
            )
            &
            (
                crops["water"] == water
            )
        ]

        if len(result) > 0:

            st.success("🌱 Possible Suitable Crops")

            st.dataframe(
                result,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No matching crop found in the sample database. "
                "Consider additional local factors and expert advice."
            )


# -------------------------------------------------
# SEARCH
# -------------------------------------------------

elif menu == "🔎 Search Resources":

    st.header("🔎 Search Agricultural Resources")

    search_text = st.text_input(
        "Enter crop name or keyword"
    )

    if search_text:

        crop_result = crops[
            crops.astype(str)
            .apply(
                lambda row:
                row.str.contains(
                    search_text,
                    case=False,
                    na=False
                ).any(),
                axis=1
            )
        ]

        if len(crop_result) > 0:

            st.subheader("🌱 Crop Results")

            st.dataframe(
                crop_result,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No matching resources found."
            )


# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.divider()

st.caption(
    "🌾 Farmer Assistance & Resource Platform | "
    "Developed using Python, Streamlit and Pandas"
)