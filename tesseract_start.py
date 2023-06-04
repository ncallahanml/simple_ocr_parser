import pytesseract
import streamlit as st
import cv2
import pandas as pd
import joblib
import os
import shutil

st.session_state['text_str_dict'] = dict()
st.session_state['pattern_dict'] = dict()
st.session_state['output_dict'] = dict()

st.markdown('# Image Processing')
src_dir = st.text_input('Process Images in Folder:', 'doc_imgs/')
dest_dir = st.text_input('Copy Finished Images to Folder:', 'finished_imgs/')
exts = st.multiselect('Extensions to Process', ['.png','.jpg'], ['.png','.jpg'])

if st.button('Process Images to Text'):
    if not os.path.exists(dest_dir): os.mkdir(dest_dir)
    with st.spinner('Processing images...'):
        for file in sorted(os.listdir(src_dir)):
            if not file.endswith(tuple(exts)): 
                st.write('Skipping File', file)
                continue
            else:
                st.write('Processing File', file)
            src_file = os.path.join(src_dir, file)
            dest_file = os.path.join(dest_dir, file)
            img = cv2.imread(src_file)
            st.session_state['text_str_dict'] = pytesseract.image_to_string(img)
            del img
            shutil.move(src_file, dest_file)

        joblib.dump(st.session_state['text_str_dict'], 'text_str_dict.joblib')
        st.message('Images Processed!')

st.markdown('# Pattern Creation')

keyword = st.text_input('Keyword:', 'keyword')
word_separation = st.slider('Number of Words Between Pattern and Values:', 0, 100, 0)
n_words = st.slider('Number of Values to Read:', 1, 10, 1)

if st.button('Add Pattern'):
    st.session_state['pattern_dict'][keyword] = (word_separation, n_words)
    for file in st.session_state['text_str_dict'].keys():
        st.session_state['output_dict'][file][keyword] = list()

output_path = st.text_input('Output CSV Path:', 'output.csv')

if st.button('Read Text Elements'):
    if not output_path.endswith('.csv'):
        st.error('Output file must end with ".csv"')
    else:
        with st.spinner('Matching patterns...'):
            for file, text_str in st.session_state['text_str_dict'].items():
                words = text_str.split(' ')
                for i, word in enumerate(words):
                    if word in st.session_state['pattern_dict']:
                        word_separation, n_words = st.session_state['pattern_dict'][word]
                        value = words[i + word_separation:i + word_separation + n_words]
                        if isinstance(value, list): value = ' '.join(value)
                        st.session_state['output_dict'][file][word].append(value)

                output_dfs = list()
                for file in st.session_state['text_str_dict'].keys():
                    output_df = pd.DataFrame(st.session_state['output_dict'][file])
                    output_df['file'] = file
                    output_dfs.append(output_df)
                full_df = pd.concat(output_dfs, axis=0).to_csv(output_path)
        st.markdown('## Finished Pattern Matching, saved to', output_path)
    