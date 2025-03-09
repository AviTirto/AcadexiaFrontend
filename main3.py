import streamlit as st
import asyncio
from api import fetch_clips

st.set_page_config(page_title="Econ 301 Search", page_icon="📚")  # Set tab title and icon

async def main():
    tab1, = st.tabs(["Lecture Clip Search 🎥"])  # Unpacking correctly

    with tab1:
        st.subheader("Econ 301 Lecture Clip Search")

        # Initialize session state variables
        if 'clips_query' not in st.session_state:
            st.session_state.clips_query = None
        if 'clips' not in st.session_state:
            st.session_state.clips = None

        clips_search_bar = st.text_input("Find me clips about...")

        if clips_search_bar and clips_search_bar != st.session_state.clips_query:
            st.session_state.clips_query = clips_search_bar
            st.session_state.clips = None  # Reset results

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
                for clip in clips:
                    with st.expander(f"{clip['start_time']} - {clip['end_time']}"):
                        st.markdown(f"""
                            <div style="text-align: center;">
                                {clip['embed_link']}
                            </div>
                        """, unsafe_allow_html=True)
                        st.divider()
                        st.subheader('Explanation')
                        st.write(clip['explanation'])
            else:
                st.warning("No clips found for your query.")

# Run the Streamlit app
if __name__ == "__main__":
    st.title("Econ 301 Lecture Clip Search")
    asyncio.run(main())
