import streamlit as st
import os.path as path

st.set_page_config()


col1, col2 = st.columns(2)

with col1:
    st.image(path.join("images","photo.jpeg"))
    
with col2:
    st.title("Dito")
    content = '''
    Cackle fruit American Main parrel gaff square-rigged fore log bilge water pillage crack Jennys tea cup ballast no prey, no pay jib Shiver me timbers flogging hogshead. Sutler Jolly Roger topgallant aye Davy Jones' Locker wherry fire in the hole deadlights heave down mutiny Arr jolly boat reef rutters Gold Road gangway. Barbary Coast capstan holystone measured fer yer chains keel list long boat loot mizzenmast swing the lead transom landlubber or just lubber lateen sail parrel gally pirate. Jolly Roger hands loot interloper belaying pin tackle stern jack jury mast brigantine rigging bowsprit transom cackle fruit Sail ho bilge water.
    '''
    st.info(content)
    
sep = st.sep()