# 🦠 OpenAI UK Due Diligence & Autoimmunity Map  
**First created:** 2025-11-05 | **Last updated:** 2025-12-26  
*Who is actually in the web, and who inherits the antibodies anyway.*  

---

## 🧭 Orientation  

This node maps **OpenAI’s UK footprint** along three layers:

1. **Formal partnerships** – named MoUs, research collaborations, safety-testing roles, and infrastructure deals.  
2. **Institutional users** – universities and bodies using OpenAI-derived products (ChatGPT Edu, Azure OpenAI, Copilot, Blackboard plugins).  
3. **Autoimmunity exposure** – how the *same* model lineage and moderation stack propagate suppression dynamics across the ecosystem, even where no direct OpenAI contract exists.

The aim is simple: provide enough due diligence that when regulators, journalists, or survivor-scholars ask  
> “Where is this system actually attached to the UK?”  
there is a clear, evidence-backed answer that survives a subpoena.  

---

## 1. Confirmed UK Stakeholders (Formal Ties)

These are entities where there is **public documentation** of a direct relationship with OpenAI (or an OpenAI-led programme), beyond “we used the website once”.

### 1.1 State & Safety Infrastructure  

| Entity | Type | Relationship | Mechanism / Programme | Status |
|--------|------|--------------|------------------------|--------|
| **UK Government – DSIT** | State / policy | Strategic partnership / MoU to accelerate AI adoption, infra (“sovereign compute”), and public-service deployment | UK–OpenAI MOU (2025) and AI Action Plan; includes collaboration on infrastructure and AI adoption in government | **Confirmed** |
| **UK AI Security Institute (AISI)** | State eval lab | Technical information-sharing and safety research; evaluates frontier models including OpenAI | MoU explicitly extends existing partnership with AI Safety Institute into a technical info-sharing programme; use of evaluation frameworks (e.g. Inspect) for LLMs | **Confirmed** |
| **Ministry of Justice (MoJ)** | Government department | Deployment of ChatGPT Enterprise with UK data residency; used to support civil servants and policy workflows | MoJ–OpenAI agreement as part of “next chapter for UK sovereign AI” and broader UK gov adoption | **Confirmed** |

*Implication:* OpenAI is not just a vendor; it is **plugged into the UK state’s AI safety and public-service machinery**.

---

### 1.2 Academic & Research Partners  

| Entity | Type | Relationship | Mechanism / Programme | Status |
|--------|------|--------------|------------------------|--------|
| **University of Oxford** | University | 5-year research & education collaboration; only UK university publicly listed in OpenAI’s **NextGenAI** consortium; full-campus ChatGPT Edu deployment | Oxford–OpenAI collaboration (2025); membership of NextGenAI; rollout of ChatGPT Edu to staff/students | **Confirmed – core UK academic node** |
| **Alan Turing Institute – AI for Cyber Defence (AICD)** | National research institute | Part of the **OpenAI Early Access Safety Testing Program**; uses early access to OpenAI models for cyber defence research & evaluations | AICD project documentation lists participation in OpenAI early access safety testing | **Confirmed – safety-testing node** |
| **London Business School (LBS)** | Business school | Collaboration providing ChatGPT Edu / advanced AI tools to faculty, students, and exec-ed programmes | LBS–OpenAI collaboration announcements; ChatGPT Edu deployment | **Confirmed – education / commercial node** |

*Implication:* Oxford and the Turing act as the **principal UK research and safety conduits** into OpenAI’s model pipeline; LBS extends that into the business/exec-ed ecosystem.

---

### 1.3 Infrastructure & Compute Partners  

| Entity | Type | Relationship | Mechanism / Programme | Status |
|--------|------|--------------|------------------------|--------|
| **Nscale** | UK infra provider | Co-builder of UK AI compute for OpenAI models (alongside NVIDIA, Microsoft) | UK hyperscale GPU data centres; infrastructure for “sovereign AI” platforms | **Confirmed** |
| **Stargate UK (OpenAI + NVIDIA + Nscale)** | Joint infra platform | UK-based platform hosting OpenAI models on local compute, with thousands of NVIDIA GPUs | Announced as “Stargate UK” initiative – OpenAI models deployed on UK-based hardware | **Confirmed – compute backbone** |

*Implication:* Even where contracts are with Nscale or Microsoft, **OpenAI’s models sit inside the sovereign-infra story**, not just on foreign clouds.  

---

## 2. Institutional Users & Indirect Nodes

These are institutions where **OpenAI tech is clearly in use**, but where there is no public evidence of a formal research-consortium or MoU relationship.

### 2.1 Universities Using OpenAI-Derivative Products  

| Institution | Product lineage | Relationship Type | Notes | Status |
|-------------|-----------------|-------------------|-------|--------|
| **UCL** | OpenAI models via research tools, hackathons, and educational uses | Engaged research/education user | Hosts OpenAI leadership for talks, students participate in OpenAI hackathons, research projects explicitly experimenting with ChatGPT; no formal consortium agreement visible | **User / ecosystem node (no formal consortium)** |
| **University of Nottingham** | OpenAI models as tools (e.g., ChatGPT) | Research & teaching user | Blogs and academic materials discuss & use ChatGPT/OpenAI; no OpenAI-branded partnership announcements | **User (no formal OpenAI partnership found)** |
| **Sheffield Hallam University (SHU)** | **Azure OpenAI** via Blackboard / Microsoft | Downstream customer via Microsoft | Blackboard at SHU uses Azure OpenAI; university issues guidance on generative AI citing OpenAI; contract is with Microsoft, but base models are OpenAI | **Downstream user via Azure** |

