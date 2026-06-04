import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()

st.set_page_config(
    page_title="FormPilot — AI Form Assistant",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
*{font-family:'Inter',sans-serif!important}
#MainMenu,footer,header{visibility:hidden}

/* ── App background ── */
.stApp{background:#13111E!important}

/* ── Sidebar ── */
[data-testid="stSidebar"]{background:#1A1730!important;border-right:1px solid #2A2545!important}
[data-testid="stSidebar"]>div:first-child{padding-top:0!important}
[data-testid="stSidebar"] *{color:#8B87A8}

/* Hide radio labels */
[data-testid="stSidebar"] .stRadio>label{display:none!important}

/* Nav items */
[data-testid="stSidebar"] .stRadio [role="radiogroup"]{gap:2px!important}
[data-testid="stSidebar"] .stRadio [data-baseweb="radio"]{
  padding:9px 10px!important;border-radius:8px!important;
  border:none!important;background:transparent!important;width:100%!important}
[data-testid="stSidebar"] .stRadio [data-baseweb="radio"]:has(input:checked){background:#2A2545!important}
[data-testid="stSidebar"] .stRadio [data-baseweb="radio"] p{font-size:14px!important;color:#8B87A8!important}
[data-testid="stSidebar"] .stRadio [data-baseweb="radio"]:has(input:checked) p{color:#A89EEA!important;font-weight:500!important}
[data-testid="stSidebar"] .stRadio [data-baseweb="radio"]>div:first-child{display:none!important}

/* ── Main area ── */
.main .block-container{padding:24px 32px!important}

/* ── Buttons ── */
.stButton>button{
  background:#534AB7!important;color:#EEEDFE!important;
  border:none!important;border-radius:10px!important;
  font-size:13px!important;font-weight:500!important;
  padding:10px 16px!important;width:100%!important;
  transition:background .15s!important}
.stButton>button:hover{background:#4338CA!important}
.stButton>button[kind="secondary"]{
  background:#2A2545!important;color:#9B96D4!important;
  border:1px solid #3D3668!important}
.stButton>button[kind="secondary"]:hover{background:#342B58!important}

/* ── Chat messages ── */
[data-testid="stChatMessage"]{
  background:#1A1730!important;border:1px solid #2A2545!important;
  border-radius:14px!important;padding:16px 20px!important;
  margin:5px 0!important}
[data-testid="stChatMessage"] p{
  font-size:14px!important;color:#D0CCF0!important;line-height:1.7!important;margin:0!important}
[data-testid="stChatMessage"] li{font-size:14px!important;color:#D0CCF0!important;line-height:1.7!important}
[data-testid="stChatMessage"] strong{color:#A89EEA!important;font-weight:500!important}
[data-testid="stChatMessage"] a{color:#7F77DD!important}

/* ── Chat input ── */
[data-testid="stBottom"]{background:#1A1730!important;border-top:1px solid #2A2545!important;padding:12px 20px!important}
[data-testid="stChatInput"] textarea{
  border-radius:22px!important;border:1px solid #3D3668!important;
  background:#2A2545!important;font-size:14px!important;
  color:#D0CCF0!important;padding:12px 20px!important}
[data-testid="stChatInput"] textarea:focus{border-color:#7F77DD!important}
[data-testid="stChatInput"] textarea::placeholder{color:#4A4665!important}

/* ── Form inputs ── */
[data-testid="stTextInput"] input{
  border-radius:10px!important;border:1px solid #3D3668!important;
  background:#2A2545!important;color:#D0CCF0!important;font-size:14px!important}
[data-testid="stTextInput"] input:focus{border-color:#7F77DD!important}
[data-testid="stSelectbox"]>div>div{
  border-radius:10px!important;border:1px solid #3D3668!important;
  background:#2A2545!important;color:#D0CCF0!important;font-size:14px!important}
[data-testid="stWidgetLabel"] p{font-size:13px!important;font-weight:500!important;color:#8B87A8!important}

/* ── Tabs ── */
[data-baseweb="tab-list"]{background:#2A2545!important;border-radius:12px!important;padding:5px!important;gap:4px!important}
button[data-baseweb="tab"]{background:transparent!important;border-radius:8px!important;color:#6B6590!important;font-size:13px!important;font-weight:500!important;border:none!important}
button[aria-selected="true"]{background:#534AB7!important;color:#EEEDFE!important;font-weight:500!important}

/* ── Metrics ── */
[data-testid="metric-container"]{background:#1A1730!important;border:1px solid #2A2545!important;border-radius:14px!important;padding:18px!important}
[data-testid="metric-container"] label{color:#6B6590!important;font-size:13px!important}
[data-testid="stMetricValue"]{color:#A89EEA!important;font-size:22px!important;font-weight:600!important}

/* ── Alerts ── */
[data-testid="stAlert"]{background:#2A2545!important;border:1px solid #3D3668!important;border-radius:12px!important;color:#D0CCF0!important}

/* ── Scrollbar ── */
::-webkit-scrollbar{width:4px;height:4px}
::-webkit-scrollbar-track{background:#1A1730}
::-webkit-scrollbar-thumb{background:#3D3668;border-radius:4px}

/* ── Sidebar collapse button ── */
[data-testid="stSidebarCollapseButton"] button{
  background:#2A2545!important;border:1px solid #3D3668!important;
  border-radius:8px!important}
[data-testid="stSidebarCollapseButton"] button svg{fill:#8B87A8!important}
[data-testid="stSidebarCollapseButton"] span{display:none!important}

/* ── Page header ── */
.fp-header{
  display:flex;align-items:center;gap:16px;
  background:#1A1730;border:1px solid #2A2545;
  border-radius:16px;padding:20px 24px;margin-bottom:22px}
.fp-header-icon{
  width:48px;height:48px;border-radius:14px;
  background:#2A2545;display:flex;
  align-items:center;justify-content:center;font-size:26px;flex-shrink:0}
.fp-header h1{font-size:18px;font-weight:600;color:#F0EFFE;margin:0}
.fp-header p{font-size:13px;color:#6B6590;margin:4px 0 0}

/* ── Sidebar components ── */
.fp-sb-logo{
  padding:22px 16px 16px;border-bottom:1px solid #2A2545;
  margin-bottom:6px;display:flex;align-items:center;gap:12px}
.fp-sb-icon{
  width:38px;height:38px;background:#534AB7;
  border-radius:11px;display:flex;align-items:center;
  justify-content:center;font-size:20px;flex-shrink:0}
.fp-sb-title{font-size:15px;font-weight:600;color:#F0EFFE}
.fp-sb-sub{font-size:11px;color:#4A4665;margin-top:1px}
.fp-sb-section{
  padding:14px 18px 6px;font-size:10px;font-weight:600;
  color:#4A4665;letter-spacing:1px;text-transform:uppercase}
.fp-chips{padding:4px 12px 12px;display:flex;flex-wrap:wrap;gap:5px}
.fp-chip{
  font-size:11px;font-weight:500;padding:4px 10px;border-radius:20px;
  background:#2A2545;color:#9B96D4;border:1px solid #3D3668}
</style>
""", unsafe_allow_html=True)

from database.user_profile import init_db
init_db()

if "lang" not in st.session_state:
    st.session_state["lang"] = "English"

# ── SIDEBAR ──
with st.sidebar:
    st.markdown("""
    <div class="fp-sb-logo">
      <div class="fp-sb-icon">🧭</div>
      <div>
        <div class="fp-sb-title">FormPilot</div>
        <div class="fp-sb-sub">AI Form Assistant</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='padding:6px 8px'>", unsafe_allow_html=True)
    page = st.radio("Navigation",
        ["💬  Chat","👤  My Profile","🛠️  Tools","📊  Evaluation"],
        label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="fp-sb-section">Supported Exams</div>', unsafe_allow_html=True)
    st.markdown("""<div class="fp-chips">
      <span class="fp-chip">SSC CGL</span><span class="fp-chip">SSC CHSL</span>
      <span class="fp-chip">UPSC</span><span class="fp-chip">MPSC</span>
      <span class="fp-chip">Railway</span><span class="fp-chip">IBPS PO</span>
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="fp-sb-section">Language</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("English", use_container_width=True,
                     type="primary" if st.session_state["lang"]=="English" else "secondary"):
            st.session_state["lang"] = "English"; st.rerun()
    with c2:
        if st.button("हिंदी", use_container_width=True,
                     type="primary" if st.session_state["lang"]=="Hindi" else "secondary"):
            st.session_state["lang"] = "Hindi"; st.rerun()

sel_lang = st.session_state.get("lang","English")

# ── CHAT ──
if page == "💬  Chat":
    st.markdown(f"""<div class="fp-header">
      <div class="fp-header-icon">💬</div>
      <div>
        <h1>{"FormPilot Chat" if sel_lang=="English" else "फॉर्मपायलट चैट"}</h1>
        <p>{"Ask anything — eligibility, documents, deadlines, fees" if sel_lang=="English" else "कोई भी सवाल पूछें — योग्यता, दस्तावेज़, समय सीमा, शुल्क"}</p>
      </div>
    </div>""", unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)
    quick_q = None
    if sel_lang == "English":
        with c1:
            if st.button("📋 SSC CGL Docs",use_container_width=True): quick_q="What documents are required for SSC CGL?"
        with c2:
            if st.button("🎂 UPSC Age Limit",use_container_width=True): quick_q="What is the age limit for UPSC CSE?"
        with c3:
            if st.button("💰 Railway Fee",use_container_width=True): quick_q="What is the application fee for Railway NTPC?"
        with c4:
            if st.button("📅 IBPS Deadlines",use_container_width=True): quick_q="What are the upcoming deadlines for IBPS PO?"
    else:
        with c1:
            if st.button("📋 SSC CGL दस्तावेज़",use_container_width=True): quick_q="SSC CGL के लिए कौन से दस्तावेज़ चाहिए?"
        with c2:
            if st.button("🎂 UPSC आयु सीमा",use_container_width=True): quick_q="UPSC CSE की आयु सीमा क्या है?"
        with c3:
            if st.button("💰 Railway शुल्क",use_container_width=True): quick_q="Railway NTPC का आवेदन शुल्क कितना है?"
        with c4:
            if st.button("📅 IBPS डेडलाइन",use_container_width=True): quick_q="IBPS PO की आगामी डेडलाइन कब है?"

    st.write("")

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role":"assistant","content":
            "Hello! 👋 I'm **FormPilot** — your AI Government Form Assistant!\n\n"
            "I can help you with:\n"
            "- 📋 **Documents** — what's needed & where to get them\n"
            "- ✅ **Eligibility** — check if you qualify\n"
            "- 📅 **Deadlines** — never miss a form date\n"
            "- 📸 **Photo/Signature** — exact size & format\n\n"
            "What would you like to know? 😊"}]

    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])

    if quick_q:
        st.session_state.messages.append({"role":"user","content":quick_q})
        with st.chat_message("user"): st.markdown(quick_q)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..." if sel_lang=="English" else "सोच रहा हूँ..."):
                from agent.agent import chat_with_formpilot
                r = chat_with_formpilot(quick_q, sel_lang)
                st.markdown(r)
                st.session_state.messages.append({"role":"assistant","content":r})
        st.rerun()

    placeholder = "Type your question here..." if sel_lang=="English" else "अपना सवाल यहाँ लिखें..."
    if prompt := st.chat_input(placeholder):
        st.session_state.messages.append({"role":"user","content":prompt})
        with st.chat_message("user"): st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..." if sel_lang=="English" else "सोच रहा हूँ..."):
                from agent.agent import chat_with_formpilot
                r = chat_with_formpilot(prompt, sel_lang)
                st.markdown(r)
                st.session_state.messages.append({"role":"assistant","content":r})

    if len(st.session_state.messages) > 1:
        st.write("")
        if st.button("🗑️  Clear Chat"):
            st.session_state.messages = st.session_state.messages[:1]; st.rerun()

# ── PROFILE ──
elif page == "👤  My Profile":
    st.markdown("""<div class="fp-header">
      <div class="fp-header-icon">👤</div>
      <div><h1>My Profile</h1><p>Fill once — reuse across all exam forms automatically</p></div>
    </div>""", unsafe_allow_html=True)

    from database.user_profile import get_profile, save_profile, delete_profile
    ex = get_profile()
    with st.form("pf"):
        c1,c2 = st.columns(2)
        with c1:
            name  = st.text_input("Full Name (as per 10th marksheet)",value=ex["name"] if ex else "")
            dob   = st.text_input("Date of Birth (DD/MM/YYYY)",value=ex["dob"] if ex else "")
            gen   = st.selectbox("Gender",["Male","Female","Other"],
                      index=["Male","Female","Other"].index(ex["gender"]) if ex and ex.get("gender") in ["Male","Female","Other"] else 0)
            cat   = st.selectbox("Category",["General","OBC","SC","ST","EWS","PwD"],
                      index=["General","OBC","SC","ST","EWS","PwD"].index(ex["category"]) if ex and ex.get("category") in ["General","OBC","SC","ST","EWS","PwD"] else 0)
        with c2:
            state = st.selectbox("State",["Maharashtra","Delhi","Uttar Pradesh","Bihar","Rajasthan","Madhya Pradesh","Gujarat","Karnataka","Tamil Nadu","West Bengal","Others"])
            qual  = st.selectbox("Qualification",["10th Pass","12th Pass","Pursuing Graduation","Graduation Complete","Post Graduation"])
            phone = st.text_input("Mobile Number",value=ex["phone"] if ex else "")
            email = st.text_input("Email Address",value=ex["email"] if ex else "")
        if st.form_submit_button("💾  Save Profile",use_container_width=True):
            if name and dob and phone and email:
                save_profile(name,dob,gen,cat,state,qual,phone,email)
                st.success("✅ Profile saved!"); st.balloons()
            else: st.error("❌ Name, DOB, Phone and Email are required!")
    if ex:
        st.markdown("---")
        c1,c2,c3 = st.columns(3)
        c1.metric("Name",ex["name"] or "—"); c2.metric("Category",ex["category"] or "—"); c3.metric("Qualification",ex["qualification"] or "—")
        if st.button("🗑️  Delete Profile"): delete_profile(); st.warning("Deleted!"); st.rerun()

# ── TOOLS ──
elif page == "🛠️  Tools":
    st.markdown("""<div class="fp-header">
      <div class="fp-header-icon">🛠️</div>
      <div><h1>Tools</h1><p>Resize photos, track deadlines, get document checklists</p></div>
    </div>""", unsafe_allow_html=True)

    t1,t2,t3 = st.tabs(["📸  Photo Resizer","📅  Deadline Tracker","📋  Document Checklist"])
    with t1:
        st.subheader("Photo & Signature Resizer")
        st.caption("Automatically resize as per exam specifications")
        c1,c2 = st.columns(2)
        with c1: ec = st.selectbox("Exam",["SSC","UPSC","RAILWAY","IBPS","MPSC"])
        with c2: it = st.selectbox("Type",["photo","signature"])
        up = st.file_uploader("Upload image",type=["jpg","jpeg","png"])
        if up:
            from utils.photo_resize import resize_image_for_exam, get_exam_photo_specs
            c1,c2 = st.columns(2)
            with c1: st.image(up,caption="Original",use_column_width=True)
            res = resize_image_for_exam(up.read(),ec,it)
            with c2: st.image(res,caption="✅ Resized",use_column_width=True)
            st.info(get_exam_photo_specs(ec))
            st.download_button("⬇️  Download",data=res,file_name=f"{ec}_{it}_resized.jpg",mime="image/jpeg",use_container_width=True)
    with t2:
        st.subheader("Exam Deadline Tracker")
        from utils.deadline import get_upcoming_deadlines
        ef = st.selectbox("Filter by Exam",["All","SSC CGL","SSC CHSL","UPSC CSE","RRB NTPC","IBPS PO","MPSC"])
        if ef == "All":
            result = get_upcoming_deadlines()
        else:
            result = get_upcoming_deadlines(ef)
        st.code(result, language=None)
    with t3:
        st.subheader("Document Checklist")
        en = st.selectbox("Select exam",["SSC CGL","SSC CHSL","UPSC CSE","RRB NTPC","IBPS PO","MPSC"])
        if st.button("📋  Get Checklist",use_container_width=True):
            from rag.retriever import retrieve_context
            with st.spinner("Fetching..."):
                st.markdown("### Required Documents:")
                st.markdown(retrieve_context(f"{en} documents required"))

# ── EVALUATION ──
elif page == "📊  Evaluation":
    st.markdown("""<div class="fp-header">
      <div class="fp-header-icon">📊</div>
      <div><h1>RAGAS Evaluation</h1><p>Measure how accurate FormPilot's answers are</p></div>
    </div>""", unsafe_allow_html=True)
    st.info("⚠️ Evaluation takes 5-10 minutes to complete.")
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Faithfulness","—"); c2.metric("Answer Relevancy","—")
    c3.metric("Context Precision","—"); c4.metric("Context Recall","—")
    if st.button("🚀  Run RAGAS Evaluation",use_container_width=True):
        with st.spinner("Running... ⏳"):
            try:
                from evaluation.ragas_eval import run_evaluation
                s = run_evaluation(); st.success("✅ Done!")
                c1.metric("Faithfulness",f"{s['faithfulness']:.2f}")
                c2.metric("Answer Relevancy",f"{s['answer_relevancy']:.2f}")
                c3.metric("Context Precision",f"{s['context_precision']:.2f}")
                c4.metric("Context Recall",f"{s['context_recall']:.2f}")
            except Exception as e: st.error(f"Error: {e}")