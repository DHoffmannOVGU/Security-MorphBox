import streamlit as st
import streamlit_antd_components as sac
import json


# Title and introduction
st.title('Morphological Box for Security')

st.info("Select the options for each of the following categories to generate a morphological box for security. The options are based on the ISO 22400-2 standard.")

with st.expander("Motivation", expanded=True):
    # [7] Possible Motivation
    st.subheader('Possible Motivation')
    motivation_options = ["Fear for workplace", "Revenge", "Rejection against progress", "Evidence drive", "Less work", "Sadist", "Follow-up order"]
    motivation = sac.segmented(items=motivation_options, index=0, align="center", size="md", grow=True)


    # [6] Role in project
    st.subheader('Role in project')
    role_options = ["Expert", "Programmer", "Maintainer", "Worker", "Hacker", "Works Council", "Supplier", "Customer", "Logistics", "PO", "Sub contractor"]
    role = sac.segmented(items=role_options, index=0, align="center", size="md", grow=True)

with st.expander("Preparation", expanded=True):
    # [5] Education level
    st.subheader('Education level')
    education_options = ["Beginner", "Advanced", "Master"]
    education = sac.segmented(items=education_options, index=0, align="center", size="md", grow=True)


    # [4] Character / approach
    st.subheader('Character / approach')
    character_options = ["Cyber", "Physical", "Cyber-Physical"]
    character = sac.segmented(items=character_options, index=0, align="center", size="md", grow=True)


    # [3] attack path
    # Note: You may need to further segment this into smaller sub-segments to avoid visual clutter
    st.subheader('Attack Domain')
    attack_path_options = ["Factory automation systems", "Robot applications", "Industrial bin picking applications"]
    attack_path = sac.segmented(items=attack_path_options, index=0, align="center", size="md", grow=True)

with st.expander("Attack", expanded=True):
    # Conditional rendering for sub-options of attack path
    st.subheader('Attacked Asset')
    if attack_path == "Factory automation systems":
        sub_options = ["Safety violation", "TCP", "Strictly according to specifications"]
    elif attack_path == "Robot applications":
        sub_options = ["Loading parameters", "Robot movement speed", "Device calibration", "Wait and delay functions", "Path points", "Robot properties", "Manipulated collision model of cell"]
    else:
        sub_options = ["Detection parameters", "Camera properties", "Manipulated resource CAD data", "Quality rating criteria for OK/n.OK supply"]

    sub_selection = sac.segmented(items=sub_options, index=0, align="center", size="md", grow=True)

    # [2] attack class
    st.subheader('Attack Class')
    attack_class_options = ["One-time", "Non permanent", "Recurring", "Permanent"]
    attack_class = sac.segmented(items=attack_class_options, index=0, align="center", size="md", grow=True)

    # [1] aim
    st.subheader('Aim')
    aim_options = ["Damage", "Performance reduction", "Information spying"]
    aim = sac.segmented(items=aim_options, index=0, align="center", size="md", grow=True)

    st.subheader('Perfomance aspect according to ISO 22400-2')
    performance_options = ["Quality", "Availability", "Performance", "Safety", "Security"]
    performance = sac.segmented(items=performance_options, index=0, align="center", size="md", grow=True)


with st.expander("Download Selected Options", expanded=True):
    # Save the data in a dict
    data = {
        "Motivation": motivation,
        "Role": role,
        "Education": education,
        "Character": character,
        "Attack Path": attack_path,
        "Attack Class": attack_class,
        "Aim": aim,
        "Performance": performance
    }

    json_string = json.dumps(data)

    st.json(json_string, expanded=True)

    st.download_button(
        label="Download JSON",
        file_name="data.json",
        mime="application/json",
        data=json_string,
        type="primary",
        use_container_width=True,
    )