import streamlit as st
import os.path as path
import pandas as pd


st.set_page_config(layout="wide")




col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.image(path.join("images","photo.jpeg"), width=300)
    
with col2:
    st.title("Dito")
    content = '''
    Cackle fruit American Main parrel gaff square-rigged fore log bilge water pillage crack Jennys tea cup ballast no prey, no pay jib Shiver me timbers flogging hogshead. Sutler Jolly Roger topgallant aye Davy Jones' Locker wherry fire in the hole deadlights heave down mutiny Arr jolly boat reef rutters Gold Road gangway. Barbary Coast capstan holystone measured fer yer chains keel list long boat loot mizzenmast swing the lead transom landlubber or just lubber lateen sail parrel gally pirate. Jolly Roger hands loot interloper belaying pin tackle stern jack jury mast brigantine rigging bowsprit transom cackle fruit Sail ho bilge water.
    '''
    st.info(content)

content2 = '''
    Deadlights pirate hogshead strike colors Shiver me timbers capstan handsomely driver lugger bilged on her anchor. Fire in the hole quarter hornswaggle line lugger mizzenmast ballast lanyard Jack Ketch rope's end
    '''

st.write(content2)


df = pd.read_csv("data.csv", sep=",")

#st.dataframe(df)

col3, col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
        st.header(f"[{row['title']}]({row['url']})")
        st.write(row["description"])
        st.image([path.join(".","images", row["image"])])
        #st.write(f"[Source]({}))
        #!SINTAX st.algo([Objeto principal](url))


with col4: 
    for index, row in df[10:].iterrows(): #! OJO: acordate que para hacer esta particion solo se puede de la ultima 
        st.header(f'[{row["title"]}]({row["url"]})')
        st.write(row["description"])
        st.image(path.join(".","images", row["image"]))

