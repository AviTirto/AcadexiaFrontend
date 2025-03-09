import streamlit as st
import asyncio
from api import fetch_clips #send_feedback  # Assuming a function to send feedback to the backend

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
        if 'feedback_given' not in st.session_state:
            st.session_state.feedback_given = {}

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
                    clip_id = str(clip['start_time'])
                    
                    # Create a unique key for this clip
                    if clip_id not in st.session_state.feedback_given:
                        st.session_state.feedback_given[clip_id] = False
                    
                    with st.expander(f"{clip['start_time']} - {clip['end_time']}", expanded=True):
                        st.markdown(f"""
                            <div style="text-align: center; margin-bottom: 10px;">
                                {clip['embed_link']}
                            </div>
                        """, unsafe_allow_html=True)
                        st.divider()
                        st.subheader('Explanation')
                        st.write(clip['explanation'])

                        # Callback functions for thumbs up/down buttons
                        def on_thumbs_up():
                            st.session_state.feedback_given[clip_id] = "up"
                            # Uncomment to send feedback to backend
                            # asyncio.create_task(send_feedback(clip['start_time'], "thumbs_up"))
                        
                        def on_thumbs_down():
                            st.session_state.feedback_given[clip_id] = "down"
                            # Uncomment to send feedback to backend
                            # asyncio.create_task(send_feedback(clip['start_time'], "thumbs_down"))

                        # Create two columns for the thumbs up/down buttons
                        col1, col2, col3 = st.columns([1, 1, 3])
                        
                        with col1:
                            thumbs_up = st.button("👍", key=f"thumbs_up_{clip_id}", on_click=on_thumbs_up)
                        
                        with col2:
                            thumbs_down = st.button("👎", key=f"thumbs_down_{clip_id}", on_click=on_thumbs_down)
                        
                        # Display feedback message if given
                        if st.session_state.feedback_given[clip_id] == "up":
                            with col3:
                                st.success("Thank you for your positive feedback!")
                        elif st.session_state.feedback_given[clip_id] == "down":
                            with col3:
                                st.warning("Thank you for your feedback. We'll improve this clip!")

            else:
                st.warning("No clips found for your query.")

# Run the Streamlit app
if __name__ == "__main__":
    st.title("Econ 301 Lecture Clip Search")
    asyncio.run(main())