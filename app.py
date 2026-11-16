import time
import streamlit as st

from pipline import run_Agent_pipline  # your file is named "pipline.py"

# ------------------------------------------------------------------ #
# Page config
# ------------------------------------------------------------------ #
st.set_page_config(
    page_title="Alenan AI Researcher",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ------------------------------------------------------------------ #
# Theme / CSS  (deep cosmic blue + glassmorphism)
# ------------------------------------------------------------------ #
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"], .stApp { font-family: 'Inter', sans-serif; }

/* ---------- Background ---------- */
.stApp {
    background:
        radial-gradient(ellipse 80% 50% at 50% -10%, rgba(59,130,246,0.55) 0%, rgba(59,130,246,0) 70%),
        radial-gradient(ellipse 60% 40% at 90% 110%, rgba(59,130,246,0.30) 0%, rgba(59,130,246,0) 70%),
        linear-gradient(180deg, #0A1128 0%, #0B1739 50%, #0F2557 100%);
    background-attachment: fixed;
    color: #E6ECFF;
}
header[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }
.block-container { max-width: 1080px; padding-top: 2.5rem; padding-bottom: 4rem; }

/* ---------- Hero ---------- */
.badge {
    display: inline-flex; align-items: center; gap: 8px;
    padding: 5px 14px 5px 6px; border-radius: 999px;
    background: rgba(59,130,246,0.15); border: 1px solid rgba(147,181,255,0.30);
    backdrop-filter: blur(10px); font-size: 0.78rem; color: #BFD3FF;
}
.badge b {
    background: #fff; color: #1D4ED8; border-radius: 999px;
    padding: 2px 9px; font-size: 0.68rem; letter-spacing: .05em;
}
.hero { text-align: center; margin: 1.2rem 0 2rem 0; }
.hero h1 {
    font-size: clamp(2.4rem, 5.5vw, 4.2rem); font-weight: 800; line-height: 1.05;
    letter-spacing: -0.03em; margin: 1.1rem 0 0.8rem 0;
    background: linear-gradient(180deg, #FFFFFF 30%, #9DBEFF 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.hero p { color: #9FB3E0; font-size: 1.05rem; max-width: 620px; margin: 0 auto; line-height: 1.6; }

/* ---------- Glass card ---------- */
.glass {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 20px; padding: 1.3rem 1.5rem;
    backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px);
    box-shadow: 0 10px 40px rgba(2,8,30,0.45), inset 0 1px 0 rgba(255,255,255,0.08);
}

/* ---------- Search form ---------- */
div[data-testid="stForm"] {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.16);
    border-radius: 22px; padding: 1rem 1.2rem;
    backdrop-filter: blur(20px);
    box-shadow: 0 18px 60px rgba(2,8,30,0.55), 0 0 0 1px rgba(59,130,246,0.15);
}
div[data-testid="stTextInput"] input {
    background: rgba(10,17,40,0.55) !important; color: #F1F5FF !important;
    border: 1px solid rgba(147,181,255,0.25) !important; border-radius: 14px !important;
    padding: 0.85rem 1rem !important; font-size: 1rem !important;
}
div[data-testid="stTextInput"] input:focus {
    border-color: #3B82F6 !important; box-shadow: 0 0 0 3px rgba(59,130,246,0.30) !important;
}
div[data-testid="stTextInput"] input::placeholder { color: #7F92BF !important; }

.stButton > button, div[data-testid="stFormSubmitButton"] button, .stDownloadButton > button {
    background: linear-gradient(135deg, #3B82F6 0%, #1D4ED8 100%);
    color: #fff; border: none; border-radius: 14px; font-weight: 600;
    padding: 0.8rem 1.4rem; width: 100%;
    box-shadow: 0 8px 24px rgba(59,130,246,0.45); transition: all .2s ease;
}
.stButton > button:hover, div[data-testid="stFormSubmitButton"] button:hover,
.stDownloadButton > button:hover {
    transform: translateY(-1px); box-shadow: 0 12px 32px rgba(59,130,246,0.65); color: #fff;
}

/* ---------- Stat tiles ---------- */
.stat { text-align: left; }
.stat .label { font-size: 0.72rem; text-transform: uppercase; letter-spacing: .08em; color: #8FA6D8; }
.stat .value { font-size: 1.5rem; font-weight: 700; color: #fff; margin-top: 2px; }
.stat .value.ok { color: #6EE7B7; }

/* ---------- Tabs ---------- */
.stTabs [data-baseweb="tab-list"] {
    gap: 6px; background: rgba(255,255,255,0.05); padding: 6px;
    border-radius: 16px; border: 1px solid rgba(255,255,255,0.10);
}
.stTabs [data-baseweb="tab"] {
    background: transparent; border-radius: 11px; color: #9FB3E0;
    padding: 0.55rem 1.1rem; font-weight: 500; height: auto;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, rgba(59,130,246,0.55), rgba(29,78,216,0.55));
    color: #fff !important; box-shadow: 0 4px 16px rgba(59,130,246,0.35);
}
.stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"] { display: none; }

/* ---------- Expanders ---------- */
div[data-testid="stExpander"] {
    background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.12);
    border-radius: 16px; backdrop-filter: blur(14px); overflow: hidden;
}
div[data-testid="stExpander"] summary { color: #DCE6FF; font-weight: 600; }

/* ---------- Status / misc ---------- */
div[data-testid="stStatusWidget"], div[data-testid="stExpander"] details { color: #DCE6FF; }
h2, h3, h4 { color: #F1F5FF; letter-spacing: -0.01em; }
hr { border-color: rgba(255,255,255,0.10); }
.stMarkdown p, .stMarkdown li { color: #D5DFF7; line-height: 1.7; }
.stMarkdown a { color: #7FB0FF; }
.stMarkdown code { background: rgba(59,130,246,0.18); color: #BFD6FF; border-radius: 6px; padding: 1px 6px; }
.footer-note { text-align: center; color: #6F83B3; font-size: .8rem; margin-top: 3rem; }
</style>
""",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------ #
# Session state
# ------------------------------------------------------------------ #
if "result" not in st.session_state:
    st.session_state.result = None
if "topic" not in st.session_state:
    st.session_state.topic = ""
if "elapsed" not in st.session_state:
    st.session_state.elapsed = None


def as_text(value) -> str:
    """Agent/chain outputs may be str or message-like objects."""
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return getattr(value, "content", None) or str(value)


# ------------------------------------------------------------------ #
# Hero
# ------------------------------------------------------------------ #
st.markdown(
    """
<div class="hero">
    <span class="badge"><b>NEW</b> Multi-agent research engine</span>
    <h1>Alenan AI Researcher</h1>
    <p>Search, scrape, write and critique — four specialised AI agents working
    together to turn any topic into a polished, reviewed research report.</p>
</div>
""",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------ #
# Search bar
# ------------------------------------------------------------------ #
with st.form("research_form", clear_on_submit=False):
    c1, c2 = st.columns([5, 1.2], vertical_alignment="center")
    topic_input = c1.text_input(
        "Research topic",
        value=st.session_state.topic,
        placeholder="Describe your research topic, e.g. “Latest breakthroughs in solid-state batteries”",
        label_visibility="collapsed",
    )
    submitted = c2.form_submit_button("Research →")

# ------------------------------------------------------------------ #
# Run pipeline
# ------------------------------------------------------------------ #
if submitted:
    topic = topic_input.strip()
    if not topic:
        st.warning("Please enter a topic to research.")
    else:
        st.session_state.topic = topic
        start = time.time()
        try:
            with st.status("Agents are working…", expanded=True) as status:
                st.write(" Search Agent → gathering recent, reliable sources")
                st.write(" Scraper Agent → extracting deep content")
                st.write(" Writer Chain → drafting the report")
                st.write(" Critic Chain → reviewing the draft")
                st.session_state.result = run_Agent_pipline(topic)
                st.session_state.elapsed = time.time() - start
                status.update(
                    label=f"Research complete in {st.session_state.elapsed:.1f}s",
                    state="complete",
                    expanded=False,
                )
        except Exception as e:  # noqa: BLE001
            st.session_state.result = None
            st.error(f"Pipeline failed: {e}")

# ------------------------------------------------------------------ #
# Results
# ------------------------------------------------------------------ #
result = st.session_state.result

if result:
    st.markdown("<br>", unsafe_allow_html=True)

    # Summary tiles
    stages = [
        ("Search", "Search_Results"),
        ("Scrape", "scraped_results"),
        ("Report", "Report"),
        ("Critic", "Feedback"),
    ]
    cols = st.columns(5)
    with cols[0]:
        st.markdown(
            f"""<div class="glass stat"><div class="label">Topic</div>
            <div class="value" style="font-size:1rem">{st.session_state.topic[:48]}</div></div>""",
            unsafe_allow_html=True,
        )
    for col, (label, key) in zip(cols[1:], stages):
        ok = bool(as_text(result.get(key)).strip())
        col.markdown(
            f"""<div class="glass stat"><div class="label">{label} agent</div>
            <div class="value {'ok' if ok else ''}">{'✓ Done' if ok else '— Empty'}</div></div>""",
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    tab_search, tab_scrape, tab_report, tab_critic = st.tabs(
        ["🔎 Search Results", "🕸️ Scraped Data", "📄 Final Report", "🧐 Critic Feedback"]
    )

    with tab_search:
        with st.expander("Search Agent output", expanded=True):
            st.markdown(as_text(result.get("Search_Results")) or "_No search results._")

    with tab_scrape:
        with st.expander("Scraped content", expanded=True):
            st.markdown(as_text(result.get("scraped_results")) or "_No scraped content._")

    with tab_report:
        report = as_text(result.get("Report"))
        st.markdown(report or "_No report generated._")
        if report:
            st.download_button(
                "⬇ Download report (.md)",
                data=report,
                file_name="alenan_research_report.md",
                mime="text/markdown",
            )

    with tab_critic:
        with st.expander("Critic feedback & conclusion", expanded=True):
            st.markdown(as_text(result.get("Feedback")) or "_No feedback generated._")

st.markdown(
    '<div class="footer-note">Alenan AI Researcher · Search → Scrape → Write → Critique</div>',
    unsafe_allow_html=True,
)