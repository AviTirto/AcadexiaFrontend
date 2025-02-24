import streamlit as st
import asyncio
from api import fetch_clips, fetch_slides

async def main():

    tab1, tab2 = st.tabs(["Lecture Clip Search 📹", "PowerPoint Search 🎒"])

    tab1.subheader("Econ 301 Lecture Clip Search")
    tab2.subheader("Econ 301 PowerPoint Search")

    if 'clips_query' not in st.session_state:
        st.session_state.clips_query = None
    if 'clips' not in st.session_state:
        st.session_state.clips = None
    if 'slides_query' not in st.session_state:
        st.session_state.slides_query = None
    if 'ppts' not in st.session_state:
        st.session_state.ppts = None
    if 'ppt_titles' not in st.session_state:
        st.session_state.ppt_titles = None
    if 'page_nums_list' not in st.session_state:
        st.session_state.page_nums_list = None
    if 'ppt_explanations_list' not in st.session_state:
        st.session_state.ppt_explanations_list = None
    if 'current_page' not in st.session_state:
        st.session_state.current_page = {}
    if 'current_explanation' not in st.session_state:
        st.session_state.current_explanation = {}
    if 'open_expander' not in st.session_state:
        st.session_state.open_expander = None

    with tab1:
        clips_search_bar = st.text_input("Find me clips about...")

        if clips_search_bar and clips_search_bar != st.session_state.clips_query:
            st.session_state.clips_query = clips_search_bar
            st.session_state.clips = None

        if st.session_state.clips_query:
            if st.session_state.clips is None: 
                with st.spinner("Searching for clips..."):
                    try:
                        st.session_state.clips = await fetch_clips(st.session_state.clips_query)
                    except Exception as e:
                        st.error(f"An error occurred: {e}")
                        st.session_state.clips = []

            clips = st.session_state.clips
            if clips:
                st.success(f"Found {len(clips)} clips!")
                for idx, clip in enumerate(clips):
                    with st.expander(f"{clip['start_time']} - {clip['end_time']}"):
                        st.markdown(
                            f"""
                            <div style="text-align: center;">
                                {clip['embed_link']}
                            </div>
                            """, 
                            unsafe_allow_html=True
                        )
                        st.divider()
                        st.subheader('Explanation')
                        st.write(clip['explanation'])
            else:
                st.warning("No clips found for your query.")

    with tab2:
        slides_search_bar = st.text_input("Find me slides about...")

        if slides_search_bar and slides_search_bar != st.session_state.slides_query:
            st.session_state.slides_query = slides_search_bar

            with st.spinner("Searching for slides..."):
                try:
                    response = await fetch_slides(st.session_state.slides_query)
                    st.session_state.ppts, st.session_state.ppt_titles, st.session_state.page_nums_list, st.session_state.ppt_explanations_list = response
                except Exception as e:
                    st.error(f"An error occurred: {e}")

        if st.session_state.ppts:
            st.success(f"Found {len(st.session_state.ppts)} slides!")
            for idx, ppt in enumerate(st.session_state.ppts):
                is_open = st.session_state.open_expander == idx
                with st.expander(st.session_state.ppt_titles[idx], expanded=is_open):
                    current_explanation = st.session_state.current_explanation.get(idx, st.session_state.ppt_explanations_list[idx][0])
                    st.write(current_explanation)
                    st.divider()
                    st.write("**More Slides**")
                    for page_num, explanation in zip(st.session_state.page_nums_list[idx], st.session_state.ppt_explanations_list[idx]):
                        if st.button(f"Slide {page_num}", key=f"slide_{idx}_{page_num}"):
                            st.session_state.current_page[idx] = page_num
                            st.session_state.current_explanation[idx] = explanation
                            st.session_state.open_expander = idx

                    current_page = st.session_state.current_page.get(idx, st.session_state.page_nums_list[idx][0])
                    st.markdown(f"""
                        <embed src="data:application/pdf;base64,{ppt}#page={current_page}" 
                               width="700" height="900" type="application/pdf">
                    """, unsafe_allow_html=True)

if __name__ == "__main__":
    asyncio.run(main())
