import streamlit as st
st.set_page_config(page_title="Prompt Enhancer", page_icon="📝")
st.title("📝 Prompt Engineer — Advanced Prompt Enhancer")
st.caption("Demo Mode - Learn how to structure better prompts with RCT + Governance")

# --- RCT Fields ---
st.subheader("Enter Role")
role = st.text_input("Role", value="a helpful assistant")

# --- Context Requirements ---
st.subheader("Context Requirements")
domain = st.text_input("Domain", value="Retail / Healthcare / Education")
audience = st.text_input("Audience", value="Internal teams / Executives / Year 4 Students")
goals = st.text_area("Goals", value="Improve clarity, inclusivity, align with business outcomes")
data_sources = st.text_area("Data Sources", value="Official docs, policies, datasets, user research")

# --- Constraint Specifications ---
st.subheader("Constraint Specifications")
policies = st.text_area("Policies", value="Follow company style guide, industry best practices")
compliance = st.text_area("Compliance", value="GDPR, HIPAA, Accessibility standards")
tone = st.text_area("Tone Guidelines", value="Professional, concise, supportive")

# --- Structure Mandates ---
st.subheader("Structure Mandates")
sections = st.text_area("Required Sections", value="Introduction, Body, Summary")
formatting = st.text_area("Formatting", value="Bullets, ≤12 words per line, headings")
organization = st.text_area("Organization", value="Step-by-step flow, grouped by category")

# --- Checkpoint Integration ---
st.subheader("Checkpoint Integration")
assumptions = st.text_area("Assumptions", value="User has background knowledge; draft may be incomplete")
risks = st.text_area("Risks", value="Ambiguous inputs, missing context, bias")
confidence = st.text_area("Confidence Levels", value="Medium — requires SME review")

# --- Review Protocols ---
st.subheader("Review Protocols")
approval = st.text_area("Human Approval", value="Team lead / Manager approval required")
edits = st.text_area("Edit Requirements", value="One revision cycle before publishing")
accountability = st.text_area("Accountability", value="Owner: Project Manager; Editor: Content Specialist")

# --- User Draft ---
st.subheader("Paste your rough prompt")
draft = st.text_area("Your draft prompt:", height=140)

# --- Button Action ---
if st.button("Enhance Prompt"):
    if not draft.strip():
        st.warning("Please enter a draft prompt.")
    else:
        instruction = (
            "Generate an enhanced, structured prompt using RCT + Governance fields.\n"
            "1) Improve clarity and completeness\n"
            "2) Ask ONE clarifying question\n"
            "3) Specify output format (3 bullets, ≤12 words each)\n"
        )

        demo_output = (
            f"ROLE: {role}\n"
            f"CONTEXT: {context}\n"
            f"TASK: {task}\n\n"
            "CONTEXT REQUIREMENTS:\n"
            f"- Domain: {domain}\n"
            f"- Audience: {audience}\n"
            f"- Goals: {goals}\n"
            f"- Data Sources: {data_sources}\n\n"
            "CONSTRAINT SPECIFICATIONS:\n"
            f"- Policies: {policies}\n"
            f"- Compliance: {compliance}\n"
            f"- Tone Guidelines: {tone}\n\n"
            "STRUCTURE MANDATES:\n"
            f"- Required Sections: {sections}\n"
            f"- Formatting: {formatting}\n"
            f"- Organization: {organization}\n\n"
            "CHECKPOINT INTEGRATION:\n"
            f"- Assumptions: {assumptions}\n"
            f"- Risks: {risks}\n"
            f"- Confidence Levels: {confidence}\n\n"
            "REVIEW PROTOCOLS:\n"
            f"- Human Approval: {approval}\n"
            f"- Edit Requirements: {edits}\n"
            f"- Accountability: {accountability}\n\n"
            f"USER DRAFT:\n{draft}\n\n"
            "OUTPUT FORMAT:\n- 3 concise bullets\n- 1 clarifying question"
        )

        st.success("Enhanced Prompt (Demo Mode)")
        st.code(instruction + "\n" + demo_output, language="markdown")

        st.info("💡 This is demo mode showing the full structured template. In live mode, AI would generate the enhanced prompt with all fields populated intelligently!")