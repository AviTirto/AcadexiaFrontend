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
            # Reset current values when search changes
            st.session_state.current_page = {}
            st.session_state.current_explanation = {}

            with st.spinner("Searching for slides..."):
                try:
                    response = await fetch_slides(st.session_state.slides_query)
                    st.session_state.ppts, st.session_state.ppt_titles, st.session_state.page_nums_list, st.session_state.ppt_explanations_list = response
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        
        # Initialize page_selection if not in session state
        if 'page_selection' not in st.session_state:
            st.session_state.page_selection = {}

        # Define callback function that uses radio buttons for selection
        def handle_page_change(idx):
            # Get the selected page index from the radio value
            if st.session_state.page_selection.get(idx) is not None:
                page_idx = st.session_state.page_nums_list[idx].index(st.session_state.page_selection[idx])
                # Update the current page and explanation
                st.session_state.current_page[idx] = st.session_state.page_selection[idx]
                st.session_state.current_explanation[idx] = st.session_state.ppt_explanations_list[idx][page_idx]
                st.session_state.open_expander = idx

        if st.session_state.ppts:
            st.success(f"Found {len(st.session_state.ppts)} slides!")
            for idx, ppt in enumerate(st.session_state.ppts):
                is_open = st.session_state.open_expander == idx
                with st.expander(st.session_state.ppt_titles[idx], expanded=is_open):
                    # Show the explanation
                    current_explanation = st.session_state.current_explanation.get(idx, st.session_state.ppt_explanations_list[idx][0])
                    st.write(current_explanation)
                    st.divider()
                    
                    # Get current page number for this PowerPoint
                    if idx not in st.session_state.current_page:
                        st.session_state.current_page[idx] = st.session_state.page_nums_list[idx][0]
                    
                    current_page = st.session_state.current_page[idx]
                    
                    # Add the slide navigation using radio buttons instead of regular buttons
                    st.write("*More Slides*")
                    
                    # Create a radio button group for slide selection
                    # This ensures only one slide is selected at a time and maintains state
                    st.session_state.page_selection[idx] = st.radio(
                        label="Select a slide:",
                        options=st.session_state.page_nums_list[idx],
                        index=st.session_state.page_nums_list[idx].index(current_page),
                        key=f"radio_{idx}_{st.session_state.slides_query}",
                        label_visibility="collapsed",
                        horizontal=True,
                        on_change=handle_page_change,
                        args=(idx,)
                    )
                    
                    st.write("")  # Add space after buttons
                    
                    # Display the PDF with the current page
                    try:
                        # Calculate the actual PDF page number (your custom formula)
                        page_to_show = max(1, int((current_page + 1)/2))
                        
                        # Display the PDF
                        st.markdown(f"""
                            <embed src="data:application/pdf;base64,{ppt}#page={page_to_show}" 
                                width="700" height="900" type="application/pdf">
                        """, unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Error displaying PDF: {e}")

if __name__ == "__main__":
    asyncio.run(main())