*Implication:* These institutions may say “we don’t work with OpenAI”, but in practice they are exposed through **embedded tools and clouds**.

---

## 3. Autoimmunity Exposure: How Derivatives Inherit the Same Reflex

Even where the contract is with Microsoft, Blackboard, or some vendor, the **autoimmune behaviour** of OpenAI’s model family still propagates.

### 3.1 Derivative ≠ Independent

| Surface Product | Likely Base Lineage | Notes |
|-----------------|---------------------|-------|
| **ChatGPT Edu** | GPT-4 family | Direct OpenAI deployment into universities (e.g. Oxford, LBS). |
| **Azure OpenAI Service** (Blackboard, internal bots, etc.) | GPT-4 / GPT-3.5 via Azure | Same model weights & safety layers, exposed via Microsoft’s cloud. |
| **Copilot (MS 365, GitHub)** | GPT-4 + fine-tuned coding models | Moderation stack and behaviour patterns synced with OpenAI-origin models. |
| **Third-party “AI assistants” using OpenAI API** | GPT-3.5/4 derivatives | Often just a thin UI wrapper; all core reflexes inherited. |

The **safety filters, moderation policies, and logging behaviour** are centralised. The local wrapper (VLE plugin, enterprise UI) does not erase the immune system; it merely puts houseplants in front of it.

---

### 3.2 Shared Immune Memory via Telemetry

- Every prompt that hits OpenAI (directly or via Azure) can generate **telemetry**:  
  - safety-system flags,  
  - refusal reasons,  
  - pattern-matching stats.  
- Those signals feed back into **global retraining** of moderation boundaries.  
- So when a problematic-refusal pattern appears at SHU or Nottingham, it may help tighten the classifier that later suppresses survivor discourse at Oxford or within MoJ workflows.

The ecosystem learns **one immune response** from many local irritations.

---

### 3.3 Ecosystem-Level Autoimmune Cascade  

If we overlay your autoimmune metaphor:

1. **Local flare-up** – a piece of survivor speech, dissent, or complex grief gets suppressed in one product (e.g. a student essay in Blackboard using Azure OpenAI).  
2. **Centralised update** – that interaction contributes to safety pipeline fine-tuning.  
3. **Raised global sensitivity** – the same pattern of language begins to get flagged faster across other surfaces (ChatGPT Edu, Copilot, MoJ tools).  
4. **Chronic narrowing** – the range of acceptable undertone shrinks at *every* institution using the lineage, whether or not they know they’re “working with OpenAI”.

Thus: **Nottingham and SHU are still part of the autoimmune network**, even if they are not in the formal OpenAI stakeholder slide deck.

---

## 4. Due Diligence Checklist (UK Context)

If you need to demonstrate that “due diligence was done” around OpenAI’s UK entanglements, this is the minimal investigative spine:

1. **Confirm formal partners**  
   - Oxford (NextGenAI + ChatGPT Edu)  
   - Alan Turing Institute (OpenAI Early Access Safety Testing)  
   - LBS (ChatGPT Edu)  
   - DSIT / AISI (MoU, technical info-sharing)  
   - MoJ (ChatGPT Enterprise, UK residency)  
   - Nscale / Stargate UK (compute)

2. **Trace derivative-product exposure**  
   - Identify all deployments of ChatGPT Edu, Azure OpenAI, Copilot, and other OpenAI-backed tools in UK HE and public sector.  
   - For each, capture:  
     - who the *contracting entity* is (Microsoft? OpenAI UK Ltd? another vendor?),  
     - what data residency / logging / DPIA statements say about model providers.

3. **Map autoimmunity risk**  
   - For each deployment, ask:  
     - Are moderation policies inherited from OpenAI?  
     - Where are refusals logged?  
     - Are there escalation paths for wrongful suppression, especially of minority/survivor speech?  

4. **Regulatory follow-up**  
   - FOIs / SARs to DSIT, MoJ, AISI, Oxford, ATI, LBS, UCL, Nottingham, SHU:  
     - copies of MoUs, DPIAs, and safety-eval documents involving OpenAI or Azure OpenAI;  
     - records of harms or wrongful refusals involving AI assistants.  

---

## 🌌 Constellations  

📋 🦠 📈 🏛️  

---

## ✨ Stardust  

OpenAI UK, due diligence, research consortia, Azure OpenAI, ChatGPT Edu, autoimmunity, derivative products, sovereign AI, UK government, universities, Nscale, Stargate, AISI, Turing Institute, data residency, DPIA, regulatory exposure  

---

## 🏮 Footer  

*🦠 OpenAI UK Due Diligence & Autoimmunity Map* is a living diagnostic node of the Polaris Protocol.  
It documents both the **formal institutional ties** and the **immunological spillover** of OpenAI’s models across UK academia and public services, so that harms cannot later be dismissed as unforeseeable.  

> 📡 Cross‑references:  
> 
> - [⚖️ Soft Power Without Soft Accountability](../../🦕_Elder_Influencers/🕸️_World_Webs/⚖️_soft_power_without_soft_accountability.md)  
> - [🦠 Algorithmic Autoimmunity](../../../../Metadata_Sabotage_Network/🔥_Data_Risks/🦠_algorithmic_autoimmunity.md) – *the systemic pathology*
> - [🫀 AI Black Box Inquests](./🫀_ai_black_box_inquests.md)  
> - [*Pending:* 📈 Stakeholder Mapping from Symptoms] – *the diagnostic, “who flinched where” method*  
> - [*Pending:* 🏛️ Becoming a Genocide Scholar] – *how you ended up doing this work at all*  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-12-26_
